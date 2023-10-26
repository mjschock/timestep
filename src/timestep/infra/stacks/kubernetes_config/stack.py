from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
from cdktf_cdktf_provider_kubernetes.manifest import Manifest
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.kubernetes_config.constructs.argo_cd.construct import (
    ArgoCDConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.kubeapps.construct import (
    KubeappsConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.kubernetes_cluster_ingress.construct import (  # noqa: E501
    KubernetesClusterIngressConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.sealed_secrets.construct import (  # noqa: E501
    SealedSecretsConstruct,
)


class KubernetesConfigStack(TerraformStack):
    id: str

    def __init__(
        self, scope: Construct, id: str, config: Settings, kube_config=None
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

        self.argo_cd_contruct: ArgoCDConstruct = ArgoCDConstruct(
            config=config,
            id="argo_cd_contruct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        # self.flux_construct: FluxConstruct = FluxConstruct(
        #     config=config,
        #     id="flux_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

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

        # self.kubernetes_dashboard_contruct: KubernetesDashboardConstruct = (
        #     KubernetesDashboardConstruct(
        #         config=config,
        #         id="kubernetes_dashboard_construct",
        #         helm_provider=self.helm_provider,
        #         scope=self,
        #     )
        # )

        # self.minio_construct: MinioConstruct = MinioConstruct(
        #     config=config,
        #     id="minio_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

        # self.postgresql_construct: PostgreSQLConstruct = PostgreSQLConstruct(
        #     config=config,
        #     id="postgresql_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

        # self.prefect_construct: PrefectConstruct = PrefectConstruct(
        #     config=config,
        #     id="prefect_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

        # self.registry_construct: RegistryConstruct = RegistryConstruct(
        #     config=config,
        #     id="registry_construct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

        self.sealed_secrets_construct: SealedSecretsConstruct = SealedSecretsConstruct(
            config=config,
            id="sealed_secrets_construct",
            helm_provider=self.helm_provider,
            scope=self,
        )

        # apiVersion: v1
        # kind: Secret
        # metadata:
        #   name: private-repo
        #   namespace: default
        #   labels:
        #     argocd.argoproj.io/secret-type: repository
        # stringData:
        #   type: git
        #   url: https://github.com/mjschock/timestep.git
        #   password: mjschock
        #   username: my-username

        SecretV1(
            id_="private_repo_secret",
            data={
                "password": config.github_api_token.get_secret_value(),
                "project": "default",
                "url": "https://github.com/mjschock/timestep.git",
                "username": "mjschock",
                "type": "git",
            },
            metadata=SecretV1Metadata(
                labels={
                    "argocd.argoproj.io/secret-type": "repository",
                },
                name="private-repo",
                namespace="default",
            ),
            scope=self,
        )

        # Manifest(
        #     id="private_repo_manifest",
        #     manifest={
        #         "apiVersion": "bitnami.com/v1alpha1",
        #         "kind": "SealedSecret",
        #         "metadata": {
        #             "name": "private-repo",
        #             "namespace": "default",
        #         },
        #         "spec": {
        #             "encryptedData": {
        #                 "password": config.github_api_token.get_secret_value(),
        #                 "project": "default",
        #                 "url": "https://github.com/mjschock/timestep.git",
        #                 "username": "mjschock",
        #                 "type": "git",
        #             },
        #             "template": {
        #                 "metadata": {
        #                     "labels": {
        #                         "argocd.argoproj.io/secret-type": "repository",
        #                     }
        #                 }
        #             },
        #         },
        #     },
        #     scope=self,
        # )

        Manifest(
            id="timestep_ai_manifest",
            manifest={
                "apiVersion": "argoproj.io/v1alpha1",
                "kind": "Application",
                "metadata": {
                    "name": "timestep-ai",
                    "namespace": "default",
                },
                "spec": {
                    "destination": {
                        "namespace": "default",
                        "server": "https://kubernetes.default.svc",
                    },
                    "project": "default",
                    "source": {
                        "path": "timestep-ai",
                        "repoURL": "https://github.com/mjschock/timestep.git",
                        "targetRevision": "HEAD",
                    },
                    "syncPolicy": {
                        "automated": {
                            "prune": True,
                            "selfHeal": True,
                        },
                        "syncOptions": ["CreateNamespace=true"],
                    },
                },
            },
            scope=self,
        )

        # self.timestep_ai_contruct: TimestepAIConstruct = TimestepAIConstruct(
        #     config=config,
        #     id="timestep_ai_contruct",
        #     helm_provider=self.helm_provider,
        #     scope=self,
        # )

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
