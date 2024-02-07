from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.kubernetes_config.argo_cd.construct import (
    ArgoCDConstruct,
)
from timestep.infra.stacks.kubernetes_config.container_registry.construct import (
    ContainerRegistryConstruct,
)
from timestep.infra.stacks.kubernetes_config.kube_prometheus_stack.construct import (
    KubePrometheusStackConstruct,
)
from timestep.infra.stacks.kubernetes_config.kubeapps.construct import (
    KubeappsConstruct,
)
from timestep.infra.stacks.kubernetes_config.kubernetes_cluster_ingress.construct import (  # noqa: E501
    KubernetesClusterIngressConstruct,
)
from timestep.infra.stacks.kubernetes_config.kubernetes_dashboard.construct import (
    KubernetesDashboardConstruct,
)
from timestep.infra.stacks.kubernetes_config.minio.construct import MinioConstruct
from timestep.infra.stacks.kubernetes_config.postgresql.construct import (
    PostgreSQLConstruct,
)
from timestep.infra.stacks.kubernetes_config.prefect.construct import PrefectConstruct
from timestep.infra.stacks.kubernetes_config.sealed_secrets.construct import (
    SealedSecretsConstruct,
)
from timestep.infra.stacks.kubernetes_config.stalwart.construct import StalwartConstruct


class KubernetesConfigStack(TerraformStack):
    id: str

    def __init__(self, scope: Construct, id: str, config: Settings, kube_config=None):
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

        self.argo_cd_contruct: ArgoCDConstruct = ArgoCDConstruct(
            config=config,
            id="argo_cd_contruct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        self.container_registry_contruct: ContainerRegistryConstruct = (
            ContainerRegistryConstruct(
                config=config,
                id="container_registry_contruct",
                helm_provider=self.helm_provider,
                scope=self,
            )
        )

        if config.kube_prometheus_stack_is_enabled:
            self.kube_prometheus_stack_contruct: KubePrometheusStackConstruct = (
                KubePrometheusStackConstruct(
                    config=config,
                    id="kube_prometheus_stack_contruct",
                    helm_provider=self.helm_provider,
                    scope=self,
                )
            )

        if config.kubeapps_is_enabled:
            self.kubeapps_contruct: KubeappsConstruct = KubeappsConstruct(
                config=config,
                id="kubeapps_contruct",
                helm_provider=self.helm_provider,
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

        self.kubernetes_dashboard_contruct: KubernetesDashboardConstruct = (
            KubernetesDashboardConstruct(
                config=config,
                id="kubernetes_dashboard_construct",
                helm_provider=self.helm_provider,
                scope=self,
            )
        )

        self.minio_construct: MinioConstruct = MinioConstruct(
            config=config,
            id="minio_construct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        self.postgresql_construct: PostgreSQLConstruct = PostgreSQLConstruct(
            config=config,
            id="postgresql_construct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        self.prefect_construct: PrefectConstruct = PrefectConstruct(
            config=config,
            id="prefect_construct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        if config.sealed_secrets_is_enabled:
            self.sealed_secrets_construct: SealedSecretsConstruct = (
                SealedSecretsConstruct(
                    config=config,
                    id="sealed_secrets_construct",
                    helm_provider=self.helm_provider,
                    scope=self,
                )
            )

        if config.stalwart_is_enabled:
            self.stalwart_construct: StalwartConstruct(
                config=config,
                id="stalwart_construct",
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
