#!/usr/bin/env python3
"""Control node: converts vision detections into STM32 `$FIRE` packets.

Pipeline
--------
    WeedArray (/weedbot/detections)
        -> select target (bbox meristem in real-world meters via homography)
        -> meters -> mm, apply sign flips (vision frame -> firmware frame)
        -> bounds check accounting for camera->galvo offset (firmware applies)
        -> cooldown + duplicate suppression
        -> $FIRE,<seq>,<mm_x>,<mm_y>,<dwell_ms>,<power_permille>*CS

Modes
-----
  DRY_RUN: serial is not opened; every packet is logged as it would appear
           on the wire, so the user can copy one into TeraTerm on the STM32
           laptop to verify formatting.
  LIVE   : opens serial, sends `$ARM,1` then `$OFFSET,x,y` on startup,
           sends `$ARM,0` on shutdown, streams ACK/ERR lines from the MCU.

Firmware frame convention
-------------------------
  +mm_x = LEFT  (vision real_world_x is +right, so flip by default)
  +mm_y = FORWARD / away from operator (vision real_world_y is +toward
          operator, so flip by default)

The camera->galvo offset is applied *by the firmware*. The control node
only uses it to pre-reject targets outside the reachable envelope.
"""

from __future__ import annotations

import math
import signal
import time
from dataclasses import dataclass
from typing import Optional, Set, Tuple

import rclpy
from rcl_interfaces.msg import SetParametersResult
from rclpy.node import Node
from std_msgs.msg import String
from weedbot_interfaces.msg import WeedArray

from weedbot_control.serial_manager import (
    SerialManager,
    build_arm,
    build_fire,
    build_offset,
)

import json


MODE_DRY_RUN = "DRY_RUN"
MODE_LIVE = "LIVE"


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


@dataclass
class Target:
    """A candidate target expressed in firmware-frame millimeters.

    `mm_x` / `mm_y` are already sign-flipped into the firmware frame.
    """

    mm_x: float
    mm_y: float
    confidence: float
    class_id: int


class ControlNode(Node):
    """ROS 2 node that drives the STM32 laser controller over serial."""

    def __init__(self) -> None:
        super().__init__("weedbot_control_node")

        self._declare_parameters()
        self._load_parameters()
        self.add_on_set_parameters_callback(self._on_set_parameters)

        self.serial = SerialManager(
            logger=self.get_logger(),
            port=self.serial_port,
            baudrate=self.serial_baudrate,
            read_timeout_s=self.serial_read_timeout_s,
            reconnect_s=self.serial_reconnect_s,
            dry_run=(self.mode == MODE_DRY_RUN),
        )

        self.detection_sub = self.create_subscription(
            WeedArray, self.detection_topic, self._detection_callback, 10
        )
        self.status_pub = self.create_publisher(String, self.status_topic, 10)
        self.debug_pub = self.create_publisher(String, self.debug_topic, 10)

        self._shot_seq = 0
        self._last_shot_at = 0.0
        self._last_target_mm: Optional[Tuple[float, float]] = None
        self._outstanding: Set[int] = set()
        self._shots_sent = 0
        self._shots_blocked_safety = 0
        self._shots_blocked_rate = 0
        self._shots_blocked_bounds = 0
        self._shots_blocked_queue = 0
        self._serial_lines_rx = 0
        self._last_ack_seq: Optional[int] = None
        self._last_err: Optional[str] = None

        self.serial.ensure_connected()
        if self.armed:
            self._send_startup_handshake()

        poll_period = 1.0 / max(self.serial_poll_hz, 1.0)
        self.serial_poll_timer = self.create_timer(poll_period, self._serial_poll)
        self.status_timer = self.create_timer(1.0, self._publish_status)

        signal.signal(signal.SIGINT, self._handle_sigint)
        signal.signal(signal.SIGTERM, self._handle_sigint)

        self.get_logger().info(
            f"control_node started mode={self.mode} armed={self.armed} "
            f"port={self.serial_port} bounds=x[{self.bounds_x_min_mm},"
            f"{self.bounds_x_max_mm}] y[{self.bounds_y_min_mm},"
            f"{self.bounds_y_max_mm}] offset=({self.offset_x_mm},"
            f"{self.offset_y_mm})"
        )

    # ------------------------------------------------------------------ params

    def _declare_parameters(self) -> None:
        # Topics
        self.declare_parameter("detection_topic", "/weedbot/detections")
        self.declare_parameter("status_topic", "/weedbot/control/status")
        self.declare_parameter("debug_topic", "/weedbot/control/debug")

        # Mode / arming
        self.declare_parameter("mode", MODE_DRY_RUN)
        self.declare_parameter("armed", False)
        self.declare_parameter("auto_fire_enabled", True)

        # Target selection / gating
        self.declare_parameter("min_confidence", 0.60)
        self.declare_parameter("target_policy", "highest_confidence")
        self.declare_parameter("shot_cooldown_ms", 220.0)
        self.declare_parameter("duplicate_radius_mm", 15.0)
        self.declare_parameter("duplicate_holdoff_ms", 600.0)

        # Firing parameters
        self.declare_parameter("dwell_ms", 500)
        self.declare_parameter("power_permille", 750)

        # Coordinate frame
        self.declare_parameter("sign_flip_x", True)
        self.declare_parameter("sign_flip_y", True)
        self.declare_parameter("cam_to_galvo_offset_x_mm", 0.0)
        self.declare_parameter("cam_to_galvo_offset_y_mm", 0.0)
        self.declare_parameter("bounds_x_min_mm", -250.0)
        self.declare_parameter("bounds_x_max_mm", 250.0)
        self.declare_parameter("bounds_y_min_mm", -250.0)
        self.declare_parameter("bounds_y_max_mm", 250.0)

        # Queue management
        self.declare_parameter("queue_max_outstanding", 14)
        self.declare_parameter("ack_timeout_ms", 10000)

        # Serial transport
        self.declare_parameter("serial_port", "/dev/ttyUSB0")
        self.declare_parameter("serial_baudrate", 115200)
        self.declare_parameter("serial_read_timeout_s", 0.02)
        self.declare_parameter("serial_reconnect_s", 2.0)
        self.declare_parameter("serial_poll_hz", 50.0)

    def _load_parameters(self) -> None:
        p = self.get_parameter
        self.detection_topic = str(p("detection_topic").value)
        self.status_topic = str(p("status_topic").value)
        self.debug_topic = str(p("debug_topic").value)

        mode_raw = str(p("mode").value).strip().upper()
        if mode_raw not in (MODE_DRY_RUN, MODE_LIVE):
            self.get_logger().warn(
                f"Unknown mode '{mode_raw}', defaulting to {MODE_DRY_RUN}"
            )
            mode_raw = MODE_DRY_RUN
        self.mode = mode_raw
        self.armed = bool(p("armed").value)
        self.auto_fire_enabled = bool(p("auto_fire_enabled").value)

        self.min_confidence = float(p("min_confidence").value)
        self.target_policy = str(p("target_policy").value)
        self.shot_cooldown_ms = float(p("shot_cooldown_ms").value)
        self.duplicate_radius_mm = float(p("duplicate_radius_mm").value)
        self.duplicate_holdoff_ms = float(p("duplicate_holdoff_ms").value)

        self.dwell_ms = int(p("dwell_ms").value)
        self.power_permille = int(p("power_permille").value)

        self.sign_flip_x = bool(p("sign_flip_x").value)
        self.sign_flip_y = bool(p("sign_flip_y").value)
        self.offset_x_mm = float(p("cam_to_galvo_offset_x_mm").value)
        self.offset_y_mm = float(p("cam_to_galvo_offset_y_mm").value)
        self.bounds_x_min_mm = float(p("bounds_x_min_mm").value)
        self.bounds_x_max_mm = float(p("bounds_x_max_mm").value)
        self.bounds_y_min_mm = float(p("bounds_y_min_mm").value)
        self.bounds_y_max_mm = float(p("bounds_y_max_mm").value)

        self.queue_max_outstanding = int(p("queue_max_outstanding").value)
        self.ack_timeout_ms = int(p("ack_timeout_ms").value)

        self.serial_port = str(p("serial_port").value)
        self.serial_baudrate = int(p("serial_baudrate").value)
        self.serial_read_timeout_s = float(p("serial_read_timeout_s").value)
        self.serial_reconnect_s = float(p("serial_reconnect_s").value)
        self.serial_poll_hz = float(p("serial_poll_hz").value)

    def _on_set_parameters(self, params) -> SetParametersResult:
        for param in params:
            if param.name == "armed":
                new_state = bool(param.value)
                if new_state == self.armed:
                    continue
                self.armed = new_state
                self.get_logger().warn(f"armed -> {self.armed}")
                if self.armed:
                    self._send_startup_handshake()
                else:
                    self.serial.send_line(build_arm(False))
            elif param.name == "auto_fire_enabled":
                self.auto_fire_enabled = bool(param.value)
            elif param.name == "dwell_ms":
                self.dwell_ms = int(param.value)
            elif param.name == "power_permille":
                self.power_permille = int(param.value)
            elif param.name == "min_confidence":
                self.min_confidence = float(param.value)
            elif param.name == "sign_flip_x":
                self.sign_flip_x = bool(param.value)
            elif param.name == "sign_flip_y":
                self.sign_flip_y = bool(param.value)
            elif param.name == "cam_to_galvo_offset_x_mm":
                self.offset_x_mm = float(param.value)
                self._push_offset()
            elif param.name == "cam_to_galvo_offset_y_mm":
                self.offset_y_mm = float(param.value)
                self._push_offset()
        return SetParametersResult(successful=True)

    # ---------------------------------------------------------------- startup

    def _send_startup_handshake(self) -> None:
        """On arm, send `$ARM,1` immediately followed by `$OFFSET,x,y`."""
        self.serial.send_line(build_arm(True))
        self._push_offset()

    def _push_offset(self) -> None:
        self.serial.send_line(build_offset(self.offset_x_mm, self.offset_y_mm))

    # -------------------------------------------------------------- detection

    def _detection_callback(self, msg: WeedArray) -> None:
        if not self.auto_fire_enabled:
            return
        target = self._select_target(msg)
        if target is None:
            return
        self._issue_shot(target)

    def _select_target(self, msg: WeedArray) -> Optional[Target]:
        candidates = []
        for det in msg.detections:
            cand = self._detection_to_target(det)
            if cand is not None:
                candidates.append(cand)
        if not candidates:
            return None
        if self.target_policy == "nearest_center":
            return min(candidates, key=lambda t: math.hypot(t.mm_x, t.mm_y))
        return max(candidates, key=lambda t: t.confidence)

    def _detection_to_target(self, det) -> Optional[Target]:
        if not det.confidences:
            return None
        confidence = float(det.confidences[0])
        if confidence < self.min_confidence:
            return None

        # meristem = bbox center in real world, in meters (from homography)
        real_x_m = float(det.real_world_x)
        real_y_m = float(det.real_world_y)

        mm_x_vision = real_x_m * 1000.0
        mm_y_vision = real_y_m * 1000.0

        mm_x = -mm_x_vision if self.sign_flip_x else mm_x_vision
        mm_y = -mm_y_vision if self.sign_flip_y else mm_y_vision

        class_id = int(det.class_ids[0]) if det.class_ids else -1
        return Target(mm_x=mm_x, mm_y=mm_y, confidence=confidence, class_id=class_id)

    # --------------------------------------------------------------- firing

    def _issue_shot(self, target: Target) -> bool:
        if not self.armed:
            self._shots_blocked_safety += 1
            return False

        # Bounds check accounts for camera->galvo offset (applied by firmware).
        reachable_x = target.mm_x - self.offset_x_mm
        reachable_y = target.mm_y - self.offset_y_mm
        if not (self.bounds_x_min_mm <= reachable_x <= self.bounds_x_max_mm and
                self.bounds_y_min_mm <= reachable_y <= self.bounds_y_max_mm):
            self._shots_blocked_bounds += 1
            self.get_logger().warn(
                f"target ({target.mm_x:.1f},{target.mm_y:.1f}) mm rejected: "
                f"reachable ({reachable_x:.1f},{reachable_y:.1f}) outside bounds"
            )
            return False

        now = time.monotonic()
        if now - self._last_shot_at < (self.shot_cooldown_ms / 1000.0):
            self._shots_blocked_rate += 1
            return False

        if self._last_target_mm is not None:
            dx = target.mm_x - self._last_target_mm[0]
            dy = target.mm_y - self._last_target_mm[1]
            if (math.hypot(dx, dy) < self.duplicate_radius_mm
                    and now - self._last_shot_at
                    < (self.duplicate_holdoff_ms / 1000.0)):
                self._shots_blocked_rate += 1
                return False

        if len(self._outstanding) >= self.queue_max_outstanding:
            self._shots_blocked_queue += 1
            return False

        dwell = int(clamp(float(self.dwell_ms), 0.0, 5000.0))
        power = int(clamp(float(self.power_permille), 0.0, 1000.0))
        seq = self._next_seq()
        packet = build_fire(seq, target.mm_x, target.mm_y, dwell, power)

        if not self.serial.send_line(packet):
            return False

        self._outstanding.add(seq)
        self._last_shot_at = now
        self._last_target_mm = (target.mm_x, target.mm_y)
        self._shots_sent += 1
        self._publish_debug({
            "event": "shot_sent",
            "seq": seq,
            "mm_x": round(target.mm_x, 2),
            "mm_y": round(target.mm_y, 2),
            "dwell_ms": dwell,
            "power_permille": power,
            "confidence": round(target.confidence, 4),
            "packet": packet.strip("\n"),
        })
        return True

    def _next_seq(self) -> int:
        self._shot_seq = (self._shot_seq + 1) & 0xFFFF
        if self._shot_seq == 0:
            self._shot_seq = 1
        return self._shot_seq

    # ---------------------------------------------------------------- serial

    def _serial_poll(self) -> None:
        self.serial.ensure_connected()
        for line in self.serial.read_lines():
            self._serial_lines_rx += 1
            self._handle_reply(line)

    def _handle_reply(self, line: str) -> None:
        self.get_logger().info(f"RX: {line}")
        if line.startswith("ACK"):
            parts = line.split(",")
            if len(parts) >= 2:
                try:
                    seq = int(parts[1])
                    self._outstanding.discard(seq)
                    self._last_ack_seq = seq
                except ValueError:
                    pass
        elif line.startswith("ERR"):
            parts = line.split(",", 2)
            if len(parts) >= 2:
                try:
                    seq = int(parts[1])
                    self._outstanding.discard(seq)
                except ValueError:
                    pass
            self._last_err = line
            self.get_logger().warn(f"STM32 error: {line}")
        elif line.startswith("BOOT"):
            self.get_logger().info("STM32 booted")

    # -------------------------------------------------------------- telemetry

    def _publish_status(self) -> None:
        status = {
            "mode": self.mode,
            "armed": self.armed,
            "auto_fire_enabled": self.auto_fire_enabled,
            "serial_connected": self.serial.connected,
            "shots_sent": self._shots_sent,
            "outstanding": len(self._outstanding),
            "blocked_safety": self._shots_blocked_safety,
            "blocked_rate": self._shots_blocked_rate,
            "blocked_bounds": self._shots_blocked_bounds,
            "blocked_queue": self._shots_blocked_queue,
            "serial_lines_rx": self._serial_lines_rx,
            "last_ack_seq": self._last_ack_seq,
            "last_err": self._last_err,
        }
        msg = String()
        msg.data = json.dumps(status, separators=(",", ":"))
        self.status_pub.publish(msg)

    def _publish_debug(self, payload: dict) -> None:
        msg = String()
        msg.data = json.dumps(payload, separators=(",", ":"))
        self.debug_pub.publish(msg)

    # -------------------------------------------------------------- shutdown

    def _handle_sigint(self, signum, frame) -> None:
        # The firmware watchdog is currently disabled; we MUST disarm on exit
        # or the laser can be left hot.
        self.get_logger().warn(f"signal {signum} received, disarming")
        self._graceful_disarm()
        rclpy.shutdown()

    def _graceful_disarm(self) -> None:
        try:
            self.serial.send_line_blocking_sync(build_arm(False))
        except Exception as exc:  # pragma: no cover - best effort
            self.get_logger().error(f"disarm send failed: {exc}")
        self.serial.close()

    def destroy_node(self) -> bool:
        self._graceful_disarm()
        return super().destroy_node()


def main(args=None) -> None:
    rclpy.init(args=args)
    node = ControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
