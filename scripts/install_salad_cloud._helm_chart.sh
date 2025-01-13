#!/usr/bin/env bash

export apiKey=${SALAD_CLOUD_API_KEY}
export organizationName=timestep-ai
export projectName=timestep-ai
export imageRepository=docker.io/mschock/virtual-kubelet-saladcloud
export imageTag=latest

echo "apiKey: ${apiKey}"
echo "organizationName: ${organizationName}"
echo "projectName: ${projectName}"
echo "imageRepository: ${imageRepository}"
echo "imageTag: ${imageTag}"

helm upgrade \
   --create-namespace \
   --namespace saladcloud \
   --set salad.apiKey=${apiKey} \
   --set salad.organizationName=${organizationName} \
   --set salad.projectName=${projectName} \
   --set provider.image.repository=${imageRepository} \
   --set provider.image.tag=${imageTag} \
   saladcloud-node \
   ./src/lib/virtual-kubelet-saladcloud/charts/virtual-kubelet
