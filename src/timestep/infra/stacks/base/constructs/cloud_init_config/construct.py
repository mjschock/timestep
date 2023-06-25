from typing import Dict
from prefect.futures import PrefectFuture
from cloud_init_gen import CloudInitDoc
from prefect_shell import ShellOperation

import os
from cdktf import TerraformDataSource, TerraformOutput, TerraformProvider, TerraformResource
from constructs import Construct
from prefect import get_run_logger, task

from timestep.conf import MainConfig
from timestep.infra.imports.cloudinit.provider import CloudinitProvider
from timestep.infra.imports.cloudinit.data_cloudinit_config import DataCloudinitConfigPart, DataCloudinitConfig

from timestep.infra.imports.local.data_local_file import DataLocalFile
from timestep.infra.imports.local.file import File
from timestep.infra.imports.local.provider import LocalProvider

from timestep.infra.imports.null.resource import Resource

from timestep.infra.imports.null.data_null_data_source import DataNullDataSource


@task
def get_cloud_init_config_provider(scope: Construct, config: MainConfig) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_init_config_provider = LocalProvider(
            id="cloud_init_config_provider",
            scope=scope,
            alias=None,
        )

    else:
        # cloud_init_config_provider = CloudinitProvider(
        #     scope=scope,
        #     id="cloud_init_config_provider",
        #     alias=None,
        # )

        cloud_init_config_provider = LocalProvider(
            id="cloud_init_config_provider",
            scope=scope,
            alias=None,
        )

    return cloud_init_config_provider


@task
def get_cloud_init_config_resource(scope: Construct, config: MainConfig, cloud_init_config_provider: TerraformProvider) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS and not config.SSH_PUBLIC_KEY: # TODO: Make this reversible
        if not os.path.exists(config.SSH_PUBLIC_KEY_PATH):
            os.makedirs(os.path.dirname(config.SSH_PUBLIC_KEY_PATH), exist_ok=True)

            with ShellOperation(
                commands=[
                    f"ssh-keygen -t rsa -C $USER@$HOSTNAME -f {config.SSH_PRIVATE_KEY_PATH} -N ''",
                ],
            ) as shell_operation:
                shell_process = shell_operation.trigger()
                shell_process.wait_for_completion()

        with open(config.SSH_PUBLIC_KEY_PATH, "r") as file:
            config.SSH_PUBLIC_KEY = file.read().strip()

    if not config.SSH_PUBLIC_KEY:
        raise Exception("No SSH_PUBLIC_KEY provided")

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
                f'$HOME/.arkade/bin/k3sup install --context {config.KUBECONTEXT} --k3s-extra-args "--disable traefik" --local --local-path $HOME/.kube/config --user ubuntu',
            ],
        ],
        users=[
            "default",
            {
                "groups": "sudo",
                "name": "ubuntu",
                "shell": "/bin/bash",
                "ssh_authorized_keys": [
                    config.SSH_PUBLIC_KEY,
                ],
                "sudo": "ALL=(ALL) NOPASSWD:ALL",
            },
        ],
    )

    user_data = CloudInitDoc()
    user_data.add(
        cloud_cfg
    )

    if config.CLOUD_INSTANCE_PROVIDER == config.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_init_config_resource = File(
            id="cloud_init_config_resource",
            content=user_data.render(),
            filename=config.CLOUD_CONFIG_PATH,
            provider=cloud_init_config_provider,
            scope=scope,
        )

    else:
        # cloud_init_config_resource = Resource( # TODO: Fix this
        #     id="cloud_init_config_resource",
        #     triggers={
        #         "content": user_data.render(),
        #     },
        #     provider=cloud_init_config_provider,
        #     scope=scope,
        # )

        cloud_init_config_resource = File(
            id="cloud_init_config_resource",
            content=user_data.render(),
            filename=config.CLOUD_CONFIG_PATH,
            provider=cloud_init_config_provider,
            scope=scope,
        )

    return cloud_init_config_resource


@task
def get_cloud_init_config_data_source(scope: Construct, config: MainConfig, cloud_init_config_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == config.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_init_config_data_source = DataLocalFile(
            id="cloud_init_config_data_source",
            filename=cloud_init_config_resource.filename,
            scope=scope,
            provider=cloud_init_config_resource.provider,
        )

    else:
        # data_cloud_init_config_part = DataCloudinitConfigPart(
        #     # content=cloud_init_config.render(),
        #     # content=cloud_init_config_resource.triggers["content"],
        #     # content=cloud_init_config_resource.triggers()["content"], # TODO: Fix this
        #     content=cloud_init_config_resource.content,
        #     content_type="text/cloud-config",
        #     filename="cloud-config.yaml",
        #     merge_type=None,
        # )

        # cloud_init_config_data_source = DataCloudinitConfig(
        #     scope=scope,
        #     id="cloud_init_config_data_source",
        #     base64_encode=None,
        #     boundary=None,
        #     gzip=None,
        #     part=[
        #         data_cloud_init_config_part,
        #     ],
        #     connection=None,
        #     count=None,
        #     depends_on=None,
        #     for_each=None,
        #     lifecycle=None,
        #     provider=cloud_init_config_resource.provider,
        #     provisioners=None,
        # )

        # cloud_init_config_data_source = DataLocalFile(
        #     id="cloud_init_config_data_source",
        #     filename=cloud_init_config_resource.filename,
        #     scope=scope,
        #     provider=cloud_init_config_resource.provider,
        # )

        cloud_init_config_data_source = DataNullDataSource(
            id="cloud_init_config_data_source",
            provider=cloud_init_config_resource.provider,
            inputs={
                "user_data": cloud_init_config_resource.content,
            },
            scope=scope,
        )

    return cloud_init_config_data_source


@task
def get_cloud_init_config_outputs(scope: Construct, config: MainConfig, cloud_init_config_data_source: TerraformDataSource) -> Dict[str, TerraformOutput]:
    cloud_init_config_outputs = {}

    if config.CLOUD_INSTANCE_PROVIDER == config.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_init_config_outputs["cloudinit_file"] = TerraformOutput(
            scope=scope,
            id="cloud_init_config_outputs_cloudinit_file",
            value=cloud_init_config_data_source.filename,
        )

    else:
        cloud_init_config_outputs["user_data"] = TerraformOutput(
            scope=scope,
            id="cloud_init_config_outputs_user_data",
            value=cloud_init_config_data_source.values.outputs["user_data"],
        )

    return cloud_init_config_outputs


class CloudInitConfigConstruct(Construct):
    def __init__(
        self, scope: Construct, id: str, config: MainConfig
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        self.cloud_init_config_provider_future: PrefectFuture[TerraformProvider] = get_cloud_init_config_provider.submit(scope=scope, config=config)
        self.cloud_init_config_resource_future: PrefectFuture[TerraformResource] = get_cloud_init_config_resource.submit(scope=scope, config=config, cloud_init_config_provider=self.cloud_init_config_provider_future)
        self.cloud_init_config_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_init_config_data_source.submit(scope=scope, config=config, cloud_init_config_resource=self.cloud_init_config_resource_future)
        self.cloud_init_config_outputs_future: PrefectFuture[Dict[str, TerraformOutput]] = get_cloud_init_config_outputs.submit(scope=scope, config=config, cloud_init_config_data_source=self.cloud_init_config_data_source_future)

        self.provider = self.cloud_init_config_provider_future.result()
        self.resource = self.cloud_init_config_resource_future.result()
        self.data_source = self.cloud_init_config_data_source_future.result()
        self.outputs = self.cloud_init_config_outputs_future.result()
