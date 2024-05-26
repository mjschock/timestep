from cdktf import TerraformDataSource
from cdktf_cdktf_provider_cloudinit.data_cloudinit_config import (
    DataCloudinitConfig,
    DataCloudinitConfigPart,
)
from cdktf_cdktf_provider_cloudinit.provider import CloudinitProvider
from cdktf_cdktf_provider_local.data_local_file import DataLocalFile
from cdktf_cdktf_provider_local.file import File
from cdktf_cdktf_provider_local.provider import LocalProvider
from cdktf_cdktf_provider_null.provider import NullProvider as NullTerraformProvider
from cdktf_cdktf_provider_null.resource import Resource
from cloud_init_gen import CloudInitDoc
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings


class CloudInitConfigConstruct(Construct):
    def __init__(self, scope: Construct, id: str, config: Settings) -> None:
        super().__init__(scope, id)

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
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
                f"sed -i -e '$aAllowUsers {config.cloud_instance_user}' /etc/ssh/sshd_config",  # noqa: E501
                "service ssh restart",
                "curl -sLS https://get.arkade.dev | sudo sh",
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    'echo "\nexport PATH=\\$HOME/.arkade/bin:\\$PATH" >> $HOME/.bashrc',
                ],
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    "arkade get k3sup",
                ],
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    f"""$HOME/.arkade/bin/k3sup install \
--context {config.kubecontext} \
--k3s-extra-args '--disable traefik' \
--local \
--user {config.cloud_instance_user}""",
                ],
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    "mkdir -p $HOME/.sky",
                ],
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    "mkdir -p $HOME/secrets",  # TODO: Remove this line?
                ],
            ],
            users=[
                "default",
                {
                    "groups": "sudo",
                    "name": config.cloud_instance_user,
                    "shell": "/bin/bash",
                    "ssh_authorized_keys": [
                        config.ssh_public_key.get_secret_value(),
                    ],
                    "sudo": "ALL=(ALL) NOPASSWD:ALL",
                },
            ],
        )

        user_data = CloudInitDoc()
        user_data.add(cloud_cfg)

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
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

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
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

        self.data_source: TerraformDataSource[
            DataLocalFile | DataCloudinitConfig
        ] = cloud_init_config_data_source
