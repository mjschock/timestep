#!/usr/bin/env sh
set -x # echo on

echo $CI_REGISTRY_USER
echo '$CI_REGISTRY_USER'
echo ${CI_REGISTRY_USER}
echo '${CI_REGISTRY_USER}'

docker login -u '$CI_REGISTRY_USER' -p '$CI_REGISTRY_PASSWORD' '$CI_REGISTRY'
docker pull '$CI_REGISTRY_IMAGE':latest || true
