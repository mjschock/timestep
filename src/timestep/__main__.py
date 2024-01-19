from cdktf import App
from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.digitalocean.compute import Droplet
from diagrams.generic.os import Ubuntu
from diagrams.k8s.compute import Deployment, ReplicaSet
from diagrams.k8s.ecosystem import Helm
from diagrams.onprem.container import K3S
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.gitops import ArgoCD
from diagrams.onprem.network import Caddy

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
    # Temporary for quick architecture diagram - TODO: move somewhere more appropriate, use C4 model, etc.  # noqa: E501
    with Diagram("Timestep AI", show=False):
        with Cluster("Infrastructure"):
            with Cluster("Platform Stack"):
                Custom("Hasura", "hasura.png") - Custom("Nhost", "nhost.png") - Helm("Timestep AI")  # noqa: E501

            with Cluster("Kubernetes Config Stack"):
                ArgoCD("Argo CD")- Caddy("Kubernetes Cluster Ingress") - Custom("MinIO", "minio.png") - PostgreSQL("PostgreSQL") - Custom("Prefect", "prefect.png")  # noqa: E501

            with Cluster("K3s Cluster Stack"):
                Ubuntu("Cloud Init Config") - Droplet("Cloud Instance") - K3S("Kube Config")  # noqa: E501

        with Cluster("Services"):
            with Cluster("Platform Services"):
                backend = ReplicaSet("backend")
                frontend = Deployment("frontend")
                backend - frontend

    main()
    # typer.run(main) # TODO: use typer for CLI
