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
            chart=f"{config.base_path}/timestep-ai-{config.version}.tgz",
            cleanup_on_fail=True,
            create_namespace=True,
            force_update=True,
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
            version=config.version,
        )

        default_sa_role = RoleV1(
            id_="default_sa_role",
            metadata=RoleV1Metadata(
                generate_name="default-sa-role-",
            ),
            rule=[
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods/exec"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods/status"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["rolebindings"],
                    verbs=["create"],
                ),
                RoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["roles"],
                    verbs=["create", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["services"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["serviceaccounts"],
                    verbs=["create", "list"],
                ),
                RoleV1Rule(
                    api_groups=["*"],
                    resources=["*"],
                    verbs=["*"],
                ),
            ],
            scope=self,
        )

        RoleBindingV1(
            id_="default_sa_role_binding",
            metadata=RoleBindingV1Metadata(
                generate_name="default-sa-role-binding-",
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
                name=default_sa_role.metadata.name,
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )

        default_sa_cluster_role = ClusterRoleV1(
            id_="default_sa_cluster_role",
            metadata=ClusterRoleV1Metadata(
                generate_name="default-sa-cluster-role-",
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
            id_="default_sa_cluster_role_binding",
            metadata=ClusterRoleBindingV1Metadata(
                generate_name="default-sa-cluster-role-binding-",
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
                name=default_sa_cluster_role.metadata.name,
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )
