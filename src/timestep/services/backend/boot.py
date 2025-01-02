import os

import yaml
from kubernetes import client
from kubernetes.client import V1Deployment, V1Service


def create_deployment() -> V1Deployment:
    """Create a Kubernetes Deployment object for the backend."""

    container = client.V1Container(
        name="backend",
        image="flet-fastapi-backend:latest",
        ports=[client.V1ContainerPort(container_port=8080)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "200m", "memory": "256Mi"},
            limits={"cpu": "500m", "memory": "512Mi"},
        ),
        liveness_probe=client.V1Probe(
            http_get=client.V1HTTPGetAction(path="/api/items", port=8080),
            initial_delay_seconds=5,
            period_seconds=10,
        ),
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "backend"}),
        spec=client.V1PodSpec(containers=[container]),
    )

    spec = client.V1DeploymentSpec(
        replicas=2,
        selector=client.V1LabelSelector(match_labels={"app": "backend"}),
        template=template,
    )

    return client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="backend-deployment"),
        spec=spec,
    )


def create_service() -> V1Service:
    """Create a Kubernetes Service object for the backend."""

    return client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(name="backend-service"),
        spec=client.V1ServiceSpec(
            selector={"app": "backend"},
            ports=[client.V1ServicePort(port=8080, target_port=8080)],
            type="ClusterIP",
        ),
    )


def generate_manifests():
    """Generate Kubernetes manifests for backend services."""

    # Create k8s directory if it doesn't exist
    os.makedirs("k8s", exist_ok=True)

    # Generate manifests
    manifests = {
        "deployment.yaml": create_deployment(),
        "service.yaml": create_service(),
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
    print("Backend Kubernetes manifests generated successfully in the 'k8s' directory.")
