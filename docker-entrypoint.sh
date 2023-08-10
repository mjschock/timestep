#!/bin/bash
set -e

eval "$(anyenv init -)"

source /home/ubuntu/.venv/bin/activate

exec "$@"
