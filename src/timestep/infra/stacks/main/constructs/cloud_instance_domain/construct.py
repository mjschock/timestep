from cdktf import (
    TerraformOutput,
)
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
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
from timestep.infra.stacks.main.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)


class CloudInstanceDomainConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        cloud_instance_construct: CloudInstanceConstruct,
    ) -> None:
        super().__init__(scope, id)

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_instance_domain_provider = LocalTerraformProvider(
                alias="cloud_instance_domain_provider",
                id="cloud_instance_domain_provider",
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_domain_provider = cloud_instance_construct.provider

        else:
            cloud_instance_provider = config.cloud_instance_provider
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            ipv4 = cloud_instance_construct.data_source.ipv4
            primary_domain_name = config.primary_domain_name
            subdomains = [
                # "alice",
                # "api",
                # "bob",
                # "example1",
                # "example2",
                # "notary",
                # "marvin",
                # "prefect-server",
                # "registry",
                # "studio",
                # "supabase",
                # "supabase-studio",
                # "talker",
                # "traefik",
                "www",
            ]

            content = ""

            for subdomain in subdomains:
                content += f"{ipv4} {subdomain}.{primary_domain_name}\n"

            content += f"{ipv4} {primary_domain_name}\n"

            # content += f"{ipv4} core.harbor.domain\n"

            cloud_instance_domain_resource = LocalFileTerraformResource(
                id="cloud_instance_domain_resource",
                content=content,
                filename="hosts",
                provider=cloud_instance_domain_provider,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_domain_resource = DigitaloceanDomainTerraformResource(
                id_="cloud_instance_domain_resource",
                ip_address=cloud_instance_construct.data_source.ipv4_address,
                name=config.primary_domain_name,
                provider=cloud_instance_domain_provider,
                scope=scope,
            )

        else:
            cloud_instance_provider = config.cloud_instance_provider
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_instance_domain_data_source = LocalFileTerraformDataSource(
                id="cloud_instance_domain_data_source",
                filename=cloud_instance_domain_resource.filename,
                provider=cloud_instance_domain_resource.provider,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_domain_data_source = DigitaloceanDomainTerraformDataSource(
                id_="cloud_instance_domain_data_source",
                name=cloud_instance_domain_resource.name,
                provider=cloud_instance_domain_resource.provider,
                scope=scope,
            )

        else:
            cloud_instance_provider = config.cloud_instance_provider
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )

        cloud_instance_domain_outputs = {}

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_instance_domain_outputs["hosts_file"] = TerraformOutput(
                id="cloud_instance_domain_outputs_hosts_file",
                value=cloud_instance_domain_data_source.filename,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            cloud_instance_domain_outputs["zone_file"] = TerraformOutput(
                id="cloud_instance_domain_outputs_zone_file",
                value=cloud_instance_domain_data_source.zone_file,
                scope=scope,
            )

        else:
            cloud_instance_provider = config.cloud_instance_provider
            raise ValueError(
                f"Unknown cloud_instance_provider: {cloud_instance_provider}"
            )
