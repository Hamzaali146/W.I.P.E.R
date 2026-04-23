#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity
from geometry_msgs.msg import Pose
import random
import os
from ament_index_python.packages import get_package_share_directory

class WeedSpawner(Node):
    def __init__(self):
        super().__init__('weed_spawner')
        
        # Parameters
        self.declare_parameter('num_weeds', 20)
        self.declare_parameter('field_length', 50.0)
        self.declare_parameter('row_spacing', 1.5)
        
        self.num_weeds = self.get_parameter('num_weeds').value
        self.field_length = self.get_parameter('field_length').value
        self.row_spacing = self.get_parameter('row_spacing').value
        
        # Wait for Gazebo spawn service
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn_entity service...')
            
        # Load weed model
        pkg_dir = get_package_share_directory('weedbot_simulation')
        model_path = os.path.join(pkg_dir, 'models', 'weed', 'model.sdf')
        
        with open(model_path, 'r') as f:
            self.weed_sdf = f.read()
            
        self.get_logger().info('Weed Spawner initialized')
        
        # Spawn weeds after a delay
        self.timer = self.create_timer(3.0, self.spawn_weeds_once)
        
    def spawn_weeds_once(self):
        """Spawn weeds once, then cancel timer"""
        self.spawn_weeds()
        self.timer.cancel()
        
    def spawn_weeds(self):
        """Spawn random weeds in the field"""
        self.get_logger().info(f'Spawning {self.num_weeds} weeds...')
        
        for i in range(self.num_weeds):
            request = SpawnEntity.Request()
            request.name = f'weed_{i}'
            request.xml = self.weed_sdf
            
            # Random position
            pose = Pose()
            pose.position.x = random.uniform(2.0, self.field_length)
            pose.position.y = random.uniform(-self.row_spacing/2, self.row_spacing/2)
            pose.position.z = 0.075
            pose.orientation.w = 1.0
            
            request.initial_pose = pose
            request.reference_frame = 'world'
            
            # Async call
            future = self.spawn_client.call_async(request)
            future.add_done_callback(
                lambda f, name=f'weed_{i}', pos=pose: self.spawn_callback(f, name, pos)
            )
            
    def spawn_callback(self, future, name, pose):
        """Handle spawn response"""
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(
                    f'Spawned {name} at x={pose.position.x:.2f}, y={pose.position.y:.2f}'
                )
            else:
                self.get_logger().error(f'Failed to spawn {name}: {response.status_message}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = WeedSpawner()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()