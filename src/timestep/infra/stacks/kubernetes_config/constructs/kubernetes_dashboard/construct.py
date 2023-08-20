from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
from cdktf_cdktf_provider_kubernetes.ingress_v1 import (
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
from constructs import Construct
from timestep.config import Settings


class KubernetesDashboardConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.kubernetes_dashboard_helm_release_resource = Release(
            id_="kubernetes_dashboard_helm_release_resource",
            atomic=True,
            chart="kubernetes-dashboard",
            create_namespace=True,
            name="kubernetes-dashboard",
            namespace="kubernetes-dashboard",
            repository="https://kubernetes.github.io/dashboard",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="app.ingress.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="cert-manager.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="nginx.enabled",
                    value="false",
                ),
            ],
            scope=self,
        )

        IngressV1(
            depends_on=[
                self.kubernetes_dashboard_helm_release_resource,
            ],
            id_="kubernetes_dashboard_ingress",
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
                name="kubernetes-dashboard",
                namespace="kubernetes-dashboard",
                # namespace=namespace,
            ),
            scope=self,
            spec=IngressV1Spec(
                # ingress_class_name=ingress_class,
                rule=[
                    IngressV1SpecRule(
                        host=f"kubernetes-dashboard.{config.primary_domain_name}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name="kubernetes-dashboard",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                # name=path["service_port_name"],
                                                number=443,  # https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard#networkpolicy
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

        # IngressV1(
        #     depends_on=[
        #         example1_service_resource,
        #         example2_service_resource,
        #     ],
        #     id_="example_ingress",
        #     metadata=IngressV1Metadata(
        #         annotations={
        #             # "cert-manager.io/cluster-issuer": cert_manager_cluster_issuer,
        #             # "cert-manager.io/issuer": issuer_type,
        #             # "ingress.kubernetes.io/proxy-body-size": "0",
        #             # "ingress.kubernetes.io/ssl-redirect": "true",
        #             "kubernetes.io/ingress.class": "caddy",
        #             # "meta.helm.sh/release-name": helm_release_name,
        #             # "meta.helm.sh/release-namespace": helm_release_namespace,
        #             # f"{ingress_class}.ingress.kubernetes.io/proxy-body-size": "0",
        #             # f"{ingress_class}.ingress.kubernetes.io/ssl-redirect": "true",
        #         },
        #         # labels={
        #         #     "app.kubernetes.io/instance": helm_release_name,
        #         #     "app.kubernetes.io/managed-by": "Helm",
        #         #     "app.kubernetes.io/name": helm_release_name,
        #         #     "helm.sh/chart": f"{helm_release_name}-{helm_release_chart_version}",  # noqa: E501
        #         # },
        #         name="example",
        #         # namespace=namespace,
        #     ),
        #     scope=self,
        #     spec=IngressV1Spec(
        #         # ingress_class_name=ingress_class,
        #         rule=[
        #             IngressV1SpecRule(
        #                 host=f"example1.{config.primary_domain_name}",
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="example1",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         # name=path["service_port_name"],
        #                                         number=8080,
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/hello1",
        #                             path_type="Prefix",
        #                             # path_type=path["path_type"],
        #                         ),
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="example2",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         # name=path["service_port_name"],
        #                                         number=8080,
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/hello2",
        #                             path_type="Prefix",
        #                             # path_type=path["path_type"],
        #                         ),
        #                     ]
        #                 ),
        #             ),
        #             IngressV1SpecRule(
        #                 host=f"example2.{config.primary_domain_name}",
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="example1",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         # name=path["service_port_name"],
        #                                         number=8080,
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/hello1",
        #                             path_type="Prefix",
        #                             # path_type=path["path_type"],
        #                         ),
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="example2",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         # name=path["service_port_name"],
        #                                         number=8080,
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/hello2",
        #                             path_type="Prefix",
        #                             # path_type=path["path_type"],
        #                         ),
        #                     ]
        #                 ),
        #             ),
        #             #     IngressV1SpecRule(
        #             #         host=f"www.{config.primary_domain_name}",
        #             #         http=IngressV1SpecRuleHttp(
        #             #             path=[
        #             #                 IngressV1SpecRuleHttpPath(
        #             #                     backend=IngressV1SpecRuleHttpPathBackend(
        #             #                         service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #             #                             name="www",
        #             #                             port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #             #                                 # name=path["service_port_name"],  # noqa: E501
        #             #                                 number=8080,
        #             #                             ),
        #             #                         ),
        #             #                     ),
        #             #                     path="/",
        #             #                     path_type="Prefix",
        #             #                     # path_type=path["path_type"],
        #             #                 ),
        #             #             ]
        #             #         ),
        #             #     ),
        #             #     IngressV1SpecRule(
        #             #         host=f"{config.primary_domain_name}",
        #             #         http=IngressV1SpecRuleHttp(
        #             #             path=[
        #             #                 IngressV1SpecRuleHttpPath(
        #             #                     backend=IngressV1SpecRuleHttpPathBackend(
        #             #                         service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #             #                             name="www",
        #             #                             port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #             #                                 # name=path["service_port_name"],  # noqa: E501
        #             #                                 number=8080,
        #             #                             ),
        #             #                         ),
        #             #                     ),
        #             #                     path="/",
        #             #                     path_type="Prefix",
        #             #                     # path_type=path["path_type"],
        #             #                 ),
        #             #             ]
        #             #         ),
        #             #     ),
        #         ],
        #         # tls=[
        #         #     IngressV1SpecTls(
        #         #         hosts=[host],
        #         #         # secret_name=f"{host}-tls",
        #         #         secret_name=f"{ingress_name}-tls",
        #         #     )
        #         # ],
        #     ),
        # )

    # def create_ingress_resource(
    #     self,
    #     config,
    #     depends_on,
    #     host,
    #     id,
    #     ingress_class,
    #     ingress_name,
    #     paths,
    #     # service_name,
    #     cert_manager_cluster_issuer="letsencrypt-prod",
    #     helm_release_chart_version=None,
    #     helm_release_name=None,
    #     helm_release_namespace=None,
    #     namespace="default",
    #     # service_port_name=None,
    #     # service_port_number=None,
    #     # path="/",
    #     # path_type="ImplementationSpecific",
    #     # issuer_type="letsencrypt-prod-issue",
    # ):  # noqa: E501
    #     IngressV1(
    #         depends_on=depends_on,
    #         id_=id,
    #         metadata=IngressV1Metadata(
    #             annotations={
    #                 "cert-manager.io/cluster-issuer": cert_manager_cluster_issuer,
    #                 # "cert-manager.io/issuer": issuer_type,
    #                 # "ingress.kubernetes.io/proxy-body-size": "0",
    #                 # "ingress.kubernetes.io/ssl-redirect": "true",
    #                 "kubernetes.io/ingress.class": ingress_class,
    #                 # "meta.helm.sh/release-name": helm_release_name,
    #                 # "meta.helm.sh/release-namespace": helm_release_namespace,
    #                 # f"{ingress_class}.ingress.kubernetes.io/proxy-body-size": "0",
    #                 # f"{ingress_class}.ingress.kubernetes.io/ssl-redirect": "true",
    #             },
    #             # labels={
    #             #     "app.kubernetes.io/instance": helm_release_name,
    #             #     "app.kubernetes.io/managed-by": "Helm",
    #             #     "app.kubernetes.io/name": helm_release_name,
    #             #     "helm.sh/chart": f"{helm_release_name}-{helm_release_chart_version}",  # noqa: E501
    #             # },
    #             name=ingress_name,
    #             namespace=namespace,
    #         ),
    #         scope=self,
    #         spec=IngressV1Spec(
    #             ingress_class_name=ingress_class,
    #             rule=[
    #                 IngressV1SpecRule(
    #                     host=host,
    #                     http=IngressV1SpecRuleHttp(
    #                         path=[
    #                             IngressV1SpecRuleHttpPath(
    #                                 backend=IngressV1SpecRuleHttpPathBackend(
    #                                     service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
    #                                         name=path["service_name"],
    #                                         port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
    #                                             name=path["service_port_name"],
    #                                             number=path["service_port_number"],
    #                                         ),
    #                                     ),
    #                                 ),
    #                                 path=path["path"],
    #                                 # path_type="Prefix",
    #                                 path_type=path["path_type"],
    #                             ) for path in paths
    #                         ]
    #                     ),
    #                 )
    #             ],
    #             tls=[
    #                 IngressV1SpecTls(
    #                     hosts=[host],
    #                     # secret_name=f"{host}-tls",
    #                     secret_name=f"{ingress_name}-tls",
    #                 )
    #             ],
    #         ),
    #     )
