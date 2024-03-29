from cdktf import TerraformOutput
from cdktf_cdktf_provider_http.data_http import DataHttp
from cdktf_cdktf_provider_http.provider import HttpProvider
from constructs import Construct

from timestep.config import DomainNameRegistrarProvider, Settings
from timestep.infra.imports.namecheap.domain_records import DomainRecords
from timestep.infra.imports.namecheap.provider import NamecheapProvider


class DomainNameRegistrarConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
    ) -> None:
        super().__init__(scope, id)

        if (
            config.domain_name_registrar_provider
            == DomainNameRegistrarProvider.NAMECHEAP
        ):
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

            domain_name_registrar_provider = NamecheapProvider(
                api_key=config.namecheap_api_key.get_secret_value(),
                api_user=config.namecheap_api_user,
                # TODO: The client_ip needs to be set up in Namecheap and GitHub Runner
                # has a dynamic IP, so this can fail. Need another way to do this
                # without relying on a self-hosted runner with known IP.
                client_ip=http_outputs_ip.value,
                id="domain_name_registrar_provider",
                scope=scope,
                user_name=config.namecheap_user_name,
            )

            DomainRecords(
                domain=config.primary_domain_name,
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
