from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
    ReleaseSet,
    ReleaseSetListStruct,
    ReleaseSetSensitive,
)
from cdktf_cdktf_provider_kubernetes.config_map_v1 import (
    ConfigMapV1,
    ConfigMapV1Metadata,
)
from constructs import Construct

from timestep.config import Settings


class PostgreSQLConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        postgresql_initdb_scripts_config_map: ConfigMapV1 = ConfigMapV1(
            id_="postgresql_initdb_scripts_config_map",
            metadata=ConfigMapV1Metadata(
                name="postgresql-initdb-scripts",
                namespace="default",
            ),
            data={
                "initdb.sql": """
-- schemas
CREATE SCHEMA IF NOT EXISTS auth;
CREATE SCHEMA IF NOT EXISTS storage;

-- extensions
CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;
CREATE EXTENSION IF NOT EXISTS cube WITH SCHEMA public;
-- https://github.com/hasura/graphql-engine/issues/3657
CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;
CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;
CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA public;
CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;
CREATE EXTENSION IF NOT EXISTS vector WITH SCHEMA public;

-- functions
CREATE OR REPLACE FUNCTION public.set_current_timestamp_updated_at() RETURNS trigger LANGUAGE plpgsql AS $$
declare _new record;
begin _new := new;
_new."updated_at" = now();
return _new;
end;
$$;
"""  # noqa: E501
            },
            scope=self,
        )

        self.release_resource = Release(
            id_="postgresql_helm_release_resource",
            atomic=True,
            chart="postgresql-ha",
            create_namespace=True,
            name="postgresql",
            namespace="default",
            repository="https://charts.bitnami.com/bitnami",
            provider=helm_provider,
            set=[
                ReleaseSet(name="postgresql.image.pullPolicy", value="Always"),
                ReleaseSet(
                    name="postgresql.image.registry",
                    value="registry.gitlab.com/timestep-ai/timestep",
                ),
                ReleaseSet(
                    name="postgresql.image.repository", value="postgresql-repmgr"
                ),
                ReleaseSet(name="postgresql.image.tag", value="latest"),
                ReleaseSet(
                    name="postgresql.initdbScriptsCM",
                    value=postgresql_initdb_scripts_config_map.metadata.name,
                ),
            ],
            set_list=[
                ReleaseSetListStruct(
                    name="postgresql.image.pullSecrets",
                    value=["regcred"],
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="pgpool.adminPassword",
                    value=config.pgpool_admin_password.get_secret_value(),
                ),
                ReleaseSetSensitive(
                    name="postgresql.password",
                    value=config.postgresql_password.get_secret_value(),
                ),
                ReleaseSetSensitive(
                    name="postgresql.repmgrPassword",
                    value=config.postgresql_repmgr_password.get_secret_value(),
                ),
            ],
            values=[
                """postgresql:
  extraVolumes:
    - name: dshm
      emptyDir:
        medium: Memory
        sizeLimit: 512Mi
  extraVolumeMounts:
    - name: dshm
      mountPath: /dev/shm
            """
            ],
            scope=self,
        )
