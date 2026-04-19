#!/usr/bin/env python3
"""Launch weedbot control node."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    config_file_arg = DeclareLaunchArgument(
        "config_file",
        default_value=PathJoinSubstitution(
            [FindPackageShare("weedbot_control"), "config", "control_params.yaml"]
        ),
        description="Path to control node parameter file",
    )

    serial_port_arg = DeclareLaunchArgument(
        "serial_port",
        default_value="COM5",
        description="Serial device for STM32 USB-TTL link",
    )

    dry_run_arg = DeclareLaunchArgument(
        "dry_run",
        default_value="true",
        description="If true, do not write to serial; log packets only",
    )

    armed_arg = DeclareLaunchArgument(
        "armed",
        default_value="false",
        description="Laser arm state at startup",
    )

    config_file = LaunchConfiguration("config_file")
    serial_port = LaunchConfiguration("serial_port")
    dry_run = LaunchConfiguration("dry_run")
    armed = LaunchConfiguration("armed")

    control_node = Node(
        package="weedbot_control",
        executable="control_node",
        name="weedbot_control_node",
        output="screen",
        parameters=[
            config_file,
            {
                "serial_port": serial_port,
                "dry_run": dry_run,
                "armed": armed,
            },
        ],
    )

    return LaunchDescription(
        [
            config_file_arg,
            serial_port_arg,
            dry_run_arg,
            armed_arg,
            control_node,
        ]
    )