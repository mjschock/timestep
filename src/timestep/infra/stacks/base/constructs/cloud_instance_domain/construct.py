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
def get_cloud_instance_domain_provider(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_domain_provider = LocalTerraformProvider(
            alias="cloud_instance_domain_provider",
            id="cloud_instance_domain_provider",
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_domain_provider = cloud_instance_construct.provider

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_domain_provider


@task
def get_cloud_instance_domain_resource(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct, cloud_instance_domain_provider: TerraformProvider) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        subdomains = [
            "registry",
            "www",
        ]

        cloud_instance_domain_resource = LocalFileTerraformResource(
            id="cloud_instance_domain_resource",
#             content=f"""
# {cloud_instance_construct.outputs["ipv4"]} {subdomains[0]}.{config.STACK_ID} # TODO: use config.DOMAIN instead of config.STACK_ID? what about breaking up into domain and tld?
# {cloud_instance_construct.outputs["ipv4"]} {subdomains[1]}.{config.STACK_ID}
# {cloud_instance_construct.outputs["ipv4"]} {config.STACK_ID}
# """,
            content=f"""
{cloud_instance_construct.data_source.ipv4} {subdomains[0]}.{config.STACK_ID}
{cloud_instance_construct.data_source.ipv4} {subdomains[1]}.{config.STACK_ID}
{cloud_instance_construct.data_source.ipv4} {config.STACK_ID}
""",
            filename=config.HOSTS_FILE_PATH,
            provider=cloud_instance_domain_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_domain_resource = DigitaloceanDomainTerraformResource(
            id_="cloud_instance_domain_resource",
            # ip_address=cloud_instance_construct.outputs["ipv4"],
            ip_address=cloud_instance_construct.data_source.ipv4_address,
            name=config.STACK_ID,
            provider=cloud_instance_domain_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_domain_resource


@task
def get_cloud_instance_domain_data_source(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct, cloud_instance_domain_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_domain_data_source = LocalFileTerraformDataSource(
            id="cloud_instance_domain_data_source",
            filename=cloud_instance_domain_resource.filename,
            provider=cloud_instance_domain_resource.provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_domain_data_source = DigitaloceanDomainTerraformDataSource(
            id_="cloud_instance_domain_data_source",
            name=cloud_instance_domain_resource.name,
            provider=cloud_instance_domain_resource.provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_domain_data_source


@task
def get_cloud_instance_domain_outputs(scope: TerraformStack, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct, cloud_instance_domain_data_source: TerraformDataSource) -> Dict[str, TerraformOutput]:
    cloud_instance_domain_outputs = {}

    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_domain_outputs["hosts_file"] = TerraformOutput(
            id="cloud_instance_domain_outputs_hosts_file",
            value=cloud_instance_domain_data_source.filename,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_domain_outputs["zone_file"] = TerraformOutput(
            id="cloud_instance_domain_outputs_zone_file",
            value=cloud_instance_domain_data_source.zone_file,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_domain_outputs


class CloudInstanceDomainConstruct(Construct):
    def __init__(
        self, scope: Construct, id: str, config: MainConfig, cloud_instance_construct: CloudInstanceConstruct
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        self.cloud_instance_domain_provider_future: PrefectFuture[TerraformProvider] = get_cloud_instance_domain_provider.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct)
        self.cloud_instance_domain_resource_future: PrefectFuture[TerraformResource] = get_cloud_instance_domain_resource.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, cloud_instance_domain_provider=self.cloud_instance_domain_provider_future)
        self.cloud_instance_domain_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_instance_domain_data_source.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, cloud_instance_domain_resource=self.cloud_instance_domain_resource_future)
        self.cloud_instance_domain_outputs_future: PrefectFuture[Dict[str, TerraformOutput]] = get_cloud_instance_domain_outputs.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, cloud_instance_domain_data_source=self.cloud_instance_domain_data_source_future)

        self.provider = self.cloud_instance_domain_provider_future.result()
        self.resource = self.cloud_instance_domain_resource_future.result()
        self.data_source = self.cloud_instance_domain_data_source_future.result()
        self.outputs = self.cloud_instance_domain_outputs_future.result()
