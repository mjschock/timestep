from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
    ReleaseSet,
    ReleaseSetListStruct,
)
from cdktf_cdktf_provider_kubernetes.config_map_v1 import (
    ConfigMapV1,
    ConfigMapV1Metadata,
)
from constructs import Construct

from timestep.config import Settings


class KubeRayConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.kube_ray_kuberay_operator_helm_release_resource = Release(
            id_="kube_ray_kuberay_operator_helm_release_resource",
            atomic=True,
            chart="kuberay-operator",
            create_namespace=True,
            name="kuberay-operator",
            namespace="default",
            repository="https://ray-project.github.io/kuberay-helm",
            provider=helm_provider,
            scope=self,
            version="1.0.0-rc.1",
        )

        # values_asset = TerraformAsset(
        #     id="kube_ray_ray_cluster_helm_release_resource_values_asset",
        #     path=os.path.join(
        #         os.path.dirname(__file__), "values.yaml" # https://github.com/ray-project/kuberay/blob/master/helm-chart/ray-cluster/values.yaml
        #     ),
        #     scope=self,
        #     type=AssetType.FILE,
        # )

        kube_ray_ray_cluster_head_config_map = ConfigMapV1(
            id_="kube_ray_ray_cluster_head_config_map",
            data={
                "RAY_GRAFANA_HOST": "http://prometheus-grafana.prometheus-system.svc:80",
                "RAY_GRAFANA_IFRAME_HOST": "http://127.0.0.1:3000",
                "RAY_PROMETHEUS_HOST": "http://prometheus-kube-prometheus-prometheus.prometheus-system.svc:9090",
            },
            metadata=ConfigMapV1Metadata(
                name="kube-ray-ray-cluster-head-config-map",
                namespace="default",
            ),
            scope=self,
        )

        self.kube_ray_ray_cluster_helm_release_resource = Release(
            depends_on=[self.kube_ray_kuberay_operator_helm_release_resource],
            id_="kube_ray_ray_cluster_helm_release_resource",
            atomic=True,
            chart="ray-cluster",
            create_namespace=True,
            name="ray-cluster",
            namespace="default",
            repository="https://ray-project.github.io/kuberay-helm",
            provider=helm_provider,
            scope=self,
            set=[
                ReleaseSet(
                    name="head.resources.limits.cpu",
                    type="string",
                    value="1",
                ),
                ReleaseSet(
                    name="head.resources.limits.memory",
                    value="2G",
                ),
                ReleaseSet(
                    name="head.resources.requests.cpu",
                    type="string",
                    value="1",
                ),
                ReleaseSet(
                    name="head.resources.requests.memory",
                    value="2G",
                ),
                ReleaseSet(
                    name="image.tag",
                    value=f"{config.ray_version}-{config.python_target_version}",
                ),
                ReleaseSet(
                    name="worker.resources.limits.cpu",
                    type="string",
                    value="1",
                ),
                ReleaseSet(
                    name="worker.resources.limits.memory",
                    value="1G",
                ),
                ReleaseSet(
                    name="worker.resources.requests.cpu",
                    type="string",
                    value="1",
                ),
                ReleaseSet(
                    name="worker.resources.requests.memory",
                    value="1G",
                ),
            ],
            set_list=[
                # ReleaseSet(
                #     name="head.envFrom",
                #     value=kube_ray_ray_cluster_head_config_map.metadata.name,
                # ),
                # https://docs.ray.io/en/latest/cluster/kubernetes/k8s-ecosystem/pyspy.html
                # TODO: Make these values configurable
                ReleaseSetListStruct(
                    name="head.securityContext.capabilities.add",
                    value=[
                        "SYS_PTRACE",
                    ],
                ),
                ReleaseSetListStruct(
                    name="worker.securityContext.capabilities.add",
                    value=[
                        "SYS_PTRACE",
                    ],
                ),
            ],
            # values=[
            #     Fn.file(values_asset.path),
            # ],
            values=[
                f"""head:
  envFrom:
    - configMapRef:
        name: {kube_ray_ray_cluster_head_config_map.metadata.name}
            """
            ],
            version="1.0.0-rc.1",
        )
