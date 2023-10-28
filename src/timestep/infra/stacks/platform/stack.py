from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
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
from cdktf_cdktf_provider_kubernetes.manifest import Manifest
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
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
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings


class PlatformStack(TerraformStack):
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

        # self.release_resource = Release(
        #     id_="timestep_ai_helm_release_resource",
        #     atomic=True,
        #     chart=f"{config.base_path}/dist/timestep-ai-{config.version}.tgz",
        #     cleanup_on_fail=True,
        #     create_namespace=True,
        #     # force_update=True,
        #     lint=True,
        #     name="timestep-ai",
        #     namespace="default",
        #     provider=helm_provider,
        #     # recreate_pods=True,
        #     # replace=True,
        #     set=[
        #         # ReleaseSet(
        #         #     name="app.kubernetes.io\\/managed-by",
        #         #     value="Helm",
        #         # ),
        #         ReleaseSet(
        #             name="ingress.hosts[0].host",
        #             value=f"{config.primary_domain_name}",
        #         ),
        #         # ReleaseSet(
        #         #     name="meta.helm.sh\\/release-name",
        #         #     value="timestep-ai",
        #         # ),
        #         # ReleaseSet(
        #         #     name="meta.helm.sh\\/release-namespace",
        #         #     value="default",
        #         # ),
        #     ],
        #     set_sensitive=[],
        #     scope=self,
        #     version=config.version,
        # )

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
                    "name": "platform",
                    "namespace": "default",
                },
                "spec": {
                    "destination": {
                        "namespace": "default",
                        "server": "https://kubernetes.default.svc",
                    },
                    "project": "default",
                    "source": {
                        "helm": {
                            "valueFiles": [
                                # "values.yaml",
                                # "values-production.yaml",
                                f"values.{config.primary_domain_name}.yaml",
                            ],
                            # "valuesObject": {
                            #     "ingress": {
                            #         "hosts": [
                            #             {
                            #                 "host": f"{config.primary_domain_name}",
                            #             }
                            #         ]
                            #     },
                            # },
                        },
                        "path": "src/timestep/infra/stacks/platform",
                        "repoURL": "https://github.com/mjschock/timestep.git",
                        "targetRevision": "HEAD",
                    },
                    "syncPolicy": {
                        "automated": {
                            "prune": True,
                            "selfHeal": True,
                        },
                        "syncOptions": [
                            # "ApplyOutOfSyncOnly=true",
                            "CreateNamespace=true",
                        ],
                    },
                },
            },
            scope=self,
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
                RoleV1Rule(  # TODO: Figure out why this is needed, it seems like a security risk!  # noqa: E501
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
