#!/usr/bin/env sh
set -e # exit on first error
set -x # echo on

# TODO: Load these using direnv w/ dotenv
CDKTF_CLI_VERSION=$(cat .env | grep ^CDKTF_CLI_VERSION | cut -d '=' -f2)
VERSION=$(cat .env | grep ^VERSION | cut -d '=' -f2)

docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}

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
    --push \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    .

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
