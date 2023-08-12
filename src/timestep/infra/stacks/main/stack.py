from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from constructs import Construct

from timestep.config import CloudInstanceProvider
from timestep.infra.stacks.main.constructs.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.main.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.main.constructs.cloud_instance_domain.construct import (
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.main.constructs.domain_name_registrar.construct import (
    DomainNameRegistrarConstruct,
)
from timestep.infra.stacks.main.constructs.kube_config.construct import (
    KubeConfigConstruct,
)
from timestep.infra.stacks.main.constructs.kubernetes_cluster_ingress.construct import (
    KubernetesClusterIngressConstruct,
)


class MainStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: dict[str, str]) -> None:
        super().__init__(scope, id)

        self.cloud_init_config_construct: CloudInitConfigConstruct = (
            CloudInitConfigConstruct(
                config=config,
                id="cloud_init_config_construct",
                scope=self,
            )
        )

        self.cloud_instance_construct: CloudInstanceConstruct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct: CloudInstanceDomainConstruct = (
            CloudInstanceDomainConstruct(
                cloud_instance_construct=self.cloud_instance_construct,
                config=config,
                id="cloud_instance_domain_construct",
                scope=self,
            )
        )

        self.domain_name_registar_construct: DomainNameRegistrarConstruct = (
            DomainNameRegistrarConstruct(
                config=config,
                id="domain_name_registar_construct",
                scope=self,
            )
        )

        self.kube_config_contruct: KubeConfigConstruct = KubeConfigConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="kube_config_contruct",
            scope=self,
        )

        self.kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct = (
            KubernetesClusterIngressConstruct(
                cloud_instance_construct=self.cloud_instance_construct,
                config=config,
                id="kubernetes_cluster_ingress_construct",
                kube_config_contruct=self.kube_config_contruct,
                scope=self,
            )
        )

        # self.timestep_ai_contruct: TimestepAIConstruct = TimestepAIConstruct(
        #     config=config,
        #     id="timestep_ai_contruct",
        #     kubernetes_cluster_ingress_construct=self.kubernetes_cluster_ingress_construct,  # noqa: E501
        #     scope=self,
        # )

        stack_id = config.primary_domain_name

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            LocalBackend(
                path=f"terraform.{stack_id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            print(f"Using {config.cloud_instance_provider} backend...")
            print(f"config.tf_http_address: {config.tf_http_address}")
            print(f"config.tf_api_token: {config.tf_api_token}")
            print(f"config.tf_username: {config.tf_username}")

            HttpBackend(
                address=config.tf_http_address,
                password=config.tf_api_token.get_secret_value(),
                scope=self,
                username=config.tf_username,
            )
