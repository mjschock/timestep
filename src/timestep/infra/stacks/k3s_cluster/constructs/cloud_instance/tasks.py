from typing import Dict

from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from prefect import task

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.digitalocean.ssh_key import SshKey
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.stacks.k3s_cluster.constructs.cloud_init_config.blocks import (
    CloudInitConfigConstruct,
)


@task
def get_cloud_instance_provider(
    scope: TerraformStack,
    config: AppConfig,
    cloud_init_config_construct: CloudInitConfigConstruct,
) -> TerraformProvider:
    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_instance_provider = MultipassTerraformProvider(
            id="cloud_instance_provider",
            scope=scope,
        )

    elif (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.DIGITALOCEAN
    ):
        cloud_instance_provider = DigitaloceanTerraformProvider(
            id="cloud_instance_provider",
            scope=scope,
            token=config.secrets.get_secret_value().get("do_token"),
        )

    else:
        cloud_instance_provider = config.variables.get("cloud_instance_provider")
        raise ValueError(f"Unknown cloud_instance_provider: {cloud_instance_provider}")

    return cloud_instance_provider


@task
def get_cloud_instance_resource(
    scope: TerraformStack,
    config: AppConfig,
    cloud_init_config_construct: CloudInitConfigConstruct,
    cloud_instance_provider: TerraformProvider,
) -> TerraformResource:
    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_instance_resource = MultipassInstanceTerraformResource(
            cloudinit_file=cloud_init_config_construct.outputs["cloudinit_file"].value,
            cpus=config.variables.get("multipass_instance_cpus"),
            disk=config.variables.get("multipass_instance_disk"),
            id="cloud_instance_resource",
            image=config.variables.get("multipass_instance_image"),
            name=config.variables.get("cloud_instance_name"),
            provider=cloud_instance_provider,
            scope=scope,
        )

    elif (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.DIGITALOCEAN
    ):
        cloud_instance_ssh_key_resource = SshKey(
            id_="cloud_instance_ssh_key_resource",
            name=f'{config.variables.get("cloud_instance_name")}_ssh_key',
            provider=cloud_instance_provider,
            public_key=config.variables.get("ssh_public_key"),
            scope=scope,
        )
        cloud_instance_resource = DigitaloceanDropletTerraformResource(
            id_="cloud_instance_resource",
            image=config.variables.get("do_droplet_image"),
            name=config.variables.get("cloud_instance_name"),
            provider=cloud_instance_provider,
            region=config.variables.get("do_droplet_region"),
            scope=scope,
            size=config.variables.get("do_droplet_size"),
            ssh_keys=[cloud_instance_ssh_key_resource.fingerprint],
            user_data=cloud_init_config_construct.outputs["user_data"].value,
        )

    else:
        cloud_instance_provider = config.variables.get("cloud_instance_provider")
        raise ValueError(f"Unknown cloud_instance_provider: {cloud_instance_provider}")

    return cloud_instance_resource


@task
def get_cloud_instance_data_source(
    scope: TerraformStack,
    config: AppConfig,
    cloud_init_config_construct: CloudInitConfigConstruct,
    cloud_instance_resource: TerraformResource,
) -> TerraformDataSource:
    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_instance_data_source = MultipassInstanceTerraformDataSource(
            id="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_resource.provider,
            scope=scope,
        )

    elif (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.DIGITALOCEAN
    ):
        cloud_instance_data_source = DigitaloceanDropletTerraformDataSource(
            id_="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_resource.provider,
            scope=scope,
        )

    else:
        cloud_instance_provider = config.variables.get("cloud_instance_provider")
        raise ValueError(f"Unknown cloud_instance_provider: {cloud_instance_provider}")

    return cloud_instance_data_source


@task
def get_cloud_instance_outputs(
    scope: TerraformStack,
    config: AppConfig,
    cloud_init_config_construct: CloudInitConfigConstruct,
    cloud_instance_data_source: TerraformDataSource,
) -> Dict[str, TerraformOutput]:
    cloud_instance_outputs = {}

    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        cloud_instance_outputs["ipv4"] = TerraformOutput(
            id="cloud_instance_outputs_ipv4",
            value=cloud_instance_data_source.ipv4,
            scope=scope,
        )

    elif (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.DIGITALOCEAN
    ):
        cloud_instance_outputs["ipv4"] = TerraformOutput(
            id="cloud_instance_outputs_ipv4",
            value=cloud_instance_data_source.ipv4_address,
            scope=scope,
        )

    else:
        cloud_instance_provider = config.variables.get("cloud_instance_provider")
        raise ValueError(f"Unknown cloud_instance_provider: {cloud_instance_provider}")

    return cloud_instance_outputs
