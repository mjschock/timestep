#!/usr/bin/env sh
set -e # exit on first error
set -x # echo on

VERSION=$(cat .env | grep ^VERSION | cut -d '=' -f2)

docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}

if [ -z ${IMAGE_NAME+x} ]; then
  echo "Building base image"

  docker buildx build \
    --cache-from ${CI_REGISTRY_IMAGE}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:${VERSION} \
    --push \
    --tag ${CI_REGISTRY_IMAGE}:latest \
    --tag ${CI_REGISTRY_IMAGE}:${VERSION} \
    .

else
  echo "Building ${IMAGE_NAME} image"

  docker buildx build \
    --cache-from ${CI_REGISTRY_IMAGE}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --push \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    src/timestep/services/${IMAGE_NAME}
fi

# docker buildx build \
#   --cache-from ${CI_REGISTRY_IMAGE}:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
#   --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#   --push \
#   --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#   --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#   src/timestep/services/${IMAGE_NAME}

# docker buildx build \
#   --cache-from ${CI_REGISTRY_IMAGE}:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
#   --cache-from ${CI_REGISTRY_IMAGE}/caddy:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}/caddy:${VERSION} \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/caddy:latest \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/caddy:${VERSION} \
#   --push \
#   --tag ${CI_REGISTRY_IMAGE}/caddy:latest \
#   --tag ${CI_REGISTRY_IMAGE}/caddy:${VERSION} \
#   src/timestep/services/caddy

# docker buildx build \
#   --cache-from ${CI_REGISTRY_IMAGE}/frontend:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}/frontend:${VERSION} \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/frontend:latest \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/frontend:${VERSION} \
#   --push \
#   --tag ${CI_REGISTRY_IMAGE}/frontend:latest \
#   --tag ${CI_REGISTRY_IMAGE}/frontend:${VERSION} \
#   src/timestep/services/frontend

# docker buildx build \
#   --cache-from ${CI_REGISTRY_IMAGE}:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
#   --cache-from ${CI_REGISTRY_IMAGE}/web:latest \
#   --cache-from ${CI_REGISTRY_IMAGE}/web:${VERSION} \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/web:latest \
#   --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/web:${VERSION} \
#   --push \
#   --tag ${CI_REGISTRY_IMAGE}/web:latest \
#   --tag ${CI_REGISTRY_IMAGE}/web:${VERSION} \
#   src/timestep/services/web
