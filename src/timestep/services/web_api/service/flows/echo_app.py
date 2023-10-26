import os

import sky
from prefect import flow, tags
from prefect_shell import shell_run_command
from sky.clouds.kubernetes import CREDENTIAL_PATH


@flow(log_prints=True)
def sky_flow():
    if not os.path.exists(os.path.expanduser(CREDENTIAL_PATH)):
        # with open(os.path.expanduser(CREDENTIAL_PATH), "w") as f:

        output = shell_run_command(
            command="ls -al /run/secrets",
            return_all=True,
        )

        print("ls -al /run/secrets: ", output)

        if os.path.exists("/run/secrets/kubeconfig"):
            print("copying /run/secrets/kubeconfig to ~/.kube/config")

            output = shell_run_command(
                command="cat /run/secrets/kubeconfig > ~/.kube/config",
                helper_command="mkdir -p ~/.kube",
                return_all=True,
            )

            print("cp output: ", output)

    assert os.path.exists(
        os.path.expanduser(CREDENTIAL_PATH)
    ), f"{os.path.expanduser(CREDENTIAL_PATH)} does not exist"  # noqa: E501

    output = shell_run_command(
        command="poetry run sky check",
        return_all=True,
    )

    with sky.Dag() as dag:
        # The setup command to build the container image
        setup = "docker build -t echo:v0 /echo_app"

        # The command to run - runs the container and mounts volumes
        run = (
            'docker run --rm --volume="/inputs:/inputs:ro" '
            '--volume="/outputs:/outputs:rw" '
            "echo:v0 /inputs/README.md /outputs/output.txt"
        )

        echo_app = sky.Task(
            setup=setup,
            run=run,
        )

        # echo_app.set_resources(

        # Configure file mounts to copy local contents to remote
        echo_app.set_file_mounts(
            {
                "/inputs": "./echo_app",
                "/echo_app": "./echo_app",
            }
        )

        # Configure outputs for the task - we'll write to a bucket using Sky Storage
        # # output_storage = sky.Storage(name=output_bucket_name,
        # #                             mode=sky.StorageMode.MOUNT)

        # output_storage = sky.Storage(name=output_bucket_name,
        #                             source=LOCAL_SOURCE_PATH)

        # echo_app.set_storage_mounts({
        #     '/outputs': output_storage,

        # Set resources if required
        # echo_app.set_resources({

    sky.launch(dag)

    print(
        "Remember to clean up resources after this script is done!\n"
        "Run sky status and sky storage ls to list current resources.\n"
        "Run sky down <cluster_name> and sky storage delete <storage_name> to "
        "delete resources."
    )


if __name__ == "__main__":
    with tags("sky"):
        sky_flow()
