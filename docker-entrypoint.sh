#!/usr/bin/env bash
set -e

# if [ "$1" = 'postgres' ]; then
#     chown -R postgres "$PGDATA"

#     if [ -z "$(ls -A "$PGDATA")" ]; then
#         gosu postgres initdb
#     fi

#     exec gosu postgres "$@"
# fi

# eval "$(direnv hook bash)"
# direnv allow .

# eval "$(anyenv init -)"

# if .venv exists, activate it
# if [ -d .venv ]; then
#   source .venv/bin/activate
# fi

# if /home/ubuntu/.config/caddy exists, change ownership to ubuntu
if [ -d /home/ubuntu/.config/caddy ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/.config/caddy
fi

# if /home/ubuntu/.local/share/caddy exists, change ownership to ubuntu
if [ -d /home/ubuntu/.local/share/caddy ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/.local/share/caddy
fi

# if /home/ubuntu/.sky exists, change ownership to ubuntu
if [ -d /home/ubuntu/.sky ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/.sky
fi

# if /home/ubuntu/.ssh exists, change ownership to ubuntu
if [ -d /home/ubuntu/.ssh ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/.ssh
fi

# if /home/ubuntu/app/data exists, change ownership to ubuntu
if [ -d /home/ubuntu/app/data ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/app/data
fi

# if /home/ubuntu/app/uploaded_files exists, change ownership to ubuntu
if [ -d /home/ubuntu/app/uploaded_files ]; then
  sudo chown -R ubuntu:ubuntu /home/ubuntu/app/uploaded_files
fi

# # if /home/ubuntu/secrets exists, change ownership to id -u:$(id -g)
# if [ -d /home/ubuntu/secrets ]; then
#   # sudo chown -R ubuntu:ubuntu /home/ubuntu/secrets
#   sudo chown -R $(id -u):$(id -g) /home/ubuntu/secrets
# fi

# if rxconfig.py exists, run migrations
# if [ -d rxconfig.py ]; then
#   reflex db migrate
# fi

exec "$@"
