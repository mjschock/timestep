from constructs import Construct
from timestep.config import Settings
from timestep.infra.imports.helm.release import Release, ReleaseSet, ReleaseSetSensitive
from timestep.infra.imports.kubernetes.ingress_v1 import (
    IngressV1,
    IngressV1Metadata,
    IngressV1Spec,
    IngressV1SpecRule,
    IngressV1SpecRuleHttp,
    IngressV1SpecRuleHttpPath,
    IngressV1SpecRuleHttpPathBackend,
    IngressV1SpecRuleHttpPathBackendService,
    IngressV1SpecRuleHttpPathBackendServicePort,
)
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
            provider=kubernetes_cluster_ingress_construct.helm_provider,
            set=[
                # ReleaseSet(
                #     name="ingress.annotations.kubernetes\\.io/ingress\\.class",
                #     value="caddy",
                # ),
                # # ReleaseSet(
                # #     name="ingress.className",
                # #     value="caddy",
                # # ),
                # ReleaseSet(
                #     name="ingress.enabled",
                #     value="true",
                # ),
                # ReleaseSet(
                #     name="ingress.host.hostname",
                #     value=f"prefect-server.{config.primary_domain_name}",
                # ),
                # ReleaseSet(
                #     name="ingress.host.path",
                #     value="/",
                # ),
                # ReleaseSet(
                #     name="ingress.host.pathType",
                #     value="Prefix",
                # ),
                # ReleaseSet(
                #     name="ingress.selfSigned",
                #     value="true",
                # ),
                # ReleaseSet(
                #     name="ingress.tls",
                #     value="true",
                # ),
                ReleaseSet(
                    name="postgresql.enabled",
                    value="true",
                ),
                ReleaseSet(
                    name="postgresql.useSubChart",
                    value="true",
                ),
                ReleaseSet(
                    name="server.image.prefectTag",
                    value="2.11-python3.11",
                ),
                ReleaseSet(
                    name="server.image.repository",
                    value="prefecthq/prefect",
                ),
                ReleaseSet(
                    name="server.publicApiUrl",
                    value=f"https://prefect-server.{config.primary_domain_name}/api",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="postgresql.auth.password",
                    value=config.postgresql_password.get_secret_value(),
                )
            ],
            scope=self,
        )

        IngressV1(
            depends_on=[
                self.prefect_helm_release_resource,
            ],
            id_="prefect_system_ingress",
            metadata=IngressV1Metadata(
                annotations={
                    # "cert-manager.io/cluster-issuer": cert_manager_cluster_issuer,
                    # "cert-manager.io/issuer": issuer_type,
                    # "ingress.kubernetes.io/proxy-body-size": "0",
                    # "ingress.kubernetes.io/ssl-redirect": "true",
                    "kubernetes.io/ingress.class": "caddy",
                    # "meta.helm.sh/release-name": helm_release_name,
                    # "meta.helm.sh/release-namespace": helm_release_namespace,
                    # f"{ingress_class}.ingress.kubernetes.io/proxy-body-size": "0",
                    # f"{ingress_class}.ingress.kubernetes.io/ssl-redirect": "true",
                },
                # labels={
                #     "app.kubernetes.io/instance": helm_release_name,
                #     "app.kubernetes.io/managed-by": "Helm",
                #     "app.kubernetes.io/name": helm_release_name,
                #     "helm.sh/chart": f"{helm_release_name}-{helm_release_chart_version}",  # noqa: E501
                # },
                name="prefect-server",
                namespace="prefect-system",
                # namespace=namespace,
            ),
            scope=self,
            spec=IngressV1Spec(
                # ingress_class_name=ingress_class,
                rule=[
                    IngressV1SpecRule(
                        host=f"prefect-server.{config.primary_domain_name}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name="prefect-server",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                # name=path["service_port_name"],
                                                number=4200,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                    # path_type=path["path_type"],
                                ),
                                # IngressV1SpecRuleHttpPath(
                                #     backend=IngressV1SpecRuleHttpPathBackend(
                                #         service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
                                #             name="example2",
                                #             port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
                                #                 # name=path["service_port_name"],
                                #                 number=8080,
                                #             ),
                                #         ),
                                #     ),
                                #     path="/hello2",
                                #     path_type="Prefix",
                                #     # path_type=path["path_type"],
                                # ),
                            ]
                        ),
                    ),
                    # IngressV1SpecRule(
                    #     host=f"example2.{config.primary_domain_name}",
                    #     http=IngressV1SpecRuleHttp(
                    #         path=[
                    #             IngressV1SpecRuleHttpPath(
                    #                 backend=IngressV1SpecRuleHttpPathBackend(
                    #                     service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
                    #                         name="example1",
                    #                         port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
                    #                             # name=path["service_port_name"],
                    #                             number=8080,
                    #                         ),
                    #                     ),
                    #                 ),
                    #                 path="/hello1",
                    #                 path_type="Prefix",
                    #                 # path_type=path["path_type"],
                    #             ),
                    #             IngressV1SpecRuleHttpPath(
                    #                 backend=IngressV1SpecRuleHttpPathBackend(
                    #                     service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
                    #                         name="example2",
                    #                         port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
                    #                             # name=path["service_port_name"],
                    #                             number=8080,
                    #                         ),
                    #                     ),
                    #                 ),
                    #                 path="/hello2",
                    #                 path_type="Prefix",
                    #                 # path_type=path["path_type"],
                    #             ),
                    #         ]
                    #     ),
                    # )
                ],
                # tls=[
                #     IngressV1SpecTls(
                #         hosts=[host],
                #         # secret_name=f"{host}-tls",
                #         secret_name=f"{ingress_name}-tls",
                #     )
                # ],
            ),
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

        # kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     depends_on=[self.prefect_helm_release_resource],
        #     helm_release_chart_version=self.prefect_helm_release_resource.version,
        #     helm_release_name=self.prefect_helm_release_resource.name,
        #     helm_release_namespace=self.prefect_helm_release_resource.namespace,
        #     host=f"prefect-server.{config.primary_domain_name}",
        #     id="prefect_ingress_resource",
        #     ingress_class="caddy",
        #     ingress_name=f"{self.prefect_helm_release_resource.name}-ingress",
        #     namespace=self.prefect_helm_release_resource.namespace,
        #     paths=[
        #         {
        #             "path": "/",
        #             "path_type": "Prefix",
        #             "service_name": "prefect-server",
        #             "service_port_name": "server-svc-port",
        #             "service_port_number": None,
        #         },
        #     ],
        # )
