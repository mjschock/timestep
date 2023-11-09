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
            scope=self,
        )

        # default_sa_cluster_role = ClusterRoleV1(
        #     id_="default_sa_cluster_role",
        #     metadata=ClusterRoleV1Metadata(
        #         generate_name="default-sa-cluster-role-",
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

        ServiceAccountV1(
            id_="admin_user_sa",
            metadata=ServiceAccountV1Metadata(
                name="admin-user",
                namespace="kubernetes-dashboard",
            ),
            scope=self,
        )

        ClusterRoleBindingV1(
            id_="kubernetes_dashboard_cluster_role_binding",
            metadata=ClusterRoleBindingV1Metadata(
                # name="kubernetes-dashboard",
                name="admin-user",
                # namespace="kubernetes-dashboard",
            ),
            role_ref=ClusterRoleBindingV1RoleRef(
                kind="ClusterRole",
                name="cluster-admin",
                api_group="rbac.authorization.k8s.io",
            ),
            subject=[
                ClusterRoleBindingV1Subject(
                    kind="ServiceAccount",
                    name="admin-user",
                    namespace="kubernetes-dashboard",
                    # api_group="",
                )
            ],
            scope=self,
        )

        SecretV1(
            id_="kubernetes_dashboard_secret",
            metadata=SecretV1Metadata(
                annotations={
                    "kubernetes.io/service-account.name": "admin-user",
                },
                name="admin-user",
                namespace="kubernetes-dashboard",
            ),
            type="kubernetes.io/service-account-token",
            scope=self,
        )

        # IngressV1(
        #     depends_on=[
        #         self.kubernetes_dashboard_helm_release_resource,
        #     ],
        #     id_="kubernetes_dashboard_ingress",
        #     metadata=IngressV1Metadata(
        #         annotations={
        #             "kubernetes.io/ingress.class": "caddy",
        #         },
        #         name="kubernetes-dashboard",
        #         namespace="kubernetes-dashboard",
        #     ),
        #     scope=self,
        #     spec=IngressV1Spec(
        #         rule=[
        #             IngressV1SpecRule(
        #                 host=f"kubernetes-dashboard.{config.primary_domain_name}",
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="kubernetes-dashboard",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         number=443,  # https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard#networkpolicy
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         ),
        #                     ]
        #                 ),
        #             ),
        #         ],
        #     ),
        # )
