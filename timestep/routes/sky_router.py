import base64
import logging
import os
from typing import List

import kubernetes
import reflex as rx
import sky
import sky.check
import sky.exceptions
import sky.clouds.kubernetes
import sky.serve.core
from sky.serve import serve_utils
import yaml

from timestep.utils import create_sky_config, serve

logger = logging.getLogger(__name__)

async def create_cluster(cluster_name: str = "sky-serve-cluster"):
    # Launch a cluster or task.
    # sky launch

    ray_serve_job_id = await serve(cluster_name=cluster_name)

    return {
        "ray_serve_job_id": ray_serve_job_id,
    }

async def create_service(service_name: str = "http-server"):
    # Launch a SkyServe service.
    # sky serve up

    task = sky.Task(
        run="serve run serve:app --host 0.0.0.0",
        # Specifying `--host` and `--port` to `serve run` is deprecated and will be removed in a future version. To specify custom HTTP options, use the `serve start` command.
        # run="serve run serve:app",
        setup="pip install -r requirements.txt",
        workdir=f"{os.getcwd()}/timestep/services/serve",
    ).set_resources(
        [
            sky.Resources(
                cloud=sky.clouds.Kubernetes(),
                cpus="1+",
                memory="0.1+",
                ports=[8000],
            ),
        ]
    ).set_service(
        service=sky.serve.SkyServiceSpec(
            initial_delay_seconds=3,
            min_replicas=1,
            readiness_path="/",
            readiness_timeout_seconds=30,
        )
    )

    try:
        service_name, endpoint = sky.serve.up(
            service_name=service_name,
            task=task,
        )

    except Exception as e:
        logger.error(f"type: {type(e)}")
        logger.error(f"Exception: {e}")

        return

    return {
        "endpoint": endpoint,
        "service_name": service_name,
    }

# async def put_service(service_name: str = "http-server"):
#     # sky serve update --mode blue_green service-name new_service.yaml
#     try:
#         sky.serve.update(
#             mode=serve_utils.UpdateMode.BLUE_GREEN,
#             service_name=service_name,
#             task=...,
#         )

#     except Exception as e:
#         logger.error(f"type: {type(e)}")
#         logger.error(f"Exception: {e}")

#         return

async def get_clusters(cluster_name: str = "sky-serve-cluster", refresh: bool = True):
    try:
        cluster_names: List[str] = [cluster_name]
        cluster_statuses = sky.status(cluster_names=cluster_names, refresh=refresh)
        logger.info(f"Cluster statuses: {cluster_statuses}")

    except Exception as e:
        logger.error(f"type: {type(e)}")
        logger.error(f"Exception: {e}")

        return

    return {
        'cluster_statuses': cluster_statuses
    }

def add_api_routes(app: rx.App):
    app.api.add_api_route(
        "/sky/clusters",
        endpoint=create_cluster,
        methods=['POST'],
    )

    app.api.add_api_route(
        "/sky/services",
        endpoint=create_service,
        methods=['POST'],
    )

    app.api.add_api_route(
        "/sky/clusters",
        endpoint=get_clusters,
        methods=['GET'],
    )

    return app
