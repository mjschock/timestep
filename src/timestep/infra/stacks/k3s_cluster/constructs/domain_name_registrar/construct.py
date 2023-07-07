from constructs import Construct
from prefect import get_run_logger

from timestep.conf.blocks import AppConfig, DomainNameRegistrarProvider
from timestep.infra.imports.namecheap.domain_records import DomainRecords
from timestep.infra.imports.namecheap.provider import NamecheapProvider
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

        if (
            config.variables.get("domain_name_registrar_provider")
            == DomainNameRegistrarProvider.NAMECHEAP
        ):  # noqa: E501
            domain_name_registrar_provider = NamecheapProvider(
                id="domain_name_registrar_provider",
                api_key=config.secrets.get_secret_value().get("namecheap_api_key"),
                api_user=config.secrets.get_secret_value().get("namecheap_api_user"),
                user_name=config.secrets.get_secret_value().get("namecheap_user_name"),
                scope=scope,
            )

            DomainRecords(
                id_="domain_name_registrar_resource",
                domain=config.variables.get("primary_domain_name"),
                mode="OVERWRITE",
                nameservers=[  # TODO: Get these dynamically
                    "ns1.digitalocean.com",
                    "ns2.digitalocean.com",
                    "ns3.digitalocean.com",
                ],
                provider=domain_name_registrar_provider,
                scope=scope,
            )
