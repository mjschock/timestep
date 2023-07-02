import os
import pathlib
from typing import Any, Dict, List, Type

from cdktf import (
    LocalExecProvisioner,
    TerraformDataSource,
    TerraformElement,
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

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
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


@task
def get_cloud_instance_provider(
    scope: TerraformStack,
    config: AppConfig,
    cloud_init_config_construct: CloudInitConfigConstruct,
) -> TerraformProvider:
    # if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
    # if config.cloud_instance_config.cloud_instance_provider is CloudInstanceProvider.MULTIPASS:
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
            # token=config.DO_TOKEN,
            # token=config.cloud_instance_config.DO_TOKEN,
            # token=config.variables.get("do_token"),
            token=config.secrets.get_secret_value().get("do_token"),
        )

    else:
        raise ValueError(
            f'Unknown cloud_instance_provider: {config.variables.get("cloud_instance_provider")}'
        )

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
        cloud_instance_resource = DigitaloceanDropletTerraformResource(
            id_="cloud_instance_resource",
            image=config.variables.get("do_droplet_image"),
            name=config.variables.get("cloud_instance_name"),
            provider=cloud_instance_provider,
            region=config.variables.get("do_droplet_region"),
            scope=scope,
            size=config.variables.get("do_droplet_size"),
            user_data=cloud_init_config_construct.outputs["user_data"].value,
        )

    else:
        raise ValueError(
            f'Unknown cloud_instance_provider: {config.variables.get("cloud_instance_provider")}'
        )

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
        raise ValueError(
            f'Unknown cloud_instance_provider: {config.variables.get("cloud_instance_provider")}'
        )

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
        raise ValueError(
            f'Unknown cloud_instance_provider: {config.variables.get("cloud_instance_provider")}'
        )

    return cloud_instance_outputs
