import os

import git
from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_kubernetes.config_map_v1 import (
    ConfigMapV1,
    ConfigMapV1Metadata,
)
from cdktf_cdktf_provider_kubernetes.manifest import Manifest
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
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
                "PRIMARY_DOMAIN_NAME": config.primary_domain_name,
            },
            metadata=ConfigMapV1Metadata(
                name="app-config-map",
                namespace="default",
            ),
            scope=self,
        )

        secret_data = {
            # "API_URL": f"https://{config.primary_domain_name}",  # TODO: why is this a secret? # noqa: E501
            # "DB_URL": f"postgresql+asyncpg://{config.postgres_username}:{config.postgres_password}@{config.postgres_hostname}/{config.postgres_database}", # noqa: E501
            # "DB_URL": f"postgresql+psycopg://{config.postgres_username}:{config.postgres_password}@{config.postgres_hostname}/{config.postgres_database}",  # noqa: E501
        }

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

        # client_config_map = ConfigMapV1(
        #     id_="client_config_map",
        #     data={
        #         "NEXT_PUBLIC_MODEL": "gpt-4-vision-preview",
        #     },
        #     metadata=ConfigMapV1Metadata(
        #         name="client-config-map",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        # client_secret = SecretV1(
        #     id_="client_secret",
        #     data={
        #         # "OPENAI_API_KEY": config.openai_api_key.get_secret_value(),
        #     },
        #     metadata=SecretV1Metadata(
        #         name="client-secret",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        # skypilot_service_account = ServiceAccountV1(
        #     id_="skypilot_service_account",
        #     metadata=ServiceAccountV1Metadata(
        #         labels={
        #             "parent": "skypilot",
        #         },
        #         name="sky-sa",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        # skypilot_system_namespace = NamespaceV1(
        #     id_="skypilot_system_namespace",
        #     metadata=NamespaceV1Metadata(
        #         name="skypilot-system",
        #         labels={
        #             "parent": "skypilot",
        #         }
        #     ),
        #     scope=self,
        # )

        # default_sa_cluster_role = ClusterRoleV1(
        #     id_="default_sa_cluster_role",
        #     metadata=ClusterRoleV1Metadata(
        #         generate_name="default-sa-cluster-role-",
        #     ),
        #     rule=[
        #         # ClusterRoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["clusterroles"],
        #         #     verbs=["list"],
        #         # ),
        #         # ClusterRoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["nodes"],
        #         #     verbs=["list"],
        #         # )
        #     ],
        #     scope=self,
        # )

        # default_sa_cluster_role_binding = ClusterRoleBindingV1(
        #     id_="default_sa_cluster_role_binding",
        #     metadata=ClusterRoleBindingV1Metadata(
        #         generate_name="default-sa-cluster-role-binding-",
        #     ),
        #     subject=[
        #         ClusterRoleBindingV1Subject(
        #             kind="ServiceAccount",
        #             name="default",
        #             api_group="",
        #         )
        #     ],
        #     role_ref=ClusterRoleBindingV1RoleRef(
        #         kind="ClusterRole",
        #         name=default_sa_cluster_role.metadata.name,
        #         api_group="rbac.authorization.k8s.io",
        #     ),
        #     scope=self,
        # )

        # default_sa_role = RoleV1(
        # skypilot_service_account_role = RoleV1(
        #     # id_="default_sa_role",
        #     id_="skypilot_service_account_role",
        #     metadata=RoleV1Metadata(
        #         # generate_name="default-sa-role-",
        #         labels={
        #             "parent": "skypilot",
        #         },
        #         name="sky-sa-role",
        #         namespace="default",
        #     ),
        #     rule=[
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["clusterroles"],
        #         #     verbs=["list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["pods"],
        #         #     verbs=["create", "delete", "get", "list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["pods/exec"],
        #         #     verbs=["create", "delete", "get", "list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["pods/status"],
        #         #     verbs=["create", "delete", "get", "list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=["rbac.authorization.k8s.io"],
        #         #     resources=["rolebindings"],
        #         #     verbs=["create", "list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=["rbac.authorization.k8s.io"],
        #         #     resources=["roles"],
        #         #     verbs=["create", "list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["secrets"],
        #         #     verbs=["create", "get", "patch"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["services"],
        #         #     verbs=["create", "delete", "get", "list"],
        #         # ),
        #         # RoleV1Rule(
        #         #     api_groups=[""],
        #         #     resources=["serviceaccounts"],
        #         #     verbs=["create", "list"],
        #         # ),
        #         RoleV1Rule(  # TODO: Figure out why this is needed, it seems like a security risk!  # noqa: E501
        #             api_groups=["*"],
        #             resources=["*"],
        #             verbs=["*"],
        #         ),
        #     ],
        #     scope=self,
        # )

        # default_sa_role_binding = RoleBindingV1(
        # skypilot_service_account_role_binding = RoleBindingV1(
        #     # id_="default_sa_role_binding",
        #     id_="skypilot_service_account_role_binding",
        #     metadata=RoleBindingV1Metadata(
        #         # generate_name="default-sa-role-binding-",
        #         labels={
        #             "parent": "skypilot",
        #         },
        #         name="sky-sa-rb",
        #         namespace="default",
        #     ),
        #     role_ref=RoleBindingV1RoleRef(
        #         api_group="rbac.authorization.k8s.io",
        #         kind="Role",
        #         # name=default_sa_role.metadata.name,
        #         name=skypilot_service_account_role.metadata.name,
        #     ),
        #     scope=self,
        #     subject=[
        #         RoleBindingV1Subject(
        #             kind="ServiceAccount",
        #             # name="default",
        #             name=skypilot_service_account.metadata.name,
        #             # api_group="",
        #         )
        #     ],
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

        # server_config_map = ConfigMapV1(
        #     id_="server_config_map",
        #     data={
        #         "KUBECONTEXT": config.kubecontext,
        #         # "LITESTREAM_ACCESS_KEY_ID": config.minio_root_user,
        #         # "MINIO_ENDPOINT": "minio.default.svc.cluster.local:9000",
        #         # "MINIO_ROOT_USER": config.minio_root_user,
        #         # "POSTGRES_DATABASE": postgres_database,
        #         # "POSTGRES_HOSTNAME": postgres_hostname,
        #         # "POSTGRES_USERNAME": postgres_username,
        #         "PREFECT_API_URL": "http://prefect-server.default.svc.cluster.local:4200/api",
        #         "PRIMARY_DOMAIN_NAME": config.primary_domain_name,
        #         # "REPLICA_URL": "s3://minio.default.svc.cluster.local:9000/default/db",
        #         # "REPLICA_URL": "http://minio.default.svc.cluster.local:9000",
        #         "VERSION": config.version,
        #     },
        #     metadata=ConfigMapV1Metadata(
        #         name="server-config-map",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        # server_secret = SecretV1(
        #     id_="server_secret",
        #     data={
        #         # "LITESTREAM_SECRET_ACCESS_KEY": config.minio_root_password.get_secret_value(),  # noqa: E501
        #         # "MINIO_ROOT_PASSWORD": config.minio_root_password.get_secret_value(), # noqa: E501
        #         "OPENAI_API_KEY": config.openai_api_key.get_secret_value(),
        #         # "POSTGRES_CONNECTION_STRING": f"postgresql+asyncpg://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}",
        #         # "POSTGRES_PASSWORD": config.postgresql_password.get_secret_value(),
        #     },
        #     metadata=SecretV1Metadata(
        #         name="server-secret",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        timestep_ai_manifest_deps = [
            app_config_map,
            app_secret,
            # client_config_map,
            # client_secret,
            # default_sa_cluster_role_binding,
            # default_sa_role_binding,
            # litestream_config_map,
            private_repo_secret,
            # server_config_map,
            # server_secret,
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
