from constructs import Construct

from timestep.config import AppConfig
from timestep.infra.imports.helm.provider import HelmProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release
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
from timestep.infra.imports.kubernetes.provider import KubernetesProvider
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
        config: AppConfig,
        cloud_instance_construct: CloudInstanceConstruct,
        kube_config_contruct: KubeConfigConstruct,
    ) -> None:
        super().__init__(scope, id)

        self.kubernetes_provider = KubernetesProvider(
            id="kubernetes_provider",
            # config_context=config.KUBE_CONTEXT,
            # config_path=config.KUBE_CONFIG_PATH,
            config_context=config.variables.get("kubecontext"),
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
            # chart=config.CADDY_INGRESS_CONTROLLER_CHART_PATH,
            create_namespace=True,
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=self.helm_provider,
            # set=[
            # {
            #     "name": "ingressController.config.email",
            #     "value": config.CADDY_INGRESS_CONTROLLER_EMAIL,
            # },
            # {
            #     "name": "ingressController.config.onDemandTLS",
            #     "value": "true",
            # },
            # ],
            scope=self,
        )

    def create_ingress_resource(self, config, id, name, port) -> None:
        return IngressV1(
            id_=id,
            metadata=IngressV1Metadata(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                },
                name=name,
            ),
            scope=self,
            spec=IngressV1Spec(
                rule=[
                    IngressV1SpecRule(
                        host=config.variables.get("primary_domain_name"),
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name=name,
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                number=port,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                ),
                            ]
                        ),
                    )
                ]
            ),
        )
