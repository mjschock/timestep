from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
)
from cdktf_cdktf_provider_cloudinit.data_cloudinit_config import DataCloudinitConfig
from cdktf_cdktf_provider_digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from cdktf_cdktf_provider_digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from cdktf_cdktf_provider_digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from cdktf_cdktf_provider_digitalocean.ssh_key import SshKey
from cdktf_cdktf_provider_local.data_local_file import DataLocalFile
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.stacks.main.constructs.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)


class CloudInstanceConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        cloud_init_config_construct: CloudInitConfigConstruct,
    ) -> None:
        super().__init__(scope, id)

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_instance_provider = MultipassTerraformProvider(
                id="cloud_instance_provider",
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_provider = DigitaloceanTerraformProvider(
                id="cloud_instance_provider",
                scope=scope,
                token=config.secrets.get_secret_value().get("do_token"),
            )

        else:
            raise ValueError(
                f"Unknown cloud_instance_provider: {config.cloud_instance_provider}"  # noqa: E501
            )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_init_config_construct_data_source: DataLocalFile = (
                cloud_init_config_construct.data_source
            )  # noqa: E501
            cloud_instance_resource = MultipassInstanceTerraformResource(
                # cloudinit_file=cloud_init_config_construct.data_source.filename,
                cloudinit_file=cloud_init_config_construct_data_source.filename,
                cpus=config.multipass_instance_cpus,
                disk=config.multipass_instance_disk,
                id="cloud_instance_resource",
                image=config.multipass_instance_image,
                memory=config.multipass_instance_memory,
                name=config.cloud_instance_name,
                provider=cloud_instance_provider,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_ssh_key_resource = SshKey(
                id_="cloud_instance_ssh_key_resource",
                name=f"{config.cloud_instance_name}_ssh_key",
                provider=cloud_instance_provider,
                public_key=config.ssh_public_key,
                scope=scope,
            )
            cloud_init_config_construct_data_source: DataCloudinitConfig = (
                cloud_init_config_construct.data_source
            )  # noqa: E501
            cloud_instance_resource = DigitaloceanDropletTerraformResource(
                id_="cloud_instance_resource",
                image=config.do_droplet_image,
                name=config.cloud_instance_name,
                provider=cloud_instance_provider,
                region=config.do_droplet_region,
                scope=scope,
                size=config.do_droplet_size,
                ssh_keys=[cloud_instance_ssh_key_resource.fingerprint],
                # user_data=cloud_init_config_construct.data_source.rendered,
                user_data=cloud_init_config_construct_data_source.rendered,
            )

        else:
            raise ValueError(
                f"Unknown cloud_instance_provider: {config.cloud_instance_provider}"  # noqa: E501
            )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_instance_data_source = MultipassInstanceTerraformDataSource(
                id="cloud_instance_data_source",
                name=cloud_instance_resource.name,
                provider=cloud_instance_resource.provider,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_data_source = DigitaloceanDropletTerraformDataSource(
                id_="cloud_instance_data_source",
                name=cloud_instance_resource.name,
                provider=cloud_instance_resource.provider,
                scope=scope,
            )

        else:
            raise ValueError(
                f"Unknown cloud_instance_provider: {config.cloud_instance_provider}"  # noqa: E501
            )

        cloud_instance_outputs = {}

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_instance_outputs["ipv4"] = TerraformOutput(
                id="cloud_instance_outputs_ipv4",
                value=cloud_instance_data_source.ipv4,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_outputs["ipv4"] = TerraformOutput(
                id="cloud_instance_outputs_ipv4",
                value=cloud_instance_data_source.ipv4_address,
                scope=scope,
            )

        else:
            raise ValueError(
                f"Unknown cloud_instance_provider: {config.cloud_instance_provider}"  # noqa: E501
            )

        self.data_source: TerraformDataSource[
            MultipassInstanceTerraformDataSource
            | DigitaloceanDropletTerraformDataSource
        ] = cloud_instance_data_source  # noqa: E501
        self.provider: TerraformProvider[
            MultipassTerraformProvider | DigitaloceanTerraformProvider
        ] = cloud_instance_provider  # noqa: E501
