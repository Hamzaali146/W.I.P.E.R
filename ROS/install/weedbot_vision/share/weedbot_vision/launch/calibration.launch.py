#!/usr/bin/env python3
"""
Launch file for camera homography calibration
This is a one-time setup process to map pixel coordinates to real-world meters
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    # Declare launch arguments
    camera_source_arg = DeclareLaunchArgument(
        'camera_source',
        default_value='0',
        description='Camera source (0 for webcam, URL for IP camera)'
    )
    
    config_file_arg = DeclareLaunchArgument(
        'config_file',
        default_value=PathJoinSubstitution([
            FindPackageShare('weedbot_vision'),
            'config',
            'vision_params.yaml'
        ]),
        description='Path to config file'
    )
    
    # Get launch configurations
    camera_source = LaunchConfiguration('camera_source')
    config_file = LaunchConfiguration('config_file')
    
    # Camera publisher node
    camera_node = Node(
        package='weedbot_vision',
        executable='camera_publisher',
        name='camera_publisher',
        parameters=[
            config_file,
        ],
        output='screen'
    )
    
    # Calibration node
    calibration_node = Node(
        package='weedbot_vision',
        executable='camera_calibration',
        name='camera_calibration',
        output='screen'
    )
    
    return LaunchDescription([
        camera_source_arg,
        config_file_arg,
        LogInfo(msg=['==========================================']),
        LogInfo(msg=['WEEDBOT HOMOGRAPHY CALIBRATION']),
        LogInfo(msg=['==========================================']),
        LogInfo(msg=['Instructions:']),
        LogInfo(msg=['1. Place 4 markers on ground in rectangle pattern']),
        LogInfo(msg=['2. Measure their positions from camera center']),
        LogInfo(msg=['3. Click markers in calibration window']),
        LogInfo(msg=['4. Enter real-world coordinates']),
        LogInfo(msg=['5. Test and save homography matrix']),
        LogInfo(msg=['==========================================']),
        camera_node,
        calibration_node,
    ])