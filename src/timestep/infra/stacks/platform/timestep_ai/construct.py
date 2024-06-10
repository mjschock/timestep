import os

import git
from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
    ReleaseSet,
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
from cdktf_cdktf_provider_kubernetes.config_map_v1 import (
    ConfigMapV1,
    ConfigMapV1Metadata,
)
from cdktf_cdktf_provider_kubernetes.manifest import Manifest
from cdktf_cdktf_provider_kubernetes.namespace_v1 import (
    NamespaceV1,
    NamespaceV1Metadata,
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
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from cdktf_cdktf_provider_kubernetes.service_account_v1 import (
    ServiceAccountV1,
    ServiceAccountV1Metadata,
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

        app_config_map = ConfigMapV1(
            id_="app_config_map",
            data={
                "API_URL": f"https://{config.primary_domain_name}",
                "KUBECONTEXT": config.kubecontext,
                "OPEN_GPTS_ASSISTANT_ID": config.open_gpts_assistant_id,
                "OPEN_GPTS_USER_ID": config.open_gpts_user_id,
                "OPEN_GPTS_THREAD_ID": config.open_gpts_thread_id,
                "PREFECT_API_URL": config.prefect_api_url,
                "PRIMARY_DOMAIN_NAME": config.primary_domain_name,
            },
            metadata=ConfigMapV1Metadata(
                name="app-config-map",
                namespace="default",
            ),
            scope=self,
        )

        secret_data = {
            # "DB_URL": f"postgresql+asyncpg://{config.postgres_username}:{config.postgres_password}@{config.postgres_hostname}/{config.postgres_database}", # noqa: E501
            # "DB_URL": f"postgresql+psycopg://{config.postgres_username}:{config.postgres_password}@{config.postgres_hostname}/{config.postgres_database}",  # noqa: E501
        }

        if config.prefect_api_key:
            secret_data["PREFECT_API_KEY"] = config.prefect_api_key.get_secret_value()

        if config.slack_bot_token and config.slack_signing_secret:
            secret_data["SLACK_BOT_TOKEN"] = config.slack_bot_token.get_secret_value()
            secret_data[
                "SLACK_SIGNING_SECRET"
            ] = config.slack_signing_secret.get_secret_value()

        app_secret = SecretV1(
            id_="app_secret",
            data=secret_data,
            metadata=SecretV1Metadata(
                name="app-secret",
                namespace="default",
            ),
            scope=self,
        )

        # litestream_yaml_file_asset = TerraformAsset(
        #     id="litestream_yaml_file_asset",
        #     path=os.path.join(os.path.dirname(__file__), "litestream.yml"),
        #     scope=self,
        #     type=AssetType.FILE,
        # )

        # litestream_config_map = ConfigMapV1(
        #     id_="litestream_config_map",
        #     data={
        #         "litestream.yml": Fn.file(litestream_yaml_file_asset.path),
        #     },
        #     metadata=ConfigMapV1Metadata(
        #         name="litestream-config-map",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        # See:
        # - https://catalog.ngc.nvidia.com/orgs/nvidia/helm-charts/gpu-operator
        # - https://github.com/skypilot-org/skypilot/blob/master/tests/kubernetes/scripts/deploy_k3s.sh#L99
        nvidia_gpu_operator_helm_release_resource = Release(
            id_="nvidia_gpu_operator_helm_release_resource",
            atomic=True,
            chart="gpu-operator",
            cleanup_on_fail=True,
            create_namespace=True,
            name="gpu-operator",
            namespace="gpu-operator",
            repository="https://helm.ngc.nvidia.com/nvidia",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="toolkit.env[0].name",
                    value="CONTAINERD_CONFIG",
                ),
                ReleaseSet(
                    name="toolkit.env[0].value",
                    value="/var/lib/rancher/k3s/agent/etc/containerd/config.toml",
                ),
                ReleaseSet(
                    name="toolkit.env[1].name",
                    value="CONTAINERD_SOCKET",
                ),
                ReleaseSet(
                    name="toolkit.env[1].value",
                    value="/run/k3s/containerd/containerd.sock",
                ),
                ReleaseSet(
                    name="toolkit.env[2].name",
                    value="CONTAINERD_RUNTIME_CLASS",
                ),
                ReleaseSet(
                    name="toolkit.env[2].value",
                    value="nvidia",
                ),
            ],
            scope=self,
            version="24.3.0",
        )

        # nvidia_runtime_class = RuntimeClassV1(
        #     id_="nvidia_runtime_class",
        #     handler="nvidia",
        #     metadata={
        #         "name": "nvidia",
        #     },
        #     scope=self,
        # )

        private_repo_secret = SecretV1(
            # TODO: Use a GitHub App Credential instead?
            # See https://github.com/argoproj/argo-cd/blob/master/docs/user-guide/private-repositories.md#github-app-credential
            id_="private_repo_secret",
            data={
                "password": config.argo_cd_private_repo_access_token.get_secret_value(),
                "project": "default",
                # "url": "https://github.com/mjschock/timestep.git",
                "url": git.Repo().remote("origin").url,
                "username": config.argo_cd_private_repo_username,
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

        skypilot_service_account = ServiceAccountV1(
            id_="skypilot_service_account",
            # image_pull_secrets=[
            #     ServiceAccountV1ImagePullSecret(
            #         name="skypilot-registry-credentials",
            #     ),
            # ],
            # image_pull_secret=[
            #     ServiceAccountV1ImagePullSecret(
            #         name="regcred",
            #     ),
            # ],
            metadata=ServiceAccountV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account",
                namespace="default",
            ),
            scope=self,
        )

        skypilot_service_account_role = RoleV1(
            id_="skypilot_service_account_role",
            metadata=RoleV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                # name="skypilot-service-account-role",
                name="skypilot-service-account-role",
                namespace="default",
            ),
            rule=[
                RoleV1Rule(
                    api_groups=[""],
                    resources=["events"],
                    verbs=["list"],
                ),
                # RoleV1Rule(
                #     api_groups=[""],
                #     resources=["clusterroles"],
                #     verbs=["list"],
                # ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods"],
                    # verbs=["list"],
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
                    verbs=["create", "list"],
                ),
                RoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["roles"],
                    verbs=["create", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    # resource_names=["sky-ssh-keys"],
                    resources=["secrets"],
                    # verbs=["get", "patch"],
                    verbs=["create", "delete", "get", "list", "patch"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["services"],
                    verbs=["create", "delete", "get", "list", "patch"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["serviceaccounts"],
                    # verbs=["create"],
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

        skypilot_service_account_role_binding = RoleBindingV1(
            id_="skypilot_service_account_role_binding",
            metadata=RoleBindingV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-role-binding",
                namespace="default",
            ),
            role_ref=RoleBindingV1RoleRef(
                api_group="rbac.authorization.k8s.io",
                kind="Role",
                name=skypilot_service_account_role.metadata.name,
            ),
            scope=self,
            subject=[
                RoleBindingV1Subject(
                    api_group="",
                    kind="ServiceAccount",
                    # name="default",
                    name=skypilot_service_account.metadata.name,
                )
            ],
        )

        skypilot_service_account_cluster_role = ClusterRoleV1(
            id_="skypilot_service_account_cluster_role",
            metadata=ClusterRoleV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-cluster-role",
            ),
            rule=[
                ClusterRoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["clusterroles"],
                    verbs=[
                        "create",
                        "delete",
                        "get",
                        "list",
                        "patch",
                        "update",
                        "watch",
                    ],
                ),
                ClusterRoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["clusterrolebindings"],
                    verbs=[
                        "create",
                        "delete",
                        "get",
                        "list",
                        "patch",
                        "update",
                        "watch",
                    ],
                ),
                ClusterRoleV1Rule(
                    api_groups=[""],
                    resources=["namespaces"],
                    verbs=["create", "get", "list", "watch"],
                ),
                ClusterRoleV1Rule(
                    api_groups=[""],
                    resources=["nodes"],
                    verbs=["get", "list", "watch"],
                ),
                ClusterRoleV1Rule(
                    api_groups=["node.k8s.io"],
                    resources=["runtimeclasses"],
                    verbs=["get", "list", "watch"],
                ),
                ClusterRoleV1Rule(
                    api_groups=["networking.k8s.io"],
                    resources=["ingressclasses"],
                    verbs=["get", "list", "watch"],
                ),
            ],
            scope=self,
        )

        skypilot_service_account_cluster_role_binding = ClusterRoleBindingV1(
            id_="skypilot_service_account_cluster_role_binding",
            metadata=ClusterRoleBindingV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-cluster-role-binding",
            ),
            role_ref=ClusterRoleBindingV1RoleRef(
                api_group="rbac.authorization.k8s.io",
                kind="ClusterRole",
                name=skypilot_service_account_cluster_role.metadata.name,
            ),
            scope=self,
            subject=[
                ClusterRoleBindingV1Subject(
                    # api_group="",
                    kind="ServiceAccount",
                    # name="default",
                    # namespace="default",
                    name=skypilot_service_account.metadata.name,
                    namespace="default",
                )
            ],
        )

        skypilot_system_namespace = NamespaceV1(
            id_="skypilot_system_namespace",
            metadata=NamespaceV1Metadata(
                name="skypilot-system",
                labels={
                    "parent": "skypilot",
                },
            ),
            scope=self,
        )

        skypilot_system_service_account_role = RoleV1(
            id_="skypilot_system_service_account_role",
            metadata=RoleV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-system-service-account-role",
                namespace=skypilot_system_namespace.metadata.name,
            ),
            rule=[
                RoleV1Rule(
                    api_groups=["*"],
                    resources=["*"],
                    verbs=["*"],
                ),
            ],
            scope=self,
        )

        skypilot_system_service_account_role_binding = RoleBindingV1(
            id_="skypilot_system_service_account_role_binding",
            metadata=RoleBindingV1Metadata(
                labels={
                    "parent": "skypilot",
                },
                # name="skypilot-system-service-account-role-binding",
                name="skypilot-system-service-account-role-binding-default",
                namespace=skypilot_system_namespace.metadata.name,
            ),
            role_ref=RoleBindingV1RoleRef(
                api_group="rbac.authorization.k8s.io",
                kind="Role",
                name=skypilot_system_service_account_role.metadata.name,
            ),
            scope=self,
            subject=[
                RoleBindingV1Subject(
                    api_group="",
                    kind="ServiceAccount",
                    # name="default",
                    name=skypilot_service_account.metadata.name,
                    namespace="default",
                )
            ],
        )

        timestep_ai_manifest_deps = [
            app_config_map,
            app_secret,
            # litestream_config_map,
            nvidia_gpu_operator_helm_release_resource,
            # nvidia_runtime_class,
            private_repo_secret,
            skypilot_service_account_cluster_role_binding,
            skypilot_service_account_role_binding,
            skypilot_system_service_account_role_binding,
        ]

        # if config.local_tls_cert_is_enabled:
        #     timestep_local_tls_secret = SecretV1(
        #         id_="timestep_local_tls_secret",
        #         data={
        #             "tls.crt": config.local_tls_crt.get_secret_value(),
        #             "tls.key": config.local_tls_key.get_secret_value(),
        #             # "tls.crt": base64.b64encode(config.local_tls_crt.get_secret_value().encode("utf-8")).decode("utf-8"), # noqa: E501
        #             # "tls.key": base64.b64encode(config.local_tls_key.get_secret_value().encode("utf-8")).decode("utf-8"), # noqa: E501
        #             # "tls.crt": base64.encode(config.local_tls_cert)
        #             # "tls.key": base64.b64encode(config.local_tls_key.get_secret_value()).decode("utf-8"), # noqa: E501
        #         },
        #         metadata=SecretV1Metadata(
        #             name="ssl-timestep.local",
        #             namespace="default",
        #         ),
        #         scope=self,
        #         type="kubernetes.io/tls",
        #     )
        #     timestep_ai_manifest_deps.append(
        #         timestep_local_tls_secret,
        #     )

        Manifest(
            depends_on=timestep_ai_manifest_deps,
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
                                f"values.{config.primary_domain_name}.tls.yaml"
                                if config.local_tls_cert_is_enabled
                                else f"values.{config.primary_domain_name}.yaml",
                            ],
                        },
                        "path": os.path.relpath(os.path.dirname(__file__), os.getcwd()),
                        "repoURL": git.Repo()
                        .remote("origin")
                        .url,  # TODO: use env var for remote # noqa: E501
                        "targetRevision": "HEAD",
                    },
                    "syncPolicy": {
                        "automated": {
                            "prune": False
                            if ".local" in config.primary_domain_name
                            else True,  # noqa: E501
                            "selfHeal": False
                            if ".local" in config.primary_domain_name
                            else True,  # noqa: E501
                        },
                        "syncOptions": [
                            "CreateNamespace=true",
                        ],
                    },
                },
            },
            scope=self,
        )
