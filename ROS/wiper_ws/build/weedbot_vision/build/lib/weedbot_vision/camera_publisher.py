#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time
import pyrealsense2 as rs
import numpy as np


class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')

        self.declare_parameter("camera_source", "0")
        self.declare_parameter("reconnect_interval", 5.0)
        self.declare_parameter("frame_rate", 30.0)

        source = self.get_parameter("camera_source").get_parameter_value().string_value
        self.reconnect_interval = self.get_parameter("reconnect_interval").value
        frame_rate = self.get_parameter("frame_rate").value

        self.source = source
        self.pipeline = None
        self.cap = None
        self.is_connected = False
        self.last_reconnect_attempt = 0

        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
        self.bridge = CvBridge()

        self.connect_camera()

        timer_period = 1.0 / frame_rate
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info(f"Camera Publisher Started")
        self.get_logger().info(f"Source: {self.source}")
        self.get_logger().info(f"Frame rate: {frame_rate} Hz")

    def connect_camera(self):
        """Attempt to connect to camera"""
        try:
            self.get_logger().info(f"Attempting to connect to camera: {self.source}")

            if self.source == "realsense":
                # RealSense connection
                if self.pipeline is not None:
                    self.pipeline.stop()

                self.pipeline = rs.pipeline()
                config = rs.config()
                config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
                self.pipeline.start(config)

                # Test read
                frames = self.pipeline.wait_for_frames(timeout_ms=5000)
                color_frame = frames.get_color_frame()

                if color_frame:
                    self.is_connected = True
                    self.get_logger().info("RealSense D435i connected successfully!")
                    self.get_logger().info("Resolution: 1280x720 @ 30fps")
                else:
                    self.is_connected = False
                    self.get_logger().error("RealSense opened but failed to read frame")

            else:
                # Original logic for webcam/IP cam fallback
                if self.cap is not None:
                    self.cap.release()

                if isinstance(self.source, str) and ('rtsp://' in self.source or 'http://' in self.source):
                    self.cap = cv2.VideoCapture(self.source, cv2.CAP_FFMPEG)
                    self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                else:
                    src = int(self.source) if self.source.isdigit() else self.source
                    self.cap = cv2.VideoCapture(src)

                if self.cap.isOpened():
                    ret, frame = self.cap.read()
                    if ret:
                        self.is_connected = True
                        self.get_logger().info("Camera connected successfully!")

                        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        fps = self.cap.get(cv2.CAP_PROP_FPS)

                        self.get_logger().info(f"Camera resolution: {width}x{height}")
                        self.get_logger().info(f"Camera FPS: {fps}")
                    else:
                        self.is_connected = False
                        self.get_logger().error("Camera opened but failed to read frame")
                else:
                    self.is_connected = False
                    self.get_logger().error("Failed to open camera")

        except Exception as e:
            self.is_connected = False
            self.get_logger().error(f"Camera connection error: {str(e)}")

    def timer_callback(self):
        """Read and publish camera frame"""
        if not self.is_connected:
            current_time = time.time()
            if current_time - self.last_reconnect_attempt > self.reconnect_interval:
                self.last_reconnect_attempt = current_time
                self.connect_camera()
            return

        try:
            if self.source == "realsense":
                frames = self.pipeline.wait_for_frames(timeout_ms=1000)
                color_frame = frames.get_color_frame()

                if not color_frame:
                    self.get_logger().warn('RealSense read failed, attempting to reconnect...')
                    self.is_connected = False
                    return

                frame = np.asanyarray(color_frame.get_data())

            else:
                ret, frame = self.cap.read()

                if not ret:
                    self.get_logger().warn('Camera read failed, attempting to reconnect...')
                    self.is_connected = False
                    return

            # Unchanged publish logic
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'camera_link'
            self.publisher_.publish(msg)

        except Exception as e:
            self.get_logger().error(f'Frame processing error: {str(e)}')
            self.is_connected = False

    def destroy_node(self):
        """Cleanup on shutdown"""
        if self.source == "realsense" and self.pipeline is not None:
            self.pipeline.stop()
        elif self.cap is not None:
            self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
