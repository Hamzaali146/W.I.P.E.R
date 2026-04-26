#!/usr/bin/env python3
"""Dry-run launch: control node + fake detection publisher.

Usage:
    ros2 launch weedbot_control laser_dry_run.launch.py
    ros2 launch weedbot_control laser_dry_run.launch.py mode:=LIVE armed:=true \\
         serial_port:=/dev/ttyUSB0

In DRY_RUN (default) every outgoing $FIRE packet is logged at INFO with its
full framed form (including *CS). Copy one into TeraTerm on the STM32 laptop
to verify the firmware accepts the format before switching to LIVE.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    pkg_share = FindPackageShare("weedbot_control")

    config_file = DeclareLaunchArgument(
        "config_file",
        default_value=PathJoinSubstitution(
            [pkg_share, "config", "control_params.yaml"]
        ),
    )
    shots_csv = DeclareLaunchArgument(
        "shots_csv",
        default_value=PathJoinSubstitution(
            [pkg_share, "config", "test_shots.csv"]
        ),
    )
    mode = DeclareLaunchArgument("mode", default_value="LIVE")
    armed = DeclareLaunchArgument("armed", default_value="true")
    serial_port = DeclareLaunchArgument("serial_port", default_value="/dev/ttyUSB0")
    # Slow cadence so each shot is visually distinguishable on the table.
    publish_rate_hz = DeclareLaunchArgument("publish_rate_hz", default_value="0.3")
    # Long dwell so the laser stays on each position long enough to observe.
    dwell_ms = DeclareLaunchArgument("dwell_ms", default_value="2000")

    control_node = Node(
        package="weedbot_control",
        executable="control_node",
        name="weedbot_control_node",
        output="screen",
        parameters=[
            LaunchConfiguration("config_file"),
            {
                "mode": LaunchConfiguration("mode"),
                "armed": ParameterValue(
                    LaunchConfiguration("armed"), value_type=bool
                ),
                "serial_port": LaunchConfiguration("serial_port"),
                "dwell_ms": ParameterValue(
                    LaunchConfiguration("dwell_ms"), value_type=int
                ),
            },
        ],
    )

    test_node = Node(
        package="weedbot_control",
        executable="laser_test_node",
        name="weedbot_laser_test_node",
        output="screen",
        parameters=[
            LaunchConfiguration("config_file"),
            {
                "shots_csv": LaunchConfiguration("shots_csv"),
                "publish_rate_hz": ParameterValue(
                    LaunchConfiguration("publish_rate_hz"), value_type=float
                ),
            },
        ],
    )

    return LaunchDescription(
        [
            config_file,
            shots_csv,
            mode,
            armed,
            serial_port,
            publish_rate_hz,
            dwell_ms,
            control_node,
            test_node,
        ]
    )
