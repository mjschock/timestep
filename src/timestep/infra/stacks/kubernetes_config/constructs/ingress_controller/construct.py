from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.helm.provider import HelmProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release, ReleaseSet
from timestep.infra.imports.kubernetes.deployment_v1 import DeploymentV1
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)
from timestep.infra.imports.kubernetes.service_v1 import ServiceV1
from timestep.infra.stacks.k3s_cluster.constructs.kube_config.blocks import (
    KubeConfigConstruct,
)


class IngressControllerConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: AppConfig,
        kube_config_construct: KubeConfigConstruct,
    ) -> None:  # noqa: E501
        # def __init__(self, id: str, scope: Construct) -> None:
        super().__init__(id=id, scope=scope)
        get_run_logger()

        kubernetes_provider = KubernetesTerraformProvider(
            config_context=kube_config_construct.outputs.get("config_context").value,
            config_path=kube_config_construct.outputs.get("config_path").value,
            id="kubernetes_provider",
            scope=scope,
        )

        helm_provider = HelmProvider(
            id="helm_provider",
            # helm_driver postgres?
            kubernetes=HelmProviderKubernetes(
                config_context=kubernetes_provider.config_context,
                config_path=kubernetes_provider.config_path,
            ),
            # registry: HelmProviderRegistry
            # registry_config_path
            scope=scope,
        )

        Release(
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            create_namespace=True,
            # depends_on=[scope.kube_config_construct],
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=helm_provider,
            set=[
                # https://github.com/caddyserver/ingress/tree/master/charts/caddy-ingress-controller#values
                ReleaseSet(
                    name="ingressController.config.acmeCA",
                    value="https://acme-staging-v02.api.letsencrypt.org/directory",
                ),
                ReleaseSet(
                    name="ingressController.config.email",
                    value="m@mjschock.com",
                ),
                ReleaseSet(
                    name="ingressController.config.onDemandTLS",
                    value="true",
                ),
                ReleaseSet(
                    name="ingressController.verbose",
                    value="false",
                ),
            ],
            scope=scope,
        )

        app_name = "caddy-server"
        # app_name = "prefect-server"

        DeploymentV1(
            scope=self,
            id_=f"{app_name}_deployment_resource",
            metadata={
                "name": app_name,
                "namespace": "default",
                "labels": {"app": app_name},
            },
            spec={
                # "replicas": "1",  # We're using SQLite, so we should only run 1 pod
                "selector": {"match_labels": {"app": app_name}},
                "template": {
                    "metadata": {"labels": {"app": app_name}},
                    "spec": {
                        "container": [
                            {
                                # "command": [
                                #     "prefect",
                                #     "server",
                                #     "start",
                                #     "--host",
                                #     "0.0.0.0",
                                #     "--log-level",
                                #     "WARNING",
                                # ],  # noqa: E501
                                # "image": "prefecthq/prefect:2.10.19-python3.11",
                                "image": "caddy",
                                "imagePullPolicy": "IfNotPresent",
                                # "name": "api",
                                "name": app_name,
                                "ports": [
                                    {"containerPort": 80},
                                    {"containerPort": 443},
                                    # {"containerPort": 4200},
                                ],
                            }
                        ]
                    },
                },
            },
        )

        ServiceV1(
            scope=self,
            id_=f"{app_name}_service_resource",
            metadata={
                "name": app_name,
                "namespace": "default",
                "labels": {"app": app_name},
            },
            spec={
                "selector": {"app": app_name},
                "port": [
                    {"name": "http", "port": 80, "target_port": 80},
                    {"name": "https", "port": 443, "target_port": 443},
                    # {"protocol": "TCP", "port": 4200, "target_port": 4200},
                ],
            },
        )

        # caddy_server_ingress_resource = Ingress(
        #     scope=self,
        #     id_='caddy_server_ingress_resource',
        #     metadata={
        #         'name': app_name,
        #         'namespace': caddy_ingress_controller_helm_release_resource.namespace,  # noqa: E501
        #         'annotations': {
        #             'kubernetes.io/ingress.class': 'caddy',
        #         }
        #     },
        #     spec={
        #         'rule': [{
        #             'host': config.variables.get('primary_domain_name'),
        #             'http': {
        #                 'path': [{
        #                     'path': '/',
        #                     'backend': {
        #                         'serviceName': app_name,
        #                         'servicePort': 80
        #                     }
        #                 }]
        #             }
        #         }]
        #     }
        # )

        # IngressV1(
        #     scope=scope,
        #     id_=f"{app_name}_ingress_resource",
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
        #                     # number=443,
        #                     # number=2019,
        #                     number=4200,
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
        #                                         # number=80,
        #                                         # number=443,
        #                                         # number=2019,
        #                                         number=4200,
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
