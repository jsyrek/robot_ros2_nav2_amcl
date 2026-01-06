# ROS2 Robot Navigation with Nav2 and AMCL

Clean, minimal ROS2 project for autonomous robot navigation using Nav2 and AMCL localization with LiDAR.

## Features
- Nav2 Navigation Stack
- AMCL Localization with LiDAR
- PointCloud2 to LaserScan conversion
- Motor control via CAN bus
- RViz2 visualization
- TF2 frame transformations

## Quick Start

### Build
```bash
cd ~/robot_ros2_nav2_amcl
colcon build
source install/setup.bash
```

### Run Everything
```bash
ros2 launch robot_navigation everything.launch.py
```

### Individual Components
- **Motors & Odometry**: `ros2 launch robot_navigation motors_and_odometry.launch.py`
- **LiDAR Conversion**: `ros2 launch robot_navigation lidar_conversion.launch.py`
- **AMCL Localization**: `ros2 launch robot_navigation amcl_localization.launch.py`
- **Nav2 Stack**: `ros2 launch robot_navigation nav2_full.launch.py`

## Project Structure
```
src/robot_navigation/
├── launch/
│   ├── motors_and_odometry.launch.py
│   ├── lidar_conversion.launch.py
│   ├── amcl_localization.launch.py
│   ├── nav2_full.launch.py
│   └── everything.launch.py
├── config/
│   ├── nav2_params_full.yaml
│   └── robot_rviz.rviz
├── maps/
│   ├── my_map.yaml
│   └── my_map.pgm
├── package.xml
├── CMakeLists.txt
└── setup.py
```

## Requirements
- ROS2 Humble or Jazzy
- Nav2 stack
- pointcloud_to_laserscan
- mks_motor_control package
- Ubuntu 22.04 LTS

## Configuration

### Map File
Place your map files in `src/robot_navigation/maps/`:
- `my_map.yaml` - Map configuration
- `my_map.pgm` - Map image (grayscale)

### Robot Parameters
Edit `src/robot_navigation/config/nav2_params_full.yaml` to tune:
- AMCL particle filter settings
- Costmap parameters
- Planner settings
- Controller parameters

## Troubleshooting

### No /scan topic
Ensure LiDAR is publishing `/unilidar/cloud` and `lidar_conversion.launch.py` is running.

### Robot not localizing
Check AMCL parameters in `amcl_localization.launch.py` and verify map file is correct.

### TF errors
Verify static transforms are being published with `ros2 run tf2_ros tf2_echo map odom`

## Author
Jakub Syrek

## License
Apache License 2.0
