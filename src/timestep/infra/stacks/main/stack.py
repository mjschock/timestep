from cdktf import (
    CloudBackend,
    LocalBackend,
    NamedCloudWorkspace,
    TerraformStack,
)
from constructs import Construct

from timestep.config import AppConfig
from timestep.infra.imports.helm.release import Release, ReleaseSet
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
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)

        stack_id: str = config.variables.get("primary_domain_name")

        self.cloud_init_config_construct: CloudInitConfigConstruct = (
            CloudInitConfigConstruct(
                config=config,
                id="cloud_init_config_construct",
                scope=self,
            )
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

        Release(
            id_="prefect_helm_release_resource",
            atomic=True,
            chart="prefect-server",
            create_namespace=True,
            name="prefect-server",
            namespace="prefect",
            repository="https://prefecthq.github.io/prefect-helm",
            provider=self.kubernetes_cluster_ingress_construct.helm_provider,
            set=[
                ReleaseSet(
                    name="ingress.enabled",
                    value="true",
                ),
                ReleaseSet(
                    name="ingress.className",
                    value="caddy",
                ),
                ReleaseSet(
                    name="ingress.host.hostname",
                    value=config.variables.get("primary_domain_name"),
                ),
                ReleaseSet(
                    name="ingress.host.path",
                    value="/",
                ),
                ReleaseSet(
                    name="pathType",
                    value="Prefix",
                ),
                ReleaseSet(
                    name="postgresql.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="publicApiUrl",
                    value=f"https://{config.variables.get('primary_domain_name')}",  # noqa: E501
                ),
            ],
            # set_sensitive=[
            #     ReleaseSetSensitive(
            #         name="postgresql.auth.password",
            #         value=config.secrets.get_secret_value().get("postgresql_password"),  # noqa: E501
            #     )
            # ],
            scope=self,
        )

        # prefect_server_ingress_resource = self.kubernetes_cluster_ingress_construct.create_ingress_resource(  # noqa: E501
        #     config=config,
        #     id="prefect_server_ingress_resource",
        #     name="prefect-server",
        #     port=4200,
        # )

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
