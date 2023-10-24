#!/usr/bin/env sh
set -e # exit on first error
set -x # echo on

docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD} ${DOCKER_REGISTRY_SERVER}

# docker run \
#  --env-file .env \
#  --env CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER} \
#  --env DO_TOKEN=${DO_TOKEN} \
#  --env DOCKER_REGISTRY_PASSWORD=${DOCKER_REGISTRY_PASSWORD} \
#  --env HTPASSWD=${HTPASSWD} \
#  --env KUBECONTEXT=${KUBECONTEXT} \
#  --env PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
#  --env TF_API_TOKEN=${TF_API_TOKEN} \
#  --env TF_USERNAME=${TF_USERNAME} \
#  --user $(id -u):$(id -g) \
#  --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
#  --volume $(pwd)/timestep-ai:/home/ubuntu/timestep-ai:rw \
#  ${CI_REGISTRY_IMAGE}:latest kompose convert --chart --file docker-compose.yml --out timestep-ai --secrets-as-files --verbose

docker run \
 --env-file .env \
 --env CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER} \
 --env DO_TOKEN=${DO_TOKEN} \
 --env DOCKER_REGISTRY_PASSWORD=${DOCKER_REGISTRY_PASSWORD} \
 --env HTPASSWD=${HTPASSWD} \
 --env KUBECONTEXT=${KUBECONTEXT} \
 --env PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
 --env TF_API_TOKEN=${TF_API_TOKEN} \
 --env TF_USERNAME=${TF_USERNAME} \
 --user $(id -u):$(id -g) \
 --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
 --volume $(pwd)/timestep-ai:/home/ubuntu/timestep-ai:rw \
 --volume $(pwd)/dist:/home/ubuntu/dist:rw \
 ${CI_REGISTRY_IMAGE}:latest helm package timestep-ai --destination /home/ubuntu/dist --version $(cat .env | grep ^VERSION | cut -d '=' -f2)

docker run \
 --env-file .env \
 --env CLOUD_INSTANCE_PROVIDER=${CLOUD_INSTANCE_PROVIDER} \
 --env DO_TOKEN=${DO_TOKEN} \
 --env DOCKER_REGISTRY_PASSWORD=${DOCKER_REGISTRY_PASSWORD} \
 --env HTPASSWD=${HTPASSWD} \
 --env INGRESS_CONTROLLER_ACME_CA=${INGRESS_CONTROLLER_ACME_CA} \
 --env INGRESS_CONTROLLER_DEBUG=${INGRESS_CONTROLLER_DEBUG} \
 --env INGRESS_CONTROLLER_EMAIL=${INGRESS_CONTROLLER_EMAIL} \
 --env KUBECONTEXT=${KUBECONTEXT} \
 --env PRIMARY_DOMAIN_NAME=${PRIMARY_DOMAIN_NAME} \
 --env TF_API_TOKEN=${TF_API_TOKEN} \
 --env TF_USERNAME=${TF_USERNAME} \
 --user $(id -u):$(id -g) \
 --volume $(pwd)/secrets:/home/ubuntu/secrets:rw \
 --volume $(pwd)/timestep-ai:/home/ubuntu/timestep-ai:rw \
 --volume $(pwd)/dist:/home/ubuntu/dist:rw \
 ${CI_REGISTRY_IMAGE}:latest poetry run cdktf deploy --auto-approve ${PRIMARY_DOMAIN_NAME}.k3s_cluster ${PRIMARY_DOMAIN_NAME}.kubernetes_config
 