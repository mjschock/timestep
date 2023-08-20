from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet, ReleaseSetSensitive
from constructs import Construct
from timestep.config import Settings


class SupabaseConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.supabase_helm_release_resource = Release(
            id_="supabase_helm_release_resource",
            atomic=True,
            chart="supabase",
            # create_namespace=True,
            name="supabase",
            # namespace="prefect-system",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="jwt.autoGenerate.forceRun",
                    value="true",
                ),
                ReleaseSet(
                    name="postgresql.enabled",
                    value="true",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="postgresql.auth.postgresPassword",
                    value=config.postgresql_password.get_secret_value(),
                )
            ],
            scope=self,
        )
