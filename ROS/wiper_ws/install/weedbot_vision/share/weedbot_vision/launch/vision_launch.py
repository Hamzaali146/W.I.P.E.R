#!/usr/bin/env python3
"""
Launch file for weedbot vision system
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    # Declare launch arguments
    config_file_arg = DeclareLaunchArgument(
        'config_file',
        default_value=PathJoinSubstitution([
            FindPackageShare('weedbot_vision'),
            'config',
            'vision_params.yaml'
        ]),
        description='Path to config file'
    )
    
    use_camera_arg = DeclareLaunchArgument(
        'use_camera',
        default_value='true',
        description='Whether to launch camera publisher node'
    )
    
    use_monitor_arg = DeclareLaunchArgument(
        'use_monitor',
        default_value='true',
        description='Whether to launch detection monitor node'
    )
    
    model_path_arg = DeclareLaunchArgument(
        'model_path',
        default_value='',
        description='Path to segmentation model'
    )
    
    device_arg = DeclareLaunchArgument(
        'device',
        default_value='cuda',
        description='Device for inference (cuda or cpu)'
    )
    
    # Get launch configurations
    config_file = LaunchConfiguration('config_file')
    use_camera = LaunchConfiguration('use_camera')
    use_monitor = LaunchConfiguration('use_monitor')
    model_path = LaunchConfiguration('model_path')
    device = LaunchConfiguration('device')
    
    # Camera publisher node
    camera_node = Node(
        package='weedbot_vision',
        executable='camera_publisher',
        name='camera_publisher',
        parameters=[config_file],
        output='screen',
        condition=IfCondition(use_camera)
    )
    
    # Vision node
    vision_node = Node(
        package='weedbot_vision',
        executable='vision_node',
        name='weedbot_vision_node',
        parameters=[
            config_file,
            # {'model_path': model_path},
            # {'device': device}
        ],
        output='screen'
    )
    
    # Detection monitor node
    monitor_node = Node(
        package='weedbot_vision',
        executable='detection_monitor',
        name='detection_monitor',
        parameters=[config_file],
        output='screen',
        condition=IfCondition(use_monitor)
    )
    
    return LaunchDescription([
        config_file_arg,
        use_camera_arg,
        use_monitor_arg,
        model_path_arg,
        device_arg,
        LogInfo(msg=['Starting weedbot vision system...']),
        camera_node,
        vision_node,
        monitor_node,
    ])