#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
source /home/ubuntu/.venv/bin/activate

exec "$@"
