#!/usr/bin/env sh
set -e # exit on first error
set -x # echo on

docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
  --push \
  --tag ${CI_REGISTRY_IMAGE}:latest \
  .

docker buildx bake --pull --push
