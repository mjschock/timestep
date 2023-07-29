from constructs import Construct
from timestep.config import Settings
from timestep.infra.imports.helm.release import Release, ReleaseSet, ReleaseSetSensitive
from timestep.infra.stacks.main.constructs.kubernetes_cluster_ingress.construct import (
    KubernetesClusterIngressConstruct,
)


class PostgreSQLConstruct(Construct):
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
            id_="postgresql_helm_release_resource",
            atomic=True,
            chart="postgresql",
            create_namespace=True,
            name="postgresql",
            namespace="postgresql",
            repository="https://charts.bitnami.com/bitnami",
            provider=self.kubernetes_cluster_ingress_construct.helm_provider,
            set=[
                ReleaseSet(
                    name="architecture",
                    value="standalone",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="auth.postgresPassword",
                    value=config.secrets.get_secret_value().get(
                        "postgresql_password"
                    ),  # noqa: E501
                )
            ],
            scope=self,
        )
