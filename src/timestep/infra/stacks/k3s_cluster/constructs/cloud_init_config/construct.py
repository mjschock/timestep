from enum import StrEnum, auto

from cdktf import (
    TerraformOutput,
)
from cloud_init_gen import CloudInitDoc
from constructs import Construct

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.cloudinit.data_cloudinit_config import (
    DataCloudinitConfig,
    DataCloudinitConfigPart,
)
from timestep.infra.imports.cloudinit.provider import CloudinitProvider
from timestep.infra.imports.local.data_local_file import DataLocalFile
from timestep.infra.imports.local.file import File
from timestep.infra.imports.local.provider import LocalProvider
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.resource import Resource


class CloudInstanceProvider(StrEnum):
    DIGITALOCEAN: str = auto()
    MULTIPASS: str = auto()


class CloudInitConfigConstruct(Construct):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)

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

        if not config.variables.get(
            "ssh_public_key", None
        ) or not config.secrets.get_secret_value().get("ssh_private_key", None):
            raise Exception("SSH credentials not found")

        username = "ubuntu"

        cloud_cfg = dict(
            disable_root=True,
            package_reboot_if_required=True,
            package_update=True,
            package_upgrade=True,
            packages=[
                "build-essential",
                "ca-certificates-java",
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
                "sed -i -E '/^#?PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config",  # noqa: E501
                f"sed -i -e '$aAllowUsers {username}' /etc/ssh/sshd_config",
                "service ssh restart",
                "curl -sLS https://get.arkade.dev | sudo sh",
                [
                    "runuser",
                    "-l",
                    username,
                    "-c",
                    'echo "\nexport PATH=\\$HOME/.arkade/bin:\\$PATH" >> $HOME/.bashrc',
                ],
                ["runuser", "-l", username, "-c", "arkade get k3sup"],
                [
                    "runuser",
                    "-l",
                    username,
                    "-c",
                    f"""$HOME/.arkade/bin/k3sup install \
--context {config.variables.get("kubecontext")} \
--k3s-extra-args '--disable traefik' \
--local \
--user {username}""",
                ],
            ],
            users=[
                "default",
                {
                    "groups": "sudo",
                    "name": username,
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
            null_provider = NullTerraformProvider(
                id="null_provider",
                scope=scope,
            )
            cloud_init_config_resource = Resource(
                id="cloud_init_config_resource",
                provider=null_provider,
                scope=scope,
                triggers={
                    "content": user_data.render(),
                },
            )

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
                base64_encode=False,
                boundary=None,
                gzip=False,
                part=[
                    data_cloud_init_config_part,
                ],
                connection=None,
                count=None,
                depends_on=None,
                for_each=None,
                lifecycle=None,
                provider=cloud_init_config_provider,
                provisioners=None,
            )

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

        self.data_source = cloud_init_config_data_source
