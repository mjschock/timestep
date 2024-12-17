import inspect
import os
import subprocess
import time
from typing import List, Optional, Tuple

import paramiko
import typer
from click import Choice
from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeImage,
    NodeLocation,
    NodeSize,
)
from libcloud.compute.providers import DRIVERS
from libcloud.compute.types import Provider
from paramiko import SSHClient
from rich.progress import track

from timestep.config import settings
from timestep.server import main as timestep_serve

CREDENTIALS = {
    # Provider.AZURE: {
    #     'key_file': os.getenv('AZURE_KEY_FILE'),
    #     'subscription_id': os.getenv('AZURE_SUBSCRIPTION_ID'),
    # },
    Provider.DIGITAL_OCEAN: {"key": os.getenv("DIGITAL_OCEAN_API_KEY")},
    # Provider.DUMMY: {
    #     'creds': os.getenv('DUMMY_CREDS')
    # },
    # Provider.EC2: {
    #     'key': os.getenv('AWS_ACCESS_KEY_ID'),
    #     'secret': os.getenv('AWS_SECRET_ACCESS_KEY')
    # },
    # Provider.GCE: {
    #     'project': os.getenv('GCE_PROJECT'),
    #     'user_id': os.getenv('GCE_USER_ID'),
    # },
    Provider.LINODE: {"key": os.getenv("LINODE_API_KEY")},
    # ... add more providers here
}

# https://cloud-images.ubuntu.com/locator/
DEFAULT_ALLOWED_IMAGES_IDS = [
    "ami-0e7c4f6b17a66658a",  # AWS
]

DEFAULT_ALLOWED_IMAGE_NAMES = [
    # " (SupportedImages) - Ubuntu 24.04 LTS x86_64 LATEST - 20240603-prod-ajeby5guflgu4", # AWS
    "24.04 (LTS) x64",  # DigitalOcean
    "Ubuntu 24.04 LTS",  # Linode
]


def initialize_node_drivers() -> List[NodeDriver]:
    provider_node_drivers: List[NodeDriver] = []

    for provider, driver_class in DRIVERS.items():
        if provider in CREDENTIALS:
            try:
                driver_class_package, driver_class_name = driver_class
                driver_module = __import__(
                    driver_class_package, fromlist=[driver_class_name]
                )
                provider_node_driver = getattr(driver_module, driver_class_name)(
                    **CREDENTIALS[provider]
                )
                provider_node_drivers.append(provider_node_driver)

                typer.echo(
                    f"Successfully initialized the provider node driver for {provider}"
                )

            except Exception as e:
                typer.echo(
                    f"Failed to initialize the provider node driver for {provider}: {str(e)}"
                )

    return provider_node_drivers


def has_gpu(size):
    if "gpu" in size.extra:
        return size.extra["gpu"] > 0

    if "gpus" in size.extra:
        return size.extra["gpus"] > 0

    if size.id.startswith(("p2", "p3", "p4", "g3", "g4")):
        return True

    if "accelerator_type" in size.extra and size.extra["accelerator_type"]:
        return True

    return False


def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep AI CLI - free, local-first, open-source AI
""" + (
        """
**Development Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install poetry==1.8.3
$ cp .env.example .env
$ direnv allow # See https://direnv.net/#getting-started
$ make
$ timestep up --dev
```

**Library Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install timestep
$ timestep up
```
"""
        if is_readme_context
        else ""
    )


typer_app = typer.Typer(
    help=get_help_message(),
    no_args_is_help=True,
)


@typer_app.callback()
def main():
    """
    Timestep AI CLI
    """


@typer_app.command()
def up(
    allowed_image_ids: Optional[List[str]] = typer.Option(
        default=DEFAULT_ALLOWED_IMAGES_IDS, help="Allowed image IDs to filter by"
    ),
    allowed_image_names: Optional[List[str]] = typer.Option(
        default=DEFAULT_ALLOWED_IMAGE_NAMES, help="Allowed image names to filter by"
    ),
    clean: bool = typer.Option(default=False, help="Clean up"),
    dev: bool = typer.Option(default=False, help="Development mode"),
    gpu: bool = typer.Option(default=False, help="Require GPU"),
    host: str = typer.Option(default="0.0.0.0", help="Host"),
    min_bandwidth: Optional[int] = typer.Option(
        default=None, help="Minimum bandwidth in GB"
    ),  # TODO: Need to check or convert to proper unit
    min_disk: Optional[int] = typer.Option(
        default=10, help="Minimum disk size in GB"
    ),  # TODO: Need to check or convert to proper unit
    min_ram: Optional[int] = typer.Option(
        # None, help="Minimum RAM in MB"
        default=2000,
        help="Minimum RAM in MB",
    ),  # TODO: Need to check or convert to proper unit
    port: int = typer.Option(default=8000, help="Port"),
    ssh_key: str = typer.Option(
        default="~/.ssh/id_ed25519",
        help="Path to the SSH key",
    ),
):
    """
    Start up the Timestep AI platform.
    """

    if clean:
        typer.echo("\nCleaning up...")

        completed_process: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["./scripts/clean.sh"]
        )

        typer.echo(f"\nCompleted process: {completed_process}")

    node_drivers: List[NodeDriver] = initialize_node_drivers()

    cheapest_nodes_by_provider = {}

    for node_driver in track(
        node_drivers, description="Finding cheapest nodes across all providers"
    ):
        node_images: List[NodeImage] = node_driver.list_images()
        node_locations: List[NodeLocation] = node_driver.list_locations()
        node_sizes: List[NodeSize] = node_driver.list_sizes()

        def node_image_filter(node_image):
            return any(
                image_id == node_image.id for image_id in allowed_image_ids
            ) or any(
                image_name == node_image.name for image_name in allowed_image_names
            )

        node_images = list(filter(node_image_filter, node_images))

        def node_size_filter(node_size):
            return (
                (min_bandwidth is None or node_size.bandwidth >= min_bandwidth)
                and (min_disk is None or node_size.disk >= min_disk)
                and node_size.price > 0
                and (min_ram is None or node_size.ram >= min_ram)
            )

        node_sizes = list(filter(node_size_filter, node_sizes))

        node_sizes_sorted_by_price_asc = sorted(
            node_sizes, key=lambda node_size: node_size.price
        )

        cheapest_nodes_by_provider[node_driver.name] = {
            "images": node_images,
            "locations": node_locations,
            "sizes": node_sizes_sorted_by_price_asc[0:3],
        }

    for provider, cheapest_nodes in cheapest_nodes_by_provider.items():
        typer.echo(f"\n{provider}:")

        for node_size in cheapest_nodes["sizes"]:
            typer.echo(f"  - {node_size}")

    cheapest_node = None

    for provider, cheapest_nodes in cheapest_nodes_by_provider.items():
        for node_size in cheapest_nodes["sizes"]:
            if cheapest_node is None or node_size.price < cheapest_node["size"].price:
                cheapest_node = {
                    "images": cheapest_nodes["images"],
                    "locations": cheapest_nodes["locations"],
                    "provider": provider,
                    "size": node_size,
                }

    provider = cheapest_node["provider"]

    def choice(item):
        return f"\n{item}"

    def value_proc(value):
        return value

    image_id = typer.prompt(
        "\nSelect a node image id",
        default=cheapest_node["images"][0].id,
        prompt_suffix=":",
        show_choices=True,
        type=Choice(sorted([choice(image) for image in cheapest_node["images"]])),
        value_proc=value_proc,
    )

    try:
        image = next(image for image in cheapest_node["images"] if image.id == image_id)

    except StopIteration:
        typer.echo(f"\nFailed to find the node image for {image_id}")

        return

    location_id = typer.prompt(
        "\nSelect a node location id",
        default="sfo3",
        show_choices=True,
        type=Choice(
            sorted([choice(location) for location in cheapest_node["locations"]])
        ),
        value_proc=value_proc,
    )

    try:
        location = next(
            location
            for location in cheapest_node["locations"]
            if location.id == location_id
        )

    except StopIteration:
        typer.echo(f"\nFailed to find the node location for {location_id}")

        return

    size_id = typer.prompt(
        "\nSelect a node size id",
        default=cheapest_node["size"].id,
        show_choices=True,
        type=Choice(sorted([choice(size) for size in [cheapest_node["size"]]])),
        value_proc=value_proc,
    )

    try:
        size = next(size for size in [cheapest_node["size"]] if size.id == size_id)

    except StopIteration:
        typer.echo(f"\nFailed to find the node size for {size_id}")

        return

    typer.echo("\nSelected node configuration:")
    typer.echo(f"Image: {image}")
    typer.echo(f"Location: {location}")
    typer.echo(f"Provider: {provider}")
    typer.echo(f"Size: {size}")

    create = typer.confirm(
        "\nDo you want to create this node?", abort=True, default=True
    )

    name: str = typer.prompt("\nEnter a name for the node", default="libcloud")

    try:
        node_driver = next(
            node_driver for node_driver in node_drivers if node_driver.name == provider
        )

    except StopIteration:
        typer.echo(f"\nFailed to find the node driver for {provider}")

        return

    if create:
        nodes: List[Node] = node_driver.list_nodes()
        node: Node | None

        try:
            node = next(node for node in nodes if node.name == name)

        except StopIteration:
            node = None

        if node:
            delete = typer.confirm(
                "\nNode already exists, do you want to delete it?",
                abort=True,
                default=True,
            )

            if delete:
                destroyed: bool = node_driver.destroy_node(node)
                typer.echo(f"\nNode destroyed: {destroyed}")

        # Path to the public key you would like to install
        KEY_PATH = os.path.expanduser(ssh_key)

        with open(KEY_PATH) as fp:
            # https://docs.libcloud.apache.org/en/stable/compute/key_pair_management.html
            content = (
                fp.read()
            )  # instead, waht about import_key_pair_from_file or import_key_pair_from_string?

        def get_or_create_key_pair(
            node_driver: NodeDriver, name: str, content: str
        ) -> KeyPair:
            # TODO: what about we want to delete the key pair? delete_key_pair

            key_pair: KeyPair | None = node_driver.get_key_pair(name=name)

            if not key_pair:
                key_pair: KeyPair = node_driver.create_key_pair(
                    name=name, public_key=content
                )

            return key_pair

        key_pair: KeyPair = get_or_create_key_pair(node_driver, name, content)

        options = {"ssh_keys": [key_pair.fingerprint]}

        node: Node = node_driver.create_node(
            ex_create_attr=options,
            image=image,
            location=location,
            name=name,
            size=size,
        )

        typer.echo(f"\nNode created: {node}")

        nodes_to_ip_addresses: List[Tuple[Node, List[str]]] = (
            node_driver.wait_until_running([node])
        )

        for node, ip_addresses in nodes_to_ip_addresses:
            typer.echo(f"\nNode {node.name} is running at {ip_addresses}")

        ip = nodes_to_ip_addresses[0][1][0]

    def ssh_connect(
        ip_address: str, script: str = None, username: str = "root"
    ) -> SSHClient:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                client.connect(
                    hostname=ip_address,
                    username=username,
                    key_filename=os.path.expanduser(ssh_key),
                    timeout=10,
                )

                stdin, stdout, stderr = client.exec_command(script)

                print("stdout:")
                print(stdout.read().decode())

                print("stderr:")
                print(stderr.read().decode())

                return client

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(10)

        raise Exception("Failed to connect after multiple attempts")

    SCRIPT = """#!/usr/bin/env bash
    adduser --disabled-password --gecos "" sky
    usermod -aG sudo sky
    echo "sky ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/sky
    mkdir -p /home/sky/.ssh
    cp /root/.ssh/authorized_keys /home/sky/.ssh/authorized_keys
    chown -R sky:sky /home/sky/.ssh
    chmod 700 /home/sky/.ssh
    chmod 600 /home/sky/.ssh/authorized_keys
    usermod -s /bin/bash sky
    usermod -d /home/sky sky
    passwd -d root
    """

    ssh_client = ssh_connect(ip, script=SCRIPT)

    with open("ips.txt", "w") as f:
        f.write(ip)
        f.write("\n")
        f.write("127.0.0.1")

    typer.echo("\nWaiting for 15 seconds...")
    time.sleep(15)

    ips_file = "ips.txt"
    username = "sky"

    completed_process: subprocess.CompletedProcess[bytes] = subprocess.run(
        [
            "./scripts/deploy_remote_cluster.sh",
            ips_file,
            username,
            os.path.expanduser(ssh_key),
        ]
    )

    typer.echo(f"\nCompleted process: {completed_process}")

    try:
        import sky.check

        sky.check.check(
            clouds=["kubernetes"],
            quiet=False,
            verbose=True,
        )

    except ModuleNotFoundError as e:
        typer.echo(f"Failed to import sky.check: {e}")

        subprocess.run(["sky", "check", "k8s"])

    subprocess.run(["sky", "show-gpus", "--cloud", "k8s"])

    SCRIPT = """#!/usr/bin/env bash
    helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow --atomic --create-namespace --namespace mlflow
    """

    ssh_client = ssh_connect(ip, script=SCRIPT, username="sky")

    # typer.echo(f"Starting up the Timestep AI platform at http://{host}:{port}...")

    # timestep_serve(
    #     dev=dev,
    #     host=host,
    #     # llamafile_path=llamafile_path,
    #     port=port,
    # )


if __name__ == "__main__":
    typer_app()
