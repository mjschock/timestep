#!/usr/bin/env sh
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .dot.env)"
eval "$(direnv dotenv bash .env)"

docker login -u ${DOCKER_REGISTRY_USERNAME} -p $(cat ./secrets/docker_registry_password) ${DOCKER_REGISTRY_SERVER}

docker run \
 --env-file .env \
 --env CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER} \
 --env DO_TOKEN=${DO_TOKEN} \
 --env DOCKER_REGISTRY_PASSWORD=${DOCKER_REGISTRY_PASSWORD} \
 --env INGRESS_CONTROLLER_ACME_CA=${INGRESS_CONTROLLER_ACME_CA} \
 --env INGRESS_CONTROLLER_DEBUG=${INGRESS_CONTROLLER_DEBUG} \
 --env INGRESS_CONTROLLER_EMAIL=${INGRESS_CONTROLLER_EMAIL} \
 --env KUBECONTEXT=${KUBECONTEXT} \
 --env PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
 --env TF_API_TOKEN=${TF_API_TOKEN} \
 --env TF_USERNAME=${TF_USERNAME} \
 --user $(id -u):$(id -g) \
 --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
 ${CI_REGISTRY_IMAGE}/cicd:latest poetry run cdktf deploy --auto-approve ${PRIMARY_DOMAIN_NAME}.k3s_cluster ${PRIMARY_DOMAIN_NAME}.kubernetes_config ${PRIMARY_DOMAIN_NAME}.platform
