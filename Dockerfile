# FROM prefecthq/prefect:2.10.8-python3.9

# FROM ros:foxy

# # install ros package
# RUN apt-get update && apt-get install -y \
#       ros-${ROS_DISTRO}-demo-nodes-cpp \
#       ros-${ROS_DISTRO}-demo-nodes-py && \
#     rm -rf /var/lib/apt/lists/*

# # launch ros package
# CMD ["ros2", "launch", "demo_nodes_cpp", "talker_listener.launch.py"]

FROM osrf/ros:humble-desktop
