from cdktf import (
    CloudBackend,
    LocalBackend,
    NamedCloudWorkspace,
    TerraformStack,
)
from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.stacks.k3s_cluster.constructs.cloud_init_config.blocks import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance_domain.blocks import (
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.k3s_cluster.constructs.domain_name_registrar.construct import (  # noqa: E501
    DomainNameRegistrarConstruct,
)


class K3sClusterStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)
        get_run_logger()

        self.cloud_init_config_construct = CloudInitConfigConstruct(
            config=config,
            id="cloud_init_config_construct",
            scope=self,
        )

        self.cloud_instance_construct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct = CloudInstanceDomainConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="cloud_instance_domain_construct",
            scope=self,
        )

        self.domain_name_registar_construct = DomainNameRegistrarConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="domain_name_registar_construct",
            scope=self,
        )

        # self.kube_config_construct = KubeConfigConstruct(
        #     cloud_instance_construct=self.cloud_instance_construct,
        #     config=config,
        #     id="kube_config_construct",
        #     scope=self,
        # )

        # self.container_registry_construct = ContainerRegistryConstruct(
        #     config=config,
        #     id="container_registry_construct",
        #     scope=self,
        # )

        # self.ingress_controller_construct = IngressControllerConstruct(
        #     # container_registry_construct=self.container_registry_construct,
        #     config=config,
        #     kube_config_construct=self.kube_config_construct,
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

        stack_id: str = config.variables.get("primary_domain_name")

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
        ):
            LocalBackend(
                path=f"terraform.{stack_id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            CloudBackend(
                hostname=config.variables.get("tf_hostname"),
                organization=config.variables.get("tf_organization"),
                scope=self,
                token=config.secrets.get_secret_value().get("tf_api_token"),
                workspaces=NamedCloudWorkspace(config.variables.get("tf_workspace")),
            )
