#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"

# if .venv exists, activate it
if [ -d .venv ]; then
  source .venv/bin/activate
fi

# if /home/ubuntu/secrets exists, change ownership to ubuntu
if [ -d /home/ubuntu/secrets ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets
fi

exec "$@"
