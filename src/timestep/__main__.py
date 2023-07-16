import os
import pathlib

from cdktf import App
from dotenv import dotenv_values

from timestep.config import (
    AppConfig,
    SecureShellCredentials,
)
from timestep.infra.stacks.main.stack import MainStack

BASE_PATH = pathlib.Path.cwd()
DIST_PATH: str = f"{BASE_PATH}/cdktf.out"


def main(config: AppConfig) -> None:
    app: App = App(
        context={
            "allowSepCharsInLogicalIds": "true",
            "excludeStackIdFromLogicalIds": "true",
        },
        outdir=DIST_PATH,
        skip_validation=False,
        stack_traces=True,
    )

    assert app.node.get_context("allowSepCharsInLogicalIds") == "true"
    assert app.node.get_context("excludeStackIdFromLogicalIds") == "true"

    MainStack(
        config=config,
        scope=app,
        id=config.variables.get("primary_domain_name"),
    )

    app.synth()


if __name__ == "__main__":
    config: dict[str, str] = {
        **dotenv_values(verbose=True),
        **os.environ,  # override loaded values with environment variables
    }

    try:
        ssh_credentials_block = SecureShellCredentials.load("ssh-credentials")

    except ValueError:
        ssh_credentials_block = SecureShellCredentials(
            public_key=config.get("SSH_PUBLIC_KEY", None),
            private_key=config.get("SSH_PRIVATE_KEY", None),
        )

        ssh_credentials_block.save(
            name="ssh-credentials",
            overwrite=False,
        )

    CPUS: int = 1
    DISK_SIZE_GB: int = 25
    MEMORY_SIZE_GB: int = 1
    DO_DROPLET_IMAGE: str = "ubuntu-22-04-x64"
    DO_DROPLET_REGION: str = "sfo3"
    DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-{MEMORY_SIZE_GB}gb"
    MULTIPASS_INSTANCE_CPUS: int = CPUS
    MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
    MULTIPASS_INSTANCE_IMAGE: str = "22.04"
    MULTIPASS_INSTANCE_MEMORY: int = f"{MEMORY_SIZE_GB}G"

    primary_domain_name = config.get("PRIMARY_DOMAIN_NAME")
    kubeconfig = f"{DIST_PATH}/stacks/{primary_domain_name}/kube-config.yaml"
    app_config_block = AppConfig(
        secrets={
            "do_token": config.get("DO_TOKEN", None),
            "namecheap_api_key": config.get("NAMECHEAP_API_KEY", None),
            "namecheap_api_user": config.get("NAMECHEAP_API_USER", None),
            "namecheap_user_name": config.get("NAMECHEAP_USER_NAME", None),
            "postgresql_password": config.get("POSTGRESQL_PASSWORD", None),
            "ssh_private_key": ssh_credentials_block.private_key,
            "tf_api_token": config.get("TF_API_TOKEN", None),
        },
        variables={
            "cdktf_outdir": config.get("CDKTF_OUTPUT", DIST_PATH),
            "cloud_instance_name": config.get("CLOUD_INSTANCE_NAME", None),
            "cloud_instance_provider": config.get("CLOUD_INSTANCE_PROVIDER", None),
            "do_droplet_image": config.get("DO_DROPLET_IMAGE", DO_DROPLET_IMAGE),
            "do_droplet_region": config.get("DO_DROPLET_REGION", DO_DROPLET_REGION),
            "do_droplet_size": config.get("DO_DROPLET_SIZE", DO_DROPLET_SIZE),
            "domain_name_registrar_provider": config.get(
                "DOMAIN_NAME_REGISTRAR_PROVIDER", None
            ),
            "kubeconfig": kubeconfig,
            "kubecontext": config.get("KUBECONTEXT", None),
            "multipass_instance_cpus": config.get(
                "MULTIPASS_INSTANCE_CPUS", MULTIPASS_INSTANCE_CPUS
            ),
            "multipass_instance_disk": config.get(
                "MULTIPASS_INSTANCE_DISK", MULTIPASS_INSTANCE_DISK
            ),
            "multipass_instance_image": config.get(
                "MULTIPASS_INSTANCE_IMAGE", MULTIPASS_INSTANCE_IMAGE
            ),
            "multipass_instance_memory": config.get(
                "MULTIPASS_INSTANCE_MEMORY", MULTIPASS_INSTANCE_MEMORY
            ),
            # "namecheap_client_ip": config.get("NAMECHEAP_CLIENT_IP", None),
            "primary_domain_name": config.get("PRIMARY_DOMAIN_NAME", None),
            "ssh_public_key": ssh_credentials_block.public_key,
            "tf_hostname": config.get("TF_HOSTNAME", None),
            "tf_organization": config.get("TF_ORGANIZATION", None),
            "tf_workspace": config.get("TF_WORKSPACE", None),
        },
    )

    main(config=app_config_block)
