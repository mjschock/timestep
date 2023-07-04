from cdktf import (
    TerraformStack,
)
from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig


class KubernetesConfigStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)
        get_run_logger()

        # self.container_registry_construct = ContainerRegistryConstruct(
        #     config=config,
        #     id="container_registry_construct",
        #     scope=self,
        # )

        # self.ingress_controller_construct = IngressControllerConstruct(
        #     container_registry_construct=self.container_registry_construct,
        #     config=config,
        #     id="ingress_controller_construct",
        #     scope=self,
        # )

        # self.minio_construct = MinioConstruct(
        #     ingress_controller_construct=self.ingress_controller_construct,
        #     config=config,
        #     id="minio_construct",
        #     scope=self,
        # )

        # self.postgres_construct = PostgresConstruct(
        #     ingress_controller_construct=self.ingress_controller_construct,
        #     config=config,
        #     id="postgres_construct",
        #     scope=self,
        # )

        # self.telemetry_construct = TelemetryConstruct(
        #     ingress_controller_construct=self.ingress_controller_construct,
        #     config=config,
        #     id="telemetry_construct",
        #     scope=self,
        # )
