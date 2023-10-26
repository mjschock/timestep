from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.platform.constructs.timestep_ai.construct import (
    TimestepAIConstruct,
)


class PlatformStack(TerraformStack):
    id: str

    def __init__(self, scope: Construct, id: str, config: Settings, kube_config=None):
        super().__init__(scope, id)
        self.id = id

        self.timestep_ai_contruct: TimestepAIConstruct = TimestepAIConstruct(
            config=config,
            id="timestep_ai_contruct",
            # helm_provider=self.helm_provider,
            scope=self,
        )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            LocalBackend(
                path=f"{config.dist_path}/terraform.{self.id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            HttpBackend(
                address=f"{config.tf_http_address}/{self.id}",
                lock_address=f"{config.tf_http_address}/{self.id}/lock",
                lock_method="POST",
                password=config.tf_api_token.get_secret_value(),
                retry_wait_min=5,
                scope=self,
                unlock_address=f"{config.tf_http_address}/{self.id}/lock",
                unlock_method="DELETE",
                username=config.tf_username,
            )
