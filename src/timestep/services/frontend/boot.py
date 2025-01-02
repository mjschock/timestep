import os

import yaml
from kubernetes import client
from kubernetes.client import V1Deployment, V1Ingress, V1Service


def create_deployment() -> V1Deployment:
    """Create a Kubernetes Deployment object for the frontend."""

    container = client.V1Container(
        name="frontend",
        image="flet-fastapi-frontend:latest",
        ports=[client.V1ContainerPort(container_port=8550)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "200m", "memory": "256Mi"},
            limits={"cpu": "500m", "memory": "512Mi"},
        ),
        env=[client.V1EnvVar(name="BACKEND_URL", value="http://backend-service:8000")],
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "frontend"}),
        spec=client.V1PodSpec(containers=[container]),
    )

    spec = client.V1DeploymentSpec(
        replicas=2,
        selector=client.V1LabelSelector(match_labels={"app": "frontend"}),
        template=template,
    )

    return client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="frontend-deployment"),
        spec=spec,
    )


def create_service() -> V1Service:
    """Create a Kubernetes Service object for the frontend."""

    return client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(name="frontend-service"),
        spec=client.V1ServiceSpec(
            selector={"app": "frontend"},
            ports=[client.V1ServicePort(port=80, target_port=8550)],
            type="LoadBalancer",
        ),
    )


def create_ingress() -> V1Ingress:
    """Create a Kubernetes Ingress object."""

    return client.V1Ingress(
        api_version="networking.k8s.io/v1",
        kind="Ingress",
        metadata=client.V1ObjectMeta(
            name="frontend-ingress",
            annotations={"nginx.ingress.kubernetes.io/rewrite-target": "/"},
        ),
        spec=client.V1IngressSpec(
            rules=[
                client.V1IngressRule(
                    http=client.V1HTTPIngressRuleValue(
                        paths=[
                            client.V1HTTPIngressPath(
                                path="/",
                                path_type="Prefix",
                                backend=client.V1IngressBackend(
                                    service=client.V1IngressServiceBackend(
                                        name="frontend-service",
                                        port=client.V1ServiceBackendPort(number=80),
                                    )
                                ),
                            )
                        ]
                    )
                )
            ]
        ),
    )


def generate_manifests():
    """Generate Kubernetes manifests for frontend services."""

    # Create k8s directory if it doesn't exist
    os.makedirs("k8s", exist_ok=True)

    # Generate manifests
    manifests = {
        "deployment.yaml": create_deployment(),
        "service.yaml": create_service(),
        "ingress.yaml": create_ingress(),
    }

    # Save manifests to files
    for filename, manifest in manifests.items():
        with open(f"k8s/{filename}", "w") as f:
            yaml.dump(
                client.ApiClient().sanitize_for_serialization(manifest),
                f,
                default_flow_style=False,
            )


if __name__ == "__main__":
    generate_manifests()
    print(
        "Frontend Kubernetes manifests generated successfully in the 'k8s' directory."
    )
