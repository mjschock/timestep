#!/usr/bin/env bash
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .dot.env)"
eval "$(direnv dotenv bash .env)"

docker login -u ${DOCKER_REGISTRY_USERNAME} -p $(cat ./secrets/docker_registry_password) ${DOCKER_REGISTRY_SERVER}

if [ -z ${IMAGE_NAME+x} ]; then
  docker buildx build \
    --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
    --build-arg PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
    --cache-from ${CI_REGISTRY_IMAGE}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:${VERSION} \
    --push \
    --tag ${CI_REGISTRY_IMAGE}:latest \
    --tag ${CI_REGISTRY_IMAGE}:${VERSION} \
    .

elif [ ${IMAGE_NAME} = "cicd" ]; then
  docker buildx build \
    --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
    --build-arg PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
    --cache-from ${CI_REGISTRY_IMAGE}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --file Dockerfile.cicd \
    --push \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    .

elif [ ${IMAGE_NAME} = "postgresql-repmgr" ]; then
  docker buildx build \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --file src/timestep/infra/stacks/kubernetes_config/postgresql_repmgr.Dockerfile \
    --push \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    src/timestep/infra/stacks/kubernetes_config

else
  docker buildx build \
    --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
    --build-arg PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
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
