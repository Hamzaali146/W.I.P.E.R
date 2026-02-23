#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')

        self.declare_parameter("camera_source", "0")
        self.declare_parameter("reconnect_interval", 5.0)  # seconds
        self.declare_parameter("frame_rate", 30.0)  # Hz
        
        source = self.get_parameter("camera_source").get_parameter_value().string_value
        self.reconnect_interval = self.get_parameter("reconnect_interval").value
        frame_rate = self.get_parameter("frame_rate").value

        # Parse source (could be int, IP stream URL, or file path)
        if source.isdigit():
            self.source = int(source)
        else:
            self.source = source

        self.cap = None
        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
        self.bridge = CvBridge()
        
        # Connection status
        self.is_connected = False
        self.last_reconnect_attempt = 0
        
        # Try initial connection
        self.connect_camera()

        # Timer for publishing frames
        timer_period = 1.0 / frame_rate
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info(f"Camera Publisher Started")
        self.get_logger().info(f"Source: {self.source}")
        self.get_logger().info(f"Frame rate: {frame_rate} Hz")

    def connect_camera(self):
        """Attempt to connect to camera"""
        try:
            self.get_logger().info(f"Attempting to connect to camera: {self.source}")
            
            # Release existing capture if any
            if self.cap is not None:
                self.cap.release()
            
            # For IP cameras, we may need special flags
            if isinstance(self.source, str) and ('rtsp://' in self.source or 'http://' in self.source):
                # IP camera stream
                self.cap = cv2.VideoCapture(self.source, cv2.CAP_FFMPEG)
                
                # Set buffer size to reduce latency
                self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            else:
                # Local camera or file
                self.cap = cv2.VideoCapture(self.source)
            
            # Test if camera is opened
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    self.is_connected = True
                    self.get_logger().info("Camera connected successfully!")
                    
                    # Get actual camera properties
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
        # Check if we need to reconnect
        if not self.is_connected:
            current_time = time.time()
            if current_time - self.last_reconnect_attempt > self.reconnect_interval:
                self.last_reconnect_attempt = current_time
                self.connect_camera()
            return
        
        # Try to read frame
        try:
            ret, frame = self.cap.read()
            
            if not ret:
                self.get_logger().warn('Camera read failed, attempting to reconnect...')
                self.is_connected = False
                return
            
            # Convert to ROS message and publish
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'camera_link'
            self.publisher_.publish(msg)
            
        except Exception as e:
            self.get_logger().error(f'Frame processing error: {str(e)}')
            self.is_connected = False

    def destroy_node(self):
        """Cleanup on shutdown"""
        if self.cap is not None:
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