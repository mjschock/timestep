#!/usr/bin/env sh
set -x # echo on

# docker login -u ${CI_REGISTRY_USER} -p ${CI_REGISTRY_PASSWORD} ${CI_REGISTRY}
# docker pull ${CI_REGISTRY_IMAGE}:latest || true

docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}
# docker pull ${CI_REGISTRY_IMAGE}:latest || true
# docker compose pull || true
