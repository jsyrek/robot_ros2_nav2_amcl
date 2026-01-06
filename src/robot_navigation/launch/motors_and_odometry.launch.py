#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mks_motor_control',
            executable='motor_driver_can',
            name='motor_driver',
            output='screen',
            emulate_tty=True,
        ),
        Node(
            package='mks_motor_control',
            executable='odometry_publisher',
            name='odometry_pub',
            output='screen',
            emulate_tty=True,
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.09', '0', '0.165', '0', '0', '0', 'base_link', 'unilidar_lidar'],
            name='tf_base_lidar',
            output='screen',
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0.1', '0', '0', '0', 'base_link', 'imu_link'],
            name='tf_base_imu',
            output='screen',
        ),
    ])
