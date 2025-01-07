import datetime
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import List, Optional

from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeImage,
    NodeLocation,
    NodeSize,
    NodeState,
)


class VagrantNodeDriver(NodeDriver):
    name: str = "Vagrant"
    ssh_public_key: str = None

    def __init__(
        self,
        key: str = None,
        secret: str = None,
        secure: bool = True,
        host: str = None,
        port: int = None,
        **kwargs,
    ):
        super().__init__(
            key=key, secret=secret, secure=secure, host=host, port=port, **kwargs
        )

        cwd = os.getcwd()
        self.work_dir = Path(cwd)

    def create_key_pair(self, name: str, public_key: str = None) -> KeyPair:
        """Store SSH public key for later use."""
        self.ssh_public_key = public_key
        return self.get_key_pair(name)

    def create_node(
        self, name, size, image, location=None, auth=None, **kwargs
    ) -> Node:
        """Create and provision a new node."""
        ex_create_attr = kwargs.get("ex_create_attr", {})
        ssh_keys = ex_create_attr.get("ssh_keys", [])

        # Generate cloud-init configuration
        # cloud_init = self._generate_cloud_init(ssh_keys[0] if ssh_keys else None)

        # Update Vagrantfile with cloud-init configuration
        # vagrant_path = self.work_dir / "Vagrantfile"
        # content = vagrant_path.read_text()
        # content = content.replace("#{CLOUD_INIT}", cloud_init)
        # vagrant_path.write_text(content)

        # Start Vagrant VM

        cloud_init_stdin = f"""users:
  - default
  - name: sky
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - {ssh_keys[0]}"""

        vagrantfile_content = f"""
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.hostname = "ubuntu-node"
  
  # Network configuration
  config.vm.network "private_network", type: "dhcp"
  
  # VM resources configuration
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
  end
  
  # Cloud-init configuration
  config.vm.provision "shell", inline: <<-SHELL
    # Write cloud-init configuration
    cat > /tmp/cloud-init.cfg <<'EOL'
{cloud_init_stdin}
EOL
    
    # Apply cloud-init configuration
    cloud-init single --name cc_users_groups --frequency always --file /tmp/cloud-init.cfg
  SHELL
end
"""

        # with os.getcwd() as work_dir:
        cwd = os.getcwd()

        with Path(f"{cwd}/Vagrantfile").open("w") as f:
            # vagrantfile_path = Path(work_dir) / "Vagrantfile"
            # vagrantfile_path.write_text(vagrantfile_content)
            f.write(vagrantfile_content)

        # raise Exception("Not implemented")

        print("Creating node...")

        try:
            subprocess.run(
                ["vagrant", "up", "--install-provider", "--provider", "virtualbox"],
                # cwd=self.work_dir,
                cwd=cwd,
                check=True,
                capture_output=True,
                text=True,
            )

        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to create node: {e.stdout}\n{e.stderr}")

        print("Node created successfully")

        return Node(
            id=name,
            name=name,
            state=NodeState.RUNNING,
            public_ips=self._get_node_ips(),
            private_ips=[],
            driver=self,
            size=size,
            image=image,
            extra={},
            created_at=datetime.datetime.now(),
        )

    def _get_node_ips(self) -> List[str]:
        """Get IP addresses of the VM."""
        try:
            result = subprocess.run(
                ["vagrant", "ssh", "-c", "hostname -I"],
                cwd=self.work_dir,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip().split()
        except subprocess.CalledProcessError:
            return []

    def _prepare(self):
        """Prepare the driver for use."""

        # If Vagrant is not installed, install it
        try:
            subprocess.run(["vagrant", "--version"], check=True, capture_output=True)

        except FileNotFoundError:
            # print("Vagrant is not installed. Please install Vagrant and try again.")
            # raise

            print("Vagrant is not installed. Installing Vagrant...")

            amazon_linux_script = """
sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install vagrant virtualbox
            """

            centos_rhel_script = """
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install vagrant virtualbox
            """

            debian_ubuntu_script = """
set -e
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt-get update && sudo apt-get install vagrant virtualbox
            """

            fedora_script = """
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf -y install vagrant virtualbox
            """

            homebrew_macos_script = """
brew tap hashicorp/tap
brew install hashicorp/tap/hashicorp-vagrant
brew install --cask virtualbox
            """

            homebrew_linux_script = """
brew tap hashicorp/tap
brew install hashicorp/tap/vagrant
brew install --cask virtualbox
            """

            windows_script = """
choco install vagrant virtualbox
            """

            os_name = os.uname().sysname
            print("os_name:", os_name)

            try:
                subprocess.run(
                    ["bash", "-c", debian_ubuntu_script],
                    check=True,
                    capture_output=True,
                )

            except subprocess.CalledProcessError as e:
                print(f"Failed to install Vagrant: {e.stderr}")
                raise

        return self

    def destroy_node(self, node: Node) -> bool:
        """Destroy the node and clean up."""
        try:
            subprocess.run(
                ["vagrant", "destroy", "-f"],
                cwd=self.work_dir,
                check=True,
                capture_output=True,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def get_key_pair(self, name: str) -> Optional[KeyPair]:
        """Retrieve stored SSH key pair."""
        if self.ssh_public_key:
            return KeyPair(
                name=name,
                public_key=self.ssh_public_key,
                fingerprint=self.ssh_public_key,
                driver=self,
                private_key="",
            )
        return None

    def list_nodes(self) -> List[Node]:
        """List all nodes."""
        try:
            status = subprocess.run(
                ["vagrant", "status", "--machine-readable"],
                cwd=self.work_dir,
                capture_output=True,
                text=True,
                check=True,
            )

            nodes = []
            for line in status.stdout.splitlines():
                if "state" in line:
                    print("line:", line)
                    _, name, _, state = line.split(",")
                    nodes.append(
                        Node(
                            id=name,
                            name=name,
                            state=(
                                NodeState.RUNNING
                                if state == "running"
                                else NodeState.UNKNOWN
                            ),
                            public_ips=(
                                self._get_node_ips() if state == "running" else []
                            ),
                            private_ips=[],
                            driver=self,
                            extra={},
                        )
                    )

            print("nodes:", nodes)
            return nodes
        except subprocess.CalledProcessError as e:
            print(f"Failed to list nodes: {e.stderr}")
            return []

    def list_sizes(self) -> List[NodeSize]:
        """List available sizes."""
        return [
            NodeSize(
                id="2vcpu-4gb",
                name="2vcpu-4gb",
                ram=4096,
                disk=10,
                bandwidth=None,
                price=0.0,
                driver=self,
                extra=dict(vcpus=2),
            )
        ]

    def list_images(self) -> List[NodeImage]:
        """List available images."""
        return [
            NodeImage(
                # id="ubuntu/focal64",
                # id="ubuntu/noble64",
                id="ubuntu/jammy64",
                # name="Ubuntu 20.04 LTS",
                name="Ubuntu 24.04 LTS",
                driver=self,
            )
        ]

    def list_locations(self) -> List[NodeLocation]:
        """List available locations."""
        return [
            NodeLocation(
                id="localhost", name="localhost", country="localhost", driver=self
            )
        ]
