from typing import Dict

from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
)
from constructs import Construct
from prefect import get_run_logger
from prefect.futures import PrefectFuture

from timestep.conf.blocks import AppConfig
from timestep.infra.stacks.base.constructs.cloud_init_config.blocks import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.base.constructs.cloud_instance.tasks import (
    get_cloud_instance_data_source,
    get_cloud_instance_outputs,
    get_cloud_instance_provider,
    get_cloud_instance_resource,
)


class CloudInstanceConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: AppConfig,
        cloud_init_config_construct: CloudInitConfigConstruct,
    ) -> None:
        super().__init__(scope, id)
        get_run_logger()

        self.cloud_instance_provider_future: PrefectFuture[
            TerraformProvider
        ] = get_cloud_instance_provider.submit(
            scope=scope,
            config=config,
            cloud_init_config_construct=cloud_init_config_construct,
        )
        self.cloud_instance_resource_future: PrefectFuture[
            TerraformResource
        ] = get_cloud_instance_resource.submit(
            scope=scope,
            config=config,
            cloud_init_config_construct=cloud_init_config_construct,
            cloud_instance_provider=self.cloud_instance_provider_future,
        )
        self.cloud_instance_data_source_future: PrefectFuture[
            TerraformDataSource
        ] = get_cloud_instance_data_source.submit(
            scope=scope,
            config=config,
            cloud_init_config_construct=cloud_init_config_construct,
            cloud_instance_resource=self.cloud_instance_resource_future,
        )
        self.cloud_instance_outputs_future: PrefectFuture[
            Dict[str, TerraformOutput]
        ] = get_cloud_instance_outputs.submit(
            scope=scope,
            config=config,
            cloud_init_config_construct=cloud_init_config_construct,
            cloud_instance_data_source=self.cloud_instance_data_source_future,
        )

        self.provider = self.cloud_instance_provider_future.result()
        self.resource = self.cloud_instance_resource_future.result()
        self.data_source = self.cloud_instance_data_source_future.result()
        self.outputs = self.cloud_instance_outputs_future.result()
