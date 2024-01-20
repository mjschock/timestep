#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
source /home/ubuntu/app/.venv/bin/activate

exec "$@"
