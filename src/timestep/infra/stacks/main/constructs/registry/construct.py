from constructs import Construct
from timestep.config import Settings
from timestep.infra.imports.helm.release import Release, ReleaseSetSensitive
from timestep.infra.stacks.main.constructs.kubernetes_cluster_ingress.construct import (
    KubernetesClusterIngressConstruct,
)


class RegistryConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct,
    ) -> None:
        super().__init__(scope, id)

        self.release_resource = Release(
            depends_on=[self.kubernetes_cluster_ingress_construct],
            id_="registry_helm_release_resource",
            atomic=True,
            chart="harbor",
            create_namespace=True,
            name="harbor",
            namespace="registry",
            repository="https://charts.bitnami.com/bitnami",
            provider=self.kubernetes_cluster_ingress_construct.helm_provider,
            # set=[
            #     ReleaseSet(
            #         name="externalURL",
            #         value="https://core.harbor.domain",
            #     ),
            # ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="adminPassword",
                    value=config.secrets.get_secret_value().get(
                        "registry_password"
                    ),  # noqa: E501
                )
            ],
            scope=self,
        )

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
