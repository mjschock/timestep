from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
from constructs import Construct
from timestep.config import Settings


class TimestepAIConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.release_resource = Release(
            id_="timestep_ai_helm_release_resource",
            atomic=True,
            chart=f"{config.base_path}/timestep-ai",
            create_namespace=True,
            lint=True,
            name="timestep-ai",
            namespace="default",
            provider=helm_provider,
            recreate_pods=True,
            set=[
                ReleaseSet(
                    name="app.kubernetes.io\\/managed-by",
                    value="Helm",
                ),
                ReleaseSet(
                    name="meta.helm.sh\\/release-name",
                    value="timestep-ai",
                ),
                ReleaseSet(
                    name="meta.helm.sh\\/release-namespace",
                    value="default",
                ),
            ],
            set_sensitive=[],
            scope=self,
        )
