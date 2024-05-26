#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
source /home/ubuntu/.venv/bin/activate

sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets

exec "$@"
