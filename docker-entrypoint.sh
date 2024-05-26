#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
source /home/ubuntu/.venv/bin/activate

# sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets

echo "=== Running docker-entrypoint.sh ==="
echo "=== Running as $(whoami) ==="
echo "=== Running with $(id -u):$(id -g) ==="
echo "=== Running in $(pwd) ==="
echo "=== Running with secrets ==="
ls -al /home/ubuntu/secrets

exec "$@"
