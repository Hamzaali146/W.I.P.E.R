#!/usr/bin/env python3
"""Control node that converts vision detections into STM32 shot commands."""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass
from typing import Optional, Tuple

import rclpy
from rcl_interfaces.msg import SetParametersResult
from rclpy.node import Node
from std_msgs.msg import String
from weedbot_interfaces.msg import WeedArray

try:
    import serial
    from serial import SerialException
except ImportError:  # pragma: no cover - handled at runtime on target machine
    serial = None

    class SerialException(Exception):
        """Fallback exception when pyserial is not installed."""


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Clamp a numeric value to a closed interval."""
    return max(min_value, min(max_value, value))


@dataclass
class TargetCandidate:
    """Candidate target extracted from one detection."""

    pixel_x: float
    pixel_y: float
    confidence: float
    class_id: int
    real_x: float
    real_y: float
    center_distance_px: float


class AsciiShotProtocol:
    """Simple framed ASCII protocol with XOR checksum."""

    @staticmethod
    def checksum(payload: str) -> int:
        """Compute XOR checksum over ASCII payload bytes."""
        value = 0
        for byte in payload.encode("ascii", errors="ignore"):
            value ^= byte
        return value

    @classmethod
    def frame(cls, payload: str) -> str:
        """Wrap payload as `$PAYLOAD*CS` line."""
        cs = cls.checksum(payload)
        return f"${payload}*{cs:02X}\n"

    @classmethod
    def shot(
        cls,
        seq: int,
        dac_x: int,
        dac_y: int,
        settle_us: int,
        fire_us: int,
        power_permille: int,
    ) -> str:
        """Build a `SHOT` packet."""
        payload = (
            f"SHOT,{seq},{dac_x},{dac_y},{settle_us},{fire_us},{power_permille}"
        )
        return cls.frame(payload)

    @classmethod
    def arm(cls, armed: bool) -> str:
        """Build an `ARM` packet."""
        state = 1 if armed else 0
        return cls.frame(f"ARM,{state}")

    @classmethod
    def target(cls, seq: int, dx_px: float, dy_px: float) -> str:
        """Build a TARGET packet with pixel offsets from camera centre.

        dx_px > 0  → weed is to the RIGHT of centre
        dy_px > 0  → weed is BELOW centre (image Y axis)
        STM32 uses these offsets to drive its actuator toward the weed.
        """
        payload = f"TARGET,{seq},{dx_px:.2f},{dy_px:.2f}"
        return cls.frame(payload)


class SerialLink:
    """Best-effort serial transport with reconnect logic."""

    def __init__(
        self,
        node: Node,
        port: str,
        baudrate: int,
        timeout_s: float,
        reconnect_s: float,
        dry_run: bool,
    ) -> None:
        self._node = node
        self._port = port
        self._baudrate = baudrate
        self._timeout_s = timeout_s
        self._reconnect_s = reconnect_s
        self._dry_run = dry_run
        self._serial = None
        self._next_retry_at = 0.0
        self._warned_no_pyserial = False

    @property
    def connected(self) -> bool:
        """Current serial link status."""
        if self._dry_run:
            return True
        return bool(self._serial and self._serial.is_open)

    def ensure_connected(self) -> bool:
        """Connect if disconnected and reconnect interval has elapsed."""
        if self.connected:
            return True

        if self._dry_run:
            return True

        if serial is None:
            if not self._warned_no_pyserial:
                self._node.get_logger().error(
                    "pyserial not installed. Run: pip install pyserial"
                )
                self._warned_no_pyserial = True
            return False

        now = time.monotonic()
        if now < self._next_retry_at:
            return False

        self._next_retry_at = now + self._reconnect_s
        try:
            self._serial = serial.Serial(
                port=self._port,
                baudrate=self._baudrate,
                timeout=self._timeout_s,
                write_timeout=self._timeout_s,
            )
            self._node.get_logger().info(
                f"Serial connected on {self._port} @ {self._baudrate}"
            )
            return True
        except SerialException as exc:
            self._node.get_logger().warn(
                f"Serial connect failed on {self._port}: {exc}"
            )
            self._serial = None
            return False

    def send_line(self, line: str) -> bool:
        """Send one protocol line."""
        if self._dry_run:
            self._node.get_logger().info(f"[DRY RUN] {line.strip()}")
            return True

        if not self.ensure_connected():
            return False

        try:
            assert self._serial is not None
            self._serial.write(line.encode("ascii"))
            self._serial.flush()
            return True
        except (SerialException, OSError) as exc:
            self._node.get_logger().error(f"Serial write failed: {exc}")
            self.close()
            return False

    def read_lines(self, limit: int = 20) -> list[str]:
        """Read up to `limit` newline-delimited lines from serial."""
        lines: list[str] = []
        if self._dry_run or not self.connected:
            return lines

        assert self._serial is not None
        for _ in range(limit):
            try:
                raw = self._serial.readline()
            except (SerialException, OSError) as exc:
                self._node.get_logger().error(f"Serial read failed: {exc}")
                self.close()
                break
            if not raw:
                break
            lines.append(raw.decode("ascii", errors="ignore").strip())
        return lines

    def close(self) -> None:
        """Close serial connection."""
        if self._serial is None:
            return
        try:
            self._serial.close()
        except Exception:  # pragma: no cover - defensive cleanup
            pass
        self._serial = None


class ControlNode(Node):
    """ROS2 control node for laser galvo targeting and firing."""

    def __init__(self) -> None:
        super().__init__("weedbot_control_node")

        self._declare_parameters()
        self._load_parameters()
        self.add_on_set_parameters_callback(self._on_set_parameters)

        self.serial_link = SerialLink(
            node=self,
            port=self.serial_port,
            baudrate=self.serial_baudrate,
            timeout_s=self.serial_timeout_s,
            reconnect_s=self.serial_reconnect_s,
            dry_run=self.dry_run,
        )
        self.serial_link.ensure_connected()

        self.detection_sub = self.create_subscription(
            WeedArray,
            self.detection_topic,
            self._detection_callback,
            10,
        )

        self.manual_sub = None
        if self.enable_manual_topic:
            self.manual_sub = self.create_subscription(
                String,
                self.manual_command_topic,
                self._manual_command_callback,
                10,
            )

        self.status_pub = self.create_publisher(String, self.status_topic, 10)
        self.debug_pub = self.create_publisher(String, self.debug_topic, 10)

        serial_poll_period = 1.0 / max(self.serial_poll_hz, 1.0)
        self.serial_poll_timer = self.create_timer(
            serial_poll_period, self._serial_poll_callback
        )
        self.status_timer = self.create_timer(1.0, self._status_timer_callback)

        self._shot_seq = 0
        self._last_shot_at = 0.0
        self._last_shot_pixel: Optional[Tuple[float, float]] = None
        self._shots_sent = 0
        self._shots_blocked_safety = 0
        self._shots_blocked_rate = 0
        self._serial_lines_rx = 0

        if self.send_arm_packet_on_start:
            self._send_arm_state()

        self.get_logger().info("Control node started")
        self.get_logger().info(
            f"Detection topic={self.detection_topic}, serial={self.serial_port}, "
            f"armed={self.armed}, dry_run={self.dry_run}"
        )

    def _declare_parameters(self) -> None:
        # ROS topics
        self.declare_parameter("detection_topic", "/weedbot/detections")
        self.declare_parameter("status_topic", "/weedbot/control/status")
        self.declare_parameter("debug_topic", "/weedbot/control/debug")
        self.declare_parameter("enable_manual_topic", False)
        self.declare_parameter("manual_command_topic", "/weedbot/laser_command")

        # Safety and firing
        self.declare_parameter("armed", False)
        self.declare_parameter("auto_fire_enabled", True)
        self.declare_parameter("min_confidence", 0.60)
        self.declare_parameter("shot_cooldown_ms", 220.0)
        self.declare_parameter("duplicate_radius_px", 35.0)
        self.declare_parameter("duplicate_holdoff_ms", 600.0)
        self.declare_parameter("fire_duration_ms", 90.0)
        self.declare_parameter("fire_power_percent", 75.0)
        self.declare_parameter("galvo_settle_ms", 12.0)
        self.declare_parameter("target_policy", "highest_confidence")
        self.declare_parameter("use_real_world_gate", False)
        self.declare_parameter("max_abs_real_x_m", 0.80)
        self.declare_parameter("min_forward_real_y_m", 0.10)
        self.declare_parameter("max_forward_real_y_m", 2.50)

        # Pixel-mode parameters (Phase 1 — no homography/calibration needed)
        self.declare_parameter("use_pixel_mode", True)
        self.declare_parameter("duplicate_radius", 35.0)
        self.declare_parameter("cam_cx_rw_m", 0.0)
        self.declare_parameter("cam_cy_rw_m", 0.0)

        # Camera and angle model
        self.declare_parameter("camera_width", 1280)
        self.declare_parameter("camera_height", 720)
        self.declare_parameter("camera_fov_x_deg", 80.0)
        self.declare_parameter("camera_fov_y_deg", 50.0)
        self.declare_parameter("invert_x", False)
        self.declare_parameter("invert_y", False)
        self.declare_parameter("galvo_x_max_deg", 20.0)
        self.declare_parameter("galvo_y_max_deg", 20.0)

        # Voltage and DAC conversion model
        self.declare_parameter("dac_bits", 16)
        self.declare_parameter("dac_vref", 5.0)
        self.declare_parameter("x_min_voltage", 1.00)
        self.declare_parameter("x_center_voltage", 2.50)
        self.declare_parameter("x_max_voltage", 4.00)
        self.declare_parameter("y_min_voltage", 1.00)
        self.declare_parameter("y_center_voltage", 2.50)
        self.declare_parameter("y_max_voltage", 4.00)

        # Serial transport
        self.declare_parameter("serial_port", "COM5")
        self.declare_parameter("serial_baudrate", 115200)
        self.declare_parameter("serial_timeout_s", 0.02)
        self.declare_parameter("serial_reconnect_s", 2.0)
        self.declare_parameter("serial_poll_hz", 50.0)
        self.declare_parameter("dry_run", True)
        self.declare_parameter("send_arm_packet_on_start", True)

    def _load_parameters(self) -> None:
        # Topics
        self.detection_topic = str(self.get_parameter("detection_topic").value)
        self.status_topic = str(self.get_parameter("status_topic").value)
        self.debug_topic = str(self.get_parameter("debug_topic").value)
        self.enable_manual_topic = bool(
            self.get_parameter("enable_manual_topic").value
        )
        self.manual_command_topic = str(
            self.get_parameter("manual_command_topic").value
        )

        # Safety and firing
        self.armed = bool(self.get_parameter("armed").value)
        self.auto_fire_enabled = bool(self.get_parameter("auto_fire_enabled").value)
        self.min_confidence = float(self.get_parameter("min_confidence").value)
        self.shot_cooldown_ms = float(self.get_parameter("shot_cooldown_ms").value)
        # duplicate_radius replaces the old duplicate_radius_px — same unit when
        # use_pixel_mode is true (pixels), metres when false.
        self.duplicate_radius_px = float(self.get_parameter("duplicate_radius").value)
        self.duplicate_holdoff_ms = float(
            self.get_parameter("duplicate_holdoff_ms").value
        )
        self.fire_duration_ms = float(self.get_parameter("fire_duration_ms").value)
        self.fire_power_percent = float(
            self.get_parameter("fire_power_percent").value
        )
        self.galvo_settle_ms = float(self.get_parameter("galvo_settle_ms").value)
        self.target_policy = str(self.get_parameter("target_policy").value)
        self.use_real_world_gate = bool(self.get_parameter("use_real_world_gate").value)
        self.max_abs_real_x_m = float(self.get_parameter("max_abs_real_x_m").value)
        self.min_forward_real_y_m = float(
            self.get_parameter("min_forward_real_y_m").value
        )
        self.max_forward_real_y_m = float(
            self.get_parameter("max_forward_real_y_m").value
        )

        # Pixel-mode (Phase 1)
        self.use_pixel_mode = bool(self.get_parameter("use_pixel_mode").value)
        self.cam_cx_rw_m = float(self.get_parameter("cam_cx_rw_m").value)
        self.cam_cy_rw_m = float(self.get_parameter("cam_cy_rw_m").value)

        # Camera and angle model
        self.camera_width = int(self.get_parameter("camera_width").value)
        self.camera_height = int(self.get_parameter("camera_height").value)
        self.camera_fov_x_deg = float(self.get_parameter("camera_fov_x_deg").value)
        self.camera_fov_y_deg = float(self.get_parameter("camera_fov_y_deg").value)
        self.invert_x = bool(self.get_parameter("invert_x").value)
        self.invert_y = bool(self.get_parameter("invert_y").value)
        self.galvo_x_max_deg = float(self.get_parameter("galvo_x_max_deg").value)
        self.galvo_y_max_deg = float(self.get_parameter("galvo_y_max_deg").value)

        # Voltage and DAC model
        self.dac_bits = int(self.get_parameter("dac_bits").value)
        self.dac_vref = float(self.get_parameter("dac_vref").value)
        self.x_min_voltage = float(self.get_parameter("x_min_voltage").value)
        self.x_center_voltage = float(self.get_parameter("x_center_voltage").value)
        self.x_max_voltage = float(self.get_parameter("x_max_voltage").value)
        self.y_min_voltage = float(self.get_parameter("y_min_voltage").value)
        self.y_center_voltage = float(self.get_parameter("y_center_voltage").value)
        self.y_max_voltage = float(self.get_parameter("y_max_voltage").value)

        # Serial transport
        self.serial_port = str(self.get_parameter("serial_port").value)
        self.serial_baudrate = int(self.get_parameter("serial_baudrate").value)
        self.serial_timeout_s = float(self.get_parameter("serial_timeout_s").value)
        self.serial_reconnect_s = float(
            self.get_parameter("serial_reconnect_s").value
        )
        self.serial_poll_hz = float(self.get_parameter("serial_poll_hz").value)
        self.dry_run = bool(self.get_parameter("dry_run").value)
        self.send_arm_packet_on_start = bool(
            self.get_parameter("send_arm_packet_on_start").value
        )

    def _on_set_parameters(self, params) -> SetParametersResult:
        for param in params:
            if param.name == "armed":
                self.armed = bool(param.value)
                self.get_logger().warn(f"Laser armed state changed: {self.armed}")
                self._send_arm_state()
            elif param.name == "auto_fire_enabled":
                self.auto_fire_enabled = bool(param.value)
                self.get_logger().info(
                    f"Auto fire changed: {self.auto_fire_enabled}"
                )
        return SetParametersResult(successful=True)

    def _send_arm_state(self) -> None:
        packet = AsciiShotProtocol.arm(self.armed)
        self.serial_link.send_line(packet)

    def _send_target_packet(self, target: TargetCandidate) -> None:
        """Compute pixel offset from camera centre and send a TARGET packet."""
        cam_cx = self.camera_width / 2.0
        cam_cy = self.camera_height / 2.0

        # Offset of weed centre from camera centre in pixels.
        # dx > 0 → weed is right of centre; dy > 0 → weed is below centre.
        dx_px = target.pixel_x - cam_cx
        dy_px = target.pixel_y - cam_cy

        seq = self._next_sequence()
        packet = AsciiShotProtocol.target(seq, dx_px, dy_px)

        sent = self.serial_link.send_line(packet)
        self._publish_debug(
            {
                "event": "target_sent",
                "seq": seq,
                "sent": sent,
                "confidence": round(target.confidence, 4),
                "weed_px": [round(target.pixel_x, 2), round(target.pixel_y, 2)],
                "cam_center_px": [cam_cx, cam_cy],
                "dx_px": round(dx_px, 2),
                "dy_px": round(dy_px, 2),
            }
        )
        self.get_logger().info(
            f"TARGET seq={seq} dx={dx_px:.1f}px dy={dy_px:.1f}px "
            f"conf={target.confidence:.3f} sent={sent}"
        )

    def _detection_callback(self, msg: WeedArray) -> None:
        if not self.auto_fire_enabled:
            return

        target = self._select_target(msg)
        if target is None:
            return

        self._send_target_packet(target)

    def _manual_command_callback(self, msg: String) -> None:
        try:
            payload = json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().warn("Manual command ignored: invalid JSON")
            return

        action = str(payload.get("action", "")).strip().lower()
        if action == "arm":
            self.armed = True
            self._send_arm_state()
            return
        if action == "disarm":
            self.armed = False
            self._send_arm_state()
            return
        if action != "fire":
            return

        mode = str(payload.get("mode", "pixel")).strip().lower()
        if mode == "pixel":
            pixel_x = float(payload.get("x_pixel", payload.get("x", 0.0)))
            pixel_y = float(payload.get("y_pixel", payload.get("y", 0.0)))
        elif mode == "normalized":
            x_norm = float(payload.get("x", 0.0))
            y_norm = float(payload.get("y", 0.0))
            pixel_x = x_norm * self.camera_width
            pixel_y = y_norm * self.camera_height
        else:
            self.get_logger().warn(
                "Manual fire ignored. Supported mode values: pixel, normalized"
            )
            return

        duration_ms = float(payload.get("duration_ms", self.fire_duration_ms))
        power_percent = float(payload.get("power_percent", self.fire_power_percent))
        manual_target = TargetCandidate(
            pixel_x=pixel_x,
            pixel_y=pixel_y,
            confidence=1.0,
            class_id=-1,
            real_x=0.0,
            real_y=0.0,
            center_distance_px=0.0,
        )
        self._issue_shot(
            manual_target,
            source="manual",
            duration_ms=duration_ms,
            power_percent=power_percent,
        )

    def _select_target(self, msg: WeedArray) -> Optional[TargetCandidate]:
        candidates: list[TargetCandidate] = []
        for det in msg.detections:
            candidate = self._candidate_from_detection(det)
            if candidate is not None:
                candidates.append(candidate)

        if not candidates:
            return None

        if self.target_policy == "nearest_center":
            return min(candidates, key=lambda item: item.center_distance_px)

        if self.target_policy not in ("highest_confidence", "nearest_center"):
            self.get_logger().warn(
                f"Unknown target_policy={self.target_policy}, using highest_confidence"
            )
        return max(candidates, key=lambda item: item.confidence)

    def _candidate_from_detection(self, det) -> Optional[TargetCandidate]:
        if not det.confidences:
            return None
        confidence = float(det.confidences[0])
        if confidence < self.min_confidence:
            return None

        if not det.bbox_x or not det.bbox_y or not det.bbox_w or not det.bbox_h:
            return None

        center_x_norm = float(det.bbox_x[0]) + (float(det.bbox_w[0]) * 0.5)
        center_y_norm = float(det.bbox_y[0]) + (float(det.bbox_h[0]) * 0.5)
        if not 0.0 <= center_x_norm <= 1.0 or not 0.0 <= center_y_norm <= 1.0:
            return None

        real_x = float(det.real_world_x)
        real_y = float(det.real_world_y)
        if self.use_real_world_gate:
            if abs(real_x) > self.max_abs_real_x_m:
                return None
            if real_y < self.min_forward_real_y_m or real_y > self.max_forward_real_y_m:
                return None

        pixel_x = center_x_norm * float(self.camera_width)
        pixel_y = center_y_norm * float(self.camera_height)
        dx = pixel_x - (0.5 * float(self.camera_width))
        dy = pixel_y - (0.5 * float(self.camera_height))
        class_id = int(det.class_ids[0]) if det.class_ids else -1

        return TargetCandidate(
            pixel_x=pixel_x,
            pixel_y=pixel_y,
            confidence=confidence,
            class_id=class_id,
            real_x=real_x,
            real_y=real_y,
            center_distance_px=math.hypot(dx, dy),
        )

    def _issue_shot(
        self,
        target: TargetCandidate,
        source: str,
        duration_ms: Optional[float] = None,
        power_percent: Optional[float] = None,
    ) -> bool:
        if not self.armed:
            self._shots_blocked_safety += 1
            return False

        now = time.monotonic()
        cooldown_s = self.shot_cooldown_ms / 1000.0
        if now - self._last_shot_at < cooldown_s:
            self._shots_blocked_rate += 1
            return False

        if self._last_shot_pixel is not None:
            dx = target.pixel_x - self._last_shot_pixel[0]
            dy = target.pixel_y - self._last_shot_pixel[1]
            distance = math.hypot(dx, dy)
            holdoff_s = self.duplicate_holdoff_ms / 1000.0
            if distance < self.duplicate_radius_px and now - self._last_shot_at < holdoff_s:
                self._shots_blocked_rate += 1
                return False

        x_angle_deg, y_angle_deg = self._pixel_to_angles(target.pixel_x, target.pixel_y)
        x_voltage = self._angle_to_voltage(
            x_angle_deg,
            self.galvo_x_max_deg,
            self.x_min_voltage,
            self.x_center_voltage,
            self.x_max_voltage,
        )
        y_voltage = self._angle_to_voltage(
            y_angle_deg,
            self.galvo_y_max_deg,
            self.y_min_voltage,
            self.y_center_voltage,
            self.y_max_voltage,
        )
        dac_x = self._voltage_to_dac_code(x_voltage)
        dac_y = self._voltage_to_dac_code(y_voltage)

        effective_duration_ms = (
            self.fire_duration_ms if duration_ms is None else duration_ms
        )
        effective_power_percent = (
            self.fire_power_percent if power_percent is None else power_percent
        )

        settle_us = int(max(self.galvo_settle_ms, 0.0) * 1000.0)
        fire_us = int(max(effective_duration_ms, 0.0) * 1000.0)
        power = clamp(float(effective_power_percent), 0.0, 100.0)
        power_permille = int(round(power * 10.0))

        sequence = self._next_sequence()
        packet = AsciiShotProtocol.shot(
            seq=sequence,
            dac_x=dac_x,
            dac_y=dac_y,
            settle_us=settle_us,
            fire_us=fire_us,
            power_permille=power_permille,
        )

        if not self.serial_link.send_line(packet):
            return False

        self._last_shot_at = now
        self._last_shot_pixel = (target.pixel_x, target.pixel_y)
        self._shots_sent += 1
        self._publish_debug(
            {
                "event": "shot_sent",
                "source": source,
                "seq": sequence,
                "confidence": round(target.confidence, 4),
                "class_id": int(target.class_id),
                "pixel_x": round(target.pixel_x, 2),
                "pixel_y": round(target.pixel_y, 2),
                "angle_x_deg": round(x_angle_deg, 3),
                "angle_y_deg": round(y_angle_deg, 3),
                "voltage_x": round(x_voltage, 4),
                "voltage_y": round(y_voltage, 4),
                "dac_x": dac_x,
                "dac_y": dac_y,
                "duration_ms": fire_us / 1000.0,
                "power_percent": power,
            }
        )
        return True

    def _pixel_to_angles(self, pixel_x: float, pixel_y: float) -> Tuple[float, float]:
        x_norm = (pixel_x / float(self.camera_width)) - 0.5
        y_norm = 0.5 - (pixel_y / float(self.camera_height))

        x_angle = x_norm * self.camera_fov_x_deg
        y_angle = y_norm * self.camera_fov_y_deg

        if self.invert_x:
            x_angle = -x_angle
        if self.invert_y:
            y_angle = -y_angle

        x_angle = clamp(x_angle, -self.galvo_x_max_deg, self.galvo_x_max_deg)
        y_angle = clamp(y_angle, -self.galvo_y_max_deg, self.galvo_y_max_deg)
        return x_angle, y_angle

    @staticmethod
    def _angle_to_voltage(
        angle_deg: float,
        max_angle_deg: float,
        min_voltage: float,
        center_voltage: float,
        max_voltage: float,
    ) -> float:
        if max_angle_deg <= 0.0:
            return center_voltage

        normalized = clamp(angle_deg / max_angle_deg, -1.0, 1.0)
        if normalized >= 0.0:
            voltage = center_voltage + normalized * (max_voltage - center_voltage)
        else:
            voltage = center_voltage + normalized * (center_voltage - min_voltage)
        return clamp(voltage, min_voltage, max_voltage)

    def _voltage_to_dac_code(self, voltage: float) -> int:
        max_code = (1 << self.dac_bits) - 1
        safe_voltage = clamp(voltage, 0.0, self.dac_vref)
        code = int(round((safe_voltage / self.dac_vref) * max_code))
        return int(clamp(float(code), 0.0, float(max_code)))

    def _next_sequence(self) -> int:
        self._shot_seq = (self._shot_seq + 1) & 0xFFFF
        return self._shot_seq

    def _serial_poll_callback(self) -> None:
        self.serial_link.ensure_connected()
        for line in self.serial_link.read_lines():
            self._serial_lines_rx += 1
            if line.startswith("ACK"):
                self.get_logger().debug(f"STM32 {line}")
            elif line.startswith("ERR"):
                self.get_logger().warn(f"STM32 {line}")
            else:
                self.get_logger().info(f"STM32 {line}")

    def _status_timer_callback(self) -> None:
        status = {
            "armed": self.armed,
            "auto_fire_enabled": self.auto_fire_enabled,
            "serial_connected": self.serial_link.connected,
            "shots_sent": self._shots_sent,
            "blocked_safety": self._shots_blocked_safety,
            "blocked_rate": self._shots_blocked_rate,
            "serial_lines_rx": self._serial_lines_rx,
        }
        msg = String()
        msg.data = json.dumps(status, separators=(",", ":"))
        self.status_pub.publish(msg)

    def _publish_debug(self, payload: dict) -> None:
        msg = String()
        msg.data = json.dumps(payload, separators=(",", ":"))
        self.debug_pub.publish(msg)

    def destroy_node(self) -> bool:
        self.serial_link.close()
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
        rclpy.shutdown()


if __name__ == "__main__":
    main() 
