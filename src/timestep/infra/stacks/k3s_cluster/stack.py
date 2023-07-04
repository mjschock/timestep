from cdktf import (
    TerraformStack,
)
from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig
from timestep.infra.stacks.k3s_cluster.constructs.cloud_init_config.blocks import (
    CloudInitConfigConstruct,
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

        # self.cloud_instance_construct = CloudInstanceConstruct(
        #     cloud_init_config_construct=self.cloud_init_config_construct,
        #     config=config,
        #     id="cloud_instance_construct",
        #     scope=self,
        # )

        # self.cloud_instance_domain_construct = CloudInstanceDomainConstruct(
        #     cloud_instance_construct=self.cloud_instance_construct,
        #     config=config,
        #     id="cloud_instance_domain_construct",
        #     scope=self,
        # )

        # self.domain_name_registar_construct = DomainNameRegistrarConstruct(
        #     cloud_instance_construct=self.cloud_instance_construct,
        #     config=config,
        #     id="domain_name_registar_construct",
        #     scope=self,
        # )

        # self.kube_config_construct = KubeConfigConstruct(
        #     cloud_instance_construct=self.cloud_instance_construct,
        #     config=config,
        #     id="kube_config_construct",
        #     scope=self,
        # )
