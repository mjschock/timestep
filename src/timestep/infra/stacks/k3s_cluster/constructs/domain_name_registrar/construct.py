from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
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

        # self.domain_name_registrar_provider_future: PrefectFuture[
        #     TerraformProvider
        # ] = get_domain_name_registrar_provider.submit(
        #     scope=scope,
        #     config=config,
        #     cloud_instance_construct=cloud_instance_construct,
        # )
        # self.domain_name_registrar_resource_future: PrefectFuture[
        #     TerraformResource
        # ] = get_domain_name_registrar_resource.submit(
        #     scope=scope,
        #     config=config,
        #     cloud_instance_construct=cloud_instance_construct,
        #     domain_name_registrar_provider=self.domain_name_registrar_provider_future,
        # )

        # self.provider = self.domain_name_registrar_provider_future.result()
        # self.resource = self.domain_name_registrar_resource_future.result()

        NullTerraformProvider(
            alias="domain_name_registrar_provider",
            id="domain_name_registrar_provider",
            scope=scope,
        )
