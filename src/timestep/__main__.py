from cdktf import App

from timestep.config import Settings
from timestep.infra.stacks.k3s_cluster.stack import K3sClusterStack
from timestep.infra.stacks.kubernetes_config.stack import KubernetesConfigStack


def main() -> None:
    config = Settings()
    app: App = App(
        context={
            "allowSepCharsInLogicalIds": "true",
            "excludeStackIdFromLogicalIds": "true",
        },
        outdir=config.cdktf_outdir,
        skip_validation=False,
        stack_traces=True,
    )

    assert app.node.get_context("allowSepCharsInLogicalIds") == "true"
    assert app.node.get_context("excludeStackIdFromLogicalIds") == "true"

    k3s_cluster_stack = K3sClusterStack(
        config=config,
        id=f"{config.primary_domain_name}.k3s_cluster",
        scope=app,
    )

    kubernetes_config_stack = KubernetesConfigStack(
        config=config,
        # kube_config=k3s_cluster_stack.kube_config_contruct.data_source.filename,
        id=f"{config.primary_domain_name}.kubernetes_config",
        scope=app,
    )

    kubernetes_config_stack.add_dependency(k3s_cluster_stack)

    # for stack in [k3s_cluster_stack, kubernetes_config_stack]:
    #     if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
    #         LocalBackend(
    #             path=f"{config.dist_path}/terraform.{stack.id}.tfstate",
    #             scope=stack,
    #             workspace_dir=None,
    #         )

    #     else:
    #         HttpBackend(
    #             address=config.tf_http_address,
    #             lock_address=f"{config.tf_http_address}/lock",
    #             lock_method="POST",
    #             password=config.tf_api_token.get_secret_value(),
    #             retry_wait_min=5,
    #             scope=stack,
    #             unlock_address=f"{config.tf_http_address}/lock",
    #             unlock_method="DELETE",
    #             username=config.tf_username,
    #         )

    app.synth()


if __name__ == "__main__":
    main()
