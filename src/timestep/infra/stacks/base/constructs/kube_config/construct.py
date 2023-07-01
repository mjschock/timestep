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
from pydantic import SecretStr

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

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.stacks.base.constructs.cloud_instance.construct import CloudInstanceConstruct

import tempfile


@task
def get_kube_config_provider(scope: TerraformStack, config: AppConfig, cloud_instance_construct: CloudInstanceConstruct) -> TerraformProvider:
    # if config.variables.get("cloud_instance_provider") == CloudInstanceProvider.MULTIPASS:
    kube_config_provider=NullTerraformProvider(
        alias="kube_config_provider",
        id="kube_config_provider",
        scope=scope,
    )

    # elif config.variables.get("cloud_instance_provider") == CloudInstanceProvider.DIGITALOCEAN:
    #     kube_config_provider=NullTerraformProvider(
    #         alias="kube_config_provider",
    #         id="kube_config_provider",
    #         scope=scope,
    #     )

    # else:
    #     raise ValueError(f"Unknown cloud_instance_provider: {config.variables.get('cloud_instance_provider')}")

    return kube_config_provider


@task
def get_kube_config_resource(scope: TerraformStack, config: AppConfig, cloud_instance_construct: CloudInstanceConstruct, kube_config_provider: TerraformProvider) -> TerraformResource:
    # if config.variables.get("cloud_instance_provider") == CloudInstanceProvider.MULTIPASS:
        # stack_dir = f"{config.BASE_PATH}/{config.CDKTF_OUTDIR}/stacks/{config.STACK_ID}"
        # if config.SSH_PUBLIC_KEY and config.SSH_PRIVATE_KEY:
        #     command = f"k3sup install --context {config.KUBECONTEXT} --ip {cloud_instance_construct.data_source.ipv4} --local-path {config.BASE_PATH}/{config.KUBECONFIG} --skip-install --ssh-key {config.BASE_PATH}/{config.SSH_PRIVATE_KEY} --user ubuntu"

        # else:
        #     command = f"k3sup install --context {config.KUBECONTEXT} --ip {cloud_instance_construct.data_source.ipv4} --local-path {config.BASE_PATH}/{config.KUBECONFIG} --skip-install --ssh-key {config.BASE_PATH}/{config.SSH_PRIVATE_KEY_PATH} --user ubuntu"

    BASE_PATH = pathlib.Path.cwd()
    DIST_PATH: str = f"{BASE_PATH}/dist"

    ip = cloud_instance_construct.data_source.ipv4 # TODO: can I use the output
    kubecontext = config.variables.get("kubecontext")
    local_path = "kube-config.yaml"
    ssh_private_key: SecretStr = config.secrets.get_secret_value().get("ssh_private_key")

    with tempfile.NamedTemporaryFile(
        # delete=False,
        dir=DIST_PATH,
    ) as fp:
        fp.write(ssh_private_key.get_secret_value().encode())
        fp.flush()

        local_exec_provisioner = LocalExecProvisioner( # TODO: use --print-config
            command=f"k3sup install --context {kubecontext} --ip {ip} --local-path {local_path} --skip-install --ssh-key {fp.name} --user ubuntu && rm {fp.name}",
            type="local-exec",
        )

    kube_config_resource = NullTerraformResource(
        id="kube_config_resource",
        provider=kube_config_provider,
        provisioners=[
            local_exec_provisioner,
        ],
        scope=scope,
        triggers={
            # "ipv4": cloud_instance_construct.data_source.ipv4_address,
            "ipv4": cloud_instance_construct.data_source.ipv4,
            # "ssh_private_key": config.secrets.get_secret_value().get("ssh_private_key")
        },
    )

    #     local_exec_provisioner = LocalExecProvisioner(
    #         # command=f"k3sup install --context {config.KUBE_CONTEXT} --ip {cloud_instance_construct.data_source.ipv4} --local-path {config.KUBE_CONFIG_PATH} --skip-install --ssh-key {config.SSH_PRIVATE_KEY_PATH} --user ubuntu",
    #         command=command,
    #         type="local-exec",
    #         # working_dir=stack_dir,
    #     )

    #     kube_config_resource = NullTerraformResource(
    #         id="kube_config_resource",
    #         provider=kube_config_provider,
    #         provisioners=[
    #             local_exec_provisioner,
    #         ],
    #         scope=scope,
    #         triggers={
    #             "ipv4": cloud_instance_construct.data_source.ipv4,
    #         },
    #     )

    # elif config.CLOUD_INSTANCE_PROVIDER == AppConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
    #     if not config.SSH_PUBLIC_KEY or not config.SSH_PRIVATE_KEY:
    #         raise Exception("SSH_PUBLIC_KEY and SSH_PRIVATE_KEY must be set")

    #     local_exec_provisioner = LocalExecProvisioner( # TODO: use --print-config
    #         command=f"k3sup install --context {config.KUBECONTEXT} --ip {cloud_instance_construct.data_source.ipv4_address} --local-path {config.BASE_PATH}/{config.KUBECONFIG} --print-config --skip-install --ssh-key {config.BASE_PATH}/{config.SSH_PRIVATE_KEY_PATH} --user ubuntu",
    #         type="local-exec",
    #     )

    #     kube_config_resource = NullTerraformResource(
    #         id="kube_config_resource",
    #         provider=kube_config_provider,
    #         provisioners=[
    #             local_exec_provisioner,
    #         ],
    #         scope=scope,
    #         triggers={
    #             "ipv4": cloud_instance_construct.data_source.ipv4_address,
    #         },
    #     )

    # else:
    #     raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return kube_config_resource


@task
def get_kube_config_data_source(scope: TerraformStack, config: AppConfig, cloud_instance_construct: CloudInstanceConstruct, kube_config_resource: TerraformResource) -> TerraformDataSource:
    if config.CLOUD_INSTANCE_PROVIDER == AppConfig.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        # stack_dir = f"{config.BASE_PATH}/{config.CDKTF_OUTDIR}/stacks/{config.STACK_ID}"
        kube_config_data_source = LocalFileTerraformDataSource(
            depends_on=[kube_config_resource],
            id="kube_config_data_source",
            # filename=config.KUBE_CONFIG_PATH,
            # filename=f"{stack_dir}/{config.KUBE_CONFIG_PATH}",
            filename=f"{config.BASE_PATH}/{config.KUBECONFIG}",
            # provider=kube_config_resource.provider,
            scope=scope,
        )

    elif config.CLOUD_INSTANCE_PROVIDER == AppConfig.CLOUD_INSTANCE_PROVIDERS.DIGITALOCEAN:
        kube_config_data_source = LocalFileTerraformDataSource(
            id="kube_config_data_source",
            filename=config.KUBE_CONFIG_PATH,
            scope=scope,
        )

    else:
        raise ValueError(f"Unknown CLOUD_INSTANCE_PROVIDER: {config.CLOUD_INSTANCE_PROVIDER}")

    return kube_config_data_source


@task
def get_kube_config_outputs(scope: TerraformStack, config: AppConfig, cloud_instance_construct: CloudInstanceConstruct, kube_config_data_source: TerraformDataSource) -> Dict[str, TerraformOutput]:
    kube_config_outputs = {}

    if config.CLOUD_INSTANCE_PROVIDER == config.CLOUD_INSTANCE_PROVIDERS.MULTIPASS:
        kube_config_outputs["config_path"] = TerraformOutput(
            scope=scope,
            id="kube_config_outputs_config_path",
            value=kube_config_data_source.filename,
        )

        kube_config_outputs["config_context"] = TerraformOutput(
            scope=scope,
            id="kube_config_outputs_config_context",
            value=config.KUBECONTEXT,
        )

    else:
        kube_config_outputs["kubeconfig"] = TerraformOutput(
            scope=scope,
            id="kube_config_outputs_kubeconfig",
            value=kube_config_data_source.inputs_input["kubeconfig"],
        )

    return kube_config_outputs


class KubeConfigConstruct(Construct):
    def __init__(
        self, scope: Construct, id: str, config: AppConfig, cloud_instance_construct: CloudInstanceConstruct
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        self.kube_config_provider_future: PrefectFuture[TerraformProvider] = get_kube_config_provider.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct)
        self.kube_config_resource_future: PrefectFuture[TerraformResource] = get_kube_config_resource.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, kube_config_provider=self.kube_config_provider_future)
        # self.kube_config_data_source_future: PrefectFuture[TerraformDataSource] = get_kube_config_data_source.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, kube_config_resource=self.kube_config_resource_future)
        # self.kube_config_outputs_future: PrefectFuture[Dict[str, TerraformOutput]] = get_kube_config_outputs.submit(scope=scope, config=config, cloud_instance_construct=cloud_instance_construct, kube_config_data_source=self.kube_config_data_source_future)

        self.provider = self.kube_config_provider_future.result()
        self.resource = self.kube_config_resource_future.result()
        # self.data_source = self.kube_config_data_source_future.result()
        # self.outputs = self.kube_config_outputs_future.result()
