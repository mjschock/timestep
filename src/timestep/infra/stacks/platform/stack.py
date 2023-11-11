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

        self.helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                config_context=self.kubernetes_provider.config_context,
                config_path=self.kubernetes_provider.config_path,
            ),
            scope=self,
        )

        config.postgresql_password.get_secret_value()

        # kubectl -n default create secret generic demo-supabase-jwt \
        #   --from-literal=anonKey='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAiYW5vbiIsCiAgICAiaXNzIjogInN1cGFiYXNlIiwKICAgICJpYXQiOiAxNjc1NDAwNDAwLAogICAgImV4cCI6IDE4MzMxNjY4MDAKfQ.ztuiBzjaVoFHmoljUXWmnuDN6QU2WgJICeqwyzyZO88' \  # noqa: E501
        #   --from-literal=serviceKey='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAic2VydmljZV9yb2xlIiwKICAgICJpc3MiOiAic3VwYWJhc2UiLAogICAgImlhdCI6IDE2NzU0MDA0MDAsCiAgICAiZXhwIjogMTgzMzE2NjgwMAp9.qNsmXzz4tG7eqJPh1Y58DbtIlJBauwpqx39UF-MwM8k' \  # noqa: E501
        #   --from-literal=secret='abcdefghijklmnopqrstuvwxyz123456'

        # self.supabase_jwt_secret_resource = SecretV1(
        #     id_="supabase_jwt_secret_resource",
        #     data={
        #         # "anon-key": config.supabase_jwt_anon_key.get_secret_value(),
        #         # "secret": config.supabase_jwt_secret.get_secret_value(),
        #         # "service-key": config.supabase_jwt_service_key.get_secret_value(),
        #         "anon-key": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAiYW5vbiIsCiAgICAiaXNzIjogInN1cGFiYXNlIiwKICAgICJpYXQiOiAxNjc1NDAwNDAwLAogICAgImV4cCI6IDE4MzMxNjY4MDAKfQ.ztuiBzjaVoFHmoljUXWmnuDN6QU2WgJICeqwyzyZO88',  # noqa: E501
        #         "secret": 'abcdefghijklmnopqrstuvwxyz123456',
        #         "service-key": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAic2VydmljZV9yb2xlIiwKICAgICJpc3MiOiAic3VwYWJhc2UiLAogICAgImlhdCI6IDE2NzU0MDA0MDAsCiAgICAiZXhwIjogMTgzMzE2NjgwMAp9.qNsmXzz4tG7eqJPh1Y58DbtIlJBauwpqx39UF-MwM8k',  # noqa: E501
        #     },
        #     metadata=SecretV1Metadata(
        #         name="supabase-jwt",
        #         namespace="default",
        #     ),
        #     scope=self,
        # )

        # self.supabase_helm_release_resource = Release(
        #     id_="supabase_helm_release_resource",
        #     atomic=True,
        #     chart="supabase",
        #     create_namespace=True,
        #     name="supabase",
        #     namespace="default",
        #     repository="https://charts.bitnami.com/bitnami",
        #     provider=self.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="externalDatabase.host",
        #             value=postgres_hostname,
        #         ),
        #         ReleaseSet(
        #             name="externalDatabase.database",
        #             value=postgres_database,
        #         ),
        #         ReleaseSet(
        #             name="externalDatabase.port",
        #             value="5432",
        #         ),
        #         ReleaseSet(
        #             name="externalDatabase.user",
        #             value=postgres_username,
        #         ),
        #         ReleaseSet(
        #             name="global.jwt.existingSecret",
        #             value=self.supabase_jwt_secret_resource.metadata.name,
        #         ),
        #         ReleaseSet(
        #             name="postgresql.enabled",
        #             value="false",
        #         ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="externalDatabase.password",
        #             value=postgres_password,
        #         )
        #     ],
        #     scope=self,
        # )

        # self.nhost_helm_release_resource = Release(
        #     id_="nhost_helm_release_resource",
        #     atomic=True,
        #     chart="nhost",
        #     create_namespace=True,
        #     name="nhost",
        #     namespace="default",
        #     repository="https://fpoussin.github.io/nhost-helm",
        #     provider=self.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="mailhog.ingress.enabled",
        #             value="false",
        #         ),
        #         ReleaseSet(
        #             name="minio.auth.rootUser",
        #             value=config.minio_root_user,
        #         ),
        #         ReleaseSet(
        #             name="minio.enabled",
        #             value="false",
        #         ),
        #         ReleaseSet(
        #             name="postgresql.enabled",
        #             value="false",
        #         ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="minio.auth.rootPassword",
        #             value=config.minio_root_password.get_secret_value(),
        #         ),
        #         ReleaseSetSensitive(
        #             name="postgresql.auth.password",
        #             value=config.postgresql_password.get_secret_value(),
        #         ),
        #         ReleaseSetSensitive(
        #             name="postgresql.auth.postgresPassword",
        #             value=config.postgresql_password.get_secret_value(),
        #         ),
        #     ],
        #     scope=self,
        # )

        # self.hasura_graphql_engine_helm_release_resource = Release(
        #     id_="hasura_graphql_engine_helm_release_resource",
        #     atomic=True,
        #     chart="graphql-engine",
        #     create_namespace=True,
        #     name="hasura",
        #     namespace="default",
        #     repository="https://hasura.github.io/helm-charts",
        #     provider=self.helm_provider,
        #     set=[
        #         # ReleaseSet(
        #         #     name="config.enabledApis",
        #         #     value="metadata",
        #         # ),
        #         ReleaseSet(
        #             name="config.metadataOnly",
        #             value="false",
        #         ),
        #         ReleaseSet(
        #             name="config.unauthorizedRole",
        #             value="public",
        #         ),
        #         # ReleaseSet(
        #         #     name="postgres.auth.username",
        #         #     value=postgres_username,
        #         # ),
        #         # ReleaseSet(
        #         #     name="postgres.auth.database",
        #         #     value=postgres_database,
        #         # ),
        #         ReleaseSet(
        #             name="postgres.enabled",
        #             value="false",
        #         ),
        #     ],
        #     set_sensitive=[
        #         # ReleaseSetSensitive(
        #         #     name="postgres.auth.password",
        #         #     value=config.postgresql_password.get_secret_value(),
        #         # ),
        #         ReleaseSetSensitive(
        #             name="secret.adminSecret",
        #             value=config.hasura_graphql_admin_secret.get_secret_value(),
        #         ),
        #         ReleaseSetSensitive(
        #             name="secret.jwtSecret.key",
        #             value=config.hasura_graphql_jwt_secret_key.get_secret_value(),
        #         ),
        #         ReleaseSetSensitive(
        #             name="secret.jwtSecret.issuer",
        #             value="hasura-auth",
        #         ),
        #         ReleaseSetSensitive(
        #             name="secret.jwtSecret.type",
        #             value="HS256",
        #         ),
        #         ReleaseSetSensitive(
        #             name="secret.metadataDbUrl",
        #             value=postgres_connection_string,
        #         )
        #     ],
        #     scope=self,
        # )

        # self.hasura_graphql_engine_deployment_resource = DeploymentV1(
        #     id_="hasura_graphql_engine_deployment_resource",
        #     metadata=DeploymentV1Metadata(
        #         labels={
        #             "app": "hasura-graphql-engine",
        #         },
        #         name="hasura-graphql-engine",
        #         namespace="default",
        #     ),
        #     spec=DeploymentV1Spec(
        #         replicas="1",
        #         selector=DeploymentV1SpecSelector(
        #             match_labels={
        #                 "app": "hasura-graphql-engine",
        #             }
        #         ),
        #         template=DeploymentV1SpecTemplate(
        #             metadata=DeploymentV1SpecTemplateMetadata(
        #                 labels={
        #                     "app": "hasura-graphql-engine",
        #                 },
        #             ),
        #             spec=DeploymentV1SpecTemplateSpec(
        #                 container=[
        #                     DeploymentV1SpecTemplateSpecContainer(
        #                         env=[
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_ADMIN_SECRET",
        #                                 value=config.hasura_graphql_admin_secret.get_secret_value(),  # noqa: E501
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_DATABASE_URL",
        #                                 value=postgres_connection_string,
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_ENABLE_CONSOLE",
        #                                 value="true",
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_JWT_SECRET",
        #                                 value=f"{{\"type\": \"HS256\", \"key\": \"{config.hasura_graphql_jwt_secret_key.get_secret_value()}\", \"issuer\": \"hasura-auth\"}}",  # noqa: E501
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_LOG_LEVEL",
        #                                 value="debug",
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_UNAUTHORIZED_ROLE",
        #                                 value="public",
        #                             ),
        #                         ],
        #                         image="hasura/graphql-engine:latest",
        #                         name="hasura-graphql-engineh",
        #                         port=[
        #                             DeploymentV1SpecTemplateSpecContainerPort(
        #                                 container_port=8080,
        #                                 name="http",
        #                             )
        #                         ]
        #                     )
        #                 ],
        #             ),
        #         ),
        #     ),
        #     scope=self,
        # )

        # self.hasura_graphql_engine_service_resource = ServiceV1(
        #     id_="hasura_graphql_engine_service_resource",
        #     metadata=ServiceV1Metadata(
        #         name="hasura-graphql-engine",
        #         namespace="default",
        #     ),
        #     spec=ServiceV1Spec(
        #         port=[
        #             ServiceV1SpecPort(
        #                 port=8080,
        #                 protocol="TCP",
        #                 # target_port=8080,
        #             )
        #         ],
        #         selector={
        #             "app": "hasura-graphql-engine",
        #         },
        #         type="ClusterIP",
        #     ),
        #     scope=self,
        # )

        # self.nhost_hasura_auth_deployment_resource = DeploymentV1(
        #     id_="nhost_hasura_auth_deployment_resource",
        #     metadata=DeploymentV1Metadata(
        #         labels={
        #             "app": "nhost-hasura-auth",
        #         },
        #         name="nhost-hasura-auth",
        #         namespace="default",
        #     ),
        #     spec=DeploymentV1Spec(
        #         replicas="1",
        #         selector=DeploymentV1SpecSelector(
        #             match_labels={
        #                 "app": "nhost-hasura-auth",
        #             }
        #         ),
        #         template=DeploymentV1SpecTemplate(
        #             metadata=DeploymentV1SpecTemplateMetadata(
        #                 labels={
        #                     "app": "nhost-hasura-auth",
        #                 },
        #             ),
        #             spec=DeploymentV1SpecTemplateSpec(
        #                 container=[
        #                     DeploymentV1SpecTemplateSpecContainer(
        #                         env=[
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_ADMIN_SECRET",
        #                                 value=config.hasura_graphql_admin_secret.get_secret_value(),  # noqa: E501
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_DATABASE_URL",
        #                                 value=postgres_connection_string,
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_GRAPHQL_URL",
        #                                 value=f"http://hasura-graphql-engine.default.svc.cluster.local:8080/v1/graphql",  # noqa: E501
        #                             ),
        #                             DeploymentV1SpecTemplateSpecContainerEnv(
        #                                 name="HASURA_GRAPHQL_JWT_SECRET",
        #                                 value=f"{{\"type\": \"HS256\", \"key\": \"{config.hasura_graphql_jwt_secret_key.get_secret_value()}\", \"issuer\": \"hasura-auth\"}}",  # noqa: E501
        #                             ),
        #                         ],
        #                         image="nhost/hasura-auth:latest",
        #                         name="nhost-hasura-auth",
        #                         port=[
        #                             DeploymentV1SpecTemplateSpecContainerPort(
        #                                 container_port=4000,
        #                                 name="http",
        #                             )
        #                         ]
        #                     )
        #                 ],
        #             ),
        #         ),
        #     ),
        #     scope=self,
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
