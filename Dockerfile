FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
  gosu \
  && rm -rf /var/lib/apt/lists/*

RUN groupadd -r timestep && useradd --no-log-init -r -g timestep timestep

USER timestep
WORKDIR /home/timestep

COPY --chown=timestep:timestep . /home/timestep/app

ENTRYPOINT [ "/home/timestep/app/src/lib/entrypoint.sh" ]
CMD [ "timestep" ]
