from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet, ReleaseSetSensitive
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


class MinioConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        # kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.minio_helm_release_resource = Release(
            # depends_on=[self.kubernetes_cluster_ingress_construct],
            id_="minio_helm_release_resource",
            atomic=True,
            chart="minio",
            create_namespace=True,
            name="minio",
            namespace="minio",
            repository="https://charts.bitnami.com/bitnami",
            # provider=self.kubernetes_cluster_ingress_construct.helm_provider,
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="auth.rootUse",
                    value="minio-admin",
                ),
                ReleaseSet(
                    name="defaultBuckets",
                    value="public",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="auth.rootPassword",
                    # value=config.minio_password.get_secret_value(), # TODO
                    value="minio-secret-password",
                )
            ],
            scope=self,
        )

        IngressV1(
            depends_on=[
                self.minio_helm_release_resource,
            ],
            id_="minio_ingress",
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
                name="minio",
                namespace="minio",
                # namespace=namespace,
            ),
            scope=self,
            spec=IngressV1Spec(
                # ingress_class_name=ingress_class,
                rule=[
                    IngressV1SpecRule(
                        host=f"minio.{config.primary_domain_name}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name="minio",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                # name=path["service_port_name"],
                                                number=9000,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                    # path_type=path["path_type"],
                                ),
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
                                            name="minio",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
                                                # name=path["service_port_name"],
                                                number=9001,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                    # path_type=path["path_type"],
                                ),
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
