from typing import Any

from fastapi import APIRouter, Depends, Request

from backend.services.evals_service import EvalsService

evals_router = APIRouter()


@evals_router.get("/evals")
def list_evals(
    request: Request,
    after: str | None = None,
    limit: str | None = None,
    order: str | None = None,
    order_by: str | None = None,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """List evaluations for a project."""
    return service.list_evals(after, limit, order, order_by)


@evals_router.post("/evals")
async def create_eval(request: Request, service: EvalsService = Depends()) -> Any:  # noqa: B008
    """
    Create the structure of an evaluation that can be used to test a model's performance.
    An evaluation is a set of testing criteria and the config for a data source, which dictates the schema of the data used in the evaluation. After creating an evaluation, you can run it on different models and model parameters. We support several types of graders and datasources.
    For more information, see the [Evals guide](/docs/guides/evals).
    """
    body = await request.json()
    return service.create_eval(body)


@evals_router.get("/evals/{eval_id}")
def get_eval(eval_id: str, request: Request, service: EvalsService = Depends()) -> Any:  # noqa: B008
    """Get an evaluation by ID."""
    return service.get_eval(eval_id)


@evals_router.post("/evals/{eval_id}")
async def update_eval(
    eval_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Update certain properties of an evaluation."""
    body = await request.json()
    return service.update_eval(eval_id, body)


@evals_router.delete("/evals/{eval_id}")
def delete_eval(
    eval_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Delete an evaluation."""
    return service.delete_eval(eval_id)


@evals_router.get("/evals/{eval_id}/runs")
def get_eval_runs(
    eval_id: str,
    request: Request,
    after: str | None = None,
    limit: str | None = None,
    order: str | None = None,
    status: str | None = None,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Get a list of runs for an evaluation."""
    return service.get_eval_runs(eval_id, after, limit, order, status)


@evals_router.post("/evals/{eval_id}/runs")
async def create_eval_run(
    eval_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """
    Kicks off a new run for a given evaluation, specifying the data source, and what model configuration to use to test. The datasource will be validated against the schema specified in the config of the evaluation.
    """
    body = await request.json()
    return service.create_eval_run(eval_id, body)


@evals_router.get("/evals/{eval_id}/runs/{run_id}")
def get_eval_run(
    eval_id: str,
    run_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Get an evaluation run by ID."""
    return service.get_eval_run(eval_id, run_id)


@evals_router.post("/evals/{eval_id}/runs/{run_id}")
def cancel_eval_run(
    eval_id: str,
    run_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Cancel an ongoing evaluation run."""
    return service.cancel_eval_run(eval_id, run_id)


@evals_router.delete("/evals/{eval_id}/runs/{run_id}")
def delete_eval_run(
    eval_id: str,
    run_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Delete an eval run."""
    return service.delete_eval_run(eval_id, run_id)


@evals_router.get("/evals/{eval_id}/runs/{run_id}/output_items")
def get_eval_run_output_items(
    eval_id: str,
    run_id: str,
    request: Request,
    after: str | None = None,
    limit: str | None = None,
    status: str | None = None,
    order: str | None = None,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Get a list of output items for an evaluation run."""
    return service.get_eval_run_output_items(
        eval_id, run_id, after, limit, status, order
    )


@evals_router.get("/evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}")
def get_eval_run_output_item(
    eval_id: str,
    run_id: str,
    output_item_id: str,
    request: Request,
    service: EvalsService = Depends(),  # noqa: B008
) -> Any:
    """Get an evaluation run output item by ID."""
    return service.get_eval_run_output_item(eval_id, run_id, output_item_id)
