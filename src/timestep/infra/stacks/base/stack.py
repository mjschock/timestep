import os
from prefect import flow, task, get_run_logger
from prefect.futures import PrefectFuture
from prefect.filesystems import LocalFileSystem
from prefect.task_runners import SequentialTaskRunner
from prefect_shell import ShellOperation
from typing import List, Type
import pathlib

from constructs import Construct
from cdktf import (
    TerraformDataSource,
    TerraformElement,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from cloud_init_gen import CloudInitDoc
from pydantic import BaseModel

from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.external.data_external import DataExternal as ExternalTerraformDataSource

from timestep.conf import AppConfig

class CLOUD_INSTANCE_PROVIDERS:
    MULTIPASS = "multipass"
    DIGITALOCEAN = "digitalocean"


@task
def get_ssh_authorized_keys(config: AppConfig) -> List[str]:
    logger = get_run_logger()

    if not os.path.exists(config.SSH_AUTHORIZED_KEYS_PATH):
        logger.info('Generating new SSH keypair and adding to authorized_keys')
        os.makedirs(os.path.dirname(config.SSH_AUTHORIZED_KEYS_PATH), exist_ok=True)

        with ShellOperation(
            commands=[
                f"ssh-keygen -t rsa -C $USER@$HOSTNAME -f {config.DIST_PATH}/.ssh/id_rsa -N ''",
                f"cat {config.DIST_PATH}/.ssh/id_rsa.pub >> {config.SSH_AUTHORIZED_KEYS_PATH}",
            ],
        ) as shell_operation:
            shell_process = shell_operation.trigger()
            shell_process.wait_for_completion()

    with open(config.SSH_AUTHORIZED_KEYS_PATH, "r") as file:
        ssh_authorized_keys = file.read().strip().splitlines()

    return ssh_authorized_keys


# @task(persist_result=True, result_storage_key="cloud-config.yaml")
@task
def get_user_data(config: AppConfig, ssh_authorized_keys: List[str]) -> CloudInitDoc:
    user_data = CloudInitDoc()

    cloud_cfg = dict(
        disable_root=True,
        package_reboot_if_required=True,
        package_update=True,
        package_upgrade=True,
        packages=[
            "build-essential",
            "curl",
            "default-jdk",
            "direnv",
            "figlet",
            "jq",
            "libbz2-dev",
            "libffi-dev",
            "liblzma-dev",
            "libncursesw5-dev",
            "libreadline-dev",
            "libsqlite3-dev",
            "libssl-dev",
            "libxml2-dev",
            "libxmlsec1-dev",
            "net-tools",
            "tk-dev",
            "unzip",
            "xz-utils",
            "zlib1g-dev",
        ],
        runcmd=[
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo "" >> $HOME/.oh-my-bash/custom/example.sh',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo OSH_THEME="zork" >> $HOME/.oh-my-bash/custom/example.sh',
            ],
            ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
            # "runuser -l ubuntu -c 'echo \"eval \\\"\$(direnv hook bash)\\\"\" >> $HOME/.bashrc'",
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo "eval \\"\$(direnv hook bash)\\"" >> $HOME/.bashrc',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "git clone https://github.com/anyenv/anyenv ~/.anyenv",
            ],
            ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "echo export PATH=\$HOME/.anyenv/bin:\$PATH >> $HOME/.bashrc",
            ],
            # "runuser -l ubuntu -c 'echo \"eval \\\"\$(anyenv init -)\\\"\" >> $HOME/.bashrc'",
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo "eval \\"\$(anyenv init -)\\"" >> $HOME/.bashrc',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install --force-init",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install jenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install nodenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install goenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install pyenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "curl -sLS https://get.arkade.dev | sudo sh",
            ],
            ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "echo export PATH=\$HOME/.arkade/bin:\$PATH >> $HOME/.bashrc",
            ],
            ["runuser", "-l", "ubuntu", "-c", "arkade get k3sup"],
            ["runuser", "-l", "ubuntu", "-c", "mkdir $HOME/.kube"],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                '$HOME/.arkade/bin/k3sup install --context timestep-ai-k3s-cluster --k3s-extra-args "--disable traefik" --local --local-path $HOME/.kube/config --user ubuntu',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "arkade install docker-registry",
            ],  # TODO: install Helm chart using Terraform instead?
        ],
        users=[
            "default",
            {
                "groups": "sudo",
                "name": "ubuntu",
                "shell": "/bin/bash",
                "ssh_authorized_keys": ssh_authorized_keys,
                "sudo": "ALL=(ALL) NOPASSWD:ALL",
            },
        ],
        # write_files = [
        #                 {
        #                     "content": f"""\
        # #!/bin/sh
        # [ -r /etc/lsb-release ] && . /etc/lsb-release
        # if [ -z \"$DISTRIB_DESCRIPTION\" ] && [ -x /usr/bin/lsb_release ]; then
        #         # Fall back to using the very slow lsb_release utility
        #         DISTRIB_DESCRIPTION=$(lsb_release -s -d)
        # fi
        # printf \"Welcome to \n%s\nv%s\nrunning on %s (%s %s %s).\n\" \"$(figlet Timestep AI)\" \"$(date +'%Y.%m.%d')\" \"$DISTRIB_DESCRIPTION\" \"$(uname -o)\" \"$(uname -r)\" \"$(uname -m)\"
        #                     """,
        #                     "path": "/etc/update-motd.d/00-header",
        #                     # "permissions": "\"0o755\"",
        #                     # "permissions": "'0755'",
        #                     "permissions": "'0755'",
        #                 },
        #                 {
        #                     "content": """\
        # mirrors:
        #   registry.timestep.local:
        #     endpoint:
        #       - "https://registry.timestep.local:5000"
        # configs:
        #   "registry.timestep.local:5000":
        #     auth:
        #       username: xxxxxx # this is the registry username
        #       password: xxxxxx # this is the registry password
        #     tls:
        #       cert_file: # path to the cert file used in the registry
        #       key_file:  # path to the key file used in the registry
        #       ca_file:   # path to the ca file used in the registry\
        # """,
        #                     "path": "/etc/rancher/k3s/registries.yaml",
        #                     "permissions": "\"0o644\""
        #                 },
        # ],
        # content = f"""\
        # - content: |
        #     mirrors:
        #         registry.localhost:
        #         endpoint:
        #             - "http://registry:5000"
        #     path: /etc/rancher/k3s/registries.yaml
        #     permissions: "0o644"
    )

    user_data.add(
        cloud_cfg
    )

    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        fs = LocalFileSystem(basepath=config.DIST_PATH)
        fs.write_path("cloud-config.yml", user_data.render_binary())
        fs.save("dist-block", overwrite=True)

    return user_data


@task
def get_cloud_instance_provider(scope: TerraformStack, config: AppConfig) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_provider = MultipassTerraformProvider(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.MULTIPASS}_provider",
            id="cloud_instance_provider",
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_provider = DigitaloceanTerraformProvider(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_provider",
            id="cloud_instance_provider",
            scope=scope,
            token=config.DO_TOKEN,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_provider


@task
def get_cloud_instance_resource(scope: TerraformStack, config: AppConfig, user_data: CloudInitDoc, cloud_instance_provider: TerraformProvider) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_resource = MultipassInstanceTerraformResource(
            cloudinit_file=f"{config.DIST_PATH}/cloud-config.yml",
            cpus=config.MULTIPASS_INSTANCE_CPUS,
            disk=config.MULTIPASS_INSTANCE_DISK,
            # id=f"{CLOUD_INSTANCE_PROVIDERS.MULTIPASS}_instance_resource",
            id="cloud_instance_resource",
            image=config.MULTIPASS_INSTANCE_IMAGE,
            name=config.CLOUD_INSTANCE_NAME,
            provider=cloud_instance_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_resource = DigitaloceanDropletTerraformResource(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_droplet_resource",
            id="cloud_instance_resource",
            image=config.DO_DROPLET_IMAGE,
            name=config.CLOUD_INSTANCE_NAME,
            provider=cloud_instance_provider,
            region=config.DO_DROPLET_REGION,
            scope=scope,
            size=config.DO_DROPLET_SIZE,
            user_data=user_data,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_resource


@task
def get_cloud_domain_resource(scope: TerraformStack, config: AppConfig, cloud_instance_provider: TerraformProvider, cloud_instance_resource: TerraformResource) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        # TODO: use hostctl to add domain to /etc/hosts for ipv4 address
        # cloud_domain_resource = ExternalTerraformDataSource(
        #     id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_domain_resource",
        #     # ip_address=cloud_instance_resource.ipv4,
        #     # name=config.DOMAIN,
        #     program=["hostctl", "add", config.DOMAIN, cloud_instance_resource.ipv4],
        #     # provider=cloud_instance_provider,
        #     scope=self.scope,
        # )
        cloud_domain_resource = None

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_domain_resource = DigitaloceanDomainTerraformResource(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_domain_resource",
            id="cloud_domain_resource",
            ip_address=cloud_instance_resource.ipv4_address,
            name=config.DOMAIN,
            provider=cloud_instance_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_domain_resource


@task
def get_cloud_instance_data_source(scope: TerraformStack, config: AppConfig, cloud_instance_provider: TerraformProvider, cloud_instance_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_data_source = MultipassInstanceTerraformDataSource(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.MULTIPASS}_instance_data_source",
            id="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_data_source = DigitaloceanDropletTerraformDataSource(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_instance_data_source",
            id="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_data_source


@task
def get_cloud_domain_data_source(scope: TerraformStack, config: AppConfig, cloud_instance_provider: TerraformProvider, cloud_domain_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        # TODO: use hostctl to add domain to /etc/hosts for ipv4 address
        # cloud_domain_data_source = ExternalTerraformDataSource(
        #     id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_domain_resource",
        #     # ip_address=cloud_instance_resource.ipv4,
        #     # name=config.DOMAIN,
        #     program=["hostctl", "add", config.DOMAIN, cloud_instance_resource.ipv4],
        #     # provider=cloud_instance_provider,
        #     scope=self.scope,
        # )
        cloud_domain_data_source = None

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_domain_data_source = DigitaloceanDomainTerraformDataSource(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_domain_data_source",
            id="cloud_domain_data_source",
            name=cloud_domain_resource.name,
            provider=cloud_instance_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_domain_data_source


@task
def get_cloud_instance_ipv4_output(scope: TerraformStack, config: AppConfig, cloud_instance_data_source: TerraformDataSource) -> TerraformOutput:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_ipv4_output = TerraformOutput(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.MULTIPASS}_instance_ipv4_output",
            id="cloud_instance_ipv4_output",
            value=cloud_instance_data_source.ipv4,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_ipv4_output = TerraformOutput(
            # id=f"{CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN}_droplet_ipv4_output",
            id="cloud_instance_ipv4_output",
            value=cloud_instance_data_source.ipv4_address,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_ipv4_output


@task
def get_cloud_instance_zone_file_output(scope: TerraformStack, config: AppConfig, cloud_domain_data_source: TerraformDataSource) -> TerraformOutput:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_zone_file_output = None

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_zone_file_output = TerraformOutput(
            # id="digitalocean_domain_zone_file_output",
            id="cloud_instance_zone_file_output",
            value=cloud_domain_data_source.zone_file,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_zone_file_output


class BaseTerraformStack(TerraformStack):
    def __init__(
        self, scope: Construct, id: str, config: AppConfig
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        ssh_authorized_keys_future: PrefectFuture = get_ssh_authorized_keys.submit(config=config)
        user_data_future: PrefectFuture = get_user_data.submit(config=config, ssh_authorized_keys=ssh_authorized_keys_future) # app_config -> cloud_config
        cloud_instance_provider_future: PrefectFuture = get_cloud_instance_provider.submit(scope=self, config=config)
        cloud_instance_resource_future: PrefectFuture = get_cloud_instance_resource.submit(scope=self, config=config, user_data=user_data_future, cloud_instance_provider=cloud_instance_provider_future)
        cloud_domain_resource_future: PrefectFuture = get_cloud_domain_resource.submit(scope=self, config=config, cloud_instance_provider=cloud_instance_provider_future, cloud_instance_resource=cloud_instance_resource_future)
        cloud_instance_data_source_future: PrefectFuture = get_cloud_instance_data_source.submit(scope=self, config=config, cloud_instance_provider=cloud_instance_provider_future, cloud_instance_resource=cloud_instance_resource_future)
        cloud_domain_data_source_future: PrefectFuture = get_cloud_domain_data_source.submit(scope=self, config=config, cloud_instance_provider=cloud_instance_provider_future, cloud_domain_resource=cloud_domain_resource_future)
        cloud_instance_ipv4_output_future: PrefectFuture = get_cloud_instance_ipv4_output.submit(scope=self, config=config, cloud_instance_data_source=cloud_instance_data_source_future)
        cloud_instance_zone_file_output_future: PrefectFuture = get_cloud_instance_zone_file_output.submit(scope=self, config=config, cloud_domain_data_source=cloud_domain_data_source_future)

        outputs = {
            "cloud_instance_ipv4": cloud_instance_ipv4_output_future.result(),
            "cloud_instance_zone_file": cloud_instance_zone_file_output_future.result(),
        }

        logger.info(f"outputs: {outputs}")
