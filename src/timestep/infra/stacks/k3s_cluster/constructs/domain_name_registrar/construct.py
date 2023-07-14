from cdktf import TerraformOutput
from constructs import Construct

from timestep.conf.blocks import AppConfig, DomainNameRegistrarProvider
from timestep.infra.imports.http.data_http import DataHttp
from timestep.infra.imports.http.provider import HttpProvider
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

        http_provider = HttpProvider(
            id="http_provider",
            scope=scope,
        )

        http_data_source = DataHttp(
            id="http_data_source",
            provider=http_provider,
            scope=scope,
            url="https://api.ipify.org",
        )

        http_outputs_ip = TerraformOutput(
            id="http_outputs_ip",
            scope=scope,
            value=http_data_source.response_body,
        )

        if (
            config.variables.get("domain_name_registrar_provider")
            == DomainNameRegistrarProvider.NAMECHEAP
        ):  # noqa: E501
            domain_name_registrar_provider = NamecheapProvider(
                api_key=config.secrets.get_secret_value().get("namecheap_api_key"),
                api_user=config.secrets.get_secret_value().get("namecheap_api_user"),
                # client_ip=config.variables.get("client_ip"),
                client_ip=http_outputs_ip.value,
                id="domain_name_registrar_provider",
                scope=scope,
                user_name=config.secrets.get_secret_value().get("namecheap_user_name"),
            )

            DomainRecords(
                domain=config.variables.get("primary_domain_name"),
                id_="domain_name_registrar_resource",
                mode="OVERWRITE",
                nameservers=[  # TODO: Get these dynamically
                    "ns1.digitalocean.com",
                    "ns2.digitalocean.com",
                    "ns3.digitalocean.com",
                ],
                provider=domain_name_registrar_provider,
                scope=scope,
            )
