from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
from cdktf_cdktf_provider_kubernetes.cluster_role_binding_v1 import (
    ClusterRoleBindingV1,
    ClusterRoleBindingV1Metadata,
    ClusterRoleBindingV1RoleRef,
    ClusterRoleBindingV1Subject,
)
from cdktf_cdktf_provider_kubernetes.secret_v1 import (
    SecretV1,
    SecretV1Metadata,
)
from cdktf_cdktf_provider_kubernetes.service_account_v1 import (
    ServiceAccountV1,
    ServiceAccountV1Metadata,
)
from constructs import Construct

from timestep.config import Settings


class KubernetesDashboardConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.kubernetes_dashboard_helm_release_resource = Release(
            id_="kubernetes_dashboard_helm_release_resource",
            atomic=True,
            chart="kubernetes-dashboard",
            create_namespace=True,
            name="kubernetes-dashboard",
            namespace="kubernetes-dashboard",
            repository="https://kubernetes.github.io/dashboard",
            provider=helm_provider,
            scope=self,
            set=[
                ReleaseSet(
                    name="app.ingress.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="cert-manager.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="nginx.enabled",
                    value="false",
                ),
            ],
            version="7.5.0",
        )

        self.kubernetes_dashboard_admin_user_service_account = ServiceAccountV1(
            depends_on=[self.kubernetes_dashboard_helm_release_resource],
            id_="kubernetes_dashboard_admin_user_service_account",
            metadata=ServiceAccountV1Metadata(
                name="admin-user",
                namespace="kubernetes-dashboard",
            ),
            scope=self,
        )

        self.kubernetes_dashboard_cluster_role_binding = ClusterRoleBindingV1(
            depends_on=[self.kubernetes_dashboard_admin_user_service_account],
            id_="kubernetes_dashboard_cluster_role_binding",
            metadata=ClusterRoleBindingV1Metadata(
                name="admin-user",
            ),
            role_ref=ClusterRoleBindingV1RoleRef(
                kind="ClusterRole",
                name="cluster-admin",
                api_group="rbac.authorization.k8s.io",
            ),
            subject=[
                ClusterRoleBindingV1Subject(
                    kind="ServiceAccount",
                    name=self.kubernetes_dashboard_admin_user_service_account.metadata.name,
                    namespace=self.kubernetes_dashboard_admin_user_service_account.metadata.namespace,
                )
            ],
            scope=self,
        )

        self.kubernetes_dashboard_admin_user_secret = SecretV1(
            depends_on=[self.kubernetes_dashboard_admin_user_service_account],
            id_="kubernetes_dashboard_admin_user_secret",
            metadata=SecretV1Metadata(
                annotations={
                    "kubernetes.io/service-account.name": "admin-user",
                },
                name=self.kubernetes_dashboard_admin_user_service_account.metadata.name,
                namespace=self.kubernetes_dashboard_admin_user_service_account.metadata.namespace,
            ),
            type="kubernetes.io/service-account-token",
            scope=self,
        )
