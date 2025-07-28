from typing import Any

from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import Response

from backend.logging_config import logger
from backend.services.files_service import FilesService

files_router = APIRouter()

# Module-level constants for dependencies to avoid ruff B008
FILE_DEPENDENCY = File(...)
FORM_DEPENDENCY = Form(...)


@files_router.get("/files")
def list_files(
    purpose: str | None = None,
    limit: int | None = None,
    order: str | None = None,
    after: str | None = None,
    service: FilesService = Depends(FilesService),  # noqa: B008
) -> dict[str, Any]:
    """
    Lists the files that have been uploaded. All query parameters are optional for OpenAI compatibility.
    """
    logger.info(f"Listing files with purpose={purpose}, limit={limit}")
    return service.list_files(purpose, str(limit) if limit else None, order, after)


@files_router.post("/files")
async def create_file(
    file: UploadFile = FILE_DEPENDENCY,
    purpose: str = FORM_DEPENDENCY,
    service: FilesService = Depends(FilesService),  # noqa: B008
) -> dict[str, Any]:
    """
    Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.
    """
    logger.info(f"Creating file: {file.filename}, purpose: {purpose}")
    return await service.create_file_with_upload(file, purpose)


@files_router.delete("/files/{file_id}")
def delete_file(file_id: str, service: FilesService = Depends()) -> dict[str, Any]:  # noqa: B008
    """Delete a file."""
    logger.info(f"Deleting file: {file_id}")
    return service.delete_file(file_id)


@files_router.get("/files/{file_id}")
def retrieve_file(file_id: str, service: FilesService = Depends()) -> dict[str, Any]:  # noqa: B008
    """Returns information about a specific file."""
    logger.info(f"Retrieving file: {file_id}")
    return service.retrieve_file(file_id)


@files_router.get("/files/{file_id}/content")
def download_file(
    file_id: str,
    service: FilesService = Depends(FilesService),  # noqa: B008
) -> Response:
    """Returns the contents of the specified file."""
    import base64

    # Response already imported at top
    logger.info(f"Downloading file: {file_id}")

    file_path = service.download_file(file_id)

    # Get file metadata to check purpose
    file_obj = service.retrieve_file(file_id)

    # Read the file content
    with open(file_path, "rb") as f:
        file_content = f.read()

    # For fine-tune-results files, return base64 encoded content
    # This matches the expected behavior in OpenAI's API for result files
    if file_obj.get("purpose") == "fine-tune-results":
        logger.debug(
            f"Returning base64 encoded content for fine-tune-results file: {file_id}"
        )
        base64_content = base64.b64encode(file_content)
        return Response(
            content=base64_content,
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f"attachment; filename={file_path.split('-', 1)[-1]}"
            },
        )
    else:
        # For other files, return raw content
        logger.debug(f"Returning raw content for file: {file_id}")
        return Response(
            content=file_content,
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f"attachment; filename={file_path.split('-', 1)[-1]}"
            },
        )
