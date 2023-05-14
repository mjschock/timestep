#!/bin/sh

multipass_instance_cpus=${MULTIPASS_INSTANCE_CPUS:-1}
multipass_instance_disk=${MULTIPASS_INSTANCE_DISK:-40G}
multipass_instance_image=${MULTIPASS_INSTANCE_IMAGE:-22.04}
multipass_instance_memory=${MULTIPASS_INSTANCE_MEMORY:-4G}
multipass_instance_name=${MULTIPASS_INSTANCE_NAME:-primary}

multipass launch \
  --cpus $multipass_instance_cpus \
  --disk $multipass_instance_disk \
  --memory $multipass_instance_memory \
  --name $multipass_instance_name \
  --cloud-init - <<EOF
users:
- name: ${USER}
  groups: sudo
  sudo: ALL=(ALL) NOPASSWD:ALL
  ssh_authorized_keys: 
  - $(cat "$PUBLIC_SSH_KEY_PATH")
EOF
