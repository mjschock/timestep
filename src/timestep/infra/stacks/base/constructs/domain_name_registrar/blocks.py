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
from timestep.infra.stacks.base.constructs.domain_name_registrar.tasks import (
    get_domain_name_registrar_data_source,
    get_domain_name_registrar_outputs,
    get_domain_name_registrar_provider,
    get_domain_name_registrar_resource,
)


class DomainNameRegistrarConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: AppConfig,
        cloud_instance_construct: CloudInstanceConstruct,
    ) -> None:
        super().__init__(scope, id)
        get_run_logger()

        self.domain_name_registrar_provider_future: PrefectFuture[
            TerraformProvider
        ] = get_domain_name_registrar_provider.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
        )
        self.domain_name_registrar_resource_future: PrefectFuture[
            TerraformResource
        ] = get_domain_name_registrar_resource.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            domain_name_registrar_provider=self.domain_name_registrar_provider_future,
        )
        self.domain_name_registrar_data_source_future: PrefectFuture[
            TerraformDataSource
        ] = get_domain_name_registrar_data_source.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            domain_name_registrar_resource=self.domain_name_registrar_resource_future,
        )
        self.domain_name_registrar_outputs_future: PrefectFuture[
            Dict[str, TerraformOutput]
        ] = get_domain_name_registrar_outputs.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            domain_name_registrar_data_source=self.domain_name_registrar_data_source_future,
        )

        self.provider = self.domain_name_registrar_provider_future.result()
        self.resource = self.domain_name_registrar_resource_future.result()
        self.data_source = self.domain_name_registrar_data_source_future.result()
        self.outputs = self.domain_name_registrar_outputs_future.result()
