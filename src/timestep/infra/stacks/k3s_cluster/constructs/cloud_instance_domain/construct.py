from cdktf import (
    TerraformOutput,
)
from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.local.data_local_file import (
    DataLocalFile as LocalFileTerraformDataSource,
)
from timestep.infra.imports.local.file import File as LocalFileTerraformResource
from timestep.infra.imports.local.provider import (
    LocalProvider as LocalTerraformProvider,
)
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)


class CloudInstanceDomainConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: AppConfig,
        cloud_instance_construct: CloudInstanceConstruct,
    ) -> None:
        super().__init__(scope, id)
        get_run_logger()

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
        ):
            cloud_instance_domain_provider = LocalTerraformProvider(
                alias="cloud_instance_domain_provider",
                id="cloud_instance_domain_provider",
                scope=scope,
            )

        elif (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.DIGITALOCEAN
        ):
            cloud_instance_domain_provider = cloud_instance_construct.provider

        else:
            cloud_instance_provider = config.variables.get("cloud_instance_provider")
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )  # noqa: E501

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
        ):
            ipv4 = cloud_instance_construct.data_source.ipv4
            primary_domain_name = config.variables.get("primary_domain_name")
            subdomains = [
                "registry",
                "www",
            ]

            cloud_instance_domain_resource = LocalFileTerraformResource(
                id="cloud_instance_domain_resource",
                content=f"""{ipv4} {subdomains[0]}.{primary_domain_name}
{ipv4} {subdomains[1]}.{primary_domain_name}
{ipv4} {primary_domain_name}
""",
                # filename=f"{config.BASE_PATH}/{config.HOSTS_FILE_PATH}",
                filename="hosts",
                provider=cloud_instance_domain_provider,
                scope=scope,
            )

        elif (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.DIGITALOCEAN
        ):
            cloud_instance_domain_resource = DigitaloceanDomainTerraformResource(
                id_="cloud_instance_domain_resource",
                # ip_address=cloud_instance_construct.outputs["ipv4"],
                ip_address=cloud_instance_construct.data_source.ipv4_address,
                name=config.variables.get("primary_domain_name"),
                provider=cloud_instance_domain_provider,
                scope=scope,
            )

        else:
            cloud_instance_provider = config.variables.get("cloud_instance_provider")
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )  # noqa: E501

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
        ):
            cloud_instance_domain_data_source = LocalFileTerraformDataSource(
                id="cloud_instance_domain_data_source",
                filename=cloud_instance_domain_resource.filename,
                provider=cloud_instance_domain_resource.provider,
                scope=scope,
            )

        elif (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.DIGITALOCEAN
        ):
            cloud_instance_domain_data_source = DigitaloceanDomainTerraformDataSource(
                id_="cloud_instance_domain_data_source",
                name=cloud_instance_domain_resource.name,
                provider=cloud_instance_domain_resource.provider,
                scope=scope,
            )

        else:
            cloud_instance_provider = config.variables.get("cloud_instance_provider")
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )  # noqa: E501

        cloud_instance_domain_outputs = {}

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
        ):
            cloud_instance_domain_outputs["hosts_file"] = TerraformOutput(
                id="cloud_instance_domain_outputs_hosts_file",
                value=cloud_instance_domain_data_source.filename,
                scope=scope,
            )

        elif (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.DIGITALOCEAN
        ):
            cloud_instance_domain_outputs["zone_file"] = TerraformOutput(
                id="cloud_instance_domain_outputs_zone_file",
                value=cloud_instance_domain_data_source.zone_file,
                scope=scope,
            )

        else:
            cloud_instance_provider = config.variables.get("cloud_instance_provider")
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )  # noqa: E501
