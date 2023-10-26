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
  --cache-from ${CI_REGISTRY_IMAGE}/frontend:latest \
  --cache-from ${CI_REGISTRY_IMAGE}/frontend:${VERSION} \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/frontend:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/frontend:${VERSION} \
  --push \
  --tag ${CI_REGISTRY_IMAGE}/frontend:latest \
  --tag ${CI_REGISTRY_IMAGE}/frontend:${VERSION} \
  src/timestep/services/frontend

docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}:latest \
  --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
  --cache-from ${CI_REGISTRY_IMAGE}/web-api:latest \
  --cache-from ${CI_REGISTRY_IMAGE}/web-api:${VERSION} \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/web-api:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/web-api:${VERSION} \
  --push \
  --tag ${CI_REGISTRY_IMAGE}/api:latest \
  --tag ${CI_REGISTRY_IMAGE}/api:${VERSION} \
  src/timestep/services/web-api
