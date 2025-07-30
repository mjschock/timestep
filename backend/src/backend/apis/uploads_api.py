from typing import Any

from fastapi import APIRouter, Depends, File, Form, Request, UploadFile

from backend.services.uploads_service import UploadsService

uploads_router = APIRouter()


@uploads_router.post("/uploads")
async def create_upload(
    request: Request,
    service: UploadsService = Depends(UploadsService),  # noqa: B008
) -> dict[str, Any]:
    """
    Creates an intermediate [Upload](/docs/api-reference/uploads/object) object
    that you can add [Parts](/docs/api-reference/uploads/part-object) to.
    Currently, an Upload can accept at most 8 GB in total and expires after an
    hour after you create it.

    Once you complete the Upload, we will create a
    [File](/docs/api-reference/files/object) object that contains all the parts
    you uploaded. This File is usable in the rest of our platform as a regular
    File object.

    For certain `purpose` values, the correct `mime_type` must be specified.
    Please refer to documentation for the
    [supported MIME types for your use case](/docs/assistants/tools/file-search#supported-files).

    For guidance on the proper filename extensions for each purpose, please
    follow the documentation on [creating a
    File](/docs/api-reference/files/create).
    """
    body = await request.json()
    return service.create_upload(body)


@uploads_router.post("/uploads/{upload_id}/cancel")
async def cancel_upload(
    upload_id: str,
    request: Request,
    service: UploadsService = Depends(UploadsService),  # noqa: B008
) -> dict[str, Any]:
    """Cancels the Upload. No Parts may be added after an Upload is cancelled."""
    return service.cancel_upload(upload_id)


@uploads_router.post("/uploads/{upload_id}/complete")
async def complete_upload(
    upload_id: str,
    request: Request,
    service: UploadsService = Depends(UploadsService),  # noqa: B008
) -> dict[str, Any]:
    """
    Completes the [Upload](/docs/api-reference/uploads/object).

    Within the returned Upload object, there is a nested [File](/docs/api-reference/files/object) object that is ready to use in the rest of the platform.

    You can specify the order of the Parts by passing in an ordered list of the Part IDs.

    The number of bytes uploaded upon completion must match the number of bytes initially specified when creating the Upload object. No Parts may be added after an Upload is completed.
    """
    body = await request.json()
    return service.complete_upload(upload_id, body)


@uploads_router.post("/uploads/{upload_id}/parts")
async def add_upload_part(
    upload_id: str,
    part: int | None = Form(None),  # Make part optional
    service: UploadsService = Depends(UploadsService),  # noqa: B008
    data: UploadFile = File(...),  # noqa: B008
) -> dict[str, Any]:
    """
    Adds a [Part](/docs/api-reference/uploads/part-object) to an [Upload](/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

    Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

    It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](/docs/api-reference/uploads/complete).
    """
    # Read the file data
    file_content = await data.read()

    # Auto-assign part number if not provided
    if part is None:
        # Get the next available part number from the service
        existing_parts = service.dao.get_upload_parts(upload_id)
        if existing_parts:
            part = max(p.part_number for p in existing_parts) + 1
        else:
            part = 1

    # Create the body in the format expected by the service
    body = {"part": part, "data": file_content}

    return service.add_upload_part(upload_id, body)
