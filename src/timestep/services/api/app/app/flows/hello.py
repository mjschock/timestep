from prefect import flow, get_run_logger, tags
from prefect.blocks.kubernetes import KubernetesClusterConfig
from prefect_kubernetes.credentials import KubernetesCredentials
from prefect_shell import shell_run_command


@flow(log_prints=True)
def hello(name: str = "Marvin"):
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")

    output = shell_run_command(
        command="whoami",
        return_all=True,
    )

    print("output: ", output)

    output = shell_run_command(
        command="pwd",
        return_all=True,
    )

    print("output: ", output)

    output = shell_run_command(
        command="ls -al",
        return_all=True,
    )

    print("output: ", output)

    k8s_config = KubernetesClusterConfig.from_file("~/.kube/config")
    KubernetesCredentials(cluster_config=k8s_config)

    output = shell_run_command(
        command="poetry run sky check",
        return_all=True,
    )

    print("output: ", output)


if __name__ == "__main__":
    with tags("local"):
        hello()
