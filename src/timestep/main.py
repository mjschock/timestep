import asyncio
import inspect
import logging
import os
import subprocess
import time
from typing import List, Optional, Tuple

import typer
from click import Choice
from libcloud.compute.base import Node
from pyhelm3 import Client

from timestep.config import settings
from timestep.infra.cloud.cloud_instance_controller import CloudInstanceController
from timestep.infra.cloud.drivers.multipass import MultipassNodeDriver
from timestep.infra.k3s.k3s_cluster_controller import K3sClusterController
from timestep.infra.sky.sky_workload_controller import SkyWorkloadController
from timestep.utils import run_kompose_convert, ssh_connect

# https://cloud-images.ubuntu.com/locator/
DEFAULT_ALLOWED_IMAGES_IDS = [
    "ami-0e7c4f6b17a66658a",  # AWS
]

DEFAULT_ALLOWED_IMAGE_NAMES = [
    # " (SupportedImages) - Ubuntu 24.04 LTS x86_64 LATEST - 20240603-prod-ajeby5guflgu4", # AWS
    "24.04 LTS",  # Multipass
    "24.04 (LTS) x64",  # DigitalOcean
    "Ubuntu 24.04 LTS",  # Linode
]

app_dir = typer.get_app_dir(__package__)

# if cwd is a git repo, set cwd to cwd else set cwd to app_dir
cwd = os.getcwd()

if not os.path.exists(f"{cwd}/.git"):
    cwd = app_dir

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep CLI - free, local-first, open-source AI
""" + (
        """
## Project Structure

```
src/timestep/
│
├── infra/                  # Infrastructure management
│   ├── cloud/              # Cloud instance management
│   │   └── cloud_instance_controller.py
│   │       - Manages cloud instances using Apache Libcloud
│   │
│   ├── k3s/                # K3s Kubernetes cluster management
│   │   └── k3s_cluster_controller.py
│   │       - Manages K3s Kubernetes clusters
│   │
│   └── sky/                # SkyPilot workload management
│       └── sky_workload_controller.py
│           - Manages computational workloads using SkyPilot
│
|── pipelines/             # Pipelines
|   ├── data_engineering/  # Data engineering pipeline
|   │   └── task.yaml
|   │       - SkyPilot task specification
|   ├── machine_learning/   # Machine learning pipeline
|   │   └── task.yaml
|   │       - SkyPilot task specification
|   ├── model_deployment/   # Model deployment pipeline
|   │   └── task.yaml
|   │       - SkyPilot task specification
|   └── model_monitoring/   # Model monitoring pipeline
|       └── task.yaml
|           - SkyPilot task specification
|
└── services/              # Services
    ├── backend/           # Backend service
    │   └── main.py
    │       - FastAPI backend service
    │
    └── frontend/          # Frontend service
        └── main.py
            - Flet frontend service
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
    "Timestep CLI"


@typer_app.command()
def up(
    accept_defaults: bool = typer.Option(
        default=False, help="Accept defaults and skip prompts"
    ),
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
    # clean: bool = typer.Option(default=False, help="Clean up"),
    down: bool = typer.Option(default=False, help="Down"),
    min_bandwidth: Optional[int] = typer.Option(
        default=None, help="Minimum bandwidth in GB"
    ),  # TODO: Need to check or convert to proper unit
    min_cpu: Optional[int] = typer.Option(default=2, help="Minimum CPU count"),
    min_disk: Optional[int] = typer.Option(
        default=10, help="Minimum disk size in GB"
    ),  # TODO: Need to check or convert to proper unit
    min_ram: Optional[int] = typer.Option(
        # None, help="Minimum RAM in MB"
        default=4000,
        help="Minimum RAM in MB",
    ),  # TODO: Need to check or convert to proper unit
    name: str = typer.Option(default="timestep", help="Name"),
    providers: Optional[List[str]] = typer.Option(
        default=None, help="Providers to filter by"
    ),
    ssh_key: str = typer.Option(
        default="~/.ssh/id_ed25519",
        help="Path to the SSH key",
    ),
):
    """
    Start up the Timestep platform.
    """

    # if clean:
    #     typer.echo("\nCleaning up...")

    #     subprocess.run(args=["./scripts/clean.sh"])

    # os.makedirs("dist", exist_ok=True)
    os.makedirs(f"{cwd}/dist", exist_ok=True)

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
        "docker": {},
        # "dummy": {
        #     'creds': os.getenv('DUMMY_CREDS')
        # },
        # "gcp": {
        #     'project': os.getenv('GCE_PROJECT'),
        #     'user_id': os.getenv('GCE_USER_ID'),
        # },
        # "linode": {"key": os.getenv("LINODE_API_KEY")},
        "multipass": {},
        "vagrant": {},
        # ... add more providers here
    }

    if providers:
        credentials = {provider: credentials[provider] for provider in providers}

    # Initialize the controller
    controller = CloudInstanceController(credentials)

    try:
        # Specify instance requirements
        instance_specs = {
            "min_bandwidth": min_bandwidth,
            "min_cpu": min_cpu,
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

        if accept_defaults:
            size_id = sizes[0].id

        else:
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

        if accept_defaults:
            image_id = images[0].id

        else:
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

        if accept_defaults:
            location_id = locations[0].id

        else:
            location_id = typer.prompt(
                "\nSelect a node location id",
                default=locations[0].id,
                show_choices=True,
                type=Choice(sorted([choice(location) for location in locations])),
                value_proc=value_proc,
            )

        selected_location = [
            location for location in locations if location.id == location_id
        ][0]

        # Confirm selection
        typer.echo("\nSelected Cloud Instance Details:")
        typer.echo(f"\tImage: {selected_image}")
        typer.echo(f"\tLocation: {selected_location}")
        typer.echo(f"\tSize: {selected_size}\n")

        if not accept_defaults and not typer.confirm(
            "\nConfirm these details?", default=True
        ):
            raise typer.Abort()

        controller.prepare_driver(selected_driver)

        instance = controller.get_instance_by_name(
            driver=selected_driver,
            name=name,
        )

        if instance:
            terminate = accept_defaults or typer.confirm(
                f"\nInstance {name} already exists. Do you want to terminate it?",
                default=True,
            )

            if terminate:
                controller.terminate_instance(instance.id)

        # Create a cost-optimized instance
        node = controller.create_instance(
            driver=selected_driver,
            image=selected_image,
            location=selected_location,
            name=name,
            ssh_key=ssh_key,
            size=selected_size,
        )

        nodes_to_ip_addresses: List[Tuple[Node, List[str]]] = (
            selected_driver.wait_until_running([node])
        )

        for node, ip_addresses in nodes_to_ip_addresses:
            typer.echo(f"\nNode {node.name} is running at {ip_addresses}")

        ip = nodes_to_ip_addresses[0][1][0]

        if selected_driver.name in [MultipassNodeDriver.name]:
            print(f"Skipping sky user creation for {selected_driver.name} driver")

        else:
            print(f"Creating sky user for {selected_driver.name} driver")

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

        attach_local_instance_as_k3s_agent_to_remote_cluster = (
            False
            if accept_defaults
            else typer.confirm(
                "Would you like to attach your local machine (127.0.0.1) as a K3s agent to the remote cluster?",
                default=False,
            )
        )

        # ips_file = "dist/ips.txt"
        ips_file = f"{cwd}/dist/ips.txt"

        with open(ips_file, "w") as f:
            f.write(ip)
            f.write("\n")

            if attach_local_instance_as_k3s_agent_to_remote_cluster:
                f.write("127.0.0.1")

    except Exception as e:
        print(f"Error: {e}")
        raise typer.Abort()

    typer.echo("\nWaiting for 15 seconds...")
    time.sleep(15)

    username = "sky"

    k3s_cluster_controller = K3sClusterController(
        cluster_config={
            "ip": ip,
            "ips_file": ips_file,
            "ssh_key": ssh_key,
            "username": username,
        }
    )

    try:
        k3s_cluster_controller.create_cluster(cwd)

    except Exception as e:
        typer.echo(f"Error: {e}")
        raise typer.Abort()

    mlflow_tracking_password = subprocess.run(  # TODO: Do this securely (set it as a secret in the config and pass it to the Helm chart)
        [
            "kubectl",
            "get",
            "secret",
            "--namespace",
            "mlflow",
            "mlflow-tracking",
            "-o",
            "jsonpath={.data.admin-password}",
        ],
        capture_output=True,
        text=True,
    ).stdout

    sky_workload_controller = SkyWorkloadController(
        project_config={
            # "HF_TOKEN": settings.hf_token.get_secret_value(),
            # "MLFLOW_TRACKING_PASSWORD": mlflow_tracking_password,
        }
    )

    should_deploy_ml_platform = not accept_defaults and typer.confirm(
        "Would you like to deploy the Timestep platform?",
        default=False,
    )

    if should_deploy_ml_platform:
        # task_spec = "src/timestep/pipelines/machine_learning/task.yaml"
        task_spec = f"{cwd}/src/timestep/pipelines/machine_learning/task.yaml"

        sky_workload_controller.launch_task(
            task_spec,
            env_overrides={
                "HF_TOKEN": settings.hf_token.get_secret_value(),
                "MLFLOW_TRACKING_PASSWORD": mlflow_tracking_password,
            },
        )

    typer.echo("\nCreating Helm chart...")
    run_kompose_convert(
        cwd=cwd,
        env={
            "PRIMARY_DOMAIN_NAME": settings.primary_domain_name,
        },
        out="timestep-ai",
    )

    typer.echo("\nBuilding Docker images...")
    subprocess.run(
        args=[
            "docker",
            "compose",
            "--file",
            f"{cwd}/docker-compose.yaml",
            "build",
        ]
    )

    typer.echo("\nPushing Docker images...")
    subprocess.run(
        args=[
            "docker",
            "compose",
            "--file",
            f"{cwd}/docker-compose.yaml",
            "push",
        ]
    )

    typer.echo("\nInstalling Helm chart...")
    helm_client = Client()

    # Fetch a chart
    chart = asyncio.get_event_loop().run_until_complete(
        helm_client.get_chart(
            # "./timestep-ai",
            f"{cwd}/timestep-ai",
        )
    )

    # Install or upgrade a release
    asyncio.get_event_loop().run_until_complete(
        helm_client.install_or_upgrade_release(
            atomic=True,
            chart=chart,
            release_name="timestep-ai",
            wait=True,
        )
    )

    typer.echo("\nWaiting for 15 seconds...")
    time.sleep(15)

    subprocess.run(
        args=[
            "kubectl",
            "apply",
            "-f",
            # "dist/metallb-config.yaml",
            f"{cwd}/dist/metallb-config.yaml",
        ]
    )

    # with open("dist/.etchosts", "w") as f:
    with open(f"{cwd}/dist/.etchosts", "w") as f:
        f.write(f"{ip} api.{settings.primary_domain_name}\n")
        f.write(f"{ip} {settings.primary_domain_name}\n")

    # print("cat dist/.etchosts | sudo $(which hostctl) add timestep-ai --wait 0")
    print(f"cat {cwd}/dist/.etchosts | sudo $(which hostctl) add timestep-ai --wait 0")

    if down:
        typer.echo("\nTearing down...")

        # k3s_cluster_controller.delete_cluster()

        controller.terminate_instance(node.id)

        typer.echo(f"\nDeleted cluster and terminated instance: {node}")


if __name__ == "__main__":
    typer_app()
