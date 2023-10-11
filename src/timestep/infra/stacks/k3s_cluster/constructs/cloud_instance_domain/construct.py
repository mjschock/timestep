from cdktf_cdktf_provider_digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from cdktf_cdktf_provider_digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from cdktf_cdktf_provider_local.data_local_file import (
    DataLocalFile as LocalFileTerraformDataSource,
)
from cdktf_cdktf_provider_local.file import File as LocalFileTerraformResource
from cdktf_cdktf_provider_local.provider import (
    LocalProvider as LocalTerraformProvider,
)
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.construct import (
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

        subdomains = [
            # "kubernetes-dashboard",
            "minio",
            "prefect-server",
            "www",
        ]

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
            content = ""

            for subdomain in subdomains:
                content += f"{ipv4} {subdomain}.{primary_domain_name}\n"

            content += f"{ipv4} {primary_domain_name}\n"

            cloud_instance_domain_resource = LocalFileTerraformResource(
                id="cloud_instance_domain_resource",
                content=content,
                filename="hosts",
                provider=cloud_instance_domain_provider,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            for subdomain in subdomains:
                DigitaloceanDomainTerraformResource(
                    id_=f"cloud_instance_domain_resource_{subdomain}",
                    ip_address=cloud_instance_construct.data_source.ipv4_address,
                    name=f"{subdomain}.{config.primary_domain_name}",
                    provider=cloud_instance_domain_provider,
                    scope=scope,
                )

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
            LocalFileTerraformDataSource(
                id="cloud_instance_domain_data_source",
                filename=cloud_instance_domain_resource.filename,
                provider=cloud_instance_domain_resource.provider,
                scope=scope,
            )

        elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
            DigitaloceanDomainTerraformDataSource(
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

        # cloud_instance_domain_outputs = {}

        # if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
        #     cloud_instance_domain_outputs["hosts_file"] = TerraformOutput(
        #         id="cloud_instance_domain_outputs_hosts_file",
        #         value=cloud_instance_domain_data_source.filename,
        #         scope=scope,
        #     )

        # elif config.cloud_instance_provider == CloudInstanceProvider.DIGITALOCEAN:
        #     cloud_instance_domain_outputs["zone_file"] = TerraformOutput(
        #         id="cloud_instance_domain_outputs_zone_file",
        #         value=cloud_instance_domain_data_source.zone_file,
        #         scope=scope,
        #     )

        # else:
        #     cloud_instance_provider = config.cloud_instance_provider
        #     raise ValueError(
        #         f"Unknown cloud_instance_provider: {cloud_instance_provider}"
        #     )
