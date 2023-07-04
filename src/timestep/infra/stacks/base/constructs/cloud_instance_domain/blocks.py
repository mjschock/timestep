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
        get_run_logger()

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
