#!/usr/bin/env sh
set -x # echo on

# docker build --cache-from ${CI_REGISTRY_IMAGE}:latest --tag ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA} --tag ${CI_REGISTRY_IMAGE}:latest .
# docker build --cache-from ${CI_REGISTRY_IMAGE}:latest --tag ${CI_REGISTRY_IMAGE}:latest .
# docker push ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}
# docker push ${CI_REGISTRY_IMAGE}:latest
# docker compose pull || true
docker buildx build \
  --cache-from ${CI_REGISTRY_IMAGE}:latest \
  --cache-to type=inline,ref=${CI_REGISTRY_IMAGE}:latest \
  --push \
  --tag ${CI_REGISTRY_IMAGE}:latest \
  .

# docker build --cache-from registry.gitlab.com/timestep-ai/caddy:latest --tag ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA} --tag ${CI_REGISTRY_IMAGE}:latest .
# docker compose build
# docker compose push
docker buildx bake --pull --push
# docker run timestep kompose convert --build local --build-command "helm package timestep-ai" --chart --file docker-compose.yml --push-image --push-command "helm push timestep-ai-0.0.1.tgz oci://registry.gitlab.com/timestep-ai/timestep" --push-image-registry registry.gitlab.com --out timestep-ai --secrets-as-files --verbose'
