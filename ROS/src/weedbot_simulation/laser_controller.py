#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from builtin_interfaces.msg import Duration
import math

# Import your custom message type
# from weedbot_vision.msg import WeedArray  # Adjust based on your actual message

class LaserController(Node):
    def __init__(self):
        super().__init__('laser_controller')
        
        # Parameters
        self.declare_parameter('camera_fov', 80.0)
        self.declare_parameter('image_width', 1280)
        self.declare_parameter('laser_range', 1.5)
        self.declare_parameter('firing_duration', 0.5)
        
        self.camera_fov = self.get_parameter('camera_fov').value
        self.image_width = self.get_parameter('image_width').value
        self.laser_range = self.get_parameter('laser_range').value
        self.firing_duration = self.get_parameter('firing_duration').value
        
        # Publishers
        self.galvo_pub = self.create_publisher(Float64, '/galvo_x_joint/command', 10)
        self.laser_marker_pub = self.create_publisher(Marker, '/laser_beam', 10)
        
        # Subscribers
        # Uncomment when you have the actual message type
        # self.detection_sub = self.create_subscription(
        #     WeedArray,
        #     '/weedbot/detections',
        #     self.detection_callback,
        #     10
        # )
        
        # State
        self.current_angle = 0.0
        self.firing = False
        self.fire_timer = None
        
        self.get_logger().info('Laser Controller initialized')
        self.get_logger().info(f'Camera FOV: {self.camera_fov}°')
        self.get_logger().info(f'Laser range: {self.laser_range}m')
        
    def detection_callback(self, msg):
        """Process weed detections and control laser"""
        if len(msg.weeds) == 0:
            return
            
        # Get the closest weed
        closest_weed = None
        min_distance = float('inf')
        
        for weed in msg.weeds:
            distance = self.estimate_distance(weed)
            if distance < min_distance:
                min_distance = distance
                closest_weed = weed
        
        if closest_weed and min_distance < self.laser_range:
            # Calculate galvo angle
            target_angle = self.pixel_to_angle(closest_weed.x_center)
            
            # Move galvo
            self.move_galvo(target_angle)
            
            # Fire laser
            self.fire_laser(closest_weed)
            
    def pixel_to_angle(self, pixel_x):
        """Convert pixel position to galvo angle"""
        normalized = (pixel_x / self.image_width) - 0.5
        fov_rad = math.radians(self.camera_fov)
        angle = normalized * fov_rad
        
        # Clamp to galvo limits
        max_angle = math.radians(45)
        angle = max(min(angle, max_angle), -max_angle)
        
        return angle
        
    def estimate_distance(self, weed):
        """Estimate distance to weed"""
        bbox_height = weed.height
        focal_length = 1000
        real_height = 0.15
        
        if bbox_height > 0:
            distance = (real_height * focal_length) / bbox_height
            return distance
        return float('inf')
        
    def move_galvo(self, target_angle):
        """Move galvo mirror"""
        msg = Float64()
        msg.data = target_angle
        self.galvo_pub.publish(msg)
        self.current_angle = target_angle
        self.get_logger().info(f'Galvo: {math.degrees(target_angle):.2f}°')
        
    def fire_laser(self, weed):
        """Fire laser at weed"""
        if self.firing:
            return
            
        self.firing = True
        self.get_logger().info(f'FIRING LASER (conf: {weed.confidence:.2f})')
        
        # Visualize laser
        self.visualize_laser_beam()
        
        # Schedule laser off
        self.fire_timer = self.create_timer(
            self.firing_duration,
            self.stop_laser
        )
        
    def visualize_laser_beam(self):
        """Create laser beam visualization"""
        marker = Marker()
        marker.header.frame_id = "laser_pointer"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "laser_beam"
        marker.id = 0
        marker.type = Marker.CYLINDER
        marker.action = Marker.ADD
        
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = -0.5
        marker.pose.orientation.w = 1.0
        
        marker.scale.x = 0.02
        marker.scale.y = 0.02
        marker.scale.z = 1.0
        
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 0.8
        
        # Set lifetime
        duration = Duration()
        duration.sec = int(self.firing_duration)
        duration.nanosec = int((self.firing_duration % 1) * 1e9)
        marker.lifetime = duration
        
        self.laser_marker_pub.publish(marker)
        
    def stop_laser(self):
        """Stop laser firing"""
        self.firing = False
        if self.fire_timer:
            self.fire_timer.cancel()
            self.fire_timer = None
        self.get_logger().info('Laser OFF')

def main(args=None):
    rclpy.init(args=args)
    node = LaserController()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()