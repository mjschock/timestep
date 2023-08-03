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
            # chart="postgresql",
            chart="supabase",
            create_namespace=True,
            name="postgresql",
            namespace="postgresql",
            repository="https://charts.bitnami.com/bitnami",
            provider=self.kubernetes_cluster_ingress_construct.helm_provider,
            set=[
                # ReleaseSet(
                #     name="architecture",
                #     value="standalone",
                # ),
                ReleaseSet(
                    name="auth.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="meta.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="realtime.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="rest.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="storage.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="studio.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="kong.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="postgresql.enabled",
                    value="true",
                ),
                ReleaseSet(
                    name="postgresql.architecture",
                    value="standalone",
                ),
            ],
            set_sensitive=[
                # ReleaseSetSensitive(
                #     name="auth.postgresPassword",
                #     value=config.secrets.get_secret_value().get(
                #         "postgresql_password"
                #     ),  # noqa: E501
                # )
                ReleaseSetSensitive(
                    name="postgresql.auth.postgresPassword",
                    value=config.postgresql_password.get_secret_value(),
                )
            ],
            scope=self,
        )
