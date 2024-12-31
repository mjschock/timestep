import datetime
import json
import os
import subprocess
from typing import List
from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeState,
    NodeImage,
    NodeLocation,
    NodeSize,
)

class MultipassNodeDriver(NodeDriver):
    name: str = "Multipass"
    ssh_public_key: str = None

    def __init__(self, key: str = None, secret: str = None, secure: bool = True, host: str = None, port: int = None, **kwargs):
        super().__init__(key=key, secret=secret, secure=secure, host=host, port=port, **kwargs)

        # self.ssh_public_key = None

    def create_key_pair(self, name: str, public_key: str = None) -> KeyPair:
        print('=== Creating key pair ===')
        print('name:')
        print(name)
        print('public_key:')
        print(public_key)

        # if public_key is None:
        #     public_key_path = os.path.expanduser(f"~/.ssh/{name}.pub")
        #     with open(public_key_path, "r") as public_key_file:
        #         public_key = public_key_file.read()

        self.ssh_public_key = public_key

        return self.get_key_pair(name)

    # def create_node(self, name: str, image: NodeImage, size: NodeSize, location: NodeLocation, ex_create_attr: dict) -> Node:
    def create_node(
        self,
        name,  # type: str
        size,  # type: NodeSize
        image,  # type: NodeImage
        location=None,  # type: Optional[NodeLocation]
        auth=None,  # type: Optional[T_Auth]
        **kwargs  # type: Any
    ) -> Node:
        print('=== Creating node ===')
        print('name:')
        print(name)
        print('size:')
        print(size)
        print('image:')
        print(image)
        print('location:')
        print(location)
        print('auth:')
        print(auth)
        print('kwargs:')
        print(kwargs)

        ex_create_attr = kwargs.get("ex_create_attr", {})
        print('ex_create_attr:')
        print(ex_create_attr)

        ssh_keys = ex_create_attr.get("ssh_keys", [])
        print('ssh_keys:')
        print(ssh_keys)

        cloud_init_stdin = f"""users:
  - default
  - name: sky
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - {ssh_keys[0]}"""

        print('cloud_init_stdin:')
        print(cloud_init_stdin)

        # info = subprocess.run(["multipass", "launch", image.id, "--name", name], capture_output=True)
        # --cloud-init <file> | <url>  Path or URL to a user-data cloud-init
        #                        configuration, or '-' for stdin
        # TODO: Pass cloud-init file to multipass launch via stdin
        info = subprocess.run(
            args=["multipass", "launch", image.id, "--cloud-init", "-", "--name", name],
            capture_output=True,
            # input=b"#!/bin/bash\napt-get update\napt-get install -y nginx\n")
            input=cloud_init_stdin.encode("utf-8"),
        )
        print('info:')
        print(info)
        print('info.stdout.decode("utf-8"):')
        print(info.stdout.decode("utf-8"))

        return Node(
            id=name,
            name=name,
            # state="running",
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
        print('=== Destroying node ===')
        info = subprocess.run(["multipass", "delete", "--purge", node.id], capture_output=True)
        print('info:')
        print(info)
        print('info.stdout.decode("utf-8"):')
        print(info.stdout.decode("utf-8"))

        return True

    def get_key_pair(self, name: str) -> KeyPair:
        print('=== Getting key pair ===')

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
        info = subprocess.run(["multipass", "find", "--format", "json"], capture_output=True)
        info_json = json.loads(info.stdout.decode("utf-8"))
        images = info_json["images"]

        node_images: List[NodeImage] = []

        for image_key, image_val in images.items():
            node_images.append(NodeImage(
                id=image_key,
                name=image_val["release"],
                driver=self
            ))

        return node_images

    def list_locations(self):
        return [NodeLocation(
            id="sfo3",
            name="localhost",
            country="localhost",
            driver=self
        )]

    def list_nodes(self) -> List[Node]:
        info = subprocess.run(["multipass", "list", "--format", "json"], capture_output=True)
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

            node_list.append(Node(
                id=node["name"],
                name=node["name"],
                state=node_state,
                public_ips=node["ipv4"],
                private_ips=[],
                driver=self,
                extra={}
            ))

        return node_list

    def list_sizes(self):
        info = subprocess.run(["multipass", "find", "--format", "json"], capture_output=True)
        info_json = json.loads(info.stdout.decode("utf-8"))
        images = info_json["images"]

        node_sizes: List[NodeSize] = []

        for image_key, image_val in images.items():
            node_sizes.append(NodeSize(
                id=image_key,
                name=image_val["release"],
                ram=2000,
                disk=10,
                bandwidth=None,
                price=0.1,
                driver=self
            ))

        return node_sizes
