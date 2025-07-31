from fastapi import APIRouter, Depends, Request

from backend.services.images_service import ImagesService

images_router = APIRouter()


@images_router.post("/images/edits")
async def create_image_edit(request: Request, service: ImagesService = Depends()):  # noqa: B008
    """
    Creates an edited or extended image given one or more source images and a prompt. This endpoint only supports `gpt-image-1` and `dall-e-2`.
    """
    return await service.create_image_edit(request)


@images_router.post("/images/generations")
async def create_image(
    request: Request,
    service: ImagesService = Depends(ImagesService),  # noqa: B008
):
    """Creates an image given a prompt. [Learn more](/docs/guides/images)."""
    return await service.create_image(request)


@images_router.post("/images/variations")
async def create_image_variation(request: Request, service: ImagesService = Depends()):  # noqa: B008
    """Creates a variation of a given image. This endpoint only supports `dall-e-2`."""
    return await service.create_image_variation(request)
