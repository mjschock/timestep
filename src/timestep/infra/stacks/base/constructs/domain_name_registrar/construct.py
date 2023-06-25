import os
from prefect import flow, task, get_run_logger
from prefect.futures import PrefectFuture
from prefect.filesystems import LocalFileSystem
from prefect.task_runners import SequentialTaskRunner
from prefect_shell import ShellOperation
from typing import Any, Dict, List, Type
import pathlib
from cdktf import LocalExecProvisioner, Token
from constructs import Construct
from cdktf import (
    TerraformDataSource,
    TerraformElement,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from cloud_init_gen import CloudInitDoc
from pydantic import BaseModel

from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.external.data_external import DataExternal as ExternalTerraformDataSource

from timestep.infra.imports.helm.provider import (
    HelmProvider as HelmTerraformProvider,
    HelmProviderKubernetes,
)
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)
from timestep.infra.imports.kubernetes.namespace import (
    Namespace as KubernetesNamespaceTerraformResource,
    NamespaceMetadata,
)
from timestep.infra.imports.namecheap.provider import NamecheapProvider as NamecheapTerraformProvider
from timestep.infra.imports.namecheap.domain_records import DomainRecords as NamecheapDomainRecordsTerraformResource

from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.data_null_data_source import DataNullDataSource as NullTerraformDataSource
from timestep.infra.imports.null.resource import Resource as NullTerraformResource

from timestep.infra.imports.cloudinit.data_cloudinit_config import DataCloudinitConfig as CloudInitConfigTerraformDataSource

from timestep.infra.imports.local.data_local_file import DataLocalFile as LocalFileTerraformDataSource
from timestep.infra.imports.local.file import File as LocalFileTerraformResource
from timestep.infra.imports.local.provider import LocalProvider as LocalTerraformProvider

from timestep.conf import MainConfig, MainConfig
from timestep.infra.stacks.base.constructs.cloud_init_config.construct import CloudInitConfigConstruct
from timestep.infra.stacks.base.constructs.cloud_instance.construct import CloudInstanceConstruct

@task
def get_domain_name_registrar_provider(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        domain_name_registrar_provider = NullTerraformProvider(
            alias="domain_name_registrar_provider",
            id="domain_name_registrar_provider",
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN: # TODO: MainConfig.DOMAIN_NAME_REGISTRAR_PROVIDERS.NAMECHEAP
        domain_name_registrar_provider = NamecheapTerraformProvider(
            id="domain_name_registrar_provider",
            api_key=config.NAMECHEAP_API_KEY,
            api_user=config.NAMECHEAP_API_USER,
            user_name=config.NAMECHEAP_USER_NAME,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return domain_name_registrar_provider


@task
def get_domain_name_registrar_resource(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct, domain_name_registrar_provider: TerraformProvider) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        domain_name_registrar_resource = NullTerraformResource(
            id="domain_name_registrar_resource",
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN: # TODO: MainConfig.DOMAIN_NAME_REGISTRAR_PROVIDERS.NAMECHEAP
        domain_name_registrar_resource = NamecheapDomainRecordsTerraformResource(
            id_="domain_name_registrar_resource",
            # domain=config.DOMAIN,
            domain=config.STACK_ID,
            mode="OVERWRITE",
            nameservers=[
                "ns1.digitalocean.com", # TODO: can I get these from the cloud_instance_construct?
                "ns2.digitalocean.com",
                "ns3.digitalocean.com",
            ],
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return domain_name_registrar_resource


@task
def get_domain_name_registrar_data_source(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct, domain_name_registrar_resource: TerraformResource) -> TerraformDataSource:
    domain_name_registrar_data_source = NullTerraformDataSource(
        id="domain_name_registrar_data_source",
        provider=domain_name_registrar_resource.provider,
        scope=scope,
    )

    return domain_name_registrar_data_source


@task
def get_domain_name_registrar_outputs(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct, domain_name_registrar_data_source: TerraformDataSource) -> Dict[str, TerraformOutput]:
    domain_name_registrar_outputs = {}

    return domain_name_registrar_outputs


class DomainNameRegistrarConstruct(Construct):
    def __init__(
        self, scope: Construct, id: str, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        self.domain_name_registrar_provider_future: PrefectFuture[TerraformProvider] = get_domain_name_registrar_provider.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct)
        self.domain_name_registrar_resource_future: PrefectFuture[TerraformResource] = get_domain_name_registrar_resource.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, domain_name_registrar_provider=self.domain_name_registrar_provider_future)
        self.domain_name_registrar_data_source_future: PrefectFuture[TerraformDataSource] = get_domain_name_registrar_data_source.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, domain_name_registrar_resource=self.domain_name_registrar_resource_future)
        self.domain_name_registrar_outputs_future: PrefectFuture[Dict[str, TerraformOutput]] = get_domain_name_registrar_outputs.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, domain_name_registrar_data_source=self.domain_name_registrar_data_source_future)

        self.provider = self.domain_name_registrar_provider_future.result()
        self.resource = self.domain_name_registrar_resource_future.result()
        self.data_source = self.domain_name_registrar_data_source_future.result()
        self.outputs = self.domain_name_registrar_outputs_future.result()
