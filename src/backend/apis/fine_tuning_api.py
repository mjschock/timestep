from fastapi import APIRouter, BackgroundTasks, Depends, Request

from backend.services.fine_tuning_service import FineTuningService

fine_tuning_router = APIRouter()


@fine_tuning_router.post("/fine_tuning/alpha/graders/run")
def run_grader(request: Request, service: FineTuningService = Depends()):  # noqa: B008
    """Run a grader."""
    return service.run_grader()


@fine_tuning_router.post("/fine_tuning/alpha/graders/validate")
def validate_grader(request: Request, service: FineTuningService = Depends()):  # noqa: B008
    """Validate a grader."""
    return service.validate_grader()


@fine_tuning_router.get(
    "/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions",
)
def list_fine_tuning_checkpoint_permissions(
    fine_tuned_model_checkpoint: str,
    project_id: str,
    after: str,
    limit: str,
    order: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """
    **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

    Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.
    """
    return service.list_fine_tuning_checkpoint_permissions()


@fine_tuning_router.post(
    "/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions",
)
def create_fine_tuning_checkpoint_permission(
    fine_tuned_model_checkpoint: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """
    **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

    This enables organization owners to share fine-tuned models with other projects in their organization.
    """
    return service.create_fine_tuning_checkpoint_permission()


@fine_tuning_router.delete(
    "/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}",
)
def delete_fine_tuning_checkpoint_permission(
    fine_tuned_model_checkpoint: str,
    permission_id: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """
    **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

    Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.
    """
    return service.delete_fine_tuning_checkpoint_permission()


@fine_tuning_router.post("/fine_tuning/jobs")
async def create_fine_tuning_job(
    request: Request,
    background_tasks: BackgroundTasks,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """
    Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

    Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

    [Learn more about fine-tuning](/docs/guides/model-optimization)
    """
    return await service.create_fine_tuning_job(request, background_tasks)


@fine_tuning_router.get("/fine_tuning/jobs")
def list_paginated_fine_tuning_jobs(
    after: str = None,
    limit: str = None,
    metadata: str = None,
    request: Request = None,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """List your organization's fine-tuning jobs"""
    return service.list_paginated_fine_tuning_jobs(after, limit, metadata)


@fine_tuning_router.get("/fine_tuning/jobs/{fine_tuning_job_id}")
def retrieve_fine_tuning_job(
    fine_tuning_job_id: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """
    Get info about a fine-tuning job.

    [Learn more about fine-tuning](/docs/guides/model-optimization)
    """
    from fastapi import HTTPException

    result = service.retrieve_fine_tuning_job(fine_tuning_job_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Fine-tuning job not found")
    return result


@fine_tuning_router.post("/fine_tuning/jobs/{fine_tuning_job_id}/cancel")
async def cancel_fine_tuning_job(
    fine_tuning_job_id: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """Immediately cancel a fine-tune job."""
    from fastapi import HTTPException

    result = service.cancel_fine_tuning_job(fine_tuning_job_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Fine-tuning job not found")
    return result


@fine_tuning_router.get("/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints")
def list_fine_tuning_job_checkpoints(
    fine_tuning_job_id: str,
    after: str = None,
    limit: str = None,
    request: Request = None,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """List checkpoints for a fine-tuning job."""
    return service.list_fine_tuning_job_checkpoints(fine_tuning_job_id, after, limit)


@fine_tuning_router.get("/fine_tuning/jobs/{fine_tuning_job_id}/events")
def list_fine_tuning_events(
    fine_tuning_job_id: str,
    after: str = None,
    limit: str = None,
    request: Request = None,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """Get status updates for a fine-tuning job."""
    from fastapi import HTTPException

    result = service.list_fine_tuning_events(fine_tuning_job_id, limit, after)
    if result is None:
        raise HTTPException(status_code=404, detail="Fine-tuning job not found")
    return result


@fine_tuning_router.post("/fine_tuning/jobs/{fine_tuning_job_id}/pause")
def pause_fine_tuning_job(
    fine_tuning_job_id: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """Pause a fine-tune job."""
    return service.pause_fine_tuning_job()


@fine_tuning_router.post("/fine_tuning/jobs/{fine_tuning_job_id}/resume")
def resume_fine_tuning_job(
    fine_tuning_job_id: str,
    request: Request,
    service: FineTuningService = Depends(),  # noqa: B008
):
    """Resume a fine-tune job."""
    return service.resume_fine_tuning_job()
