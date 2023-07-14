from cdktf import (
    CloudBackend,
    LocalBackend,
    NamedCloudWorkspace,
    TerraformStack,
)
from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.stacks.k3s_cluster.constructs.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance_domain.construct import (  # noqa: E501
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.k3s_cluster.constructs.domain_name_registrar.construct import (  # noqa: E501
    DomainNameRegistrarConstruct,
)


class K3sClusterStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)
        get_run_logger()

        self.cloud_init_config_construct = CloudInitConfigConstruct(
            config=config,
            id="cloud_init_config_construct",
            scope=self,
        )

        self.cloud_instance_construct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct = CloudInstanceDomainConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="cloud_instance_domain_construct",
            scope=self,
        )

        self.domain_name_registar_construct = DomainNameRegistrarConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="domain_name_registar_construct",
            scope=self,
        )

        stack_id: str = config.variables.get("primary_domain_name")

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInstanceProvider.MULTIPASS
        ):
            LocalBackend(
                path=f"terraform.{stack_id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            CloudBackend(
                hostname=config.variables.get("tf_hostname"),
                organization=config.variables.get("tf_organization"),
                scope=self,
                token=config.secrets.get_secret_value().get("tf_api_token"),
                workspaces=NamedCloudWorkspace(config.variables.get("tf_workspace")),
            )
