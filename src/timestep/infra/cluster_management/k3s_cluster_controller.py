import logging
import os
import subprocess

from timestep.utils import ssh_connect


class K3sClusterController:
    """Manages K3s Kubernetes cluster operations."""

    def __init__(self, cluster_config):
        """
        Initialize K3s cluster controller.

        Args:
            cluster_config (dict): Cluster configuration parameters
        """
        self.logger = logging.getLogger(__name__)
        self.cluster_config = cluster_config

    def create_cluster(self):
        """
        Create a new K3s cluster.

        Returns:
            bool: Cluster creation status
        """
        subprocess.run(
            [
                "./scripts/deploy_remote_cluster.sh",
                self.cluster_config["ips_file"],
                self.cluster_config["username"],
                os.path.expanduser(self.cluster_config["ssh_key"]),
            ]
        )

        try:
            import sky.check

            sky.check.check(
                clouds=["kubernetes"],
                quiet=False,
                verbose=True,
            )

        except ModuleNotFoundError as e:
            self.logger.error(f"Failed to import sky.check: {e}")

            subprocess.run(["sky", "check", "k8s"])

        subprocess.run(["sky", "show-gpus", "--cloud", "k8s"])

        SCRIPT = """#!/usr/bin/env bash
        helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow --atomic --create-namespace --namespace mlflow
        """

        ssh_connect(
            self.cluster_config["ip"],
            script=SCRIPT,
            username=self.cluster_config["username"],
            ssh_key=os.path.expanduser(self.cluster_config["ssh_key"]),
        )

    def delete_cluster(self):
        """
        Delete the existing K3s cluster.

        Returns:
            bool: Cluster deletion status
        """
        raise NotImplementedError()
