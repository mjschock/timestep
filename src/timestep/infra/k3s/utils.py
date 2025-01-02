import os
import subprocess


# ANSI color codes for terminal output
class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    NC = "\033[0m"  # No color


def print_color(message: str, color: str) -> None:
    """Print a message with color."""
    print(f"{color}{message}{Colors.NC}")


def progress_message(message: str) -> None:
    """Show a progress message."""
    print_color(f"➜ {message}", Colors.YELLOW)


def success_message(message: str) -> None:
    """Show a success message."""
    print_color(f"✔ {message}", Colors.GREEN)


def run_remote(node_ip: str, user: str, ssh_key: str, command: str) -> str:
    """Run a command on a remote machine via SSH."""
    ssh_cmd = [
        "ssh",
        "-o",
        "StrictHostKeyChecking=no",
        "-i",
        ssh_key,
        f"{user}@{node_ip}",
        command,
    ]
    try:
        result = subprocess.run(ssh_cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print_color(f"Error running command on {node_ip}: {e.stderr}", Colors.RED)
        raise


def check_gpu(node_ip: str, user: str, ssh_key: str) -> bool:
    """Check if a node has a GPU."""
    if node_ip == "127.0.0.1":
        try:
            subprocess.run(
                ["nvidia-smi", "--list-gpus"], capture_output=True, check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    else:
        try:
            run_remote(
                node_ip,
                user,
                ssh_key,
                "command -v nvidia-smi && nvidia-smi --list-gpus | grep 'GPU 0'",
            )
            return True
        except subprocess.CalledProcessError:
            return False


def cleanup_server_node(node_ip: str, user: str, ssh_key: str) -> None:
    """Uninstall k3s and clean up the state on a server node."""
    print_color(f"Cleaning up head node {node_ip}...", Colors.YELLOW)
    cleanup_cmd = """
        echo 'Uninstalling k3s...' &&
        /usr/local/bin/k3s-uninstall.sh || true &&
        sudo rm -rf /etc/rancher /var/lib/rancher /var/lib/kubelet /etc/kubernetes ~/.kube
    """
    run_remote(node_ip, user, ssh_key, cleanup_cmd)
    success_message(f"Node {node_ip} cleaned up successfully.")


def cleanup_agent_node(node_ip: str, user: str, ssh_key: str) -> None:
    """Uninstall k3s and clean up the state on an agent node."""
    print_color(f"Cleaning up node {node_ip}...", Colors.YELLOW)

    if node_ip == "127.0.0.1":
        print("Running command locally...")
        try:
            subprocess.run(["/usr/local/bin/k3s-agent-uninstall.sh"], check=False)
            subprocess.run(
                [
                    "sudo",
                    "rm",
                    "-rf",
                    "/etc/rancher",
                    "/var/lib/rancher",
                    "/var/lib/kubelet",
                    "/etc/kubernetes",
                    os.path.expanduser("~/.kube"),
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print_color(f"Error during local cleanup: {e}", Colors.RED)
    else:
        cleanup_cmd = """
            echo 'Uninstalling k3s...' &&
            /usr/local/bin/k3s-agent-uninstall.sh || true &&
            sudo rm -rf /etc/rancher /var/lib/rancher /var/lib/kubelet /etc/kubernetes ~/.kube
        """
        run_remote(node_ip, user, ssh_key, cleanup_cmd)

    success_message(f"Node {node_ip} cleaned up successfully.")
