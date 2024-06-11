import logging
import os

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
        logger.debug(f"Cluster statuses: {cluster_statuses}")

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

    try:
        # with sky.Dag() as dag:
        # A Task that will sync up local workdir '.', containing
        # requirements.txt and train.py.
        # sky.Task(setup='pip install requirements.txt',
        #          run='python train.py',
        #          workdir='.')

        # sky.down(
        #     cluster_name="sky-train-cluster",
        # )

        task = sky.Task(
            # run='echo "Hello, SkyPilot!"',
            run="python train.py",
            setup="pip install -r requirements.txt",
            workdir=f"{os.getcwd()}/app/api/services/ray_train",
        )
        # task.set_resources([
        task.set_resources(
            sky.Resources(
                cloud=sky.clouds.Kubernetes(),
                cpus="1+",
                memory="0.1+",
            ),
            # ])
        )
        job_id, handle = sky.launch(
            task,
            cluster_name="sky-train-cluster",  # "sky-serve-cluster",
            down=True,
        )

        logger.info(f"Job ID: {job_id}")
        logger.info(f"Handle: {handle}")

        logger.debug(f"cwd: {os.getcwd()}")

        ray_serve_task = sky.Task(
            run="serve run serve:app --host 0.0.0.0",
            # setup='pip install "ray[serve]"',
            setup="pip install -r requirements.txt",
            workdir=f"{os.getcwd()}/app/api/services/ray_serve",
        )
        ray_serve_task.set_resources(
            [
                sky.Resources(
                    cloud=sky.clouds.Kubernetes(),
                    cpus="1+",
                    memory="0.1+",
                    ports=[8000],
                ),
            ]
        )
        ray_serve_task.set_service(
            service=sky.serve.SkyServiceSpec(
                initial_delay_seconds=3,
                min_replicas=1,
                readiness_path="/",
            )
        )
        ray_serve_job_id, ray_serve_handle = sky.launch(
            ray_serve_task,
            cluster_name="sky-serve-cluster",
        )

        logger.info(f"Ray Serve Job ID: {ray_serve_job_id}")
        logger.info(f"Ray Serve Handle: {ray_serve_handle}")
    except RuntimeError as e:
        logger.error(f"Runtime error: {e}")

        return app

    except sky.exceptions.ResourcesUnavailableError as e:
        logger.error(f"Resources unavailable: {e}")

        return app

    except Exception as e:
        logger.error(f"type: {type(e)}")
        logger.error(f"Exception: {e}")

    return app
