import os
from typing import Dict

from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
)
from cloud_init_gen import CloudInitDoc
from constructs import Construct
from prefect import get_run_logger, task
from prefect.futures import PrefectFuture
from prefect_shell import ShellOperation

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.cloudinit.data_cloudinit_config import (
    DataCloudinitConfig,
    DataCloudinitConfigPart,
)
from timestep.infra.imports.cloudinit.provider import CloudinitProvider
from timestep.infra.imports.local.data_local_file import DataLocalFile
from timestep.infra.imports.local.file import File
from timestep.infra.imports.local.provider import LocalProvider
from timestep.infra.imports.null.data_null_data_source import DataNullDataSource
from timestep.infra.imports.null.provider import NullProvider
from timestep.infra.imports.null.resource import Resource
from timestep.infra.stacks.base.constructs.cloud_init_config.tasks import (
    get_cloud_init_config_data_source,
    get_cloud_init_config_outputs,
    get_cloud_init_config_provider,
    get_cloud_init_config_resource,
)


class CloudInitConfigConstruct(Construct):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        self.cloud_init_config_provider_future: PrefectFuture[
            TerraformProvider
        ] = get_cloud_init_config_provider.submit(scope=scope, config=config)
        self.cloud_init_config_resource_future: PrefectFuture[
            TerraformResource
        ] = get_cloud_init_config_resource.submit(
            scope=scope,
            config=config,
            cloud_init_config_provider=self.cloud_init_config_provider_future,
        )
        self.cloud_init_config_data_source_future: PrefectFuture[
            TerraformDataSource
        ] = get_cloud_init_config_data_source.submit(
            scope=scope,
            config=config,
            cloud_init_config_resource=self.cloud_init_config_resource_future,
        )
        # self.cloud_init_config_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_init_config_data_source.submit(scope=scope, config=config, cloud_init_config_provider=self.cloud_init_config_provider_future)
        self.cloud_init_config_outputs_future: PrefectFuture[
            Dict[str, TerraformOutput]
        ] = get_cloud_init_config_outputs.submit(
            scope=scope,
            config=config,
            cloud_init_config_data_source=self.cloud_init_config_data_source_future,
        )

        self.provider = self.cloud_init_config_provider_future.result()
        self.resource = self.cloud_init_config_resource_future.result()
        self.data_source = self.cloud_init_config_data_source_future.result()
        self.outputs = self.cloud_init_config_outputs_future.result()
