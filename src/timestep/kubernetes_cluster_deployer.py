#!/usr/bin/env python3

import os
import shutil
import socket
import subprocess
import sys
import tempfile
from typing import List, Optional

import paramiko

# Requires:
# pip install paramiko


class KubernetesClusterDeployer:
    def __init__(
        self, ips_file: str, username: str, ssh_key: str, cleanup: bool = False
    ):
        self.RED = "\033[0;31m"
        self.GREEN = "\033[0;32m"
        self.YELLOW = "\033[1;33m"
        self.NC = "\033[0m"  # No color

        self.ips_file = ips_file
        self.username = username
        self.ssh_key = ssh_key
        self.cleanup = cleanup
        self.k3s_token = "mytoken"

        # Validate inputs
        self._validate_inputs()

        # Read IPs
        self.head_node, self.worker_nodes = self._read_ips()

    def _validate_inputs(self):
        """Validate input arguments and files."""
        if not os.path.exists(self.ssh_key):
            self._error(f"SSH key not found: {self.ssh_key}")

        if not os.path.exists(self.ips_file):
            self._error(f"IPs file not found: {self.ips_file}")

    def _read_ips(self) -> tuple:
        """Read head node and worker nodes from IPs file."""
        with open(self.ips_file, "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        if not lines:
            self._error("IPs file is empty or not formatted correctly")

        return lines[0], lines[1:]

    def _error(self, message: str):
        """Print error and exit."""
        print(f"{self.RED}Error: {message}{self.NC}", file=sys.stderr)
        sys.exit(1)

    def _progress_message(self, message: str):
        """Print a progress message."""
        print(f"{self.YELLOW}➜ {message}{self.NC}")

    def _success_message(self, message: str):
        """Print a success message."""
        print(f"{self.GREEN}✔ {message}{self.NC}")

    def _ssh_connect(self, hostname: str):
        """Create an SSH connection."""
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname, username=self.username, key_filename=self.ssh_key)
            return ssh
        except Exception as e:
            self._error(f"SSH connection failed to {hostname}: {e}")

    def _run_remote_command(self, hostname: str, command: str) -> tuple:
        """Run a command on a remote host via SSH."""
        with self._ssh_connect(hostname) as ssh:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode("utf-8")
            error = stderr.read().decode("utf-8")
            return output, error

    def _copy_remote_file(self, hostname: str, remote_path: str, local_path: str):
        """Copy a file from remote host to local machine."""
        with self._ssh_connect(hostname) as ssh:
            sftp = ssh.open_sftp()
            sftp.get(remote_path, local_path)
            sftp.close()

    def cleanup_node(self, node_ip: str, is_server: bool = False):
        """Cleanup a node by uninstalling k3s."""
        self._progress_message(f"Cleaning up node {node_ip}...")

        if node_ip == "127.0.0.1":
            # Local cleanup
            uninstall_cmd = (
                "/usr/local/bin/k3s-uninstall.sh"
                if is_server
                else "/usr/local/bin/k3s-agent-uninstall.sh"
            )
            cleanup_paths = [
                "/etc/rancher",
                "/var/lib/rancher",
                "/var/lib/kubelet",
                "/etc/kubernetes",
                os.path.expanduser("~/.kube"),
            ]

            try:
                subprocess.run([uninstall_cmd], check=False)
                for path in cleanup_paths:
                    shutil.rmtree(path, ignore_errors=True)
            except Exception as e:
                print(f"Warning: Local cleanup failed: {e}")
        else:
            # Remote cleanup
            cleanup_script = f"""
            echo 'Uninstalling k3s...' &&
            {'k3s-uninstall.sh' if is_server else 'k3s-agent-uninstall.sh'} || true &&
            sudo rm -rf /etc/rancher /var/lib/rancher /var/lib/kubelet /etc/kubernetes ~/.kube
            """
            self._run_remote_command(node_ip, cleanup_script)

        self._success_message(f"Node {node_ip} cleaned up successfully.")

    def check_gpu(self, node_ip: str) -> bool:
        """Check if a GPU is available on the node."""
        try:
            if node_ip == "127.0.0.1":
                result = subprocess.run(
                    ["nvidia-smi", "--list-gpus"], capture_output=True, text=True
                )
                return "GPU 0" in result.stdout
            else:
                output, _ = self._run_remote_command(
                    node_ip,
                    "command -v nvidia-smi &> /dev/null && nvidia-smi --list-gpus | grep 'GPU 0'",
                )
                return "GPU 0" in output
        except Exception:
            return False

    def deploy_cluster(self):
        """Deploy Kubernetes cluster."""
        if self.cleanup:
            self._cleanup_all()
            return

        # Step 1: Install k3s on head node
        self._deploy_head_node()

        # Step 2: Deploy worker nodes
        self._deploy_worker_nodes()

        # Step 3: Configure local kubectl
        self._configure_kubectl()

        # Optional GPU Operator installation
        self._install_gpu_operator()

        # Final messages
        self._final_configuration()

    def _deploy_head_node(self):
        """Deploy k3s on the head node."""
        self._progress_message(
            f"Deploying Kubernetes on head node ({self.head_node})..."
        )

        install_cmd = f"""
        curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --cluster-init --disable=traefik --flannel-backend=wireguard-native" K3S_TOKEN={self.k3s_token} sh - &&
        mkdir -p ~/.kube &&
        sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config &&
        sudo chown $(id -u):$(id -g) ~/.kube/config
        """

        output, error = self._run_remote_command(self.head_node, install_cmd)

        if error:
            self._error(f"Head node deployment failed: {error}")

        self._success_message("K3s deployed on head node.")

    def _deploy_worker_nodes(self):
        """Deploy k3s on worker nodes."""
        master_addr = self._get_master_address()

        for node in self.worker_nodes:
            self._progress_message(f"Deploying Kubernetes on worker node ({node})...")

            install_cmd = f"""
            curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="agent" K3S_TOKEN={self.k3s_token} K3S_URL=https://{master_addr}:6443 sh -
            """

            if node == "127.0.0.1":
                subprocess.run(install_cmd, shell=True, check=True)
            else:
                self._run_remote_command(node, install_cmd)

            self._success_message(f"Kubernetes deployed on worker node ({node}).")

    def _get_master_address(self) -> str:
        """Get the internal IP of the master node."""
        output, _ = self._run_remote_command(
            self.head_node, "hostname -I | awk '{print $1}'"
        )
        return output.strip()

    def _configure_kubectl(self):
        """Configure local kubectl to connect to the cluster."""
        self._progress_message("Configuring local kubectl to connect to the cluster...")

        # Ensure .kube directory exists
        os.makedirs(os.path.expanduser("~/.kube"), exist_ok=True)

        # Copy kubeconfig
        local_kubeconfig = os.path.expanduser("~/.kube/config")

        # Backup existing config if it exists
        if os.path.exists(local_kubeconfig):
            shutil.copy(local_kubeconfig, f"{local_kubeconfig}.bak")

        # Get remote kubeconfig and modify it
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_config:
            self._copy_remote_file(self.head_node, "~/.kube/config", temp_config.name)

        # Modify kubeconfig to use head node's IP
        with open(temp_config.name, "r") as f:
            config_content = f.read()

        modified_config = config_content.replace(
            "server: https://127.0.0.1:6443", f"server: https://{self.head_node}:6443"
        )
        modified_config = modified_config.replace(
            "certificate-authority-data:",
            "# certificate-authority-data:\n    insecure-skip-tls-verify: true",
        )

        with open(local_kubeconfig, "w") as f:
            f.write(modified_config)

        os.unlink(temp_config.name)

        self._success_message("kubectl configured to connect to the cluster.")

    def _install_gpu_operator(self):
        """Install Nvidia GPU Operator if GPUs are detected."""
        gpu_detected = self.check_gpu(self.head_node) or any(
            self.check_gpu(node) for node in self.worker_nodes
        )

        if not gpu_detected:
            print(
                f"{self.YELLOW}No GPUs detected. Skipping GPU Operator installation.{self.NC}"
            )
            return

        self._progress_message("GPU detected. Installing Nvidia GPU Operator...")

        gpu_install_cmd = """
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 &&
        chmod 700 get_helm.sh &&
        ./get_helm.sh &&
        helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update &&
        kubectl create namespace gpu-operator --kubeconfig ~/.kube/config || true &&
        sudo ln -s /sbin/ldconfig /sbin/ldconfig.real || true &&
        helm install gpu-operator -n gpu-operator --create-namespace nvidia/gpu-operator \\
        --set 'toolkit.env[0].name=CONTAINERD_CONFIG' \\
        --set 'toolkit.env[0].value=/var/lib/rancher/k3s/agent/etc/containerd/config.toml' \\
        --set 'toolkit.env[1].name=CONTAINERD_SOCKET' \\
        --set 'toolkit.env[1].value=/run/k3s/containerd/containerd.sock' \\
        --set 'toolkit.env[2].name=CONTAINERD_RUNTIME_CLASS' \\
        --set 'toolkit.env[2].value=nvidia'
        """

        output, error = self._run_remote_command(self.head_node, gpu_install_cmd)

        if error:
            self._error(f"GPU Operator installation failed: {error}")

        self._success_message("GPU Operator installed successfully.")

    def _final_configuration(self):
        """Display final configuration and success message."""
        print(
            f"{self.GREEN}==== 🎉 Kubernetes cluster deployment completed successfully 🎉 ===={self.NC}"
        )
        print("You can now interact with your Kubernetes cluster through SkyPilot: ")
        print("  • List available GPUs: sky show-gpus --cloud kubernetes")
        print(
            "  • Launch a GPU development pod: sky launch -c devbox --cloud kubernetes --gpus A100:1"
        )
        print("  • Connect to pod with SSH: ssh devbox")
        print("  • Connect to pod with VSCode: code --remote ssh-remote+devbox '/'")

    def _cleanup_all(self):
        """Cleanup all nodes in the cluster."""
        print(f"{self.YELLOW}Starting cleanup...{self.NC}")

        # Cleanup head node
        self.cleanup_node(self.head_node, is_server=True)

        # Cleanup worker nodes
        for node in self.worker_nodes:
            self.cleanup_node(node, is_server=False)

        self._success_message("Cleanup completed successfully.")


def main():
    if len(sys.argv) < 4:
        print(
            "Usage: python kubernetes_cluster_deployer.py ips.txt username path/to/ssh/key [--cleanup]"
        )
        sys.exit(1)

    ips_file = sys.argv[1]
    username = sys.argv[2]
    ssh_key = sys.argv[3]
    cleanup = "--cleanup" in sys.argv

    deployer = KubernetesClusterDeployer(ips_file, username, ssh_key, cleanup)
    deployer.deploy_cluster()


if __name__ == "__main__":
    main()
