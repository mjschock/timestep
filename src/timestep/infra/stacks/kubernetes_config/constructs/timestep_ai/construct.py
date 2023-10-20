from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
from cdktf_cdktf_provider_kubernetes.cluster_role_binding_v1 import (
    ClusterRoleBindingV1,
    ClusterRoleBindingV1Metadata,
    ClusterRoleBindingV1RoleRef,
    ClusterRoleBindingV1Subject,
)
from cdktf_cdktf_provider_kubernetes.cluster_role_v1 import (
    ClusterRoleV1,
    ClusterRoleV1Metadata,
    ClusterRoleV1Rule,
)
from cdktf_cdktf_provider_kubernetes.role_binding_v1 import (
    RoleBindingV1,
    RoleBindingV1Metadata,
    RoleBindingV1RoleRef,
    RoleBindingV1Subject,
)
from cdktf_cdktf_provider_kubernetes.role_v1 import (
    RoleV1,
    RoleV1Metadata,
    RoleV1Rule,
)
from constructs import Construct
from timestep.config import Settings


class TimestepAIConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.release_resource = Release(
            id_="timestep_ai_helm_release_resource",
            atomic=True,
            chart=f"{config.base_path}/timestep-ai",
            create_namespace=True,
            lint=True,
            name="timestep-ai",
            namespace="default",
            provider=helm_provider,
            recreate_pods=True,
            set=[
                ReleaseSet(
                    name="app.kubernetes.io\\/managed-by",
                    value="Helm",
                ),
                ReleaseSet(
                    name="meta.helm.sh\\/release-name",
                    value="timestep-ai",
                ),
                ReleaseSet(
                    name="meta.helm.sh\\/release-namespace",
                    value="default",
                ),
            ],
            set_sensitive=[],
            scope=self,
        )

        default_sa_pod_lister_role = RoleV1(
            id_="default_sa_pod_lister_role",
            metadata=RoleV1Metadata(
                name="pod-lister",
                namespace=self.release_resource.namespace,
            ),
            rule=[
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods"],
                    verbs=["list"],
                )
            ],
            scope=self,
        )

        RoleBindingV1(
            id_="default_sa_list_pods_role_binding",
            metadata=RoleBindingV1Metadata(
                name="list-pods",
                namespace=self.release_resource.namespace,
            ),
            subject=[
                RoleBindingV1Subject(
                    kind="ServiceAccount",
                    name="default",
                    api_group="",
                )
            ],
            role_ref=RoleBindingV1RoleRef(
                kind="Role",
                name=default_sa_pod_lister_role.metadata.name,
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )

        default_sa_node_lister_cluster_role = ClusterRoleV1(
            id_="default_sa_node_lister_cluster_role",
            metadata=ClusterRoleV1Metadata(
                name="node-lister",
            ),
            rule=[
                ClusterRoleV1Rule(
                    api_groups=[""],
                    resources=["nodes"],
                    verbs=["list"],
                )
            ],
            scope=self,
        )

        ClusterRoleBindingV1(
            id_="default_sa_list_nodes_cluster_role_binding",
            metadata=ClusterRoleBindingV1Metadata(
                name="list-nodes",
            ),
            subject=[
                ClusterRoleBindingV1Subject(
                    kind="ServiceAccount",
                    name="default",
                    api_group="",
                )
            ],
            role_ref=ClusterRoleBindingV1RoleRef(
                kind="ClusterRole",
                name=default_sa_node_lister_cluster_role.metadata.name,
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )
