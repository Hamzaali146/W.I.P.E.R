#!/usr/bin/env python3
"""Publishes fake WeedArray detections from a CSV for dry-run testing.

CSV columns (header required):
    label,x_m,y_m,confidence

`x_m` / `y_m` are in the vision homography frame (meters, +right /
+toward-operator). Each row is emitted as a one-detection WeedArray on
`/weedbot/detections` at `publish_rate_hz`. Bounding box fields are
populated with a dummy centered box so selectors that walk bbox_x/y/w/h
don't trip.
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from typing import List

import rclpy
from rclpy.node import Node
from weedbot_interfaces.msg import WeedArray, WeedDetection


@dataclass
class FakeShot:
    label: str
    real_x_m: float
    real_y_m: float
    confidence: float


def load_shots(path: str) -> List[FakeShot]:
    shots: List[FakeShot] = []
    with open(path, "r", newline="") as handle:
        reader = csv.DictReader(
            row for row in handle if row.strip() and not row.lstrip().startswith("#")
        )
        for row in reader:
            shots.append(FakeShot(
                label=row["label"].strip(),
                real_x_m=float(row["x_m"]),
                real_y_m=float(row["y_m"]),
                confidence=float(row["confidence"]),
            ))
    return shots


class LaserTestNode(Node):
    """Cycle through a list of fake shots, one per publish tick."""

    def __init__(self) -> None:
        super().__init__("weedbot_laser_test_node")

        self.declare_parameter("detection_topic", "/weedbot/detections")
        self.declare_parameter("shots_csv", "")
        self.declare_parameter("publish_rate_hz", 1.0)
        self.declare_parameter("loop", True)

        self.detection_topic = str(self.get_parameter("detection_topic").value)
        self.shots_csv = str(self.get_parameter("shots_csv").value)
        self.publish_rate_hz = float(self.get_parameter("publish_rate_hz").value)
        self.loop = bool(self.get_parameter("loop").value)

        if not self.shots_csv or not os.path.isfile(self.shots_csv):
            self.get_logger().error(
                f"shots_csv not found: '{self.shots_csv}' — pass an absolute path"
            )
            self.shots: List[FakeShot] = []
        else:
            self.shots = load_shots(self.shots_csv)
            self.get_logger().info(
                f"loaded {len(self.shots)} fake shots from {self.shots_csv}"
            )

        self.pub = self.create_publisher(WeedArray, self.detection_topic, 10)
        period = 1.0 / max(self.publish_rate_hz, 0.01)
        self.timer = self.create_timer(period, self._tick)
        self._index = 0

    def _tick(self) -> None:
        if not self.shots:
            return
        if self._index >= len(self.shots):
            if not self.loop:
                self.get_logger().info("CSV exhausted; loop=false, stopping timer")
                self.timer.cancel()
                return
            self._index = 0

        shot = self.shots[self._index]
        self._index += 1

        detection = WeedDetection()
        detection.header.stamp = self.get_clock().now().to_msg()
        detection.header.frame_id = "test_shot"
        # Dummy centered bbox (normalized) so any consumer walking bbox_* is safe.
        detection.bbox_x = [0.45]
        detection.bbox_y = [0.45]
        detection.bbox_w = [0.10]
        detection.bbox_h = [0.10]
        detection.confidences = [shot.confidence]
        detection.class_ids = [0]
        detection.real_world_x = shot.real_x_m
        detection.real_world_y = shot.real_y_m
        detection.real_world_z = 0.0

        msg = WeedArray()
        msg.header = detection.header
        msg.detections = [detection]
        msg.total_weeds = 1
        msg.inference_time_ms = 0.0
        self.pub.publish(msg)

        self.get_logger().info(
            f"published fake shot '{shot.label}' x={shot.real_x_m:.3f}m "
            f"y={shot.real_y_m:.3f}m conf={shot.confidence:.2f}"
        )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = LaserTestNode()
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
