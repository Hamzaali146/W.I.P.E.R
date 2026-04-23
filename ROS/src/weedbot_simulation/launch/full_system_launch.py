#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    
    pkg_weedbot_sim = get_package_share_directory('weedbot_simulation')
    pkg_weedbot_vision = get_package_share_directory('weedbot_vision')
    
    # Include simulation launch
    simulation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_weedbot_sim, 'launch', 'simulation_launch.py')
        )
    )
    
    # Launch vision system (if you have a launch file)
    # vision_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(pkg_weedbot_vision, 'launch', 'vision_launch.py')
    #     )
    # )
    
    # Laser Controller Node
    laser_controller = Node(
        package='weedbot_simulation',
        executable='laser_controller',
        name='laser_controller',
        output='screen',
        parameters=[{
            'camera_fov': 80.0,
            'image_width': 1280,
            'laser_range': 1.5,
            'firing_duration': 0.5
        }]
    )
    
    # Tractor Controller Node
    tractor_controller = Node(
        package='weedbot_simulation',
        executable='tractor_controller',
        name='tractor_controller',
        output='screen',
        parameters=[{
            'forward_speed': 0.5,
            'field_length': 50.0
        }]
    )
    
    # Weed Spawner
    weed_spawner = Node(
        package='weedbot_simulation',
        executable='weed_spawner',
        name='weed_spawner',
        output='screen',
        parameters=[{
            'num_weeds': 20,
            'field_length': 50.0,
            'row_spacing': 1.5
        }]
    )
    
    # RViz (optional)
    # rviz = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     name='rviz2',
    #     arguments=['-d', os.path.join(pkg_weedbot_sim, 'config', 'weedbot.rviz')]
    # )
    
    return LaunchDescription([
        simulation_launch,
        # vision_launch,
        laser_controller,
        tractor_controller,
        weed_spawner,
        # rviz,
    ])