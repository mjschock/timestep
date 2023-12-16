from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet, ReleaseSetSensitive
from constructs import Construct

from timestep.config import Settings


class MinioConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.minio_helm_release_resource = Release(
            id_="minio_helm_release_resource",
            atomic=True,
            chart="minio",
            create_namespace=True,
            name="minio",
            namespace="default",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="auth.rootUser",
                    value=config.minio_root_user,
                ),
                ReleaseSet(
                    name="mode",
                    value="distributed",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="auth.rootPassword",
                    value=config.minio_root_password.get_secret_value(),
                ),
            ],
            scope=self,
        )
