from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider
from timestep.infra.imports.helm.provider import HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)


class ContainerRegistryConstruct(Construct):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        # def __init__(self, id: str, scope: Construct) -> None:
        super().__init__(id=id, scope=scope)
        get_run_logger()

        kubernetes_provider = KubernetesTerraformProvider(
            config_context=scope.kube_config_construct.outputs.get(
                "config_context"
            ).value,
            config_path=scope.kube_config_construct.outputs.get("config_path").value,
            id="kubernetes_provider",
            scope=scope,
        )

        helm_provider = HelmTerraformProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                # config_context=config.KUBE_CONTEXT,
                # config_path=config.KUBE_CONFIG_PATH,
                config_context=kubernetes_provider.config_context,
                config_path=kubernetes_provider.config_path,
            ),
            scope=scope,
        )

        HelmReleaseTerraformResource(
            id_="docker_registry_helm_release_resource",
            atomic=True,
            chart="docker-registry",
            name="docker-registry",
            # namespace=caddy_ingress_controller_helm_release_resource.namespace,
            repository="https://helm.twun.io",
            provider=helm_provider,
            set=[  # https://github.com/twuni/docker-registry.helm#configuration
                # ReleaseSet(
                #     name="ingress.annotations.kubernetes\\.io/ingress\\.class",
                #     value="caddy",
                # ),
                # ReleaseSet(
                #     name="ingress.className",
                #     value="caddy",
                # ),
                # ReleaseSet(
                #     name="ingress.enabled",
                #     value="false",
                # ),
                # # {
                # #     "name": "ingress.labels",
                # #     "value": {},
                # # },
                # ReleaseSet(
                #     name="ingress.path",
                #     value="/",
                # )
                # {
                #     "name": "ingress.tls",
                #     "value": []
                # }
                # {
                #     "name": "persistence.enabled",
                #     "value": "false",
                # },
                # {
                #     "name": "secrets.htpasswd",
                #     "value": "admin:$2y$05$Z3Z1Z3Z1Z3Z1Z3Z",
                #     # "value": "",
                # },
            ],
            set_list=[
                # ReleaseSetListStruct(
                #     name="ingress.hosts",
                #     value=[f"registry.{config.variables.get('primary_domain_name')}"],
                # ),
                # {
                #     "name": "ingress.tls",
                #     "value": [
                #         {
                #             "hosts": [
                #                 "registry.timestep.local"
                #             ],
                #             "secretName": "ssl-registry.timestep.local"
                #         }
                #     ],
                # },
            ],
            scope=scope,
        )

        # IngressV1(
        #     scope=scope,
        #     id_="docker_registry_ingress_resource",
        #     metadata=IngressV1Metadata(
        #         annotations={
        #             "kubernetes.io/ingress.class": "caddy",
        #         },
        #         name=docker_registry_helm_release_resource.name,
        #         namespace=docker_registry_helm_release_resource.namespace,
        #     ),
        #     spec=IngressV1Spec(
        #         ingress_class_name="caddy",
        #         rule=[
        #             IngressV1SpecRule(
        #                 host=f"registry.{config.variables.get('primary_domain_name')}",  # noqa: E501
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name="docker-registry",
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         number=5000,
        #                                     ),
        #                                 )
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         )
        #                     ]
        #                 ),
        #             )
        #         ],
        #         # tls=[
        #         #     IngressV1SpecTls(
        #         #         hosts=[
        #         #             "registry.timestep.local"
        #         #         ],
        #         #         secret_name="ssl-registry.timestep.local"
        #         #     )
        #         # ],
        #     ),
        # )

        # app_name = "caddy-server"

        # Deployment(
        #     scope=self,
        #     id_="caddy_server_deployment_resource",
        #     metadata={
        #         "name": app_name,
        #         # "namespace": caddy_ingress_controller_helm_release_resource.namespace,  # noqa: E501
        #         "labels": {"app": app_name},
        #     },
        #     spec={
        #         #    'replicas': 2,
        #         "selector": {"match_labels": {"app": app_name}},
        #         "template": {
        #             "metadata": {"labels": {"app": app_name}},
        #             "spec": {
        #                 "container": [
        #                     {
        #                         "image": "caddy",
        #                         "name": app_name,
        #                         "ports": [
        #                             {"containerPort": 80},
        #                             {"containerPort": 443},
        #                         ],
        #                     }
        #                 ]
        #             },
        #         },
        #     },
        # )

        # Service(
        #     scope=self,
        #     id_="caddy_server_service_resource",
        #     metadata={
        #         "name": app_name,
        #         # "namespace": caddy_ingress_controller_helm_release_resource.namespace,  # noqa: E501
        #     },
        #     spec={
        #         "selector": {"app": app_name},
        #         "port": [
        #             {"name": "http", "port": 80, "target_port": 80},
        #             {"name": "https", "port": 443, "target_port": 443},
        #         ],
        #     },
        # )

        # # caddy_server_ingress_resource = Ingress(
        # #     scope=self,
        # #     id_='caddy_server_ingress_resource',
        # #     metadata={
        # #         'name': app_name,
        # #         'namespace': caddy_ingress_controller_helm_release_resource.namespace,  # noqa: E501
        # #         'annotations': {
        # #             'kubernetes.io/ingress.class': 'caddy',
        # #         }
        # #     },
        # #     spec={
        # #         'rule': [{
        # #             'host': config.variables.get('primary_domain_name'),
        # #             'http': {
        # #                 'path': [{
        # #                     'path': '/',
        # #                     'backend': {
        # #                         'serviceName': app_name,
        # #                         'servicePort': 80
        # #                     }
        # #                 }]
        # #             }
        # #         }]
        # #     }
        # # )

        # IngressV1(
        #     scope=scope,
        #     id_="docker_registry_ingcaddy_server_ingress_resourceress_resource",
        #     metadata=IngressV1Metadata(
        #         annotations={
        #             "kubernetes.io/ingress.class": "caddy",
        #             # "cert-manager.io/cluster-issuer": "letsencrypt-staging",
        #         },
        #         # name=docker_registry_helm_release_resource.name,
        #         # namespace=docker_registry_helm_release_resource.namespace,
        #         name=app_name,
        #         # namespace=caddy_ingress_controller_helm_release_resource.namespace,
        #     ),
        #     spec=IngressV1Spec(
        #         default_backend=IngressV1SpecDefaultBackend(
        #             # resource=IngressV1SpecDefaultBackendResource(
        #             #     api_group=ingress_class.api_group,
        #             #     kind=ingress_class.kind,
        #             #     name=ingress_class.name,
        #             # ),
        #             service=IngressV1SpecDefaultBackendService(
        #                 name=app_name,
        #                 port=IngressV1SpecDefaultBackendServicePort(
        #                     # name="http",
        #                     number=443,
        #                 ),
        #             )
        #         ),
        #         ingress_class_name="caddy",
        #         rule=[
        #             IngressV1SpecRule(
        #                 host=f"{config.variables.get('primary_domain_name')}",
        #                 http=IngressV1SpecRuleHttp(
        #                     path=[
        #                         IngressV1SpecRuleHttpPath(
        #                             backend=IngressV1SpecRuleHttpPathBackend(
        #                                 service=IngressV1SpecRuleHttpPathBackendService(  # noqa: E501
        #                                     name=app_name,
        #                                     port=IngressV1SpecRuleHttpPathBackendServicePort(  # noqa: E501
        #                                         number=80,
        #                                     ),
        #                                 )
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         )
        #                     ]
        #                 ),
        #             )
        #         ],
        #         # tls=[
        #         #     IngressV1SpecTls(
        #         #         hosts=[
        #         #             "registry.timestep.local"
        #         #         ],
        #         #         secret_name="ssl-registry.timestep.local"
        #         #     )
        #         # ],
        #     ),
        # )

        # # platform_helm_release_resource = HelmReleaseTerraformResource(
        # #     id_="platform_helm_release_resource",
        # #     atomic=True,
        # #     chart=config.PLATFORM_CHART_PATH,
        # #     # name="timestep-ai-platform",
        # #     name="platform",
        # #     namespace="default",
        # #     provider=helm_provider,
        # #     scope=self,
        # # )
