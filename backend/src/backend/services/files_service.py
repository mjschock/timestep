import os
import time
import uuid
from typing import Any

from fastapi import HTTPException, Request, UploadFile

from backend.logging_config import logger

DATA_DIR = os.path.join("data", "files")
os.makedirs(DATA_DIR, exist_ok=True)

# In-memory metadata store (replace with persistent storage as needed)
FILES_METADATA: dict[str, dict[str, Any]] = {}


class FilesService:
    def list_files(
        self,
        purpose: str | None = None,
        limit: str | None = None,
        order: str | None = None,
        after: str | None = None,
    ) -> dict[str, Any]:
        files = list(FILES_METADATA.values())
        if purpose:
            files = [f for f in files if f["purpose"] == purpose]
        # OpenAI API: order, after, limit (not fully implemented, stub)
        if order == "desc":
            files = sorted(files, key=lambda x: x["created_at"], reverse=True)
        else:
            files = sorted(files, key=lambda x: x["created_at"])
        if after:
            idx = next((i for i, f in enumerate(files) if f["id"] == after), None)
            if idx is not None:
                files = files[idx + 1 :]
        if limit:
            files = files[: int(limit)]
        return {"object": "list", "data": files}

    async def create_file_with_upload(
        self, upload: UploadFile, purpose: str
    ) -> dict[str, Any]:
        """Create a file from an UploadFile object."""
        logger.info(f"Creating file: {upload.filename}, purpose: {purpose}")
        file_id = f"file-{uuid.uuid4().hex[:8]}"
        filename = upload.filename or "unknown"
        file_path = os.path.join(DATA_DIR, file_id + "-" + filename)
        # Save file
        with open(file_path, "wb") as f:
            content = await upload.read()
            f.write(content)
        logger.info(f"File uploaded: {filename} as {file_id}")
        file_obj = {
            "id": file_id,
            "object": "file",
            "bytes": len(content),
            "created_at": int(time.time()),
            "filename": filename,
            "purpose": purpose,
            "status": "uploaded",
            "status_details": None,
        }
        FILES_METADATA[file_id] = file_obj
        return file_obj

    async def create_file(self, request: Request) -> dict[str, Any]:
        form = await request.form()
        logger.info(f"Received form data: {form}")
        upload = form.get("file")
        purpose = form.get("purpose")
        logger.info(f"Upload type: {type(upload)}, Upload value: {upload}")
        logger.info(f"Purpose: {purpose}")
        if not isinstance(upload, UploadFile):
            logger.error("File upload failed: 'file' must be an uploaded file")
            raise HTTPException(
                status_code=400, detail="'file' must be an uploaded file"
            )
        if not upload or not purpose:
            logger.error("File upload failed: missing 'file' or 'purpose'")
            raise HTTPException(
                status_code=400, detail="'file' and 'purpose' are required."
            )
        file_id = f"file-{uuid.uuid4().hex[:8]}"
        filename = upload.filename or "unknown"
        file_path = os.path.join(DATA_DIR, file_id + "-" + filename)
        # Save file
        with open(file_path, "wb") as f:
            content = await upload.read()
            f.write(content)
        logger.info(f"File uploaded: {filename} as {file_id}")
        file_obj = {
            "id": file_id,
            "object": "file",
            "bytes": len(content),
            "created_at": int(time.time()),
            "filename": filename,
            "purpose": purpose,
            "status": "uploaded",
            "status_details": None,
        }
        FILES_METADATA[file_id] = file_obj
        return file_obj

    def delete_file(self, file_id: str) -> dict[str, Any]:
        file_obj = FILES_METADATA.get(file_id)
        if not file_obj:
            logger.error(f"File deletion failed: {file_id} not found")
            raise HTTPException(status_code=404, detail="File not found")
        file_path = os.path.join(DATA_DIR, file_id + "-" + file_obj["filename"])
        try:
            os.remove(file_path)
            logger.info(f"File deleted: {file_id}")
        except FileNotFoundError:
            logger.warning(f"File not found on disk during deletion: {file_id}")
        del FILES_METADATA[file_id]
        return {"id": file_id, "object": "file", "deleted": True}

    def retrieve_file(self, file_id: str) -> dict[str, Any]:
        file_obj = FILES_METADATA.get(file_id)
        if not file_obj:
            raise HTTPException(status_code=404, detail="File not found")
        return file_obj

    def download_file(self, file_id: str) -> str:
        file_obj = FILES_METADATA.get(file_id)
        if not file_obj:
            raise HTTPException(status_code=404, detail="File not found")
        file_path = os.path.join(DATA_DIR, file_id + "-" + file_obj["filename"])
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found on disk")
        return file_path  # The API layer should stream this file
