from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
from constructs import Construct

from timestep.config import CloudInstanceProvider
from timestep.infra.stacks.kubernetes_config.constructs.kubernetes_cluster_ingress.construct import (  # noqa: E501
    KubernetesClusterIngressConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.minio.construct import (
    MinioConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.prefect.construct import (
    PrefectConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.timestep_ai.construct import (
    TimestepAIConstruct,
)


class KubernetesConfigStack(TerraformStack):
    id: str = None

    def __init__(
        self, scope: Construct, id: str, config: dict[str, str], kube_config=None
    ):  # noqa: E501
        super().__init__(scope, id)
        self.id = id

        self.kubernetes_provider = KubernetesProvider(
            id="kubernetes_provider",
            config_context=config.kubecontext,
            config_path=f"{config.base_path}/secrets/kubeconfig",
            scope=self,
        )

        self.helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                config_context=self.kubernetes_provider.config_context,
                config_path=self.kubernetes_provider.config_path,
            ),
            scope=self,
        )

        self.kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct = (
            KubernetesClusterIngressConstruct(
                config=config,
                id="kubernetes_cluster_ingress_construct",
                helm_provider=self.helm_provider,
                scope=self,
            )
        )

        # self.kubernetes_dashboard_contruct: KubernetesDashboardConstruct = (
        #     KubernetesDashboardConstruct(
        #         config=config,
        #         id="kubernetes_dashboard_construct",
        #         helm_provider=self.helm_provider,
        #         scope=self,
        #     )
        # )

        self.minio_construct: MinioConstruct = MinioConstruct(
            config=config,
            id="minio_construct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        # self.postgresql_construct: PostgreSQLConstruct = PostgreSQLConstruct(
        #     config=config,
        #     id="postgresql_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

        self.prefect_construct: PrefectConstruct = PrefectConstruct(
            config=config,
            id="prefect_construct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        # self.registry_construct: RegistryConstruct = RegistryConstruct(
        #     config=config,
        #     id="registry_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

        self.timestep_ai_contruct: TimestepAIConstruct = TimestepAIConstruct(
            config=config,
            id="timestep_ai_contruct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            LocalBackend(
                path=f"{config.dist_path}/terraform.{self.id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            HttpBackend(
                address=f"{config.tf_http_address}/{self.id}",
                lock_address=f"{config.tf_http_address}/{self.id}/lock",
                lock_method="POST",
                password=config.tf_api_token.get_secret_value(),
                retry_wait_min=5,
                scope=self,
                unlock_address=f"{config.tf_http_address}/{self.id}/lock",
                unlock_method="DELETE",
                username=config.tf_username,
            )
