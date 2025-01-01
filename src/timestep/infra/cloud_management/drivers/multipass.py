import datetime
import json
import subprocess
from typing import List

from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeImage,
    NodeLocation,
    NodeSize,
    NodeState,
)


class MultipassNodeDriver(NodeDriver):
    name: str = "Multipass"
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

    def create_key_pair(self, name: str, public_key: str = None) -> KeyPair:
        self.ssh_public_key = public_key

        return self.get_key_pair(name)

    def create_node(
        self, name, size, image, location=None, auth=None, **kwargs
    ) -> Node:
        ex_create_attr = kwargs.get("ex_create_attr", {})
        ssh_keys = ex_create_attr.get("ssh_keys", [])

        cloud_init_stdin = f"""users:
  - default
  - name: sky
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - {ssh_keys[0]}"""

        info = subprocess.run(
            args=[
                "multipass",
                "launch",
                image.id,
                "--cloud-init",
                "-",
                "--cpus",
                "2",
                "--disk",
                "10G",
                "--memory",
                "4G",
                "--name",
                name,
            ],
            capture_output=True,
            input=cloud_init_stdin.encode("utf-8"),
        )

        return Node(
            id=name,
            name=name,
            state=NodeState.RUNNING,
            public_ips=[],
            private_ips=[],
            driver=self,
            size=size,
            image=image,
            extra={},
            created_at=datetime.datetime.now(),
        )

    def destroy_node(self, node: Node):
        print("=== Destroying node ===")
        info = subprocess.run(
            ["multipass", "delete", "--purge", node.id], capture_output=True
        )
        print("info:")
        print(info)
        print('info.stdout.decode("utf-8"):')
        print(info.stdout.decode("utf-8"))

        return True

    def get_key_pair(self, name: str) -> KeyPair:
        if self.ssh_public_key is not None:
            return KeyPair(
                name=name,
                public_key=self.ssh_public_key,
                fingerprint=self.ssh_public_key,
                driver=self,
                private_key="",
            )

        return None

    def list_images(self):
        info = subprocess.run(
            ["multipass", "find", "--format", "json"], capture_output=True
        )
        info_json = json.loads(info.stdout.decode("utf-8"))
        images = info_json["images"]

        node_images: List[NodeImage] = []

        for image_key, image_val in images.items():
            node_images.append(
                NodeImage(id=image_key, name=image_val["release"], driver=self)
            )

        return node_images

    def list_locations(self):
        return [
            NodeLocation(id="sfo3", name="localhost", country="localhost", driver=self)
        ]

    def list_nodes(self) -> List[Node]:
        info = subprocess.run(
            ["multipass", "list", "--format", "json"], capture_output=True
        )
        info_json = json.loads(info.stdout.decode("utf-8"))
        nodes = info_json["list"]

        node_list: List[Node] = []

        for node in nodes:
            if node["state"] == "Running":
                print(node["state"])
                node_state = NodeState.RUNNING
            else:
                print(node["state"])
                node_state = NodeState.UNKNOWN

            node_list.append(
                Node(
                    id=node["name"],
                    name=node["name"],
                    state=node_state,
                    public_ips=node["ipv4"],
                    private_ips=[],
                    driver=self,
                    extra={},
                )
            )

        return node_list

    def list_sizes(self):
        info = subprocess.run(
            ["multipass", "find", "--format", "json"], capture_output=True
        )
        info_json = json.loads(info.stdout.decode("utf-8"))
        images = info_json["images"]

        node_sizes: List[NodeSize] = []

        for image_key, image_val in images.items():
            node_sizes.append(
                NodeSize(
                    id=image_key,
                    name=image_val["release"],
                    ram=2000,
                    disk=10,
                    bandwidth=None,
                    price=0.1,
                    driver=self,
                )
            )

        return node_sizes
