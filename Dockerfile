FROM osrf/ros:humble-desktop

# RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

RUN apt-get update && apt-get install -y \
  # ~nros-humble-rqt* \
  gosu \
  python3-colcon-common-extensions \
  # ros-humble-turtlesim \
  ros-humble-nav2-util \
  ros-humble-turtlebot3-bringup \
  ros-humble-turtlebot3-gazebo \
  wget \
  && rm -rf /var/lib/apt/lists/*

RUN groupadd -r timestep && useradd --no-log-init -r -g timestep timestep

USER timestep
WORKDIR /home/timestep

# COPY --chown=timestep:timestep . /home/timestep/app
COPY --chown=timestep:timestep . /home/timestep/

# ENTRYPOINT [ "/home/timestep/app/src/lib/entrypoint.sh" ]
# ENTRYPOINT [ "/ros_entrypoint.sh" ]
# CMD [ "timestep" ]
