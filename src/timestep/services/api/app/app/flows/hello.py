import os

# from kubernetes import client, config
import kubernetes
import sky
from prefect import flow, get_run_logger, tags
from prefect_shell import shell_run_command


@flow(log_prints=True)
def hello(name: str = "Marvin"):
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")

    output = shell_run_command(
        command="whoami",
        return_all=True,
    )

    print("whoami: ", output)

    output = shell_run_command(
        command="pwd",
        return_all=True,
    )

    print("pwd: ", output)

    output = shell_run_command(
        command="ls -al",
        return_all=True,
    )

    print("ls -al: ", output)

    output = shell_run_command(
        command="ls -al /run/secrets",
        return_all=True,
    )

    print("ls -al /run/secrets: ", output)

    # k8s_config = KubernetesClusterConfig.from_file("~/.kube/config")
    # cluster_config_block = KubernetesClusterConfig.from_file("/run/secrets/kubeconfig")  # noqa: E501

    # print("cluster_config_block: ", cluster_config_block)

    # KubernetesCredentials(cluster_config=cluster_config_block)

    # output = shell_run_command(
    #     command="cp /run/secrets/kubeconfig ~/.kube/config",
    #     helper_command="mkdir -p ~/.kube",
    #     return_all=True,
    # )

    # print("cp output: ", output)

    # if ~/.kube/config does not exist
    if not os.path.exists("~/.kube/config"):
        print("creating ~/.kube/config")

        if os.path.exists("/run/secrets/kubeconfig"):
            print("copying /run/secrets/kubeconfig to ~/.kube/config")

            output = shell_run_command(
                command="cp /run/secrets/kubeconfig ~/.kube/config",
                helper_command="mkdir -p ~/.kube",
                return_all=True,
            )

            print("cp output: ", output)

        else:
            print("creating ~/.kube/config from incluster config")

            kubernetes.config.load_incluster_config()
            config: kubernetes.client.Configuration = (
                kubernetes.client.Configuration.get_default_copy()
            )  # noqa: E501

            print("config: ", config)

    assert os.path.exists("~/.kube/config"), "~/.kube/config does not exist"

    output = shell_run_command(
        command="poetry run sky check",
        return_all=True,
    )

    print("output: ", output)

    task = sky.Task(
        run="echo hello SkyPilot!",
    )
    sky.launch(task)

    return output


if __name__ == "__main__":
    with tags("local"):
        hello()
