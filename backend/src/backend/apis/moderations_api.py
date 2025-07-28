from typing import Any

from fastapi import APIRouter, Depends, Request

from backend.services.moderations_service import ModerationsService

moderations_router = APIRouter()


@moderations_router.post("/moderations")
async def create_moderation(
    request: Request,
    service: ModerationsService = Depends(ModerationsService),  # noqa: B008
) -> dict[str, Any]:
    """
    Classifies if text and/or image inputs are potentially harmful. Learn
    more in the [moderation guide](/docs/guides/moderation).
    """
    body = await request.json()
    return service.create_moderation(body)
