from __future__ import annotations

import asyncio
from typing import Any

from timestep.flows.__main__ import main
from timestep.flows.register_prefect_flow import my_flow


def cli() -> None:
    pass


def run(*args: list[Any], **kwargs: dict[str, Any]) -> None:
    # print('args:', args)
    # print('kwargs:', kwargs)

    pipeline_name = "__default__"
    env = "base"
    # deployment_name = "example"
    # work_pool_name = "default"
    # work_queue_name = "default"
    # version = "1.0"

    # print('...')
    # prefect_deploy(
    #     pipeline_name, env, deployment_name, work_pool_name, work_queue_name, version
    # )

    # prefect_deploy_params = inspect.signature(prefect_deploy).parameters
    # print('prefect_deploy_params:', prefect_deploy_params)

    # prefect_deploy(
    #     *args, **kwargs
    # )

    my_flow(pipeline_name, env)

    # main()
    asyncio.run(main(*args, **kwargs))
