#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"

# if .venv exists, activate it
if [ -d .venv ]; then
  source .venv/bin/activate
fi

# if /home/ubuntu/.ssh exists, change ownership to ubuntu
# if /home/ubuntu/.ssh exists, change ownership to id -u:$(id -g)
if [ -d /home/ubuntu/.ssh ]; then
  # sudo chown -R ubuntu:ubuntu /home/ubuntu/.ssh
  sudo chown -R $(id -u):$(id -g) /home/ubuntu/.ssh
fi

# if /home/ubuntu/.sky exists, change ownership to ubuntu
# if /home/ubuntu/.sky exists, change ownership to id -u:$(id -g)
if [ -d /home/ubuntu/.sky ]; then
  # sudo chown -R ubuntu:ubuntu /home/ubuntu/.sky
  sudo chown -R $(id -u):$(id -g) /home/ubuntu/.sky
fi

# if /home/ubuntu/secrets exists, change ownership to ubuntu
# if /home/ubuntu/secrets exists, change ownership to id -u:$(id -g)
if [ -d /home/ubuntu/secrets ]; then
  # sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets
  sudo chown -R $(id -u):$(id -g) /home/ubuntu/secrets
fi

# TODO: just chown -R $(id -u):$(id -g) /home/ubuntu?

exec "$@"
