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


@task
def get_cloud_instance_provider(scope: TerraformStack, config: MainConfig, cloud_init_config_construct: CloudInitConfigConstruct) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_provider = MultipassTerraformProvider(
            id="cloud_instance_provider",
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_provider = DigitaloceanTerraformProvider(
            id="cloud_instance_provider",
            scope=scope,
            token=config.DO_TOKEN,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_provider


@task
def get_cloud_instance_resource(scope: TerraformStack, config: MainConfig, cloud_init_config_construct: CloudInitConfigConstruct, cloud_instance_provider: TerraformProvider) -> TerraformResource:
    # cloud_init_config_data_source: TerraformDataSource = cloud_init_config_construct.cloud_init_config_data_source_future.result()

    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_resource = MultipassInstanceTerraformResource(
            # cloudinit_file=cloud_init_config_local_file_data_source.filename,
            # cloudinit_file=cloud_init_config_data_source.filename,
            cloudinit_file=cloud_init_config_construct.outputs["cloudinit_file"].value,
            cpus=config.MULTIPASS_INSTANCE_CPUS,
            disk=config.MULTIPASS_INSTANCE_DISK,
            id="cloud_instance_resource",
            image=config.MULTIPASS_INSTANCE_IMAGE,
            name=config.CLOUD_INSTANCE_NAME,
            provider=cloud_instance_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_resource = DigitaloceanDropletTerraformResource(
            id_="cloud_instance_resource",
            image=config.DO_DROPLET_IMAGE,
            name=config.CLOUD_INSTANCE_NAME,
            provider=cloud_instance_provider,
            region=config.DO_DROPLET_REGION,
            scope=scope,
            size=config.DO_DROPLET_SIZE,
            # user_data=cloud_init_config.render(),
            # user_data=cloud_init_config_construct.outputs["user_data"].value,
            user_data=cloud_init_config_construct.outputs["cloudinit_file"].value,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_resource


@task
def get_cloud_instance_data_source(scope: TerraformStack, config: MainConfig, cloud_init_config_construct: CloudInitConfigConstruct, cloud_instance_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_data_source = MultipassInstanceTerraformDataSource(
            id="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_resource.provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_data_source = DigitaloceanDropletTerraformDataSource(
            id_="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_resource.provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_data_source


# @task
# def get_cloud_instance_ipv4_output(scope: TerraformStack, config: MainConfig, cloud_init_config_construct: CloudInitConfigConstruct, cloud_instance_data_source: TerraformDataSource) -> TerraformOutput:
#     if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
#         cloud_instance_ipv4_output = TerraformOutput(
#             id="cloud_instance_ipv4_output",
#             value=cloud_instance_data_source.ipv4,
#             scope=scope,
#         )

#     elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
#         cloud_instance_ipv4_output = TerraformOutput(
#             id="cloud_instance_ipv4_output",
#             value=cloud_instance_data_source.ipv4_address,
#             scope=scope,
#         )

#     else:
#         raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

#     return cloud_instance_ipv4_output


# @task
# def get_cloud_instance_zone_file_output(scope: TerraformStack, config: MainConfig, cloud_instance_domain_data_source: TerraformDataSource) -> TerraformOutput:
#     if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
#         cloud_instance_zone_file_output = TerraformOutput(
#             id="cloud_instance_zone_file_output",
#             value=cloud_instance_domain_data_source.filename,
#             scope=scope,
#         )

#     elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
#         cloud_instance_zone_file_output = TerraformOutput(
#             id="cloud_instance_zone_file_output",
#             value=cloud_instance_domain_data_source.zone_file,
#             scope=scope,
#         )

#     else:
#         raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

#     return cloud_instance_zone_file_output

@task
def get_cloud_instance_outputs(scope: TerraformStack, config: MainConfig, cloud_init_config_construct: CloudInitConfigConstruct, cloud_instance_data_source: TerraformDataSource) -> Dict[str, TerraformOutput]:
    cloud_instance_outputs = {}

    if config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_outputs["ipv4"] = TerraformOutput(
            id="cloud_instance_outputs_ipv4",
            value=cloud_instance_data_source.ipv4,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == MainConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_outputs["ipv4"] = TerraformOutput(
            id="cloud_instance_outputs_ipv4",
            value=cloud_instance_data_source.ipv4_address,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_outputs


class CloudInstanceConstruct(Construct):
    def __init__(
        self, scope: Construct, id: str, config: MainConfig, cloud_init_config_construct: CloudInitConfigConstruct
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()
        # logger.info(f"config: {config}")

        self.cloud_instance_provider_future: PrefectFuture[TerraformProvider] = get_cloud_instance_provider.submit(scope=scope, config=config, cloud_init_config_construct=cloud_init_config_construct)
        self.cloud_instance_resource_future: PrefectFuture[TerraformResource] = get_cloud_instance_resource.submit(scope=scope, config=config, cloud_init_config_construct=cloud_init_config_construct, cloud_instance_provider=self.cloud_instance_provider_future)
        self.cloud_instance_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_instance_data_source.submit(scope=scope, config=config, cloud_init_config_construct=cloud_init_config_construct, cloud_instance_resource=self.cloud_instance_resource_future)
        self.cloud_instance_outputs_future: PrefectFuture[Dict[str, TerraformOutput]] = get_cloud_instance_outputs.submit(scope=scope, config=config, cloud_init_config_construct=cloud_init_config_construct, cloud_instance_data_source=self.cloud_instance_data_source_future)

        # self.cloud_instance_output_futures: Dict[str, PrefectFuture[TerraformOutput]] = {
        #     "ipv4": get_cloud_instance_ipv4_output.submit(scope=scope, config=config, cloud_init_config_construct=cloud_init_config_construct, cloud_instance_data_source=self.cloud_instance_data_source_future),
        # }

        self.provider = self.cloud_instance_provider_future.result()
        self.resource = self.cloud_instance_resource_future.result()
        self.data_source = self.cloud_instance_data_source_future.result()
        self.outputs = self.cloud_instance_outputs_future.result()
