#!/usr/bin/env bash
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .dot.env)"
eval "$(direnv dotenv bash .env)"

docker login -u ${DOCKER_REGISTRY_USERNAME} -p $(cat ./secrets/docker_registry_password) ${DOCKER_REGISTRY_SERVER}

if [ ${STACK_NAME} = "k3s_cluster" ]; then
    docker run \
    --env-file .dot.env \
    --env-file .env \
    --user $(id -u):$(id -g) \
    --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
    ${CI_REGISTRY_IMAGE}/cicd:latest poetry run cdktf diff ${PRIMARY_DOMAIN_NAME}.k3s_cluster

elif [ ${STACK_NAME} = "kubernetes_config" ]; then
    docker run \
    --env-file .dot.env \
    --env-file .env \
    --user $(id -u):$(id -g) \
    --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
    ${CI_REGISTRY_IMAGE}/cicd:latest poetry run cdktf diff ${PRIMARY_DOMAIN_NAME}.kubernetes_config

elif [ ${STACK_NAME} = "platform" ]; then
    docker run \
    --env-file .dot.env \
    --env-file .env \
    --user $(id -u):$(id -g) \
    --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
    ${CI_REGISTRY_IMAGE}/cicd:latest poetry run cdktf diff ${PRIMARY_DOMAIN_NAME}.platform

fi
