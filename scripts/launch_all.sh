#!/usr/bin/env bash

screen -d -m -S ros_core ~/launch_roscore.sh
sleep 5
screen -d -m -S ros_selfbalance ~/launch_selfbalance.sh
