from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider
from timestep.infra.imports.helm.provider import HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.helm.release import ReleaseSet
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)


class IngressControllerConstruct(Construct):
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
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            create_namespace=True,
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