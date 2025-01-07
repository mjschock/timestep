import datetime
from pathlib import Path
from typing import List

import docker
from docker.models.containers import Container
from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeImage,
    NodeLocation,
    NodeSize,
    NodeState,
)


class DockerNodeDriver(NodeDriver):
    name: str = "Docker"
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

        def cleanup_existing_container(client, container_name):
            """Remove existing container with the same name if it exists"""
            try:
                container = client.containers.get(container_name)
                print(f"Found existing container '{container_name}'. Removing...")
                container.stop()
                container.remove()
                print(f"Removed container '{container_name}'")
            except docker.errors.NotFound:
                pass

        client = docker.from_env(use_ssh_client=True)

        cleanup_existing_container(client, name)

        public_key = ssh_keys[0]

        # Create a temporary Dockerfile to set up SSH with the public key
        dockerfile_content = """
        FROM ubuntu:24.04

        # Install systemd and SSH server
        RUN apt-get update && \
            apt-get install -y curl openssh-server sudo systemd systemd-sysv && \
            apt-get clean && \
            rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

        # Configure SSH
        RUN mkdir -p /var/run/sshd
        RUN mkdir -p /root/.ssh
        RUN chmod 700 /root/.ssh
        COPY authorized_keys /root/.ssh/
        RUN chmod 600 /root/.ssh/authorized_keys

        # Allow root login with SSH key
        RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
        echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config && \
        echo "PasswordAuthentication no" >> /etc/ssh/sshd_config

         # Start SSH service
        RUN service ssh start

        # Configure systemd
        RUN cd /lib/systemd/system/sysinit.target.wants/ && \
            rm $(ls | grep -v systemd-tmpfiles-setup)
        RUN rm -f /lib/systemd/system/multi-user.target.wants/* \
            /etc/systemd/system/*.wants/* \
            /lib/systemd/system/local-fs.target.wants/* \
            /lib/systemd/system/sockets.target.wants/*udev* \
            /lib/systemd/system/sockets.target.wants/*initctl* \
            /lib/systemd/system/basic.target.wants/* \
            /lib/systemd/system/anaconda.target.wants/*

        VOLUME [ "/sys/fs/cgroup" ]
        EXPOSE 22

        # Enable and start SSH service
        RUN systemctl enable ssh
        
        ENTRYPOINT ["/lib/systemd/systemd"]

        CMD ["--system"]
        """

        # Create a temporary build context
        build_dir = Path("/tmp/docker_ssh_build")
        build_dir.mkdir(exist_ok=True)

        # Write Dockerfile and authorized_keys
        (build_dir / "Dockerfile").write_text(dockerfile_content)
        (build_dir / "authorized_keys").write_text(public_key)

        # Build the image
        image, _ = client.images.build(
            path=str(build_dir),
            tag="systemd-ssh-enabled-container",
            rm=True,  # Remove intermediate containers
        )

        # Clean up build context
        for file in build_dir.iterdir():
            file.unlink()

        build_dir.rmdir()

        print("before container run")
        print("containers:", client.containers.list())

        # Create and run the container
        container = client.containers.run(
            command="tail -f /dev/null",
            image=image.id,
            name=name,
            detach=True,
            ports={"22/tcp": 2222},  # map container port 22 to host port 2222
            cgroupns="host",  # required for systemd
            privileged=True,  # required for systemd
            volumes={
                "/sys/fs/cgroup": {"bind": "/sys/fs/cgroup", "mode": "rw"},
            },
            tmpfs={
                "/run": "",
                "/run/lock": "",
            },
        )

        # Wait a moment for services to start
        import time

        print("Waiting for container to start...")
        time.sleep(3)

        # Start SSH service
        print("Starting SSH service...")
        container.exec_run("service ssh start")

        # docker exec -it timestep rm -f /var/run/nologin
        print("Removing /var/run/nologin...")
        container.exec_run("rm -f /var/run/nologin")

        print(f"Container created with ID: {container.id}")
        print("You can now SSH into the container using:")
        print(f"ssh -p 2222 root@localhost")

        if container.status == "running":
            node_state = NodeState.RUNNING
        else:
            node_state = NodeState.UNKNOWN

        node = Node(
            id=container.id,
            name=container.name,
            state=node_state,
            public_ips=[container.attrs["NetworkSettings"]["IPAddress"]],
            private_ips=[],
            driver=self,
            size=size,
            image=image,
            extra={},
            created_at=datetime.datetime.now(),
        )

        print("node:", node)

        return node

    def destroy_node(self, node: Node):
        # subprocess.run(["docker", "delete", "--purge", node.id], capture_output=True)
        client = docker.from_env()

        container = client.containers.get(node.id)
        container.stop()
        container.remove()

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
        print("list_images")

        # info = subprocess.run(
        #     ["docker", "find", "--format", "json"], capture_output=True
        # )
        # info_json = json.loads(info.stdout.decode("utf-8"))
        # images = info_json["images"]

        # node_images: List[NodeImage] = []

        # for image_key, image_val in images.items():
        #     node_images.append(
        #         NodeImage(id=image_key, name=image_val["release"], driver=self)
        #     )

        node_images = [NodeImage(id="ubuntu:24.04", name="24.04 LTS", driver=self)]

        return node_images

    def list_locations(self):
        return [
            # NodeLocation(id="sfo3", name="localhost", country="localhost", driver=self)
            NodeLocation(
                id="localhost", name="localhost", country="localhost", driver=self
            )
        ]

    def list_nodes(self) -> List[Node]:
        # info = subprocess.run(
        #     ["docker", "list", "--format", "json"], capture_output=True
        # )
        # info_json = json.loads(info.stdout.decode("utf-8"))
        # nodes = info_json["list"]

        print("list_nodes")

        client = docker.from_env()

        containers: List[Container] = client.containers.list()
        print("containers:", containers)

        # for container in containers:
        #     print('container:', container)
        #     print('container.id:', container.id)
        #     print('container.name:', container.name)
        #     # print('container.status:', container.status)
        #     # print('container.attrs:', container.attrs)
        #     pprint(container.attrs)
        #     print('container.attrs["NetworkSettings"]:')
        #     pprint(container.attrs["NetworkSettings"])

        # raise NotImplementedError

        node_list: List[Node] = []

        # for node in nodes:
        for node in containers:
            # if node["state"] == "running":
            if node.status == "running":
                node_state = NodeState.RUNNING
            else:
                node_state = NodeState.UNKNOWN

            node_list.append(
                Node(
                    # id=node["name"],
                    id=node.id,
                    # name=node["name"],
                    name=node.name,
                    state=node_state,
                    # public_ips=node["ipv4"],
                    public_ips=[node.attrs["NetworkSettings"]["IPAddress"]],
                    private_ips=[],
                    driver=self,
                    extra={},
                )
            )

        print("node_list:", node_list)

        return node_list

    def list_sizes(self):
        print("list_sizes")

        # info = subprocess.run(
        #     ["docker", "find", "--format", "json"], capture_output=True
        # )
        # info_json = json.loads(info.stdout.decode("utf-8"))
        # images = info_json["images"]

        node_sizes: List[NodeSize] = []

        # for image_key, image_val in images.items():
        node_sizes.append(
            NodeSize(
                # id=image_key,
                id="2vcpu-4gb",
                # name=image_val["release"],
                name="2vcpu-4gb",
                ram=4096,  # TODO: Get default values from the config
                disk=10,  # TODO: Get default values from the config
                bandwidth=None,  # TODO: Get default values from the config
                # price=0.1,
                price=0.0,
                driver=self,
                extra=dict(
                    # vcpus=2,  # TODO: Get default values from the config
                    vcpus=4,
                ),
            )
        )

        return node_sizes
