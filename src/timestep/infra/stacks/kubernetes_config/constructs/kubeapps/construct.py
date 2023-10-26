from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release
from cdktf_cdktf_provider_kubernetes.cluster_role_binding_v1 import (
    ClusterRoleBindingV1,
    ClusterRoleBindingV1Metadata,
    ClusterRoleBindingV1RoleRef,
    ClusterRoleBindingV1Subject,
)
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from cdktf_cdktf_provider_kubernetes.service_account_v1 import (
    ServiceAccountV1,
    ServiceAccountV1Metadata,
)
from constructs import Construct
from timestep.config import Settings


class KubeappsConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.kubeapps_helm_release_resource = Release(
            id_="kubeapps_helm_release_resource",
            atomic=True,
            chart="kubeapps",
            create_namespace=True,
            name="kubeapps",
            namespace="kubeapps",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            scope=self,
        )

        self.kubeapps_operator_service_account_resource = ServiceAccountV1(
            id_="kubeapps_operator_service_account_resource",
            metadata=ServiceAccountV1Metadata(
                name="kubeapps-operator",
                namespace="default",
            ),
            scope=self,
        )

        # self.cluster_admin_cluster_role_resource = ClusterRoleV1(
        #     id_="cluster_admin_cluster_role_resource",
        #     metadata=ClusterRoleV1Metadata(
        #         name="cluster-admin",
        #     ),
        #     rule=[
        #         ClusterRoleV1Rule(
        #             api_groups=[""],
        #             resources=["nodes"],
        #             verbs=["list"],
        #         )
        #     ],
        #     scope=self,
        # )

        self.kubeapps_operator_cluster_role_binding_resource = ClusterRoleBindingV1(
            id_="kubeapps_operator_cluster_role_binding_resource",
            metadata=ClusterRoleBindingV1Metadata(
                name="kubeapps-operator",
            ),
            subject=[
                ClusterRoleBindingV1Subject(
                    # api_group="",
                    # api_group
                    kind="ServiceAccount",
                    # kind=self.kubeapps_operator_service_account_resource.kind,
                    # name="kubeapps-operator",
                    name=self.kubeapps_operator_service_account_resource.metadata.name,
                    # namespace="default",
                    namespace=self.kubeapps_operator_service_account_resource.metadata.namespace,
                )
            ],
            role_ref=ClusterRoleBindingV1RoleRef(
                # name=self.cluster_admin_cluster_role_resource.metadata.name,
                api_group="rbac.authorization.k8s.io",
                kind="ClusterRole",
                name="cluster-admin",
            ),
            scope=self,
        )

        self.kubeapps_operator_token_secret_resource = SecretV1(
            id_="kubeapps_operator_token_secret_resource",
            metadata=SecretV1Metadata(
                name="kubeapps-operator-token",
                namespace="default",
                annotations={
                    "kubernetes.io/service-account.name": "kubeapps-operator",
                },
            ),
            scope=self,
            type="kubernetes.io/service-account-token",
        )
