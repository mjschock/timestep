from cdktf import (
    CloudBackend,
    LocalBackend,
    NamedCloudWorkspace,
    TerraformStack,
)
from constructs import Construct

# from timestep.config import AppConfig
from timestep.infra.stacks.main.constructs.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.main.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.main.constructs.cloud_instance_domain.construct import (
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.main.constructs.domain_name_registrar.construct import (
    DomainNameRegistrarConstruct,
)
from timestep.infra.stacks.main.constructs.kube_config.construct import (
    KubeConfigConstruct,
)
from timestep.infra.stacks.main.constructs.kubernetes_cluster_ingress.construct import (
    KubernetesClusterIngressConstruct,
)


class MainStack(TerraformStack):
    # def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
    def __init__(self, scope: Construct, id: str, config: dict[str, str]) -> None:
        super().__init__(scope, id)

        # cloud_instance_provider = TerraformVariable(
        #     scope=self,
        #     id="cloud_instance_provider",
        #     type=VariableType.STRING,
        #     default=config.get("CLOUD_INSTANCE_PROVIDER", None),
        #     nullable=False,
        # )

        # primary_domain_name = TerraformVariable(
        #     scope=self,
        #     id="primary_domain_name",
        #     type=VariableType.STRING,
        #     default=config.get("PRIMARY_DOMAIN_NAME", None),
        #     nullable=False,
        # )

        # public_variables = TerraformVariable(
        #     scope=self,
        #     id="public_variables",
        #     type=VariableType.MAP,
        #     nullable=False,
        #     default={
        #         "primary_domain_name": primary_domain_name,
        #     },
        # )

        # public_variables = TerraformVariable(
        #     scope=self,
        #     id="public_variables",
        #     # type=VariableType.MAP,
        #     type=VariableType.object({
        #         "primary_domain_name": VariableType.STRING,
        #     }),
        #     nullable=False,
        #     default={
        #         "primary_domain_name": primary_domain_name,
        #     },
        # )

        # stack_id: str = config.variables.get("primary_domain_name")
        # stack_id: str = config.value.get("primary_domain_name")
        # stack_id: str = config.

        self.cloud_init_config_construct: CloudInitConfigConstruct = CloudInitConfigConstruct(  # noqa: E501
            # config=config,
            # config=public_variables,
            # config=primary_domain_name,
            # config=cloud_instance_provider,
            config=config,
            id="cloud_init_config_construct",
            scope=self,
        )

        self.cloud_instance_construct: CloudInstanceConstruct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct: CloudInstanceDomainConstruct = (
            CloudInstanceDomainConstruct(  # noqa: E501
                cloud_instance_construct=self.cloud_instance_construct,
                config=config,
                id="cloud_instance_domain_construct",
                scope=self,
            )
        )

        self.domain_name_registar_construct: DomainNameRegistrarConstruct = (
            DomainNameRegistrarConstruct(  # noqa: E501
                config=config,
                id="domain_name_registar_construct",
                scope=self,
            )
        )

        self.kube_config_contruct: KubeConfigConstruct = KubeConfigConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="kube_config_contruct",
            scope=self,
        )

        self.kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct = (
            KubernetesClusterIngressConstruct(  # noqa: E501
                cloud_instance_construct=self.cloud_instance_construct,
                config=config,
                id="kubernetes_cluster_ingress_construct",
                kube_config_contruct=self.kube_config_contruct,
                scope=self,
            )
        )

        # self.kubernetes_cluster_ingress_construct.create_ingress_resource(  # noqa: E501
        #     config=config,
        #     host=f"registry.{config.variables.get('primary_domain_name')}",
        #     id="docker_registry_ingress_resource",
        #     # ingress_class="caddy",
        #     ingress_class="traefik-internal",
        #     issue_type="letsencrypt-staging-issuer",
        #     name="docker-registry",
        #     # path_type="Prefix",
        #     port=5000,
        # )

        # Release(
        #     id_="docker_registry_helm_release_resource",
        #     atomic=True,
        #     chart="docker-registry",
        #     create_namespace=True,
        #     name="docker-registry",
        #     namespace="default",
        #     repository="https://helm.twun.io",
        #     provider=self.kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="ingress.annotations.cert-manager\\.io/cluster-issuer",
        #             value="letsencrypt-staging",
        #         ),
        #         ReleaseSet(
        #             name="ingress.annotations.kubernetes\\.io/ingress\\.class",
        #             value="traefik-internal",
        #         ),
        #         ReleaseSet(
        #             name="ingress.className",
        #             value="traefik-internal",
        #         ),
        #         ReleaseSet(
        #             name="ingress.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="ingress.hosts[0]",
        #             value=f"registry.{config.variables.get('primary_domain_name')}",
        #         ),
        #         ReleaseSet(
        #             name="persistence.enabled",
        #             value="true",
        #         ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="secrets.htpasswd",
        #             # value=config.secrets.get_secret_value().get("postgresql_password"),  # noqa: E501
        #             value=config.secrets.get_secret_value().get("docker_registry_htpasswd"),  # noqa: E501
        #         )
        #     ],
        #     scope=self,
        # )

        # example1_deployment_resource = DeploymentV1(
        #     id_="example1_deployment_resource",
        #     metadata=DeploymentV1Metadata(
        #         annotations=None,
        #         labels={
        #             "app": "example1",
        #         },
        #         name="example1",
        #     ),
        #     scope=self,
        #     spec=DeploymentV1Spec(
        #         replicas="1",
        #         selector=DeploymentV1SpecSelector(
        #             match_labels={
        #                 "app": "example1",
        #             },
        #         ),
        #         template=DeploymentV1SpecTemplate(
        #             metadata=DeploymentV1SpecTemplateMetadata(
        #                 labels={
        #                     "app": "example1",
        #                 },
        #             ),
        #             spec=DeploymentV1SpecTemplateSpec(
        #                 container=[
        #                     DeploymentV1SpecTemplateSpecContainer(
        #                         args=[
        #                             "-listen=:8080",
        #                             "-text=hello world 1",
        #                         ],
        #                         image="hashicorp/http-echo",
        #                         name="httpecho",
        #                         port=[
        #                             DeploymentV1SpecTemplateSpecContainerPort(
        #                                 container_port=8080,
        #                             )
        #                         ]
        #                     ),
        #                 ]
        #             ),
        #         )
        #     ),
        # )

        # example1_service_resource = ServiceV1(
        #     depends_on=[example1_deployment_resource],
        #     id_="example1_service_resource",
        #     metadata=ServiceV1Metadata(
        #         name="example1",
        #     ),
        #     scope=self,
        #     spec=ServiceV1Spec(
        #         port=[
        #             ServiceV1SpecPort(
        #                 port=8080,
        #                 protocol="TCP",
        #                 target_port="8080",
        #             ),
        #         ],
        #         selector={
        #             "app": "example1",
        #         },
        #         type="ClusterIP",
        #     )
        # )

        # self.kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     depends_on=[example1_service_resource],
        #     host=f"example1.{config.variables.get('primary_domain_name')}",
        #     id="example1_ingress_resource",
        #     ingress_class="caddy",
        #     name="example1",
        #     path="/",
        #     path_type="Prefix",
        #     port=8080,
        # )

        # self.kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     host=f"registry.{config.variables.get('primary_domain_name')}",
        #     id="registry_ingress_resource",
        #     ingress_class="caddy",
        #     name="registry",
        #     path="/",
        #     path_type="Prefix",
        #     port=5000,
        # )

        # supabase_release_resource = Release(
        #     id_="supabase_release_resource",
        #     atomic=True,
        #     chart="supabase",
        #     # create_namespace=True,
        #     force_update=True,
        #     name="supabase",
        #     # namespace="prefect-system",
        #     # repository="oci://registry-1.docker.io/bitnamicharts/supabase",
        #     repository="https://charts.bitnami.com/bitnami",
        #     provider=self.kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="kong.enabled",
        #             value="true",
        #         ),
        #         # ReleaseSet(
        #         #     name="server.publicApiUrl",
        #         #     value=f"https://prefect.{config.variables.get('primary_domain_name')}/api",
        #         # ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="postgresql.auth.postgresPassword",
        #             value=config.secrets.get_secret_value().get("postgresql_password"),  # noqa: E501
        #         )
        #     ],
        #     scope=self,
        # )

        # jwt_auto_generate_config_map_resource = ConfigMapV1(
        #     id_="config_map_resource",
        # )

        # jwt_auto_generate_secret_resource = SecretV1(
        #     id_="secret_resource",
        #     string_data={
        #         "JWT_AUTO_GENERATE_KEY": config.secrets.get_secret_value().get("jwt_auto_generate_key"),  # noqa: E501
        #     },
        # )

        # supabase_release_resource = Release(
        #     id_="supabase_release_resource",
        #     atomic=True,
        #     chart="supabase",
        #     # create_namespace=True,
        #     # force_update=True,
        #     name="supabase",
        #     # namespace="prefect-system",
        #     # repository="oci://registry-1.docker.io/bitnamicharts/supabase",
        #     repository="https://charts.bitnami.com/bitnami",
        #     # repository="https://github.com/supabase-community/supabase-kubernetes/tree/main/charts/supabase",  # noqa: E501
        #     provider=self.kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="auth.enabled",
        #             value="true",
        #         ),
        #         # ReleaseSet(
        #         #     name="jwt.autoGenerate.extraEnvVarsCM",
        #         #     value=jwt_auto_generate_config_map_resource.id,
        #         # ),
        #         # ReleaseSet(
        #         #     name="jwt.autoGenerate.extraEnvVarsSecret",
        #         #     value=jwt_auto_generate_secret_resource.id,
        #         # ),
        #         ReleaseSet(
        #             name="jwt.autoGenerate.forceRun",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="kong.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="kong.ingress.enabled",
        #             value="false",
        #         ),
        #         ReleaseSet(
        #             name="kong.ingress.hostname",
        #             value=f"supabase.{config.variables.get('primary_domain_name')}",
        #         ),
        #         ReleaseSet(
        #             name="kong.ingressController.enabled",
        #             value="false",
        #         ),
        #         ReleaseSet(
        #             name="meta.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="postgresql.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="publicURL",
        #             # value=f"https://api.{config.variables.get('primary_domain_name')}",
        #             value=f"https://supabase.{config.variables.get('primary_domain_name')}",  # noqa: E501
        #         ),
        #         ReleaseSet(
        #             name="realtime.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="rest.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="storage.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="studio.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="studio.ingress.enabled",
        #             value="false",
        #         ),
        #         # ReleaseSet(
        #         #     name="studio.ingress.hostname",
        #         #     value=f"supabase-studio.{config.variables.get('primary_domain_name')}",  # noqa: E501
        #         # ),
        #         ReleaseSet(
        #             name="studio.publicURL",
        #             # value=f"https://studio.{config.variables.get('primary_domain_name')}",
        #             value=f"https://supabase-studio.{config.variables.get('primary_domain_name')}",  # noqa: E501
        #         ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="postgresql.auth.postgresPassword",
        #             value=config.secrets.get_secret_value().get("postgresql_password"),  # noqa: E501
        #         )
        #     ],
        #     scope=self,
        # )

        # prefect_helm_release_resource = Release(
        #     depends_on=[supabase_release_resource],
        #     id_="prefect_helm_release_resource",
        #     atomic=True,
        #     chart="prefect-server",
        #     create_namespace=True,
        #     name="prefect-server",
        #     namespace="prefect-system",
        #     repository="https://prefecthq.github.io/prefect-helm",
        #     provider=self.kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="postgresql.enabled",
        #             value="true",
        #         ),
        #         ReleaseSet(
        #             name="postgresql.useSubChart",
        #             value="false",
        #         ),
        #         ReleaseSet(
        #             name="server.publicApiUrl",
        #             value=f"https://prefect.{config.variables.get('primary_domain_name')}/api",
        #         ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="postgresql.auth.password",
        #             value=config.secrets.get_secret_value().get("postgresql_password"),  # noqa: E501
        #         )
        #     ],
        #     scope=self,
        # )

        # prefect_helm_agent_release_resource = Release(
        #     depends_on=[prefect_helm_release_resource],
        #     id_="prefect_helm_agent_release_resource",
        #     atomic=True,
        #     chart="prefect-agent",
        #     # create_namespace=True,
        #     name="prefect-agent",
        #     namespace="prefect-system",
        #     repository="https://prefecthq.github.io/prefect-helm",
        #     provider=self.kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="agent.apiConfig",
        #             value="server",
        #         ),
        #         ReleaseSet(
        #             name="agent.config.workPool",
        #             value="default-agent-pool",
        #         ),
        #         ReleaseSet(
        #             name="agent.serverApiConfig.apiUrl",
        #             value="http://prefect-server.prefect-system.svc.cluster.local:4200/api",  # noqa: E501
        #         ),
        #     ],
        #     scope=self,
        # )

        # prefect_helm_worker_release_resource = Release(
        #     depends_on=[prefect_helm_release_resource],
        #     id_="prefect_helm_worker_release_resource",
        #     atomic=True,
        #     chart="prefect-worker",
        #     # create_namespace=True,
        #     name="prefect-worker",
        #     namespace="prefect-system",
        #     repository="https://prefecthq.github.io/prefect-helm",
        #     provider=self.kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="worker.apiConfig",
        #             value="server",
        #         ),
        #         ReleaseSet(
        #             name="worker.config.workPool",
        #             value="default-worker-pool",
        #         ),
        #         ReleaseSet(
        #             name="worker.serverApiConfig.apiUrl",
        #             value="http://prefect-server.prefect-system.svc.cluster.local:4200/api",  # noqa: E501
        #         ),
        #     ],
        #     scope=self,
        # )

        # self.kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     depends_on=[prefect_helm_release_resource],
        #     host=f"prefect.{config.variables.get('primary_domain_name')}",
        #     id="prefect_ingress_resource",
        #     ingress_class="caddy",
        #     name="prefect-server",
        #     namespace="prefect-system",
        #     path="/",
        #     path_type="Prefix",
        #     port=4200,
        # )

        stack_id = config.primary_domain_name

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInitConfigConstruct.CloudInstanceProvider.MULTIPASS
        ):
            LocalBackend(
                path=f"terraform.{stack_id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            CloudBackend(
                hostname=config.variables.get("tf_hostname"),
                organization=config.variables.get("tf_organization"),
                scope=self,
                token=config.secrets.get_secret_value().get("tf_api_token"),
                workspaces=NamedCloudWorkspace(config.variables.get("tf_workspace")),
            )
