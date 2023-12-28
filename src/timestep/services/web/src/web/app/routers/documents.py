import httpx
from fastapi import APIRouter

client = httpx.AsyncClient()

router = APIRouter(
    prefix="/api/documents",
    tags=["documents"],
    # dependencies=[Depends(get_current_user)],
    # responses={404: {"description": "Not found"}},
)


@router.on_event("startup")
async def startup():
    # logger.info("Starting up agents router")
    print("=== (print) Starting up documents router ===")

    # await documents_service.init_documents_service()


@router.get(
    "",
)
async def get_threads():
    return {"documents": []}
