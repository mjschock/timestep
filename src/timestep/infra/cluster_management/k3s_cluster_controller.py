import logging
import os
import subprocess
import sys
import tempfile

from timestep.infra.cluster_management.utils import (
    Colors,
    check_gpu,
    cleanup_agent_node,
    cleanup_server_node,
    print_color,
    progress_message,
    run_remote,
    success_message,
)
from timestep.utils import ssh_connect


class K3sClusterController:
    """Manages K3s Kubernetes cluster operations."""

    def __init__(self, cluster_config):
        """
        Initialize K3s cluster controller.

        Args:
            cluster_config (dict): Cluster configuration parameters
        """
        self.logger = logging.getLogger(__name__)
        self.cluster_config = cluster_config

    def create_cluster(self):
        """
        Create a new Kubernetes cluster using k3s.

        Returns:
            bool: Cluster creation status
        """
        cleanup = False
        ips_file = self.cluster_config["ips_file"]
        ssh_key = os.path.expanduser(self.cluster_config["ssh_key"])
        user = self.cluster_config["username"]

        # Check if SSH key exists
        if not os.path.isfile(ssh_key):
            print_color(f"Error: SSH key not found: {ssh_key}", Colors.RED)
            sys.exit(1)

        # Check if IPs file exists
        if not os.path.isfile(ips_file):
            print_color(f"Error: IPs file not found: {ips_file}", Colors.RED)
            sys.exit(1)

        # Read nodes from file
        with open(ips_file) as f:
            nodes = f.read().splitlines()

        if not nodes:
            print_color(
                "Error: IPs file is empty or not formatted correctly.", Colors.RED
            )
            sys.exit(1)

        head_node = nodes[0]
        worker_nodes = nodes[1:]

        k3s_token = "mytoken"  # Any string can be used as the token
        install_gpu = False

        # If cleanup flag is set, uninstall k3s and exit
        if cleanup:
            print_color("Starting cleanup...", Colors.YELLOW)
            cleanup_server_node(head_node, user, ssh_key)
            for node in worker_nodes:
                cleanup_agent_node(node, user, ssh_key)
            print_color("Cleanup completed successfully.", Colors.GREEN)
            return

        # Deploy head node
        progress_message(f"Deploying Kubernetes on head node ({head_node})...")
        head_node_cmd = f"""
            curl -sfL https://get.k3s.io | \
            INSTALL_K3S_EXEC="server --cluster-init --disable=traefik --flannel-backend=wireguard-native" \
            K3S_TOKEN={k3s_token} sh - &&
            mkdir -p ~/.kube &&
            sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config &&
            sudo chown $(id -u):$(id -g) ~/.kube/config &&
            for i in $(seq 1 3); do
                if kubectl wait --for=condition=ready node --all --timeout=2m --kubeconfig ~/.kube/config; then
                    break
                else
                    echo 'Waiting for nodes to be ready...'
                    sleep 5
                fi
            done
            if [ $i -eq 3 ]; then
                echo 'Failed to wait for nodes to be ready after 3 attempts'
                exit 1
            fi
        """
        run_remote(head_node, user, ssh_key, head_node_cmd)
        success_message("K3s deployed on head node.")

        # Check for GPU on head node
        if check_gpu(head_node, user, ssh_key):
            print_color(f"GPU detected on head node ({head_node}).", Colors.YELLOW)
            install_gpu = True

        # Get head node's internal IP
        master_addr = run_remote(
            head_node, user, ssh_key, "hostname -I | awk '{print $1}'"
        )
        print_color(f"Master node internal IP: {master_addr}", Colors.GREEN)

        # Deploy worker nodes
        for node in worker_nodes:
            progress_message(f"Deploying Kubernetes on worker node ({node})...")

            if node == "127.0.0.1":
                # Local installation
                cmd = f"""
                    curl -sfL https://get.k3s.io | \
                    INSTALL_K3S_EXEC="agent" \
                    K3S_TOKEN={k3s_token} \
                    K3S_URL=https://{master_addr}:6443 sh -
                """
                subprocess.run(cmd, shell=True, check=True)
            else:
                # Remote installation
                worker_cmd = f"""
                    curl -sfL https://get.k3s.io | \
                    INSTALL_K3S_EXEC="agent" \
                    K3S_TOKEN={k3s_token} \
                    K3S_URL=https://{master_addr}:6443 sh -
                """
                run_remote(node, user, ssh_key, worker_cmd)

            success_message(f"Kubernetes deployed on worker node ({node}).")

            # Check for GPU on worker node
            if check_gpu(node, user, ssh_key):
                print_color(f"GPU detected on worker node ({node}).", Colors.YELLOW)
                install_gpu = True

        # Configure local kubectl
        progress_message("Configuring local kubectl to connect to the cluster...")
        kubeconfig_dir = os.path.expanduser("~/.kube")
        os.makedirs(kubeconfig_dir, exist_ok=True)

        # Copy kubeconfig from master node
        scp_cmd = [
            "scp",
            "-o",
            "StrictHostKeyChecking=no",
            "-i",
            ssh_key,
            f"{user}@{head_node}:~/.kube/config",
            os.path.join(kubeconfig_dir, "config"),
        ]
        subprocess.run(scp_cmd, check=True)

        # Update kubeconfig
        kubeconfig_path = os.path.join(kubeconfig_dir, "config")
        if os.path.exists(kubeconfig_path):
            print("Backing up existing kubeconfig")
            subprocess.run(
                ["cp", kubeconfig_path, f"{kubeconfig_path}.bak"], check=True
            )

        # Modify kubeconfig
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            with open(kubeconfig_path) as f:
                in_cluster = False
                for line in f:
                    if line.strip() == "clusters:":
                        in_cluster = True
                    elif line.strip() == "users:":
                        in_cluster = False

                    if in_cluster and "certificate-authority-data:" in line:
                        continue
                    elif in_cluster and "server:" in line:
                        temp_file.write(f"    server: https://{head_node}:6443\n")
                        temp_file.write("    insecure-skip-tls-verify: true\n")
                    else:
                        temp_file.write(line)

        os.replace(temp_file.name, kubeconfig_path)
        success_message("kubectl configured to connect to the cluster.")

        # Install GPU operator if needed
        if install_gpu:
            print_color(
                "GPU detected in the cluster. Installing Nvidia GPU Operator...",
                Colors.YELLOW,
            )
            gpu_install_cmd = """
                curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 &&
                chmod 700 get_helm.sh &&
                ./get_helm.sh &&
                helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update &&
                kubectl create namespace gpu-operator --kubeconfig ~/.kube/config || true &&
                sudo ln -s /sbin/ldconfig /sbin/ldconfig.real || true &&
                helm install gpu-operator -n gpu-operator --create-namespace nvidia/gpu-operator \
                --set 'toolkit.env[0].name=CONTAINERD_CONFIG' \
                --set 'toolkit.env[0].value=/var/lib/rancher/k3s/agent/etc/containerd/config.toml' \
                --set 'toolkit.env[1].name=CONTAINERD_SOCKET' \
                --set 'toolkit.env[1].value=/run/k3s/containerd/containerd.sock' \
                --set 'toolkit.env[2].name=CONTAINERD_RUNTIME_CLASS' \
                --set 'toolkit.env[2].value=nvidia' &&
                echo 'Waiting for GPU operator installation...' &&
                while ! kubectl describe nodes --kubeconfig ~/.kube/config | grep -q 'nvidia.com/gpu:'; do
                    echo 'Waiting for GPU operator...'
                    sleep 5
                done
                echo 'GPU operator installed successfully.'
            """
            run_remote(head_node, user, ssh_key, gpu_install_cmd)
            success_message("GPU Operator installed.")
        else:
            print_color(
                "No GPUs detected. Skipping GPU Operator installation.", Colors.YELLOW
            )
            helm_install_cmd = """
                curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 &&
                chmod 700 get_helm.sh &&
                ./get_helm.sh
            """
            run_remote(head_node, user, ssh_key, helm_install_cmd)
            success_message("Helm installed.")

        # Configure SkyPilot
        progress_message("Configuring SkyPilot...")
        success_message("SkyPilot configured successfully.")

        # Final success message
        print_color(
            "==== 🎉 Kubernetes cluster deployment completed successfully 🎉 ====",
            Colors.GREEN,
        )
        print("You can now interact with your Kubernetes cluster through SkyPilot: ")
        print("  • List available GPUs: sky show-gpus --cloud kubernetes")
        print(
            "  • Launch a GPU development pod: sky launch -c devbox --cloud kubernetes --gpus A100:1"
        )
        print("  • Connect to pod with SSH: ssh devbox")
        print("  • Connect to pod with VSCode: code --remote ssh-remote+devbox '/'")

        try:
            import sky.check

            sky.check.check(
                clouds=["kubernetes"],
                quiet=False,
                verbose=True,
            )

        except ModuleNotFoundError as e:
            self.logger.error(f"Failed to import sky.check: {e}")

            subprocess.run(["sky", "check", "k8s"])

        subprocess.run(["sky", "show-gpus", "--cloud", "k8s"])

        self.logger.info(
            f"Deploying Helm charts to K3s cluster: {self.cluster_config['ip']}"
        )

        SCRIPT = """#!/usr/bin/env bash
        echo "Installing Helm chart for MLflow..."
        # helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow --atomic --create-namespace --namespace mlflow --set nodeSelector.name=timestep
        helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow --create-namespace --namespace mlflow --set nodeSelector.name=timestep
        echo "...done"
        """

        ssh_connect(
            self.cluster_config["ip"],
            script=SCRIPT,
            username=self.cluster_config["username"],
            ssh_key=os.path.expanduser(self.cluster_config["ssh_key"]),
        )

    def delete_cluster(self):
        """
        Delete the existing K3s cluster.

        Returns:
            bool: Cluster deletion status
        """
        raise NotImplementedError()
