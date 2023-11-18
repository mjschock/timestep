#!/usr/bin/bash sh
set -e # exit on first error
set -x # echo on

# Install NVIDIA Container Toolkit
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit

# Configure the repository
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && \
    sudo apt-get update

# Install the NVIDIA Container Toolkit packages
sudo apt-get install -y nvidia-container-toolkit # TODO: is this needed?

# Install the NVIDIA Container Runtime packages
# https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#ubuntu-lts
# https://docs.k3s.io/advanced#nvidia-container-runtime-support
sudo apt-get install linux-headers-$(uname -r)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g')
wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb && rm cuda-keyring_1.0-1_all.deb
sudo apt-get update
# sudo apt-get -y install cuda-drivers
sudo apt-get install --no-install-recommends -y nvidia-container-runtime cuda-drivers-fabricmanager
nvidia_driver_version=$(modinfo $(find /usr/lib/modules -name nvidia.ko) | grep ^version | awk '{print $2}' | cut -d '.' -f1)
sudo apt-get install --no-install-recommends -y nvidia-headless-$nvidia_driver_version

# Restart K3s
# TODO

# Confirm that the nvidia container runtime has been found by k3s: grep nvidia /var/lib/rancher/k3s/agent/etc/containerd/config.toml
sudo grep nvidia /var/lib/rancher/k3s/agent/etc/containerd/config.toml
