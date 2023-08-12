from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
from cdktf_cdktf_provider_helm.release import Release
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
from constructs import Construct
from timestep.config import Settings
from timestep.infra.stacks.main.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.main.constructs.kube_config.construct import (
    KubeConfigConstruct,
)


class KubernetesClusterIngressConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        cloud_instance_construct: CloudInstanceConstruct,
        kube_config_contruct: KubeConfigConstruct,
    ) -> None:
        super().__init__(scope, id)

        self.kubernetes_provider = KubernetesProvider(
            id="kubernetes_provider",
            # config_context=config.KUBE_CONTEXT,
            # config_path=config.KUBE_CONFIG_PATH,
            config_context=config.kubecontext,
            config_path=kube_config_contruct.data_source.filename,
            scope=self,
        )

        self.helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                # config_context=config.KUBE_CONTEXT,
                # config_path=config.KUBE_CONFIG_PATH,
                config_context=self.kubernetes_provider.config_context,
                config_path=self.kubernetes_provider.config_path,
            ),
            scope=self,
        )

        self.caddy_ingress_controller_helm_release_resource = Release(  # noqa: F841
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            create_namespace=True,
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=self.helm_provider,
            set=[
                {
                    "name": "ingressController.config.acmeCA",
                    "value": "https://acme-staging-v02.api.letsencrypt.org/directory",
                },
                {
                    "name": "ingressController.config.debug",
                    "value": "true",
                },
                {
                    "name": "ingressController.config.email",
                    "value": config.ingress_controller_email,
                },
                # {
                #     "name": "ingressController.config.onDemandTLS",
                #     "value": "true",
                # },
            ],
            scope=self,
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
        #                         ],
        #                     ),
        #                 ]
        #             ),
        #         ),
        #     ),
        # )

        # example2_deployment_resource = DeploymentV1(
        #     id_="example2_deployment_resource",
        #     metadata=DeploymentV1Metadata(
        #         annotations=None,
        #         labels={
        #             "app": "example2",
        #         },
        #         name="example2",
        #     ),
        #     scope=self,
        #     spec=DeploymentV1Spec(
        #         replicas="1",
        #         selector=DeploymentV1SpecSelector(
        #             match_labels={
        #                 "app": "example2",
        #             },
        #         ),
        #         template=DeploymentV1SpecTemplate(
        #             metadata=DeploymentV1SpecTemplateMetadata(
        #                 labels={
        #                     "app": "example2",
        #                 },
        #             ),
        #             spec=DeploymentV1SpecTemplateSpec(
        #                 container=[
        #                     DeploymentV1SpecTemplateSpecContainer(
        #                         args=[
        #                             "-listen=:8080",
        #                             "-text=hello world 2",
        #                         ],
        #                         image="hashicorp/http-echo",
        #                         name="httpecho",
        #                         port=[
        #                             DeploymentV1SpecTemplateSpecContainerPort(
        #                                 container_port=8080,
        #                             )
        #                         ],
        #                     ),
        #                 ]
        #             ),
        #         ),
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
        #                 name="http",
        #                 port=8080,
        #                 protocol="TCP",
        #                 target_port="8080",
        #             ),
        #         ],
        #         selector={
        #             "app": "example1",
        #         },
        #         type="ClusterIP",
        #     ),
        # )

        # example2_service_resource = ServiceV1(
        #     depends_on=[example2_deployment_resource],
        #     id_="example2_service_resource",
        #     metadata=ServiceV1Metadata(
        #         name="example2",
        #     ),
        #     scope=self,
        #     spec=ServiceV1Spec(
        #         port=[
        #             ServiceV1SpecPort(
        #                 name="http",
        #                 port=8080,
        #                 protocol="TCP",
        #                 target_port="8080",
        #             ),
        #         ],
        #         selector={
        #             "app": "example2",
        #         },
        #         type="ClusterIP",
        #     ),
        # )

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
