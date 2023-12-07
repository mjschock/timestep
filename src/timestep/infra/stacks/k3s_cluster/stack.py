from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.k3s_cluster.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.k3s_cluster.cloud_instance.construct import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.k3s_cluster.cloud_instance_domain.construct import (
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.k3s_cluster.domain_name_registrar.construct import (
    DomainNameRegistrarConstruct,
)
from timestep.infra.stacks.k3s_cluster.kube_config.construct import (
    KubeConfigConstruct,
)


class K3sClusterStack(TerraformStack):
    id: str = None

    def __init__(self, scope: Construct, id: str, config: Settings):
        super().__init__(scope, id)
        self.id = id

        self.cloud_init_config_construct: CloudInitConfigConstruct = (
            CloudInitConfigConstruct(
                config=config,
                id="cloud_init_config_construct",
                scope=self,
            )
        )

        self.cloud_instance_construct: CloudInstanceConstruct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct: CloudInstanceDomainConstruct = (
            CloudInstanceDomainConstruct(
                cloud_instance_construct=self.cloud_instance_construct,
                config=config,
                id="cloud_instance_domain_construct",
                scope=self,
            )
        )

        self.domain_name_registar_construct: DomainNameRegistrarConstruct = (
            DomainNameRegistrarConstruct(
                config=config,
                id="domain_name_registar_construct",
                scope=self,
            )
        )

        self.kube_config_contruct: KubeConfigConstruct = KubeConfigConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="kube_config_contruct",
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
