#!/usr/bin/env sh
set -x # echo on

docker run \
 --env-file .env \
 --env CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER} \
 --env HTPASSWD=${HTPASSWD} \
 --env PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
 --env SSH_PRIVATE_KEY=${SSH_PRIVATE_KEY} \
 --env TF_API_TOKEN=${CI_JOB_TOKEN} \
 --env TF_USERNAME=${CI_REGISTRY_USER} \
 ${CI_REGISTRY_IMAGE}:latest poetry run cdktf deploy --auto-approve ${PRIMARY_DOMAIN_NAME}
