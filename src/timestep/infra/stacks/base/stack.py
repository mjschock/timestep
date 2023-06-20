import os
from prefect import flow, task, get_run_logger
from prefect.futures import PrefectFuture
from prefect.filesystems import LocalFileSystem
from prefect.task_runners import SequentialTaskRunner
from prefect_shell import ShellOperation
from typing import Any, Dict, List, Type
import pathlib
from cdktf import LocalExecProvisioner, Token
from constructs import Construct
from cdktf import (
    TerraformDataSource,
    TerraformElement,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from cloud_init_gen import CloudInitDoc
from pydantic import BaseModel

from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.external.data_external import DataExternal as ExternalTerraformDataSource

from timestep.infra.imports.helm.provider import (
    HelmProvider as HelmTerraformProvider,
    HelmProviderKubernetes,
)
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)
from timestep.infra.imports.kubernetes.namespace import (
    Namespace as KubernetesNamespaceTerraformResource,
    NamespaceMetadata,
)
from timestep.infra.imports.namecheap.provider import NamecheapProvider as NamecheapTerraformProvider
from timestep.infra.imports.namecheap.domain_records import DomainRecords as NamecheapDomainRecordsTerraformResource

from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.data_null_data_source import DataNullDataSource as NullTerraformDataSource
from timestep.infra.imports.null.resource import Resource as NullTerraformResource

from timestep.infra.imports.cloudinit.data_cloudinit_config import DataCloudinitConfig as CloudInitConfigTerraformDataSource

from timestep.infra.imports.local.data_local_file import DataLocalFile as LocalFileTerraformDataSource
from timestep.infra.imports.local.file import File as LocalFileTerraformResource
from timestep.infra.imports.local.provider import LocalProvider as LocalTerraformProvider

from timestep.conf import AppConfig

class CLOUD_INSTANCE_PROVIDERS:
    MULTIPASS = "multipass"
    DIGITALOCEAN = "digitalocean"


@task
def get_ssh_authorized_keys(config: AppConfig) -> List[str]: # TODO: Can I use Terraform's SSHProvisionerConnection instead?
    logger = get_run_logger()

    if not os.path.exists(config.SSH_AUTHORIZED_KEYS_PATH) or not os.path.exists(config.SSH_PUBLIC_KEY_PATH) or not os.path.exists(config.SSH_PRIVATE_KEY_PATH):
        logger.info('Generating new SSH keypair and adding to authorized_keys')
        os.makedirs(os.path.dirname(config.SSH_AUTHORIZED_KEYS_PATH), exist_ok=True)

        with ShellOperation(
            commands=[
                f"ssh-keygen -t rsa -C $USER@$HOSTNAME -f {config.SSH_PRIVATE_KEY_PATH} -N ''",
                f"cat {config.SSH_PUBLIC_KEY_PATH} >> {config.SSH_AUTHORIZED_KEYS_PATH}",
            ],
        ) as shell_operation:
            shell_process = shell_operation.trigger()
            shell_process.wait_for_completion()

    with open(config.SSH_AUTHORIZED_KEYS_PATH, "r") as file:
        ssh_authorized_keys = file.read().strip().splitlines()

    return ssh_authorized_keys


@task
def get_cloud_init_config(config: AppConfig, ssh_authorized_keys: List[str]) -> CloudInitDoc:
# def get_cloud_init_config_data_source(scope: TerraformStack, config: AppConfig, ssh_authorized_keys: List[str]) -> TerraformDataSource:
    user_data = CloudInitDoc()

    cloud_cfg = dict(
        disable_root=True,
        package_reboot_if_required=True,
        package_update=True,
        package_upgrade=True,
        packages=[
            "build-essential",
            "curl",
            "default-jdk",
            "direnv",
            "figlet",
            "jq",
            "libbz2-dev",
            "libffi-dev",
            "liblzma-dev",
            "libncursesw5-dev",
            "libreadline-dev",
            "libsqlite3-dev",
            "libssl-dev",
            "libxml2-dev",
            "libxmlsec1-dev",
            "net-tools",
            "tk-dev",
            "unzip",
            "xz-utils",
            "zlib1g-dev",
        ],
        runcmd=[
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo "" >> $HOME/.oh-my-bash/custom/example.sh',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo OSH_THEME="zork" >> $HOME/.oh-my-bash/custom/example.sh',
            ],
            ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
            # "runuser -l ubuntu -c 'echo \"eval \\\"\$(direnv hook bash)\\\"\" >> $HOME/.bashrc'",
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo "eval \\"\$(direnv hook bash)\\"" >> $HOME/.bashrc',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "git clone https://github.com/anyenv/anyenv ~/.anyenv",
            ],
            ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "echo export PATH=\$HOME/.anyenv/bin:\$PATH >> $HOME/.bashrc",
            ],
            # "runuser -l ubuntu -c 'echo \"eval \\\"\$(anyenv init -)\\\"\" >> $HOME/.bashrc'",
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                'echo "eval \\"\$(anyenv init -)\\"" >> $HOME/.bashrc',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install --force-init",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install jenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install nodenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install goenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "$HOME/.anyenv/bin/anyenv install pyenv",
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "curl -sLS https://get.arkade.dev | sudo sh",
            ],
            ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "echo export PATH=\$HOME/.arkade/bin:\$PATH >> $HOME/.bashrc",
            ],
            ["runuser", "-l", "ubuntu", "-c", "arkade get k3sup"],
            ["runuser", "-l", "ubuntu", "-c", "mkdir $HOME/.kube"],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                f'$HOME/.arkade/bin/k3sup install --context {config.KUBE_CONTEXT} --k3s-extra-args "--disable traefik" --local --local-path $HOME/.kube/config --user ubuntu',
            ],
            [
                "runuser",
                "-l",
                "ubuntu",
                "-c",
                "arkade install docker-registry",
            ],  # TODO: install Helm chart using Terraform instead?
        ],
        users=[
            "default",
            {
                "groups": "sudo",
                "name": "ubuntu",
                "shell": "/bin/bash",
                "ssh_authorized_keys": ssh_authorized_keys,
                "sudo": "ALL=(ALL) NOPASSWD:ALL",
            },
        ],
        # write_files = [
        #                 {
        #                     "content": f"""\
        # #!/bin/sh
        # [ -r /etc/lsb-release ] && . /etc/lsb-release
        # if [ -z \"$DISTRIB_DESCRIPTION\" ] && [ -x /usr/bin/lsb_release ]; then
        #         # Fall back to using the very slow lsb_release utility
        #         DISTRIB_DESCRIPTION=$(lsb_release -s -d)
        # fi
        # printf \"Welcome to \n%s\nv%s\nrunning on %s (%s %s %s).\n\" \"$(figlet Timestep AI)\" \"$(date +'%Y.%m.%d')\" \"$DISTRIB_DESCRIPTION\" \"$(uname -o)\" \"$(uname -r)\" \"$(uname -m)\"
        #                     """,
        #                     "path": "/etc/update-motd.d/00-header",
        #                     # "permissions": "\"0o755\"",
        #                     # "permissions": "'0755'",
        #                     "permissions": "'0755'",
        #                 },
        #                 {
        #                     "content": """\
        # mirrors:
        #   registry.timestep.local:
        #     endpoint:
        #       - "https://registry.timestep.local:5000"
        # configs:
        #   "registry.timestep.local:5000":
        #     auth:
        #       username: xxxxxx # this is the registry username
        #       password: xxxxxx # this is the registry password
        #     tls:
        #       cert_file: # path to the cert file used in the registry
        #       key_file:  # path to the key file used in the registry
        #       ca_file:   # path to the ca file used in the registry\
        # """,
        #                     "path": "/etc/rancher/k3s/registries.yaml",
        #                     "permissions": "\"0o644\""
        #                 },
        # ],
        # content = f"""\
        # - content: |
        #     mirrors:
        #         registry.localhost:
        #         endpoint:
        #             - "http://registry:5000"
        #     path: /etc/rancher/k3s/registries.yaml
        #     permissions: "0o644"
    )

    user_data.add(
        cloud_cfg
    )

    return user_data


@task
def get_cloud_instance_provider(scope: TerraformStack, config: AppConfig) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_provider = MultipassTerraformProvider(
            id="cloud_instance_provider",
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_provider = DigitaloceanTerraformProvider(
            id="cloud_instance_provider",
            scope=scope,
            token=config.DO_TOKEN,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_provider


@task
def get_cloud_instance_resource(scope: TerraformStack, config: AppConfig, cloud_init_config: CloudInitDoc, cloud_instance_provider: TerraformProvider) -> TerraformResource: # TODO: rename CloudInitDoc to CloudInitConfig?
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_init_config_local_provider = LocalTerraformProvider(
            id="cloud_init_config_local_provider",
            scope=scope,
        )

        cloud_init_config_local_file_resource = LocalFileTerraformResource(
            id="cloud_init_config_local_file_resource",
            content=cloud_init_config.render(),
            filename=config.CLOUD_CONFIG_PATH,
            provider=cloud_init_config_local_provider,
            scope=scope,
        )

        cloud_init_config_local_file_data_source = LocalFileTerraformDataSource(
            id="cloud_init_config_local_file_data_source",
            filename=cloud_init_config_local_file_resource.filename,
            scope=scope,
        )

        cloud_instance_resource = MultipassInstanceTerraformResource(
            cloudinit_file=cloud_init_config_local_file_data_source.filename,
            cpus=config.MULTIPASS_INSTANCE_CPUS,
            disk=config.MULTIPASS_INSTANCE_DISK,
            id="cloud_instance_resource",
            image=config.MULTIPASS_INSTANCE_IMAGE,
            name=config.CLOUD_INSTANCE_NAME,
            provider=cloud_instance_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_resource = DigitaloceanDropletTerraformResource(
            id_="cloud_instance_resource",
            image=config.DO_DROPLET_IMAGE,
            name=config.CLOUD_INSTANCE_NAME,
            provider=cloud_instance_provider,
            region=config.DO_DROPLET_REGION,
            scope=scope,
            size=config.DO_DROPLET_SIZE,
            user_data=cloud_init_config.render(),
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_resource


@task
def get_domain_name_registrar_provider(scope: TerraformStack, config: AppConfig) -> TerraformProvider:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        domain_name_registrar_provider = NullTerraformProvider(
            id="domain_name_registrar_provider",
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        domain_name_registrar_provider = NamecheapTerraformProvider(
            id="domain_name_registrar_provider",
            api_key=config.NAMECHEAP_API_KEY,
            api_user=config.NAMECHEAP_API_USER,
            user_name=config.NAMECHEAP_USER_NAME,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return domain_name_registrar_provider


@task
def get_domain_name_registrar_resource(scope: TerraformStack, config: AppConfig, domain_name_registrar_provider: TerraformProvider) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        domain_name_registrar_resource = NullTerraformResource(
            id="domain_name_registrar_resource",
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        domain_name_registrar_resource = NamecheapDomainRecordsTerraformResource(
            id_="domain_name_registrar_resource",
            domain=config.DOMAIN,
            mode="OVERWRITE",
            nameservers=[
                "ns1.digitalocean.com",
                "ns2.digitalocean.com",
                "ns3.digitalocean.com",
            ],
            provider=domain_name_registrar_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return domain_name_registrar_resource


@task
def get_cloud_instance_domain_resource(scope: TerraformStack, config: AppConfig, cloud_instance_provider: TerraformProvider, cloud_instance_resource: TerraformResource, cloud_instance_data_source: TerraformDataSource) -> TerraformResource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        hosts_file_local_provider = LocalTerraformProvider(
            alias="hosts_file_local_provider",
            id="hosts_file_local_provider",
            scope=scope,
        )

        hosts_file_local_file_resource = LocalFileTerraformResource(
            id="hosts_file_local_file_resource",
            content=f"{cloud_instance_data_source.ipv4} {config.DOMAIN}",
            filename=config.HOSTS_FILE_PATH,
            provider=hosts_file_local_provider,
            scope=scope,
        )

        return hosts_file_local_file_resource

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_domain_resource = DigitaloceanDomainTerraformResource(
            id_="cloud_domain_resource",
            ip_address=cloud_instance_data_source.ipv4_address,
            name=config.DOMAIN,
            provider=cloud_instance_provider, # TODO: use cloud_instance_domain_provider instead?
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_domain_resource


@task
def get_cloud_instance_data_source(scope: TerraformStack, config: AppConfig, cloud_instance_provider: TerraformProvider, cloud_instance_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_data_source = MultipassInstanceTerraformDataSource(
            id="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_data_source = DigitaloceanDropletTerraformDataSource(
            id_="cloud_instance_data_source",
            name=cloud_instance_resource.name,
            provider=cloud_instance_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_data_source


@task
def get_cloud_domain_data_source(scope: TerraformStack, config: AppConfig, cloud_instance_provider: TerraformProvider, cloud_instance_domain_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_domain_data_source = LocalFileTerraformDataSource(
            id="cloud_domain_data_source",
            filename=cloud_instance_domain_resource.filename,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_domain_data_source = DigitaloceanDomainTerraformDataSource(
            id_="cloud_domain_data_source",
            name=cloud_instance_domain_resource.name,
            provider=cloud_instance_provider,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_domain_data_source


@task
def get_cloud_instance_ipv4_output(scope: TerraformStack, config: AppConfig, cloud_instance_data_source: TerraformDataSource) -> TerraformOutput:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_ipv4_output = TerraformOutput(
            id="cloud_instance_ipv4_output",
            value=cloud_instance_data_source.ipv4,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_ipv4_output = TerraformOutput(
            id="cloud_instance_ipv4_output",
            value=cloud_instance_data_source.ipv4_address,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_ipv4_output


@task
def get_cloud_instance_zone_file_output(scope: TerraformStack, config: AppConfig, cloud_instance_domain_data_source: TerraformDataSource) -> TerraformOutput:
    if config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        cloud_instance_zone_file_output = TerraformOutput(
            id="cloud_instance_zone_file_output",
            value=cloud_instance_domain_data_source.filename,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        cloud_instance_zone_file_output = TerraformOutput(
            id="cloud_instance_zone_file_output",
            value=cloud_instance_domain_data_source.zone_file,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return cloud_instance_zone_file_output


@task
def get_kube_config(scope: TerraformStack, config: AppConfig, cloud_instance_data_source: TerraformDataSource) -> TerraformDataSource:
    local_exec_provisioner = LocalExecProvisioner(
        command=f"k3sup install --context {config.KUBE_CONTEXT} --ip {cloud_instance_data_source.ipv4} --local-path {config.KUBE_CONFIG_PATH} --skip-install --ssh-key {config.SSH_PRIVATE_KEY_PATH} --user ubuntu",
        type="local-exec",
    )

    kube_config_resource = NullTerraformResource(
        id="kube_config_resource",
        provider=NullTerraformProvider(
            alias="kube_config_provider",
            id="kube_config_provider",
            scope=scope,
        ),
        provisioners=[
            local_exec_provisioner,
        ],
        scope=scope,
        triggers={
            "ipv4": cloud_instance_data_source.ipv4,
        },
    )

    return kube_config_resource


class BaseTerraformStack(TerraformStack):
    def __init__(
        self, scope: Construct, id: str, config: AppConfig
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        # Point the Domain Name Registrar's Domain Name Servers to the Cloud's Domain Name Servers for the Domain
        domain_name_registrar_provider_future: PrefectFuture[TerraformProvider] = get_domain_name_registrar_provider.submit(scope=self, config=config)
        domain_name_registrar_resource_future: PrefectFuture[TerraformResource] = get_domain_name_registrar_resource.submit(scope=self, config=config, domain_name_registrar_provider=domain_name_registrar_provider_future)

        # Prepare the Cloud Config for the Cloud Instance
        ssh_authorized_keys_future: PrefectFuture[List[str]] = get_ssh_authorized_keys.submit(config=config)
        cloud_init_config_future: PrefectFuture[CloudInitDoc] = get_cloud_init_config.submit(config=config, ssh_authorized_keys=ssh_authorized_keys_future)

        # Create the Cloud Instance
        cloud_instance_provider_future: PrefectFuture = get_cloud_instance_provider.submit(scope=self, config=config)
        cloud_instance_resource_future: PrefectFuture = get_cloud_instance_resource.submit(scope=self, config=config, cloud_init_config=cloud_init_config_future, cloud_instance_provider=cloud_instance_provider_future)
        cloud_instance_data_source_future: PrefectFuture = get_cloud_instance_data_source.submit(scope=self, config=config, cloud_instance_provider=cloud_instance_provider_future, cloud_instance_resource=cloud_instance_resource_future)

        # Associate the Cloud Instance's ipv4 address with the Domain
        cloud_instance_domain_resource_future: PrefectFuture = get_cloud_instance_domain_resource.submit(scope=self, config=config, cloud_instance_provider=cloud_instance_provider_future, cloud_instance_resource=cloud_instance_resource_future, cloud_instance_data_source=cloud_instance_data_source_future)
        cloud_instance_domain_data_source_future: PrefectFuture = get_cloud_domain_data_source.submit(scope=self, config=config, cloud_instance_provider=cloud_instance_provider_future, cloud_instance_domain_resource=cloud_instance_domain_resource_future)

        cloud_instance_ipv4_output_future: PrefectFuture = get_cloud_instance_ipv4_output.submit(scope=self, config=config, cloud_instance_data_source=cloud_instance_data_source_future)
        cloud_instance_zone_file_output_future: PrefectFuture = get_cloud_instance_zone_file_output.submit(scope=self, config=config, cloud_instance_domain_data_source=cloud_instance_domain_data_source_future)

        kube_config_future: PrefectFuture = get_kube_config.submit(scope=self, config=config, cloud_instance_data_source=cloud_instance_data_source_future)

        helm_provider = HelmTerraformProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                config_context=config.KUBE_CONTEXT,
                config_path=config.KUBE_CONFIG_PATH,
            ),
            scope=self,
        )

        caddy_ingress_controller_helm_release_resource = HelmReleaseTerraformResource(
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            create_namespace=True,
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=helm_provider,
            scope=self,
        )

        platform_helm_release_resource = HelmReleaseTerraformResource(
            id_="platform_helm_release_resource",
            atomic=True,
            chart=config.PLATFORM_CHART_PATH,
            # name="timestep-ai-platform",
            name="platform",
            namespace="default",
            provider=helm_provider,
            scope=self,
        )
