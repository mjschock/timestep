from constructs import Construct

from timestep.config import AppConfig
from timestep.infra.imports.helm.provider import HelmProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release
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

        kubernetes_provider = KubernetesProvider(
            id="kubernetes_provider",
            # config_context=config.KUBE_CONTEXT,
            # config_path=config.KUBE_CONFIG_PATH,
            config_context=config.variables.get("kubecontext"),
            config_path=kube_config_contruct.data_source.filename,
            scope=self,
        )

        helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                # config_context=config.KUBE_CONTEXT,
                # config_path=config.KUBE_CONFIG_PATH,
                config_context=kubernetes_provider.config_context,
                config_path=kubernetes_provider.config_path,
            ),
            scope=self,
        )

        caddy_ingress_controller_helm_release_resource = Release(  # noqa: F841
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            # chart=config.CADDY_INGRESS_CONTROLLER_CHART_PATH,
            create_namespace=True,
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=helm_provider,
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
