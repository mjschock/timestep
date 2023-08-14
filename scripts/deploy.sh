#!/usr/bin/env sh
set -x # echo on

mkdir -p secrets
echo ${SSH_PRIVATE_KEY} > secrets/ssh_private_key
echo ${SSH_PRIVATE_KEY_ENV_VAR} > secrets/ssh_private_key_env_var
cat secrets/ssh_private_key_env_var
ls -al secrets
# chmod 600 secrets/ssh_private_key
id

docker run \
 --env-file .env \
 --env CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER} \
 --env DO_TOKEN=${DO_TOKEN} \
 --env DOCKER_REGISTRY_PASSWORD=${DOCKER_REGISTRY_PASSWORD} \
 --env HTPASSWD=${HTPASSWD} \
 --env KUBECONFIG=${KUBECONFIG} \
 --env KUBECONTEXT=${KUBECONTEXT} \
 --env POSTGRESQL_PASSWORD=${POSTGRESQL_PASSWORD} \
 --env PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
 --env TF_API_TOKEN=${TF_API_TOKEN} \
 --env TF_USERNAME=${TF_USERNAME} \
 --user $(id -u):$(id -g) \
 --volume $(pwd)/secrets:/home/ubuntu/secrets:ro \
 ${CI_REGISTRY_IMAGE}:latest poetry run cdktf deploy --auto-approve ${PRIMARY_DOMAIN_NAME}
