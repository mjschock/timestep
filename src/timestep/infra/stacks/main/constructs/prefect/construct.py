from constructs import Construct
from timestep.config import Settings
from timestep.infra.imports.helm.release import Release, ReleaseSet, ReleaseSetSensitive
from timestep.infra.stacks.main.constructs.kubernetes_cluster_ingress.construct import (
    KubernetesClusterIngressConstruct,
)


class PrefectConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct,
        # postgresql_helm_release_resource: PostgreSQLConstruct,
    ) -> None:
        super().__init__(scope, id)

        self.prefect_helm_release_resource = Release(
            depends_on=[kubernetes_cluster_ingress_construct],
            # depends_on=[postgresql_helm_release_resource],
            id_="prefect_helm_release_resource",
            atomic=True,
            chart="prefect-server",
            create_namespace=True,
            name="prefect-server",
            namespace="prefect-system",
            repository="https://prefecthq.github.io/prefect-helm",
            provider=self.kubernetes_cluster_ingress_construct.helm_provider,
            set=[
                ReleaseSet(
                    name="postgresql.enabled",
                    value="true",
                ),
                ReleaseSet(
                    name="postgresql.useSubChart",
                    value="true",
                ),
                ReleaseSet(
                    name="server.publicApiUrl",
                    value=f"https://prefect.{config.variables.get('primary_domain_name')}/api",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="postgresql.auth.password",
                    value=config.secrets.get_secret_value().get(
                        "postgresql_password"
                    ),  # noqa: E501
                )
            ],
            scope=self,
        )

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
