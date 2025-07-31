from fastapi import APIRouter, Depends, Request

from backend.services.batches_service import BatchesService

batches_router = APIRouter()


@batches_router.post("/batches")
async def create_batch(request: Request, service: BatchesService = Depends()):  # noqa: B008
    """Creates and executes a batch from an uploaded file of requests"""
    body = await request.json()
    return service.create_batch(body)


@batches_router.get("/batches")
def list_batches(
    after: str = None,
    limit: str = None,
    request: Request = None,
    service: BatchesService = Depends(),  # noqa: B008
):
    """List your organization's batches."""
    return service.list_batches(after, limit)


@batches_router.get("/batches/{batch_id}")
def retrieve_batch(
    batch_id: str,
    request: Request = None,
    service: BatchesService = Depends(),  # noqa: B008
):
    """Retrieves a batch."""
    return service.retrieve_batch(batch_id)


@batches_router.post("/batches/{batch_id}/cancel")
def cancel_batch(
    batch_id: str,
    request: Request = None,
    service: BatchesService = Depends(),  # noqa: B008
):
    """
    Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.
    """
    return service.cancel_batch(batch_id)
