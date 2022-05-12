# roboclaw_ros
[![Build Status](https://travis-ci.org/sonyccd/roboclaw_ros.svg?branch=master)](https://travis-ci.org/sonyccd/roboclaw_ros)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6f65acd1242e4a0582ecb04c7cc70f68)](https://www.codacy.com/app/snakes-in-the-box/roboclaw_ros?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sonyccd/roboclaw_ros&amp;utm_campaign=Badge_Grade)

This is the fork of ROS driver for the Roboclaw motor controllers made by [Ion Motion Control](http://www.ionmc.com/).
## Usage
Just clone the repo into your catkin workspace. It contains the ROS package and the motor controller driver.  Remmeber to make sure ROS has permisions to use the dev port you give it.
```bash
cd <workspace>/src
git clone https://github.com/sonyccd/roboclaw_ros.git
cd <workspace>
catkin_make
source devel/setup.bash
roslaunch roboclaw_node roboclaw.launch
```

## Parameters
The launch file can be configure at the command line with arguments, by changing the value in the launch file or through the rosparam server.

|Parameter|Default|Definition|
|-----|----------|-------|
|dev|/dev/roboclaw|Dev that is the Roboclaw|
|baud|115200|Baud rate the Roboclaw is configured for|
|address|128|The address the Roboclaw is set to, 128 is 0x80|
|max_speed|0.5|Max speed allowed for motors in meters per second|
|ticks_per_meter|100|The number of encoder ticks per meter of movement|
|base_width|0.2|Width from one wheel edge to another in meters|

## Topics
###Subscribed
/cmd_vel [(geometry_msgs/Twist)](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)  
Velocity commands for the mobile base.
###Published
/odom [(nav_msgs/Odometry)](http://docs.ros.org/api/nav_msgs/html/msg/Odometry.html)  
Odometry output from the mobile base.
