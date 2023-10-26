#!/usr/bin/env sh
set -e # exit on first error
set -x # echo on

VERSION=$(cat .env | grep ^VERSION | cut -d '=' -f2)

docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}:latest \
  --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:${VERSION} \
  --push \
  --tag ${CI_REGISTRY_IMAGE}:latest \
  --tag ${CI_REGISTRY_IMAGE}:${VERSION} \
  .

# docker buildx bake --pull --push

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}:latest \
  --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
  --cache-from ${CI_REGISTRY_IMAGE}/api:latest \
  --cache-from ${CI_REGISTRY_IMAGE}/api:${VERSION} \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/api:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/api:${VERSION} \
  --push \
  --tag ${CI_REGISTRY_IMAGE}/api:latest \
  --tag ${CI_REGISTRY_IMAGE}/api:${VERSION} \
  src/timestep/services/api

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}/caddy:latest \
  --cache-from ${CI_REGISTRY_IMAGE}/caddy:${VERSION} \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/caddy:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/caddy:${VERSION} \
  --push \
  --tag ${CI_REGISTRY_IMAGE}/caddy:latest \
  --tag ${CI_REGISTRY_IMAGE}/caddy:${VERSION} \
  src/timestep/services/caddy

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}/www:latest \
  --cache-from ${CI_REGISTRY_IMAGE}/www:${VERSION} \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/www:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/www:${VERSION} \
  --push \
  --tag ${CI_REGISTRY_IMAGE}/www:latest \
  --tag ${CI_REGISTRY_IMAGE}/www:${VERSION} \
  src/timestep/services/www
