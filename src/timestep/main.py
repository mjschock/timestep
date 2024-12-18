import inspect
import logging
import os
import subprocess
import time
from typing import List, Optional, Tuple

import typer
from click import Choice
from libcloud.compute.base import Node

from timestep.infra.cloud_management.cloud_instance_controller import (
    CloudInstanceController,
)
from timestep.infra.cluster_management.k3s_cluster_controller import (
    K3sClusterController,
)
from timestep.utils import ssh_connect

# https://cloud-images.ubuntu.com/locator/
DEFAULT_ALLOWED_IMAGES_IDS = [
    "ami-0e7c4f6b17a66658a",  # AWS
]

DEFAULT_ALLOWED_IMAGE_NAMES = [
    # " (SupportedImages) - Ubuntu 24.04 LTS x86_64 LATEST - 20240603-prod-ajeby5guflgu4", # AWS
    "24.04 (LTS) x64",  # DigitalOcean
    "Ubuntu 24.04 LTS",  # Linode
]

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep AI CLI - free, local-first, open-source AI
""" + (
        """
## Project Structure

```
src/timestep/
│
├── infra/                  # Infrastructure management
│   ├── cloud_management/   # Cloud instance operations
│   │   └── cloud_instance_controller.py
│   │       - Manages cloud instances using Apache Libcloud
│   │
│   ├── cluster_management/ # Kubernetes cluster management
│   │   └── k3s_cluster_controller.py
│   │       - Manages K3s Kubernetes clusters
│   │
│   └── workload_management/ # Workload orchestration
│       └── sky_workload_controller.py
│           - Manages computational workloads using SkyPilot
│
└── pipelines/              # Data and ML pipeline components
    ├── data_engineering/   # Data preparation stage
    │   └── task.yaml
    │
    ├── machine_learning/   # Model development stage
    │   └── task.yaml
    │
    └── model_deployment/   # Model deployment and monitoring
        └── task.yaml
```

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
    "Timestep AI CLI"


@typer_app.command()
def up(
    allowed_image_ids: Optional[List[str]] = typer.Option(
        default=DEFAULT_ALLOWED_IMAGES_IDS, help="Allowed image IDs to filter by"
    ),
    allowed_image_names: Optional[List[str]] = typer.Option(
        default=DEFAULT_ALLOWED_IMAGE_NAMES, help="Allowed image names to filter by"
    ),
    allowed_location_countries: Optional[List[str]] = typer.Option(
        default=None, help="Allowed location countries to filter by"
    ),
    allowed_location_ids: Optional[List[str]] = typer.Option(
        default=None, help="Allowed location IDs to filter by"
    ),
    allowed_location_names: Optional[List[str]] = typer.Option(
        default=None, help="Allowed location names to filter by"
    ),
    clean: bool = typer.Option(default=False, help="Clean up"),
    dev: bool = typer.Option(default=False, help="Development mode"),
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
    name: str = typer.Option(default="timestep", help="Name"),
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

    # Example credentials (these would be securely stored)
    credentials = {
        # "aws": {
        #     'key': os.getenv('AWS_ACCESS_KEY_ID'),
        #     'secret': os.getenv('AWS_SECRET_ACCESS_KEY')
        # },
        # "azure": {
        #     'key_file': os.getenv('AZURE_KEY_FILE'),
        #     'subscription_id': os.getenv('AZURE_SUBSCRIPTION_ID'),
        # },
        "digital_ocean": {"key": os.getenv("DIGITAL_OCEAN_API_KEY")},
        # "dummy": {
        #     'creds': os.getenv('DUMMY_CREDS')
        # },
        # "gcp": {
        #     'project': os.getenv('GCE_PROJECT'),
        #     'user_id': os.getenv('GCE_USER_ID'),
        # },
        "linode": {"key": os.getenv("LINODE_API_KEY")},
        # ... add more providers here
    }

    # Initialize the controller
    controller = CloudInstanceController(credentials)

    try:
        # Specify instance requirements
        instance_specs = {
            "min_bandwidth": min_bandwidth,
            "min_disk": min_disk,
            "min_ram": min_ram,
        }

        # Find matching sizes
        sizes = controller.find_matching_sizes(instance_specs)

        if not sizes:
            raise typer.BadParameter("No matching instance sizes found")

        def choice(item):
            return f"\n{item}"

        def value_proc(value):
            return value

        size_id = typer.prompt(
            "\nSelect a node size id",
            default=sizes[0].id,
            show_choices=True,
            type=Choice([choice(size) for size in sizes]),
            value_proc=value_proc,
        )

        selected_driver = [size.driver for size in sizes if size.id == size_id][0]
        selected_size = [size for size in sizes if size.id == size_id][0]

        # Find matching images
        images = controller.find_matching_images(
            selected_driver,
            allowed_image_ids,
            allowed_image_names,
        )

        if not images:
            raise typer.BadParameter("No matching images found")

        image_id = typer.prompt(
            "\nSelect a node image id",
            default=images[0].id,
            prompt_suffix=":",
            show_choices=True,
            type=Choice(sorted([choice(image) for image in images])),
            value_proc=value_proc,
        )

        selected_image = [image for image in images if image.id == image_id][0]

        # Find matching locations
        locations = controller.find_matching_locations(
            selected_driver,
            allowed_location_countries,
            allowed_location_ids,
            allowed_location_names,
        )

        if not locations:
            raise typer.BadParameter("No matching locations found")

        location_id = typer.prompt(
            "\nSelect a node location id",
            default="sfo3",
            show_choices=True,
            type=Choice(sorted([choice(location) for location in locations])),
            value_proc=value_proc,
        )

        selected_location = [
            location for location in locations if location.id == location_id
        ][0]

        # Confirm selection
        typer.echo("\nSelected Cloud Instance Details:\n")
        typer.echo(f"Image: {selected_image}")
        typer.echo(f"Location: {selected_location}")
        typer.echo(f"Size: {selected_size}")

        if not typer.confirm("\nConfirm these details?"):
            raise typer.Abort()

        instance = controller.get_instance_by_name(
            driver=selected_driver,
            name=name,
        )

        if instance:
            terminate = typer.confirm(
                f"\nInstance {name} already exists. Do you want to terminate it?"
            )

            if terminate:
                controller.terminate_instance(instance.id)
                typer.echo(f"Terminated instance: {instance}")

        # Create a cost-optimized instance
        node = controller.create_instance(
            driver=selected_driver,
            image=selected_image,
            location=selected_location,
            name=name,
            ssh_key=ssh_key,
            size=selected_size,
        )
        print(f"Created instance: {node}")

        nodes_to_ip_addresses: List[Tuple[Node, List[str]]] = (
            selected_driver.wait_until_running([node])
        )

        for node, ip_addresses in nodes_to_ip_addresses:
            typer.echo(f"\nNode {node.name} is running at {ip_addresses}")

        ip = nodes_to_ip_addresses[0][1][0]

        print(f"ip: {ip}")

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

        ssh_connect(ip, script=SCRIPT, username="root", ssh_key=ssh_key)

        ips_file = "ips.txt"

        with open(ips_file, "w") as f:
            f.write(ip)
            f.write("\n")
            f.write("127.0.0.1")

    except Exception as e:
        print(f"Error: {e}")

    typer.echo("\nWaiting for 15 seconds...")
    time.sleep(15)

    username = "sky"

    controller = K3sClusterController(
        cluster_config={
            "ip": ip,
            "ips_file": ips_file,
            "ssh_key": ssh_key,
            "username": username,
        }
    )

    try:
        controller.create_cluster()

    except Exception as e:
        print(f"Error: {e}")

    # typer.echo(f"Starting up the Timestep AI platform at http://{host}:{port}...")

    # timestep_serve(
    #     dev=dev,
    #     host=host,
    #     # llamafile_path=llamafile_path,
    #     port=port,
    # )


if __name__ == "__main__":
    typer_app()
