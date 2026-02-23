#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class TractorController(Node):
    def __init__(self):
        super().__init__('tractor_controller')
        
        # Parameters
        self.declare_parameter('forward_speed', 0.5)
        self.declare_parameter('field_length', 50.0)
        
        self.forward_speed = self.get_parameter('forward_speed').value
        self.field_length = self.get_parameter('field_length').value
        
        # Publishers
        self.cmd_vel_pub = self.create_publisher(Twist, '/weedbot/cmd_vel', 10)
        
        # Subscribers
        self.odom_sub = self.create_subscription(
            Odometry,
            '/weedbot/odom',
            self.odom_callback,
            10
        )
        
        # State
        self.current_position = 0.0
        self.start_position = None
        self.finished = False
        
        # Control timer
        self.timer = self.create_timer(0.1, self.control_loop)
        
        self.get_logger().info('Tractor Controller initialized')
        self.get_logger().info(f'Speed: {self.forward_speed} m/s')
        self.get_logger().info(f'Field length: {self.field_length} m')
        
    def odom_callback(self, msg):
        """Track tractor position"""
        if self.start_position is None:
            self.start_position = msg.pose.pose.position.x
            
        self.current_position = msg.pose.pose.position.x - self.start_position
        
    def move_forward(self):
        """Command tractor to move forward"""
        cmd = Twist()
        cmd.linear.x = self.forward_speed
        cmd.linear.y = 0.0
        cmd.linear.z = 0.0
        cmd.angular.x = 0.0
        cmd.angular.y = 0.0
        cmd.angular.z = 0.0
        
        self.cmd_vel_pub.publish(cmd)
        
    def stop(self):
        """Stop the tractor"""
        cmd = Twist()
        self.cmd_vel_pub.publish(cmd)
        self.get_logger().info('Tractor STOPPED')
        
    def control_loop(self):
        """Main control loop"""
        if self.finished:
            return
            
        # Check if reached end
        if self.current_position >= self.field_length:
            self.get_logger().info(f'Reached end of field ({self.field_length}m)')
            self.stop()
            self.finished = True
            return
            
        # Move forward
        self.move_forward()
        
        # Log progress every 2 seconds
        if self.current_position > 0:
            progress = (self.current_position / self.field_length) * 100
            self.get_logger().info(
                f'Progress: {progress:.1f}% ({self.current_position:.2f}m)',
                throttle_duration_sec=2.0
            )

def main(args=None):
    rclpy.init(args=args)
    node = TractorController()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()