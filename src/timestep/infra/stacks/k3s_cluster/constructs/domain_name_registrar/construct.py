from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)


class DomainNameRegistrarConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: AppConfig,
        cloud_instance_construct: CloudInstanceConstruct,
    ) -> None:
        super().__init__(scope, id)
        get_run_logger()
