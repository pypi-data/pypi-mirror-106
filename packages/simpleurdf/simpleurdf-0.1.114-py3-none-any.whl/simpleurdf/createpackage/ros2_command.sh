#!/bin/sh

cd $1
. /opt/ros/foxy/setup.sh
ros2 pkg create --build-type ament_python $2
mv $3/createpackage/python_templates/demo.launch.py $2/$2/launch/demo.launch.py
mv $3/createpackage/python_templates/state_publisher.py $2/$2/launch/demo.launch.py
