from cdktf import (
    LocalBackend,
    TerraformStack,
)
from constructs import Construct

from timestep.config import CloudInstanceProvider
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

        # stack_id: str = config.primary_domain_name
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

        stack_id = config.primary_domain_name

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            LocalBackend(
                path=f"terraform.{stack_id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            # CloudBackend(
            #     hostname=config.variables.get("tf_hostname"),
            #     organization=config.variables.get("tf_organization"),
            #     scope=self,
            #     token=config.secrets.get_secret_value().get("tf_api_token"),
            #     workspaces=NamedCloudWorkspace(config.variables.get("tf_workspace")),
            # )

            raise NotImplementedError(
                f"CloudInstanceProvider: {config.cloud_instance_provider}"
            )  # noqa: E501
