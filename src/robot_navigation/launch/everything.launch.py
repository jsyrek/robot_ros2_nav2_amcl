#!/usr/bin/env python3
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_dir = get_package_share_directory('robot_navigation')
    launch_dir = os.path.join(pkg_dir, 'launch')
    return LaunchDescription([
        IncludeLaunchDescription(
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(os.path.join(launch_dir, 'motors_and_odometry.launch.py'))
        # ),        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'lidar_conversion.launch.py'))),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'amcl_localization.launch.py'))),
    ])
