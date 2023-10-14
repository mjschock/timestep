#!/usr/bin/env sh
set -x # echo on

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
  --push \
  --tag ${CI_REGISTRY_IMAGE}:latest \
  .

docker buildx bake --pull --push
