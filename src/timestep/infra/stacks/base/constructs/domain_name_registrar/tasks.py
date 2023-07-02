import os
import pathlib
from typing import Any, Dict, List, Type

from cdktf import (
    LocalExecProvisioner,
    TerraformDataSource,
    TerraformElement,
    TerraformLocal,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
    Token,
)
from cloud_init_gen import CloudInitDoc
from constructs import Construct
from prefect import flow, get_run_logger, task
from prefect.filesystems import LocalFileSystem
from prefect.futures import PrefectFuture
from prefect.task_runners import SequentialTaskRunner
from prefect_shell import ShellOperation
from pydantic import BaseModel

from timestep.conf.blocks import AppConfig, DomainNameRegistrarProvider
from timestep.infra.imports.cloudinit.data_cloudinit_config import (
    DataCloudinitConfig as CloudInitConfigTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.external.data_external import (
    DataExternal as ExternalTerraformDataSource,
)
from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider
from timestep.infra.imports.helm.provider import HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.namespace import (
    Namespace as KubernetesNamespaceTerraformResource,
)
from timestep.infra.imports.kubernetes.namespace import NamespaceMetadata
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)
from timestep.infra.imports.local.data_local_file import (
    DataLocalFile as LocalFileTerraformDataSource,
)
from timestep.infra.imports.local.file import File as LocalFileTerraformResource
from timestep.infra.imports.local.provider import (
    LocalProvider as LocalTerraformProvider,
)
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.imports.namecheap.domain_records import (
    DomainRecords as NamecheapDomainRecordsTerraformResource,
)
from timestep.infra.imports.namecheap.provider import (
    NamecheapProvider as NamecheapTerraformProvider,
)
from timestep.infra.imports.null.data_null_data_source import (
    DataNullDataSource as NullTerraformDataSource,
)
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.resource import Resource as NullTerraformResource
from timestep.infra.stacks.base.constructs.cloud_init_config.blocks import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.base.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)


@task
def get_domain_name_registrar_provider(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
) -> TerraformProvider:
    if config.variables.get("domain_name_registrar_provider") == None:
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
            api_key=config.NAMECHEAP_API_KEY,
            api_user=config.NAMECHEAP_API_USER,
            user_name=config.NAMECHEAP_USER_NAME,
            scope=scope,
        )

    else:
        raise ValueError(
            f"Unknown domain_name_registrar_provider: {config.variables.get('domain_name_registrar_provider')}"
        )

    return domain_name_registrar_provider


@task
def get_domain_name_registrar_resource(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    domain_name_registrar_provider: TerraformProvider,
) -> TerraformResource:
    if config.variables.get("domain_name_registrar_provider") == None:
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
            domain=config.DOMAIN,
            mode="OVERWRITE",
            nameservers=[
                "ns1.digitalocean.com",  # TODO: can I get these from the cloud_instance_construct?
                "ns2.digitalocean.com",
                "ns3.digitalocean.com",
            ],
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    else:
        raise ValueError(
            f"Unknown domain_name_registrar_provider: {config.variables.get('domain_name_registrar_provider')}"
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
