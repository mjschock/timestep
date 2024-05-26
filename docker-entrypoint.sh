#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
# source /home/ubuntu/.venv/bin/activate
source .venv/bin/activate

# if /home/ubuntu/secrets exists, change ownership to ubuntu
if [ -d /home/ubuntu/secrets ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets
fi

exec "$@"
