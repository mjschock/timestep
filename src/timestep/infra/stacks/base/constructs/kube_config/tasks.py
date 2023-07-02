import os
import pathlib
import tempfile
from typing import Any, Dict, List, Type

from cdktf import (
    LocalExecProvisioner,
    TerraformDataSource,
    TerraformElement,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
    Token,
)
from cloud_init_gen import CloudInitDoc
from constructs import Construct
from prefect import flow, get_run_logger, task
from prefect.filesystems import LocalFileSystem
from prefect.futures import PrefectFuture
from prefect.task_runners import SequentialTaskRunner
from prefect_shell import ShellOperation
from pydantic import BaseModel, SecretStr

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.imports.cloudinit.data_cloudinit_config import (
    DataCloudinitConfig as CloudInitConfigTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.external.data_external import (
    DataExternal as ExternalTerraformDataSource,
)
from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider
from timestep.infra.imports.helm.provider import HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.namespace import (
    Namespace as KubernetesNamespaceTerraformResource,
)
from timestep.infra.imports.kubernetes.namespace import NamespaceMetadata
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)
from timestep.infra.imports.local.data_local_file import (
    DataLocalFile as LocalFileTerraformDataSource,
)
from timestep.infra.imports.local.file import File as LocalFileTerraformResource
from timestep.infra.imports.local.provider import (
    LocalProvider as LocalTerraformProvider,
)
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.imports.namecheap.domain_records import (
    DomainRecords as NamecheapDomainRecordsTerraformResource,
)
from timestep.infra.imports.namecheap.provider import (
    NamecheapProvider as NamecheapTerraformProvider,
)
from timestep.infra.imports.null.data_null_data_source import (
    DataNullDataSource as NullTerraformDataSource,
)
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.resource import Resource as NullTerraformResource
from timestep.infra.stacks.base.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)


@task
def get_kube_config_provider(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
) -> TerraformProvider:
    kube_config_provider = NullTerraformProvider(
        alias="kube_config_provider",
        id="kube_config_provider",
        scope=scope,
    )

    return kube_config_provider


@task
def get_kube_config_resource(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    kube_config_provider: TerraformProvider,
) -> TerraformResource:
    ipv4 = cloud_instance_construct.outputs["ipv4"].value
    kubecontext = config.variables.get("kubecontext")
    # local_path = config.variables.get("kubeconfig")
    local_path = "kube-config.yaml"
    ssh_private_key: SecretStr = config.secrets.get_secret_value().get(
        "ssh_private_key"
    )
    ssh_private_key_path: str

    with tempfile.NamedTemporaryFile(
        delete=False,
    ) as fp:
        ssh_private_key_path = fp.name

        command = f"k3sup install --context {kubecontext} --ip {ipv4} --local-path {local_path} --skip-install --ssh-key {ssh_private_key_path} --user ubuntu && rm {ssh_private_key_path}"
        local_exec_provisioner = LocalExecProvisioner(
            command=command,
            type="local-exec",
        )

        fp.write(ssh_private_key.get_secret_value().encode())
        fp.flush()

    kube_config_resource = NullTerraformResource(
        id="kube_config_resource",
        provider=kube_config_provider,
        provisioners=[
            local_exec_provisioner,
        ],
        scope=scope,
        triggers={
            "ipv4": ipv4,
            "kubecontext": kubecontext,
            "local_path": local_path,
            "ssh_private_key": ssh_private_key_path,
        },
    )

    return kube_config_resource


@task
def get_kube_config_data_source(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    kube_config_resource: TerraformResource,
) -> TerraformDataSource:
    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        kube_config_data_source = LocalFileTerraformDataSource(
            depends_on=[kube_config_resource],
            filename=config.variables.get("kubeconfig"),
            id="kube_config_data_source",
            scope=scope,
        )

    elif (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.DIGITALOCEAN
    ):
        kube_config_data_source = LocalFileTerraformDataSource(
            depends_on=[kube_config_resource],
            filename=config.variables.get("kubeconfig"),
            id="kube_config_data_source",
            scope=scope,
        )

    else:
        raise ValueError(
            f"Unknown cloud instance provider: {config.variables.get('cloud_instance_provider')}"
        )

    return kube_config_data_source


@task
def get_kube_config_outputs(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    kube_config_data_source: TerraformDataSource,
) -> Dict[str, TerraformOutput]:
    kube_config_outputs = {}

    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        kube_config_outputs["config_path"] = TerraformOutput(
            scope=scope,
            id="kube_config_outputs_config_path",
            value=kube_config_data_source.filename,
        )

        kube_config_outputs["config_context"] = TerraformOutput(
            scope=scope,
            id="kube_config_outputs_config_context",
            value=config.variables.get("kubecontext"),
        )

    else:
        kube_config_outputs["kubeconfig"] = TerraformOutput(
            scope=scope,
            id="kube_config_outputs_kubeconfig",
            value=kube_config_data_source.inputs_input["kubeconfig"],
        )

    return kube_config_outputs
