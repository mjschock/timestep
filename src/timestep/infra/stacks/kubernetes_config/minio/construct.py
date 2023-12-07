from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet, ReleaseSetSensitive
from constructs import Construct

from timestep.config import Settings


class MinioConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.minio_helm_release_resource = Release(
            id_="minio_helm_release_resource",
            atomic=True,
            chart="minio",
            create_namespace=True,
            name="minio",
            namespace="default",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="auth.rootUser",
                    value=config.minio_root_user,
                ),
                ReleaseSet(
                    name="mode",
                    value="distributed",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="auth.rootPassword",
                    value=config.minio_root_password.get_secret_value(),
                ),
            ],
            scope=self,
        )

        # IngressV1(
        #     depends_on=[
        #         self.minio_helm_release_resource,
        #     ],
        #     id_="minio_api_ingress",
        #     metadata=IngressV1Metadata(
        #         annotations={
        #             "kubernetes.io/ingress.class": "caddy",
        #         },
        #         name="minio-api",
        #         namespace="minio",
        #     ),
        #     scope=self,
        #     spec=IngressV1Spec(
        #         rule=[
        #             IngressV1SpecRule(
        #                 host=f"minio.{config.primary_domain_name}",
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="minio",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         number=9000,
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         ),
        #                     ]
        #                 ),
        #             ),
        #         ],
        #     ),
        # )

        # IngressV1(
        #     depends_on=[
        #         self.minio_helm_release_resource,
        #     ],
        #     id_="minio_ingress",
        #     metadata=IngressV1Metadata(
        #         annotations={
        #             "kubernetes.io/ingress.class": "caddy",
        #         },
        #         name="minio",
        #         namespace="minio",
        #     ),
        #     scope=self,
        #     spec=IngressV1Spec(
        #         rule=[
        #             IngressV1SpecRule(
        #                 host=f"minio.{config.primary_domain_name}",
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="minio",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         number=9001,
        #                                     ),
        #                                 ),
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         ),
        #                     ]
        #                 ),
        #             ),
        #         ],
        #     ),
        # )
