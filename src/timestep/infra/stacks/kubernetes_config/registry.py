from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSetSensitive
from constructs import Construct

from timestep.config import Settings


class RegistryConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.release_resource = Release(
            id_="registry_helm_release_resource",
            atomic=True,
            chart="harbor",
            create_namespace=True,
            name="harbor",
            namespace="default",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            set=[],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="adminPassword",
                    value=config.registry_admin_password.get_secret_value(),
                )
            ],
            scope=self,
        )
