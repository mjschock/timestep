from cdktf import App

from timestep.config import Settings
from timestep.infra.stacks.k3s_cluster.stack import K3sClusterStack
from timestep.infra.stacks.kubernetes_config.stack import KubernetesConfigStack
from timestep.infra.stacks.platform.stack import PlatformStack


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
        id=f"{config.primary_domain_name}.kubernetes_config",
        scope=app,
    )

    kubernetes_config_stack.add_dependency(k3s_cluster_stack)

    platform_stack = PlatformStack(
        config=config,
        id=f"{config.primary_domain_name}.platform",
        scope=app,
    )

    platform_stack.add_dependency(kubernetes_config_stack)

    app.synth()


if __name__ == "__main__":
    main()
