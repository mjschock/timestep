from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release
from constructs import Construct
from timestep.config import Settings


class SealedSecretsConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.sealed_secrets_helm_release_resource = Release(
            id_="sealed_secrets_helm_release_resource",
            atomic=True,
            chart="sealed-secrets",
            create_namespace=True,
            name="sealed-secrets",
            namespace="default",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            scope=self,
        )
