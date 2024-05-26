from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release
from constructs import Construct

from timestep.config import Settings


class OllamaConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        # See https://artifacthub.io/packages/helm/ollama-helm/ollama for more info
        self.ollama_helm_release_resource = Release(
            id_="ollama_helm_release_resource",
            atomic=True,
            chart="ollama-helm/ollama",
            create_namespace=True,
            name="ollama",
            namespace="ollama",
            repository="https://otwld.github.io/ollama-helm/",
            provider=helm_provider,
            scope=self,
            version="0.1.38",
        )
