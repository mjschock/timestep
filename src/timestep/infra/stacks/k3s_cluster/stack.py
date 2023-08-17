from cdktf import (
    TerraformStack,
)
from constructs import Construct

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
from timestep.infra.stacks.k3s_cluster.constructs.kube_config.construct import (
    KubeConfigConstruct,
)


class K3sClusterStack(TerraformStack):
    id: str = None

    def __init__(self, scope: Construct, id: str, config: dict[str, str]):
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
