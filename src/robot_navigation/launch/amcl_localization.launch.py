#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    robot_nav_dir = get_package_share_directory('robot_navigation')
    map_file = os.path.join(robot_nav_dir, 'maps', 'my_map.yaml')
    return LaunchDescription([
        DeclareLaunchArgument('map', default_value=map_file),
        Node(package='nav2_map_server', executable='map_server', name='map_server', output='screen',
            parameters=[{'yaml_filename': LaunchConfiguration('map'), 'use_sim_time': False}]),
        Node(package='nav2_lifecycle_manager', executable='lifecycle_manager',
            name='lifecycle_manager_localization', output='screen',
            parameters=[{'use_sim_time': False, 'autostart': True, 'node_names': ['map_server', 'amcl']}]),
        Node(package='nav2_amcl', executable='amcl', name='amcl', output='screen',
            parameters=[{'use_sim_time': False, 'alpha1': 0.2, 'alpha2': 0.2, 'alpha3': 0.2,
                        'alpha4': 0.2, 'alpha5': 0.2, 'base_frame_id': 'base_link', 'global_frame_id': 'map',
                        'odom_frame_id': 'odom', 'laser_model_type': 'likelihood_field', 'odom_model_type': 'diff',
                        'min_particles': 500, 'max_particles': 2000, 'max_beams': 60, 'laser_min_range': 0.12,
                        'laser_max_range': 30.0, 'laser_likelihood_max_dist': 2.0, 'transform_tolerance': 1.0,
                        'tf_broadcast': True, 'update_min_d': 0.25, 'update_min_a': 0.5, 'resample_interval': 1,
                        'recovery_alpha_fast': 0.0, 'recovery_alpha_slow': 0.0, 'z_hit': 0.5, 'z_short': 0.05,
                        'z_max': 0.05, 'z_rand': 0.5, 'sigma_hit': 0.2, 'sigma_short': 0.1, 'lambda_short': 0.1}]),
    ])
