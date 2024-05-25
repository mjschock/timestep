#!/usr/bin/env bash
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .dot.env)"
eval "$(direnv dotenv bash .env)"

docker login -u ${DOCKER_REGISTRY_USERNAME} -p $(cat ./secrets/docker_registry_password) ${DOCKER_REGISTRY_SERVER}

# docker run \
#  --env-file .dot.env \
#  --env-file .env \
#  --user $(id -u):$(id -g) \
#  --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
#  ${CI_REGISTRY_IMAGE}/cicd:latest poetry run cdktf deploy --auto-approve ${PRIMARY_DOMAIN_NAME}.k3s_cluster ${PRIMARY_DOMAIN_NAME}.kubernetes_config ${PRIMARY_DOMAIN_NAME}.platform

docker run \
 --env-file .dot.env \
 --env-file .env \
 --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
 ${CI_REGISTRY_IMAGE}/cicd:latest poetry run cdktf deploy --auto-approve ${PRIMARY_DOMAIN_NAME}.k3s_cluster ${PRIMARY_DOMAIN_NAME}.kubernetes_config ${PRIMARY_DOMAIN_NAME}.platform
