#!/usr/bin/env bash
set -ex

# Function to wait for SkyPilot GPU labeling jobs to complete
wait_for_gpu_labeling_jobs() {
    echo "Starting wait for SkyPilot GPU labeling jobs to complete..."

    SECONDS=0
    TIMEOUT=600  # 10 minutes in seconds

    while true; do
        TOTAL_JOBS=$(kubectl get jobs -n kube-system -l job=sky-gpu-labeler --no-headers | wc -l)
        COMPLETED_JOBS=$(kubectl get jobs -n kube-system -l job=sky-gpu-labeler --no-headers | grep "1/1" | wc -l)

        if [[ $COMPLETED_JOBS -eq $TOTAL_JOBS ]]; then
            echo "All SkyPilot GPU labeling jobs completed ($TOTAL_JOBS)."
            break
        elif [ $SECONDS -ge $TIMEOUT ]; then
            echo "Timeout reached while waiting for GPU labeling jobs."
            exit 1
        else
            echo "Waiting for GPU labeling jobs to complete... ($COMPLETED_JOBS/$TOTAL_JOBS completed)"
            echo "To check status, see GPU labeling pods:"
            echo "kubectl get jobs -n kube-system -l job=sky-gpu-labeler"
            sleep 5
        fi
    done
}

# install k3s
# echo "Installing k3s"
# curl -sfL https://get.k3s.io | sh -

# Copy over kubeconfig file
# echo "Copying kubeconfig file"
# mkdir -p $HOME/.kube
# sudo cp /etc/rancher/k3s/k3s.yaml $HOME/.kube/config
# sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Wait for k3s to be ready
echo "Waiting for k3s to be ready"
sleep 5
kubectl wait --for=condition=ready node --all --timeout=5m

# =========== GPU support ===========
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update

# Create namespace if it doesn't exist
echo "Creating namespace gpu-operator"
kubectl create namespace gpu-operator || true

# Install GPU operator
echo "Installing GPU operator"
helm install gpu-operator -n gpu-operator --create-namespace \
nvidia/gpu-operator $HELM_OPTIONS \
  --set 'toolkit.env[0].name=CONTAINERD_CONFIG' \
  --set 'toolkit.env[0].value=/var/lib/rancher/k3s/agent/etc/containerd/config.toml' \
  --set 'toolkit.env[1].name=CONTAINERD_SOCKET' \
  --set 'toolkit.env[1].value=/run/k3s/containerd/containerd.sock' \
  --set 'toolkit.env[2].name=CONTAINERD_RUNTIME_CLASS' \
  --set 'toolkit.env[2].value=nvidia' || true

# Create RuntimeClass
echo "Creating RuntimeClass"
kubectl apply -f - <<EOF
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: nvidia
handler: nvidia
EOF

# Label nodes with GPUs
echo "Labelling nodes with GPUs..."
python -m sky.utils.kubernetes.gpu_labeler

# Wait for all the GPU labeling jobs to complete
wait_for_gpu_labeling_jobs

echo "K3s cluster ready! To setup Kubernetes access in SkyPilot, run: sky check kubernetes"
