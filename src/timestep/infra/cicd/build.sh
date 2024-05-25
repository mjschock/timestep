#!/usr/bin/env bash
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .dot.env)"
eval "$(direnv dotenv bash .env)"

docker login -u ${DOCKER_REGISTRY_USERNAME} -p $(cat ./secrets/docker_registry_password) ${DOCKER_REGISTRY_SERVER}

if [ -z ${IMAGE_NAME+x} ]; then
  docker buildx build \
    --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
    --build-arg GOENV_VERSION=${GOENV_VERSION} \
    --build-arg NODENV_VERSION=${NODENV_VERSION} \
    --build-arg PYENV_VERSION=${PYENV_VERSION} \
    --build-arg UBUNTU_VERSION=${UBUNTU_VERSION} \
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
    --build-arg GOENV_VERSION=${GOENV_VERSION} \
    --build-arg NODENV_VERSION=${NODENV_VERSION} \
    --build-arg PYENV_VERSION=${PYENV_VERSION} \
    --build-arg UBUNTU_VERSION=${UBUNTU_VERSION} \
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

elif [ ${IMAGE_NAME} = "caddy" ]; then
  docker buildx build \
    --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
    --build-arg GOENV_VERSION=${GOENV_VERSION} \
    --build-arg NODENV_VERSION=${NODENV_VERSION} \
    --build-arg PYENV_VERSION=${PYENV_VERSION} \
    --build-arg UBUNTU_VERSION=${UBUNTU_VERSION} \
    --cache-from ${CI_REGISTRY_IMAGE}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --push \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    src/timestep/platform

else
  docker buildx build \
    --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
    --build-arg GOENV_VERSION=${GOENV_VERSION} \
    --build-arg NODENV_VERSION=${NODENV_VERSION} \
    --build-arg PYENV_VERSION=${PYENV_VERSION} \
    --build-arg UBUNTU_VERSION=${UBUNTU_VERSION} \
    --cache-from ${CI_REGISTRY_IMAGE}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    --push \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
    --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
    src/timestep/platform/${IMAGE_NAME}

fi
