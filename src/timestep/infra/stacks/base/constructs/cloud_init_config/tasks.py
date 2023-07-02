import os
from typing import Dict

from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
)
from cloud_init_gen import CloudInitDoc
from constructs import Construct
from prefect import get_run_logger, task
from prefect.futures import PrefectFuture
from prefect_shell import ShellOperation

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.imports.cloudinit.data_cloudinit_config import (
    DataCloudinitConfig,
    DataCloudinitConfigPart,
)
from timestep.infra.imports.cloudinit.provider import CloudinitProvider
from timestep.infra.imports.local.data_local_file import DataLocalFile
from timestep.infra.imports.local.file import File
from timestep.infra.imports.local.provider import LocalProvider
from timestep.infra.imports.null.data_null_data_source import DataNullDataSource
from timestep.infra.imports.null.provider import NullProvider
from timestep.infra.imports.null.resource import Resource


@task
def get_cloud_init_config_provider(
    scope: Construct, config: AppConfig
) -> TerraformProvider:
    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_init_config_provider = LocalProvider(
            id="cloud_init_config_provider",
            scope=scope,
            alias=None,
        )

    else:
        cloud_init_config_provider = CloudinitProvider(
            scope=scope,
            id="cloud_init_config_provider",
            alias=None,
        )

    return cloud_init_config_provider


@task
def get_cloud_init_config_resource(
    scope: Construct, config: AppConfig, cloud_init_config_provider: TerraformProvider
) -> TerraformResource:
    if not config.variables.get(
        "ssh_public_key", None
    ) or not config.secrets.get_secret_value().get("ssh_private_key", None):
        raise Exception("SSH credentials not found")

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
                f'$HOME/.arkade/bin/k3sup install --context {config.variables.get("kubecontext")} --k3s-extra-args "--disable traefik" --local --local-path $HOME/.kube/config --user ubuntu',
            ],
        ],
        users=[
            "default",
            {
                "groups": "sudo",
                "name": "ubuntu",
                "shell": "/bin/bash",
                "ssh_authorized_keys": [
                    config.variables.get("ssh_public_key").strip(),
                ],
                "sudo": "ALL=(ALL) NOPASSWD:ALL",
            },
        ],
    )

    user_data = CloudInitDoc()
    user_data.add(cloud_cfg)

    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_init_config_resource = File(
            id="cloud_init_config_resource",
            content=user_data.render(),
            filename="cloud-config.yaml",
            provider=cloud_init_config_provider,
            scope=scope,
        )

    else:
        cloud_init_config_resource = Resource(
            id="cloud_init_config_resource",
            # provider=cloud_init_config_provider,
            scope=scope,
            triggers={
                "content": user_data.render(),
            },
        )

    return cloud_init_config_resource


@task
def get_cloud_init_config_data_source(
    scope: Construct, config: AppConfig, cloud_init_config_resource: TerraformResource
) -> TerraformDataSource:
    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_init_config_data_source = DataLocalFile(
            id="cloud_init_config_data_source",
            filename=cloud_init_config_resource.filename,
            scope=scope,
            provider=cloud_init_config_resource.provider,
        )

    else:
        data_cloud_init_config_part = DataCloudinitConfigPart(
            content=cloud_init_config_resource.triggers_input["content"],
            content_type="text/cloud-config",
            filename="cloud-config.yaml",
            merge_type=None,
        )

        cloud_init_config_data_source = DataCloudinitConfig(
            scope=scope,
            id="cloud_init_config_data_source",
            base64_encode=False
            if config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
            else True,
            boundary=None,
            gzip=False
            if config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
            else True,
            part=[
                data_cloud_init_config_part,
            ],
            connection=None,
            count=None,
            depends_on=None,
            for_each=None,
            lifecycle=None,
            # provider=cloud_init_config_resource.provider,
            provisioners=None,
        )

    return cloud_init_config_data_source


@task
def get_cloud_init_config_outputs(
    scope: Construct,
    config: AppConfig,
    cloud_init_config_data_source: TerraformDataSource,
) -> Dict[str, TerraformOutput]:
    cloud_init_config_outputs = {}

    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_init_config_outputs["cloudinit_file"] = TerraformOutput(
            scope=scope,
            id="cloud_init_config_outputs_cloudinit_file",
            value=cloud_init_config_data_source.filename,
        )

    else:
        cloud_init_config_outputs["user_data"] = TerraformOutput(
            scope=scope,
            id="cloud_init_config_outputs_user_data",
            value=cloud_init_config_data_source.rendered,
        )

    return cloud_init_config_outputs
