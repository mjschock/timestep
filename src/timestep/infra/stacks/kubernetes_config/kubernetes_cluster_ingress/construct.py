from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
from constructs import Construct

from timestep.config import Settings


class KubernetesClusterIngressConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.caddy_ingress_controller_helm_release_resource = Release(  # noqa: F841
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            create_namespace=True,
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="ingressController.config.acmeCA",
                    value=config.ingress_controller_acme_ca,
                ),
                ReleaseSet(
                    name="ingressController.config.debug",
                    value=config.ingress_controller_debug,
                ),
                ReleaseSet(
                    name="ingressController.config.email",
                    value=config.ingress_controller_email,
                ),
            ],
            scope=self,
        )
