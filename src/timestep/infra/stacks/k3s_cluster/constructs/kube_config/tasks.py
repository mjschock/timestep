import datetime
import tempfile
from typing import Dict

from cdktf import (
    LocalExecProvisioner,
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from prefect import task
from pydantic import SecretStr

from timestep.conf.blocks import AppConfig, CloudInstanceProvider
from timestep.infra.imports.local.data_local_file import (
    DataLocalFile as LocalFileTerraformDataSource,
)
from timestep.infra.imports.local.provider import LocalProvider
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.resource import Resource
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.blocks import (
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

    # kube_config_provider = LocalProvider(
    #     alias="kube_config_provider",
    #     id="kube_config_provider",
    #     scope=scope,
    # )

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
    local_path = config.variables.get("kubeconfig")
    # local_path = "kube-config.yaml"

    ssh_private_key: SecretStr = config.secrets.get_secret_value().get(
        "ssh_private_key"
    )
    ssh_private_key_path: str

    with tempfile.NamedTemporaryFile(
        delete=False,
    ) as fp:
        ssh_private_key_path = fp.name

        command = f"""k3sup install \
--context {kubecontext} \
--ip {ipv4} \
--local-path {local_path} \
--skip-install \
--ssh-key {ssh_private_key_path} \
--user ubuntu && rm {ssh_private_key_path}"""

        local_exec_provisioner = LocalExecProvisioner(
            command=command,
            type="local-exec",
        )

        fp.write(ssh_private_key.get_secret_value().encode())
        fp.flush()

        kube_config_resource = Resource(
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
                "now": datetime.datetime.now().isoformat(),
                "ssh_private_key": str(
                    ssh_private_key
                ),  # TODO: Make sure this is hidden  # noqa: E501
            },
        )

        # kube_config_resource = LocalFileTerraformResource(
        #     id="kube_config_resource",
        #     #             content=f"""{ipv4} {subdomains[0]}.{primary_domain_name}
        #     # {ipv4} {subdomains[1]}.{primary_domain_name}
        #     # {ipv4} {primary_domain_name}
        #     # """,
        #     # filename=f"{config.BASE_PATH}/{config.HOSTS_FILE_PATH}",
        #     # filename="hosts",
        #     filename=local_path,
        #     source=local_path,
        #     provider=kube_config_provider,
        #     # provisioners=[
        #     #     local_exec_provisioner,
        #     # ],
        #     scope=scope,
        # )

    return kube_config_resource


@task
def get_kube_config_data_source(
    scope: TerraformStack,
    config: AppConfig,
    cloud_instance_construct: CloudInstanceConstruct,
    kube_config_resource: TerraformResource,
) -> TerraformDataSource:
    local_provider = LocalProvider(
        alias="local_provider",
        id="local_provider",
        scope=scope,
    )

    if (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.MULTIPASS
    ):
        kube_config_data_source = LocalFileTerraformDataSource(
            depends_on=[kube_config_resource],
            # filename=config.variables.get("kubeconfig"),
            # filename=kube_config_resource.filename,
            filename=kube_config_resource.triggers_input["local_path"],
            id="kube_config_data_source",
            provider=local_provider,
            scope=scope,
        )

    elif (
        config.variables.get("cloud_instance_provider")
        == CloudInstanceProvider.DIGITALOCEAN
    ):
        kube_config_data_source = LocalFileTerraformDataSource(
            depends_on=[kube_config_resource],
            # filename=config.variables.get("kubeconfig"),
            # filename=kube_config_resource.filename,
            filename=kube_config_resource.triggers_input["local_path"],
            id="kube_config_data_source",
            provider=local_provider,
            scope=scope,
        )

    else:
        cloud_instance_provider = config.variables.get("cloud_instance_provider")
        raise ValueError(f"Unknown cloud instance provider: {cloud_instance_provider}")

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
        # kube_config_outputs["kubeconfig"] = TerraformOutput(
        #     scope=scope,
        #     id="kube_config_outputs_kubeconfig",
        #     value=kube_config_data_source.inputs_input["kubeconfig"],
        # )

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

    return kube_config_outputs
