#!/bin/bash
set -e

eval "$(direnv hook bash)"
direnv allow .

eval "$(anyenv init -)"
source /home/ubuntu/app/.venv/bin/activate

# echo "Testing env vars"
# echo $MINIO_ENDPOINT
# echo $MINIO_ROOT_USER
# echo $MINIO_ROOT_PASSWORD
# export MINIO_BUCKET="default"

# export LITESTREAM_ACCESS_KEY_ID=${MINIO_ROOT_USER}
# export LITESTREAM_SECRET_ACCESS_KEY=${MINIO_ROOT_PASSWORD}
# export AWS_ACCESS_KEY_ID=${MINIO_ROOT_USER}
# export AWS_SECRET_ACCESS_KEY=${MINIO_ROOT_PASSWORD}

# cat /etc/litestream.yml

# if [ -f /home/ubuntu/.sky/benchmark.db ]; then
#     echo "Database already exists, skipping restore"

# else
# 	echo "No database found, restoring from replica if exists"
#     litestream restore -if-replica-exists /home/ubuntu/.sky/benchmark.db
#     litestream restore -if-replica-exists /home/ubuntu/.sky/jobs.db
#     litestream restore -if-replica-exists /home/ubuntu/.sky/spot_jobs.db
#     litestream restore -if-replica-exists /home/ubuntu/.sky/state.db

# fi

exec "$@"
# exec litestream replicate -exec "poetry run python main.py"
