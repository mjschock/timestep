#!/usr/bin/env bash
set -e # exit on first error
set -x # echo on

# Load secrets from JSON file
secrets_json=$(cat secrets.json)

# Print the content of the JSON file for debugging
echo "$secrets_json"

# Extract keys and values
keys=($(echo "$secrets_json" | jq -r 'keys_unsorted[]'))
values=($(echo "$secrets_json" | jq -r 'to_entries[] | .value'))

# Loop through keys and save each secret to a file
for ((i=0; i<${#keys[@]}; i++)); do
    lowercase_key=$(echo "${keys[i]}" | tr '[:upper:]' '[:lower:]')
    echo "${values[i]}" > "secrets/$lowercase_key"
done


# json_secrets=$1
# echo "json_secrets: ${json_secrets}"

# args=("$@")
# echo "args: ${args[@]}"
# echo "args[0]: ${args[0]}"
# echo "args[1]: ${args[1]}"
# echo "args[2]: ${args[2]}"
# echo "args[3]: ${args[3]}"

# Read secrets.json to json_secrets
# json_secrets=$(cat secrets.json)
# cat secrets.json

# json_vars=$(cat vars.json)
# cat vars.json

# print each key/value pair
# for key in $(echo ${json_secrets} | jq -r "keys[]" ); do
#   echo "key: ${key}"
#   echo "value: $(echo ${json_secrets} | jq -r ".[\"$key\"]")"
# done

# Read vars.json to json_vars
# json_vars=$(cat vars.json)
# echo "json_vars: ${json_vars}"

# # For each key in json_secrets, export the key/value pair
# for key in $(echo ${json_secrets} | jq -r "keys[]" ); do
#   export $key=$(echo ${json_secrets} | jq -r ".[\"$key\"]")
# done



# mkdir -p secrets
# Use jq to parse the json_secrets and write to secrets
# jq -r '.[] | .key + "=" + .value' ${json_secrets} > secrets/.env

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
