import logging

import reflex as rx
import sky
import sky.check
import sky.exceptions
import sky.serve.core
from fastapi import FastAPI

from app.utils import create_sky_config, load_kubeconfig  # noqa: F401

logger = logging.getLogger(__name__)


async def lifespan(app: FastAPI):
    # Load the ML model
    # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    # yield
    # # Clean up the ML models and release the resources
    # ml_models.clear()

    # load_kubeconfig(overwrite=True)

    # await sky.check.check(
    #     clouds=None,
    #     quiet=False,
    #     verbose=True,
    # )

    # cluster_statuses = await sky.status(refresh=True)
    # logger.info(f"Cluster statuses: {cluster_statuses}")
    # click.echo(f"Cluster statuses: {cluster_statuses}")
    # print(f"Cluster statuses: {cluster_statuses}")

    # service_statuses = await sky.serve.core.status()
    # logger.info(f"Service statuses: {service_statuses}")
    # click.echo(f"Service statuses: {service_statuses}")
    # print(f"Service statuses: {service_statuses}")

    # # task = sky.Task(run='echo "Hello, SkyPilot!"')
    # # await sky.launch(task)

    pass


def add_api_routes(app: rx.App):
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")

    app.register_lifespan_task(
        task=lifespan,
        # task_kwargs={
        #     "logger": logger,
        # }
    )

    logger.info("Done registering lifespan task")
    logger.info("Launching task")

    # load_kubeconfig(overwrite=True)
    # create_sky_config(overwrite=True)

    try:
        sky.check.check(
            clouds=None,
            quiet=False,
            verbose=True,
        )

    except SystemExit as e:
        logger.error(f"System exit: {e}")

        return app

    try:
        cluster_statuses = sky.status(refresh=True)
        logger.warn(f"Cluster statuses: {cluster_statuses}")

    except Exception as e:
        logger.error(f"type: {type(e)}")
        logger.error(f"Exception: {e}")

        return app

    # try:
    #     service_statuses = sky.serve.core.status()
    #     logger.debug(f"Service statuses: {service_statuses}")

    # except sky.exceptions.ClusterNotUpError as e:
    #     logger.error(f"Cluster not up: {e}")

    # return app

    # try:

    #     # with sky.Dag() as dag:
    #     task = sky.Task(run='echo "Hello, SkyPilot!"')
    #     # task.set_resources([
    #     task.set_resources(
    #         sky.Resources(
    #             # cloud=sky.clouds.Kubernetes(),
    #             cpus="0.1+",
    #             # cpus=3,
    #             memory="0.1+",
    #             # memory=3
    #         ),
    #     # ])
    #     )
    #     job_id, handle = sky.launch(
    #         task,
    #         # cluster_name="sky-9b40-ubuntu",
    #         cluster_name="sky-train-cluster", # "sky-serve-cluster",
    #     )

    #     logger.info(f"Job ID: {job_id}")
    #     logger.info(f"Handle: {handle}")

    # except sky.exceptions.ResourcesUnavailableError as e:
    #     logger.error(f"Resources unavailable: {e}")

    #     return app

    return app
