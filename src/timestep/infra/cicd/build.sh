#!/usr/bin/env bash
set -e # exit on first error
# set -x # echo on

# If direnv is not installed,
# then install it
# and add the hook to the shell
# and allow the current directory
# and rerun this script
# if ! command -v direnv &> /dev/null
# then
#   echo "direnv could not be found"
#   echo "Installing direnv"
#   curl -sfL https://direnv.net/install.sh | bash
#   eval "$(direnv hook bash)"
#   direnv allow .
#   # Sleep for a short time to allow the shell to settle
#   sleep 1
#   # Source this script to apply changes to the current shell session
#   source "$0" "$@"
#   exit  # Ensure the script exits after sourcing
# else
#   echo "direnv is installed"
# fi

curl -sfL https://direnv.net/install.sh | bash
eval "$(direnv hook bash)"
direnv allow .

eval "$(direnv dotenv bash .dot.env)"
eval "$(direnv dotenv bash .env)"

# cat .dot.env | grep ^CDKTF_CLI_VERSION | cut -d '=' -f2
# echo "CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION}"

# cat .env | grep ^CLOUD_INSTANCE_PROVIDER | cut -d '=' -f2
# echo "CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER}"

echo "CI_REGISTRY_IMAGE=${CI_REGISTRY_IMAGE}"
echo "DOCKER_REGISTRY_USERNAME=${DOCKER_REGISTRY_USERNAME}"
echo "DOCKER_REGISTRY_PASSWORD=${DOCKER_REGISTRY_PASSWORD}"
echo "DOCKER_REGISTRY_SERVER=${DOCKER_REGISTRY_SERVER}"
echo "IMAGE_NAME=${IMAGE_NAME}"
echo "PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME}"
echo "SHELL=${SHELL}"
echo "VERSION=${VERSION}"

# ls -al secrets

# TODO: Load these using direnv w/ dotenv
# CDKTF_CLI_VERSION=$(cat .env | grep ^CDKTF_CLI_VERSION | cut -d '=' -f2)
# VERSION=$(cat .env | grep ^VERSION | cut -d '=' -f2)

# docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}

# if [ -z ${IMAGE_NAME+x} ]; then
#   docker buildx build \
#     --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
#     --build-arg PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
#     --cache-from ${CI_REGISTRY_IMAGE}:latest \
#     --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:${VERSION} \
#     --push \
#     --tag ${CI_REGISTRY_IMAGE}:latest \
#     --tag ${CI_REGISTRY_IMAGE}:${VERSION} \
#     .

# elif [ ${IMAGE_NAME} = "cicd" ]; then
#   docker buildx build \
#     --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
#     --build-arg PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
#     --cache-from ${CI_REGISTRY_IMAGE}:latest \
#     --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
#     --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#     --file Dockerfile.cicd \
#     --push \
#     --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#     .

# elif [ ${IMAGE_NAME} = "postgresql-repmgr" ]; then
#   docker buildx build \
#     --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --file src/timestep/infra/stacks/kubernetes_config/postgresql_repmgr.Dockerfile \
#     --push \
#     --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     src/timestep/infra/stacks/kubernetes_config

# else
#   docker buildx build \
#     --build-arg CDKTF_CLI_VERSION=${CDKTF_CLI_VERSION} \
#     --build-arg PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
#     --cache-from ${CI_REGISTRY_IMAGE}:latest \
#     --cache-from ${CI_REGISTRY_IMAGE}:${VERSION} \
#     --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --cache-from ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#     --push \
#     --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:latest \
#     --tag ${CI_REGISTRY_IMAGE}/${IMAGE_NAME}:${VERSION} \
#     src/timestep/services/${IMAGE_NAME}

# fi
