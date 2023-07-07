from typing import Dict

from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from prefect import task

from timestep.conf.blocks import AppConfig, DomainNameRegistrarProvider
from timestep.infra.imports.namecheap.domain_records import (
    DomainRecords as NamecheapDomainRecordsTerraformResource,
)
from timestep.infra.imports.namecheap.provider import (
    NamecheapProvider as NamecheapTerraformProvider,
)
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.resource import Resource as NullTerraformResource
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)


@task
def get_domain_name_registrar_provider(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
) -> TerraformProvider:
    if config.variables.get("domain_name_registrar_provider") is None:
        domain_name_registrar_provider = NullTerraformProvider(
            alias="domain_name_registrar_provider",
            id="domain_name_registrar_provider",
            scope=scope,
        )

    elif (
        config.variables.get("domain_name_registrar_provider")
        == DomainNameRegistrarProvider.NAMECHEAP
    ):
        domain_name_registrar_provider = NamecheapTerraformProvider(
            id="domain_name_registrar_provider",
            api_key=config.secrets.get_secret_value().get("namecheap_api_key"),
            api_user=config.secrets.get_secret_value().get("namecheap_api_user"),
            user_name=config.secrets.get_secret_value().get("namecheap_user_name"),
            scope=scope,
        )

    else:
        domain_name_registrar_provider = config.variables.get(
            "domain_name_registrar_provider"
        )
        raise ValueError(
            f"Unknown domain_name_registrar_provider: {domain_name_registrar_provider}"
        )

    return domain_name_registrar_provider


@task
def get_domain_name_registrar_resource(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    domain_name_registrar_provider: TerraformProvider,
) -> TerraformResource:
    if config.variables.get("domain_name_registrar_provider") is None:
        domain_name_registrar_resource = NullTerraformResource(
            id="domain_name_registrar_resource",
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    elif (
        config.variables.get("domain_name_registrar_provider")
        == DomainNameRegistrarProvider.NAMECHEAP
    ):
        domain_name_registrar_resource = NamecheapDomainRecordsTerraformResource(
            id_="domain_name_registrar_resource",
            domain=config.variables.get("primary_domain_name"),
            mode="OVERWRITE",
            nameservers=[  # TODO: Get these dynamically
                "ns1.digitalocean.com",
                "ns2.digitalocean.com",
                "ns3.digitalocean.com",
            ],
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    else:
        domain_name_registrar_provider = config.variables.get(
            "domain_name_registrar_provider"
        )
        raise ValueError(
            f"Unknown domain_name_registrar_provider: {domain_name_registrar_provider}"
        )

    return domain_name_registrar_resource


@task
def get_domain_name_registrar_data_source(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    domain_name_registrar_resource: TerraformResource,
) -> TerraformDataSource:
    # if config.variables.get("domain_name_registrar_provider") == None:
    # domain_name_registrar_data_source = NullTerraformDataSource(
    #     id="domain_name_registrar_data_source",
    #     provider=domain_name_registrar_resource.provider,
    #     scope=scope,
    # )

    # domain_name_registrar_data_source = TerraformLocal(
    #     id="domain_name_registrar_data_source",
    #     expression=Token.from_str("null_data_source"),
    #     scope=scope,
    # )

    # else:
    # domain_name_registrar_data_source = NullTerraformDataSource(
    #     id="domain_name_registrar_data_source",
    #     scope=scope,
    # )

    # domain_name_registrar_data_source = TerraformLocal(
    #     id="domain_name_registrar_data_source",
    #     scope=scope,
    # )

    # domain_name_registrar_data_source = TerraformDataSource(
    #     id="domain_name_registrar_data_source",
    #     # provider=domain_name_registrar_resource.provider,
    #     # terraform_resource_type=type(domain_name_registrar_resource).__name__,
    #     terraform_resource_type="data_source",
    #     scope=scope,
    # )

    domain_name_registrar_data_source = None

    return domain_name_registrar_data_source


@task
def get_domain_name_registrar_outputs(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    domain_name_registrar_data_source: TerraformDataSource,
) -> Dict[str, TerraformOutput]:
    domain_name_registrar_outputs = {}

    return domain_name_registrar_outputs
