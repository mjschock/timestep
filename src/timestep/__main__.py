import logging
import os
import pathlib
import sys

from cdktf import (
    App,
    IRemoteWorkspace,
    LocalBackend,
    NamedRemoteWorkspace,
    RemoteBackend,
    TerraformOutput,
    TerraformStack,
)
from constructs import Construct
from dotenv import dotenv_values, load_dotenv
from prefect import flow, get_run_logger
from prefect_shell import ShellOperation

from timestep.conf.blocks import (
    AppConfig,
    CloudInitConfig,
    CloudInstanceConfig,
    CloudInstanceProvider,
    SecureShellCredentials,
)
from timestep.infra.stacks.base.stack import BaseStack

BASE_PATH = pathlib.Path.cwd()
DIST_PATH: str = f"{BASE_PATH}/dist"


@flow()
def main(config: AppConfig) -> None:
    logger = get_run_logger()
    # logger.info(f"config: {config}")
    # logger.warning(f"config: {config}")

    # if not os.path.exists(f"{DIST_PATH}/.ssh"):
    #     os.makedirs(f"{DIST_PATH}/.ssh")

    # shell_output = ShellOperation(
    #     commands=[
    #         f"ssh-keygen -t ed25519 -f {DIST_PATH}/.ssh/id_ed25519 -N ''",
    #     ],
    # ).run()

    # ssh_credentials_block = SecureShellCredentials(
    #     # public_key=config.get("SSH_PUBLIC_KEY", None),
    #     # private_key=config.get("SSH_PRIVATE_KEY", None),
    # )

    # ssh_credentials.run()

    # ssh_credentials_block.save(
    #     name="ssh-credentials",
    #     overwrite=True,
    # )

    # ssh_credentials_block = SecureShellCredentials.load("ssh-credentials")

    # ssh_credentials_block()

    # ssh_credentials.generate_ssh_keypair()

    app: App = App()

    stack: TerraformStack = BaseStack(
        app, config.variables.get("primary_domain_name"), config=config
    )

    # if (
    #     config.variables.get("cloud_instance_provider")
    #     == CloudInstanceProvider.MULTIPASS
    # ):
    backend: LocalBackend = LocalBackend(
        scope=stack,
        path=f'terraform.{config.variables.get("primary_domain_name")}.tfstate',
        workspace_dir=None,
    )

    # else:
    # workspaces: IRemoteWorkspace = NamedRemoteWorkspace(
    #     # name=config.TERRAFORM_WORKSPACE,
    #     name=config.variables.get("tf_workspace"),
    # )
    # backend: RemoteBackend = RemoteBackend(
    #     scope=stack,
    #     # hostname=config.TERRAFORM_HOSTNAME,
    #     hostname=config.variables.get("tf_hostname"),
    #     # organization=config.TERRAFORM_ORGANIZATION,
    #     organization=config.variables.get("tf_organization"),
    #     # token=config.TF_API_TOKEN,
    #     token=config.secrets.get_secret_value().get("tf_api_token"),
    #     workspaces=workspaces,
    # )

    app.synth()


if __name__ == "__main__":
    config: dict[str, str] = {
        **dotenv_values(verbose=True),
        **os.environ,  # override loaded values with environment variables
    }

    try:
        ssh_credentials_block = SecureShellCredentials.load("ssh-credentials")

    except ValueError as e:
        ssh_credentials_block = SecureShellCredentials(
            public_key=config.get("SSH_PUBLIC_KEY", None),
            private_key=config.get("SSH_PRIVATE_KEY", None),
        )

        ssh_credentials_block.save(
            name="ssh-credentials",
            overwrite=False,
        )

    # cloud_init_config_block = CloudInitConfig(
    #     ssh_credentials=SecureShellCredentials.load("ssh-credentials"),
    # )

    # cloud_init_config_block.save(
    #     name="cloud-init-config",
    #     overwrite=True,
    # )

    # cloud_instance_config_block = CloudInstanceConfig(
    #     **config,
    #     cloud_init_config=CloudInitConfig.load("cloud-init-config"),
    # )

    # cloud_instance_config_block.save(
    #     name="cloud-instance-config",
    #     overwrite=True,
    # )

    # main_config_block = MainConfig(
    #     **config,
    #     cloud_instance_config=CloudInstanceConfig.load("cloud-instance-config"),
    # )

    # main_config_block.save(
    #     name="main-config",
    #     overwrite=True,
    # )

    # main_config_block = MainConfig.load("main-config")

    CPUS: int = 1
    DISK_SIZE_GB: int = 10

    # BASE_PATH: str = f"{BASE_PATH}"
    # CLOUD_CONFIG_PATH: str = "dist/cloud-config.yaml"
    # CLOUD_INSTANCE_PROVIDER: str = CLOUD_INSTANCE_PROVIDERS.MULTIPASS
    # CLOUD_INSTANCE_NAME: str = "timestep-ai"
    DO_DROPLET_IMAGE: str = "ubuntu-22-04-x64"
    DO_DROPLET_REGION: str = "sfo3"
    DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-512mb-{DISK_SIZE_GB}gb"
    # DO_TOKEN: str = None
    # DOMAIN: str = None
    # HOSTS_FILE_PATH: str = None
    # KUBECONFIG: str = "dist/kube-config.yml"
    # KUBECONTEXT: str = "default"
    MULTIPASS_INSTANCE_CPUS: int = CPUS
    MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
    MULTIPASS_INSTANCE_IMAGE: str = "22.04"
    # NAMECHEAP_API_KEY: str = None
    # NAMECHEAP_API_USER: str = None
    # NAMECHEAP_USER_NAME: str = None
    # SSH_PUBLIC_KEY: str = None
    # SSH_PRIVATE_KEY: str = None
    # SSH_PUBLIC_KEY_PATH: str = "dist/.ssh/id_rsa.pub"
    # SSH_PRIVATE_KEY_PATH: str = "dist/.ssh/id_rsa"
    # TF_API_TOKEN: str = None
    # TERRAFORM_HOSTNAME: str = "app.terraform.io"
    # TERRAFORM_ORGANIZATION: str = "timestep-ai"
    # TERRAFORM_WORKSPACE: str = "timestep-ai"

    app_config_block = AppConfig(
        secrets={
            "do_token": config.get("DO_TOKEN", None),
            "ssh_private_key": ssh_credentials_block.private_key,
            "tf_api_token": config.get("TF_API_TOKEN", None),
        },
        variables={
            "cloud_instance_name": config.get("CLOUD_INSTANCE_NAME", None),
            "cloud_instance_provider": config.get("CLOUD_INSTANCE_PROVIDER", None),
            "do_droplet_image": config.get("DO_DROPLET_IMAGE", DO_DROPLET_IMAGE),
            "do_droplet_region": config.get("DO_DROPLET_REGION", DO_DROPLET_REGION),
            "do_droplet_size": config.get("DO_DROPLET_SIZE", DO_DROPLET_SIZE),
            "domain_name_registrar_provider": config.get(
                "DOMAIN_NAME_REGISTRAR_PROVIDER", None
            ),
            "multipass_instance_cpus": config.get(
                "MULTIPASS_INSTANCE_CPUS", MULTIPASS_INSTANCE_CPUS
            ),
            "multipass_instance_disk": config.get(
                "MULTIPASS_INSTANCE_DISK", MULTIPASS_INSTANCE_DISK
            ),
            "multipass_instance_image": config.get(
                "MULTIPASS_INSTANCE_IMAGE", MULTIPASS_INSTANCE_IMAGE
            ),
            "kubecontext": config.get("KUBECONTEXT", None),
            "primary_domain_name": config.get("PRIMARY_DOMAIN_NAME", None),
            "ssh_public_key": ssh_credentials_block.public_key,
            "tf_hostname": config.get("TF_HOSTNAME", None),
            "tf_organization": config.get("TF_ORGANIZATION", None),
            "tf_workspace": config.get("TF_WORKSPACE", None),
        },
    )

    main(config=app_config_block)
