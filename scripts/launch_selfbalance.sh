#!/usr/bin/env bash

source /opt/ros/kinetic/setup.sh
source ~/ros_ws/devel/setup.bash

rosrun rosserial_python serial_node.py _port:=tcp

