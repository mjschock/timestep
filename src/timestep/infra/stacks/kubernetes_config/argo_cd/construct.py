from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release
from constructs import Construct

from timestep.config import Settings


class ArgoCDConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.argo_cd_helm_release_resource = Release(
            id_="argo_cd_helm_release_resource",
            atomic=True,
            chart="argo-cd",
            create_namespace=True,
            name="argo-cd",
            namespace="default",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            scope=self,
            version="5.4.3",
        )
