#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():

    pkg_weedbot_sim = get_package_share_directory('weedbot_simulation')

    world_file = os.path.join(pkg_weedbot_sim, 'worlds', 'farm_field.world')
    urdf_file  = os.path.join(pkg_weedbot_sim, 'urdf', 'tractor.urdf.xacro')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # --- Start Gazebo (ros_gz) ---
    gz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': f'-r {world_file}'
        }.items()
    )

    # --- Robot description ---
    robot_description = Command(['xacro ', urdf_file])

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'use_sim_time': use_sim_time,
            'robot_description': robot_description
        }],
        output='screen'
    )

    # --- Spawn robot in Gazebo ---
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'weedbot_tractor',
            '-x', '0', '-y', '0', '-z', '0.5'
        ],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        gz_launch,
        robot_state_publisher,
        spawn_robot,
    ])
