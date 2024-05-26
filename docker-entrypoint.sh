#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
source /home/ubuntu/.venv/bin/activate

echo "=== Running docker-entrypoint.sh ==="
echo "=== Running as $(whoami) ==="
echo "=== Running with $(id -u):$(id -g) ==="
echo "=== Running in $(pwd) ==="

echo "=== secrets before ==="
ls -al /home/ubuntu/secrets

# chown -R ubuntu:ubuntu /home/ubuntu/secrets
sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets

echo "=== secrets after ==="
ls -al /home/ubuntu/secrets

exec "$@"
