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
from timestep.infra.stacks.base.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.base.constructs.cloud_instance_domain.tasks import (
    get_cloud_instance_domain_data_source,
    get_cloud_instance_domain_outputs,
    get_cloud_instance_domain_provider,
    get_cloud_instance_domain_resource,
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
        logger = get_run_logger()

        self.cloud_instance_domain_provider_future: PrefectFuture[
            TerraformProvider
        ] = get_cloud_instance_domain_provider.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
        )
        self.cloud_instance_domain_resource_future: PrefectFuture[
            TerraformResource
        ] = get_cloud_instance_domain_resource.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            cloud_instance_domain_provider=self.cloud_instance_domain_provider_future,
        )
        self.cloud_instance_domain_data_source_future: PrefectFuture[
            TerraformDataSource
        ] = get_cloud_instance_domain_data_source.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            cloud_instance_domain_resource=self.cloud_instance_domain_resource_future,
        )
        self.cloud_instance_domain_outputs_future: PrefectFuture[
            Dict[str, TerraformOutput]
        ] = get_cloud_instance_domain_outputs.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            cloud_instance_domain_data_source=self.cloud_instance_domain_data_source_future,
        )

        self.provider = self.cloud_instance_domain_provider_future.result()
        self.resource = self.cloud_instance_domain_resource_future.result()
        self.data_source = self.cloud_instance_domain_data_source_future.result()
        self.outputs = self.cloud_instance_domain_outputs_future.result()
