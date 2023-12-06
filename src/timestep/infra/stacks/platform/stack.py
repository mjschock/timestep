from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
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
from cdktf_cdktf_provider_kubernetes.deployment_v1 import (
    DeploymentV1,
    DeploymentV1Metadata,
    DeploymentV1Spec,
    DeploymentV1SpecSelector,
    DeploymentV1SpecTemplate,
    DeploymentV1SpecTemplateMetadata,
    DeploymentV1SpecTemplateSpec,
    DeploymentV1SpecTemplateSpecContainer,
    DeploymentV1SpecTemplateSpecContainerEnv,
    DeploymentV1SpecTemplateSpecContainerPort,
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
from cdktf_cdktf_provider_kubernetes.service_v1 import (
    ServiceV1,
    ServiceV1Metadata,
    ServiceV1Spec,
    ServiceV1SpecPort,
)
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

        self.helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                config_context=self.kubernetes_provider.config_context,
                config_path=self.kubernetes_provider.config_path,
            ),
            scope=self,
        )

        postgres_database = "postgres"
        postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
        postgres_password = config.postgresql_password.get_secret_value()
        postgres_username = "postgres"

        self.hasura_graphql_engine_deployment_resource = DeploymentV1(
            id_="hasura_graphql_engine_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "hasura-graphql-engine",
                },
                name="hasura-graphql-engine",
                namespace="default",
            ),
            spec=DeploymentV1Spec(
                replicas="1",
                selector=DeploymentV1SpecSelector(
                    match_labels={
                        "app": "hasura-graphql-engine",
                    }
                ),
                template=DeploymentV1SpecTemplate(
                    metadata=DeploymentV1SpecTemplateMetadata(
                        labels={
                            "app": "hasura-graphql-engine",
                        },
                    ),
                    spec=DeploymentV1SpecTemplateSpec(
                        container=[
                            DeploymentV1SpecTemplateSpecContainer(
                                env=[
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_ADMIN_SECRET",
                                        value=config.hasura_graphql_admin_secret.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_DEV_MODE",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_DATABASE_URL",
                                        value=f"postgres://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_ENABLE_CONSOLE",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_JWT_SECRET",
                                        value=f'{{"type": "HS256", "key": "{config.hasura_graphql_jwt_secret_key.get_secret_value()}", "issuer": "hasura-auth"}}',  # noqa: E501
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_LOG_LEVEL",
                                        value="debug",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_UNAUTHORIZED_ROLE",
                                        value="public",
                                    ),
                                ],
                                image="hasura/graphql-engine:latest",
                                image_pull_policy="IfNotPresent",
                                name="hasura-graphql-engine",
                                port=[
                                    DeploymentV1SpecTemplateSpecContainerPort(
                                        container_port=8080,
                                        name="http",
                                        protocol="TCP",
                                    )
                                ],
                            )
                        ],
                    ),
                ),
            ),
            scope=self,
        )

        self.hasura_graphql_engine_service_resource = ServiceV1(
            depends_on=[self.hasura_graphql_engine_deployment_resource],
            id_="hasura_graphql_engine_service_resource",
            metadata=ServiceV1Metadata(
                labels={
                    "app": "hasura-graphql-engine",
                },
                name="hasura-graphql-engine",
                namespace="default",
            ),
            spec=ServiceV1Spec(
                port=[
                    ServiceV1SpecPort(
                        port=8080,
                        protocol="TCP",
                    )
                ],
                selector={
                    "app": "hasura-graphql-engine",
                },
                type="ClusterIP",
            ),
            scope=self,
        )

        self.nhost_hasura_auth_deployment_resource = DeploymentV1(
            id_="nhost_hasura_auth_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "nhost-hasura-auth",
                },
                name="nhost-hasura-auth",
                namespace="default",
            ),
            spec=DeploymentV1Spec(
                replicas="1",
                selector=DeploymentV1SpecSelector(
                    match_labels={
                        "app": "nhost-hasura-auth",
                    }
                ),
                template=DeploymentV1SpecTemplate(
                    metadata=DeploymentV1SpecTemplateMetadata(
                        labels={
                            "app": "nhost-hasura-auth",
                        },
                    ),
                    spec=DeploymentV1SpecTemplateSpec(
                        container=[
                            DeploymentV1SpecTemplateSpecContainer(
                                env=[
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_CLIENT_URL",
                                        value=f"https://www.{config.primary_domain_name}",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_MFA_ENABLED",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_PASSWORD_HIBP_ENABLED",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_PASSWORD_MIN_LENGTH",
                                        value="14",  # https://bitwarden.com/blog/how-long-should-my-password-be/
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SERVER_URL",
                                        value=f"https://www.{config.primary_domain_name}/v1/auth",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_HOST",
                                        value="smtp.gmail.com",  # The sending limit is 2,000 messages per day.  # noqa: E501
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_PASS",
                                        value=config.smtp_password.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_PORT",
                                        value="587",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_SENDER",
                                        value=config.smtp_sender,
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_USER",
                                        value="agent@timestep.ai",
                                        # value="Timestep AI Agent"
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_ADMIN_SECRET",
                                        value=config.hasura_graphql_admin_secret.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_DATABASE_URL",
                                        value=f"postgres://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_GRAPHQL_URL",
                                        value="http://hasura-graphql-engine.default.svc.cluster.local:8080/v1/graphql",  # noqa: E501
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_JWT_SECRET",
                                        value=f'{{"type": "HS256", "key": "{config.hasura_graphql_jwt_secret_key.get_secret_value()}", "issuer": "hasura-auth"}}',  # noqa: E501
                                    ),
                                ],
                                image="nhost/hasura-auth:latest",
                                name="nhost-hasura-auth",
                                port=[
                                    DeploymentV1SpecTemplateSpecContainerPort(
                                        container_port=4000,
                                        name="http",
                                    )
                                ],
                            )
                        ],
                    ),
                ),
            ),
            scope=self,
        )

        self.nhost_hasura_auth_service_resource = ServiceV1(
            depends_on=[
                self.hasura_graphql_engine_service_resource,
                self.nhost_hasura_auth_deployment_resource,
            ],
            id_="nhost_hasura_auth_service_resource",
            metadata=ServiceV1Metadata(
                labels={
                    "app": "nhost-hasura-auth",
                },
                name="nhost-hasura-auth",
                namespace="default",
            ),
            spec=ServiceV1Spec(
                port=[
                    ServiceV1SpecPort(
                        port=4000,
                        protocol="TCP",
                    )
                ],
                selector={
                    "app": "nhost-hasura-auth",
                },
                type="ClusterIP",
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

        default_sa_cluster_role_binding = ClusterRoleBindingV1(
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
                    resources=["secrets"],
                    verbs=["create"],
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

        default_sa_role_binding = RoleBindingV1(
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

        private_repo_secret = SecretV1(
            # TODO: Use a GitHub App Credential instead?
            # See https://github.com/argoproj/argo-cd/blob/master/docs/user-guide/private-repositories.md#github-app-credential
            id_="private_repo_secret",
            data={
                "password": config.argo_cd_private_repo_access_token.get_secret_value(),
                "project": "default",
                "url": "https://github.com/mjschock/timestep.git",
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

        postgres_database = "postgres"
        postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
        postgres_password = config.postgresql_password.get_secret_value()
        postgres_username = "postgres"

        web_secret = SecretV1(
            id_="web_secret",
            data={
                "MINIO_ROOT_PASSWORD": config.minio_root_password.get_secret_value(),
                "POSTGRES_CONNECTION_STRING": f"postgresql+asyncpg://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}",
                "POSTGRES_PASSWORD": config.postgresql_password.get_secret_value(),
            },
            metadata=SecretV1Metadata(
                name="web-secret",
                namespace="default",
            ),
            scope=self,
        )

        timestep_ai_manifest_deps = [
            default_sa_cluster_role_binding,
            default_sa_role_binding,
            private_repo_secret,
            web_secret,
        ]

        if config.local_tls_cert_is_enabled:
            timestep_local_tls_secret = SecretV1(
                id_="timestep_local_tls_secret",
                data={
                    "tls.crt": config.local_tls_crt.get_secret_value(),
                    "tls.key": config.local_tls_key.get_secret_value(),
                },
                metadata=SecretV1Metadata(
                    name="timestep-local-tls",
                    namespace="default",
                ),
                scope=self,
                type="kubernetes.io/tls",
            )
            timestep_ai_manifest_deps.append(
                timestep_local_tls_secret,
            )

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
                                # "values.yaml",
                                # "values-production.yaml",
                                f"values.{config.primary_domain_name}.tls.yaml"
                                if config.local_tls_cert_is_enabled
                                else f"values.{config.primary_domain_name}",  # noqa: E501
                            ],
                            #                             "values": f"""
                            # ingress:
                            #   hosts:
                            #     - host: {config.primary_domain_name}
                            #   tls:
                            #     - hosts:
                            #       - timestep.local
                            #       - www.timestep.local
                            #       secretName: timestep-local-tls
                            # replicaCount: {1 if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS else 3}  # noqa: E501
                            # """,  # noqa: E501
                        },
                        "path": "src/timestep/infra/stacks/platform",
                        "repoURL": "https://github.com/mjschock/timestep.git",
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
                            # "ApplyOutOfSyncOnly=true",
                            "CreateNamespace=true",
                        ],
                    },
                },
            },
            # provider=NullProvider(
            #     alias="argocd",
            #     id="argocd_provider",
            #     scope=self,
            # ),
            # provisioners=[
            #     LocalExecProvisioner(
            #         command=f"argocd app sync platform",
            #         type="local-exec",
            #         when="create",
            #     ),
            #     LocalExecProvisioner(
            #         command=f"argocd app delete platform",
            #         type="local-exec",
            #         when="destroy",
            #     ),
            # ],
            scope=self,
            # wait=ManifestWait(
            #     # condition=[
            #     #     ManifestWaitCondition(
            #     #         status="Healthy",
            #     #         type="health",
            #     #     ),
            #     #     ManifestWaitCondition(
            #     #         status="Synced",
            #     #         type="sync",
            #     #     ),
            #     # ],
            #     fields={
            #         "status.phase
            #     },
            #     # rollout=True,
            # ),
        )

        # argocd_kubernetes_provider = ArgocdProviderKubernetes(
        #     client_certificate=self.kubernetes_provider.client_certificate,
        #     client_key=self.kubernetes_provider.client_key,
        #     cluster_ca_certificate=self.kubernetes_provider.cluster_ca_certificate,
        #     config_context=self.kubernetes_provider.config_context,
        #     config_context_auth_info=self.kubernetes_provider.config_context_auth_info,  # noqa: E501
        #     config_context_cluster=self.kubernetes_provider.config_context_cluster,
        #     exec=self.kubernetes_provider.exec,
        #     host=self.kubernetes_provider.host,
        #     insecure=self.kubernetes_provider.insecure,
        #     password=self.kubernetes_provider.password,
        #     token=self.kubernetes_provider.token,
        #     username=self.kubernetes_provider.username,
        #     # exec=ArgocdProviderKubernetesExec(
        #     #     api_version="client.authentication.k8s.io/v1beta1",
        #     #     command="kubectl",
        #     #     # command="kubectl -n default get secret argocd-secret -o jsonpath="{.data.clearPassword}" | base64 -d",  # noqa: E501
        #     #     # command=[
        #     #     #     "kubectl",
        #     #     #     "-n",
        #     #     #     "default",
        #     #     #     "get",
        #     #     #     "secret",
        #     #     #     "argocd-secret",
        #     #     #     "-o",
        #     #     #     "jsonpath={.data.clearPassword}",
        #     #     # ],
        #     #     # command="kubectl -n default get secret argocd-secret -o jsonpath='{.data.clearPassword}' | base64 -d", # noqa: E501
        #     #     env={
        #     #         "name": "KUBECONFIG",
        #     #         "value": self.kubernetes_provider.config_path,
        #     #     },
        #     # ),
        # )

        # argocd_provider = ArgocdProvider(
        #     id="argocd_provider",
        # #     # kubernetes=ArgocdProviderKubernetes(
        # #     #     config_context=self.kubernetes_provider.config_context,
        # #     #     # config_context="kind-argocd",
        # #     #     config_context_cluster=self.kubernetes_provider.config_context_cluster,  # noqa: E501
        # #     # #     # config_path=self.kubernetes_provider.config_path,
        # #     # ),
        #     # kubernetes=argocd_kubernetes_provider,
        # #     scope=self,
        # #     # use_local_config=True,
        # #     # auth_token=config.argocd_api_token.get_secret_value(),
        # #     # auth_token="kubeapps-operator-token",
        # #     # auth_token="argocd-secret",
        #     username="admin",
        #     password="sqcYr7ymHm",
        # #     # port_forward=True,
        # #     port_forward_with_namespace="default",
        # #     # server_addr="argo-cd-server.default.svc.cluster.local:443",
        # #     # server_addr="argo-cd-server.default.svc.cluster.local:80",
        # #     # core=True, # Error: failed to start local server
        # #     # port_forward_with_namespace=True,
        #     # core=True,
        #     # context=self.kubernetes_provider.config_context,
        #     # config_path=self.kubernetes_provider.config_path,
        #     # kubernetes=ArgocdProviderKubernetes(
        #     #     # config_context=self.kubernetes_provider.config_context,
        #     #     # config_context_cluster=self.kubernetes_provider.config_context_cluster,  # noqa: E501
        #     #     config_context=self.kubernetes_provider.config_context,
        #     #     # config_path=self.kubernetes_provider.config_path,
        #     # ),
        #     port_forward=True,
        #     # use_local_config=True,
        #     scope=self,
        # )

        # Application(
        #     # id_="timestep_ai_argocd_application",
        #     id_="timestep_ai_manifest",
        #     metadata=ApplicationMetadata(
        #         name="platform",
        #         namespace="default",
        #     ),
        #     provider=argocd_provider,
        #     # provider=NullProvider(
        #     #     alias="argocd",
        #     #     id="argocd_provider",
        #     #     scope=self,
        #     # ),
        #     spec=ApplicationSpec(
        #         destination=ApplicationSpecDestination(
        #             namespace="default",
        #             server="https://kubernetes.default.svc",
        #         ),
        #         project="default",
        #         source=[
        #             ApplicationSpecSource(
        #                 # chart= # TODO: add this?
        #                 helm=ApplicationSpecSourceHelm(
        #                     # pass_credentials=True, # TODO: ?
        #                     value_files=[
        #                         # "values.yaml",
        #                         # "values-production.yaml",
        #                         f"values.{config.primary_domain_name}.yaml",
        #                     ],
        #                     # values_object={
        #                     #     "ingress": {
        #                     #         "hosts": [
        #                     #             {
        #                     #                 "host": f"{config.primary_domain_name}",
        #                     #             }
        #                     #         ]
        #                     #     },
        #                     # },
        #                 ),
        #                 path="src/timestep/infra/stacks/platform",
        #                 repo_url="https://github.com/mjschock/timestep.git",
        #                 target_revision="HEAD",
        #             ),
        #         ],
        #         sync_policy=ApplicationSpecSyncPolicy(
        #             automated=ApplicationSpecSyncPolicyAutomated(
        #                 prune=False
        #                 if ".local" in config.primary_domain_name
        #                 else True,  # noqa: E501
        #                 self_heal=False
        #                 if ".local" in config.primary_domain_name
        #                 else True,  # noqa: E501
        #             ),
        #             sync_options=[
        #                 # "ApplyOutOfSyncOnly=true",
        #                 "CreateNamespace=true",
        #             ],
        #         ),
        #     ),
        #     scope=self,
        #     # wait=False, # TODO: added
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
