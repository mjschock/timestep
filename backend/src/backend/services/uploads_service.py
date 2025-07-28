import os
import time
import uuid
from typing import Any

from fastapi import HTTPException

DATA_DIR = os.path.join("data", "uploads")
os.makedirs(DATA_DIR, exist_ok=True)

# In-memory metadata store (replace with persistent storage as needed)
UPLOADS_METADATA: dict[str, dict[str, Any]] = {}
UPLOAD_PARTS: dict[str, list[dict[str, Any]]] = {}  # upload_id -> list of parts


class UploadsService:
    def __init__(self) -> None:
        pass

    def create_upload(self, body: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates an intermediate Upload object that you can add Parts to.

        Args:
            body: Request body containing upload metadata

        Returns:
            Dictionary with upload object
        """
        try:
            if not body:
                body = {}

            # Extract required parameters
            filename = body.get("filename")
            purpose = body.get("purpose")
            bytes_size = body.get("bytes")
            mime_type = body.get("mime_type")

            # Validate required parameters
            if not filename:
                raise HTTPException(status_code=400, detail="'filename' is required")
            if not purpose:
                raise HTTPException(status_code=400, detail="'purpose' is required")
            if not bytes_size:
                raise HTTPException(status_code=400, detail="'bytes' is required")
            if not mime_type:
                raise HTTPException(status_code=400, detail="'mime_type' is required")

            # Validate purpose
            valid_purposes = [
                "assistants",
                "assistants_output",
                "batch",
                "fine-tune",
                "fine-tune-results",
            ]
            if purpose not in valid_purposes:
                raise HTTPException(
                    status_code=400,
                    detail=f"'purpose' must be one of: {', '.join(valid_purposes)}",
                )

            # Validate file size (8 GB max)
            max_size = 8 * 1024 * 1024 * 1024  # 8 GB
            if bytes_size > max_size:
                raise HTTPException(
                    status_code=400,
                    detail=f"File size cannot exceed 8 GB, got {bytes_size} bytes",
                )

            # Create upload object
            upload_id = f"upload-{uuid.uuid4().hex[:8]}"
            current_time = int(time.time())

            upload_obj = {
                "id": upload_id,
                "object": "upload",
                "bytes": bytes_size,
                "created_at": current_time,
                "filename": filename,
                "purpose": purpose,
                "status": "created",
                "expires_at": current_time + 3600,  # 1 hour expiration
                "mime_type": mime_type,
            }

            # Store upload metadata
            UPLOADS_METADATA[upload_id] = upload_obj
            UPLOAD_PARTS[upload_id] = []

            return upload_obj

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to create upload: {str(e)}"
            ) from e

    def add_upload_part(
        self, upload_id: str, body: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Adds a Part to an Upload object.

        Args:
            upload_id: The ID of the upload
            body: Request body containing part data

        Returns:
            Dictionary with part object
        """
        try:
            if not body:
                body = {}

            upload_obj = self._validate_upload_exists(upload_id)
            self._validate_upload_status(upload_obj)
            self._validate_upload_not_expired(upload_obj)

            part_number, data = self._extract_and_validate_part_data(body)
            self._validate_part_number(part_number, upload_id)
            self._validate_part_size(data)

            part_obj = self._create_part_object(part_number, data)
            self._store_part_data(upload_id, part_number, data)
            self._add_part_to_upload(upload_id, part_obj)

            return part_obj

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to add upload part: {str(e)}"
            ) from e

    def _validate_upload_exists(self, upload_id: str) -> dict[str, Any]:
        """Validate that upload exists."""
        upload_obj = UPLOADS_METADATA.get(upload_id)
        if not upload_obj:
            raise HTTPException(status_code=404, detail="Upload not found")
        return upload_obj

    def _validate_upload_status(self, upload_obj: dict[str, Any]) -> None:
        """Validate upload status is valid for adding parts."""
        if upload_obj["status"] != "created":
            raise HTTPException(
                status_code=400,
                detail=f"Cannot add parts to upload with status: {upload_obj['status']}",
            )

    def _validate_upload_not_expired(self, upload_obj: dict[str, Any]) -> None:
        """Validate upload has not expired."""
        if time.time() > upload_obj["expires_at"]:
            raise HTTPException(status_code=400, detail="Upload has expired")

    def _extract_and_validate_part_data(
        self, body: dict[str, Any]
    ) -> tuple[int, bytes]:
        """Extract and validate part data from request body."""
        part_number = body.get("part")  # OpenAI uses 'part' instead of 'part_number'
        data = body.get("data")

        if part_number is None:
            raise HTTPException(status_code=400, detail="'part' is required")
        if not data:
            raise HTTPException(status_code=400, detail="'data' is required")

        return part_number, data

    def _validate_part_number(self, part_number: int, upload_id: str) -> None:
        """Validate part number is valid and not duplicate."""
        if not isinstance(part_number, int) or part_number < 1:
            raise HTTPException(
                status_code=400, detail="'part_number' must be a positive integer"
            )

        existing_parts = UPLOAD_PARTS[upload_id]
        if any(part["part_number"] == part_number for part in existing_parts):
            raise HTTPException(
                status_code=400, detail=f"Part number {part_number} already exists"
            )

    def _validate_part_size(self, data: bytes) -> None:
        """Validate part size is within limits."""
        max_part_size = 64 * 1024 * 1024  # 64 MB
        if len(data) > max_part_size:
            raise HTTPException(
                status_code=400,
                detail=f"Part size cannot exceed 64 MB, got {len(data)} bytes",
            )

    def _create_part_object(self, part_number: int, data: bytes) -> dict[str, Any]:
        """Create part object."""
        part_id = f"part-{uuid.uuid4().hex[:8]}"
        return {
            "id": part_id,
            "object": "upload_part",
            "part_number": part_number,
            "bytes": len(data),
            "created_at": int(time.time()),
        }

    def _store_part_data(self, upload_id: str, part_number: int, data: bytes) -> None:
        """Store part data to file."""
        part_path = os.path.join(DATA_DIR, f"{upload_id}-part-{part_number}")
        with open(part_path, "wb") as f:
            f.write(data)

    def _add_part_to_upload(self, upload_id: str, part_obj: dict[str, Any]) -> None:
        """Add part object to upload."""
        UPLOAD_PARTS[upload_id].append(part_obj)

    def complete_upload(
        self, upload_id: str, body: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Completes the Upload and creates a File object.

        Args:
            upload_id: The ID of the upload
            body: Request body containing part IDs in order

        Returns:
            Dictionary with completed upload object including nested file
        """
        try:
            if not body:
                body = {}

            upload_obj = self._validate_upload_exists(upload_id)
            self._validate_upload_status_for_completion(upload_obj)
            self._validate_upload_not_expired(upload_obj)

            part_ids = self._extract_and_validate_part_ids(body)
            all_parts = UPLOAD_PARTS[upload_id]
            ordered_parts = self._validate_and_order_parts(part_ids, all_parts)

            total_bytes = self._calculate_total_bytes(ordered_parts)
            self._validate_total_size(total_bytes, upload_obj["bytes"])

            file_obj = self._create_combined_file(
                upload_obj, ordered_parts, total_bytes
            )
            self._update_upload_status(upload_obj, file_obj)
            self._cleanup_part_files(upload_id, all_parts)

            return upload_obj

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to complete upload: {str(e)}"
            ) from e

    def _validate_upload_status_for_completion(
        self, upload_obj: dict[str, Any]
    ) -> None:
        """Validate upload status is valid for completion."""
        if upload_obj["status"] != "created":
            raise HTTPException(
                status_code=400,
                detail=f"Cannot complete upload with status: {upload_obj['status']}",
            )

    def _extract_and_validate_part_ids(self, body: dict[str, Any]) -> list[str]:
        """Extract and validate part IDs from request body."""
        part_ids = body.get("part_ids", [])
        if not part_ids:
            raise HTTPException(status_code=400, detail="'part_ids' is required")
        return part_ids

    def _validate_and_order_parts(
        self, part_ids: list[str], all_parts: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Validate part IDs exist and return ordered parts."""
        existing_part_ids = {part["id"] for part in all_parts}
        for part_id in part_ids:
            if part_id not in existing_part_ids:
                raise HTTPException(
                    status_code=400, detail=f"Part ID {part_id} not found in upload"
                )

        ordered_parts = []
        for part_id in part_ids:
            part = next(p for p in all_parts if p["id"] == part_id)
            ordered_parts.append(part)

        return ordered_parts

    def _calculate_total_bytes(self, ordered_parts: list[dict[str, Any]]) -> int:
        """Calculate total bytes from ordered parts."""
        return sum(part["bytes"] for part in ordered_parts)

    def _validate_total_size(self, total_bytes: int, expected_bytes: int) -> None:
        """Validate total size matches expected size."""
        if total_bytes != expected_bytes:
            raise HTTPException(
                status_code=400,
                detail=f"Total bytes ({total_bytes}) does not match expected bytes ({expected_bytes})",
            )

    def _create_combined_file(
        self,
        upload_obj: dict[str, Any],
        ordered_parts: list[dict[str, Any]],
        total_bytes: int,
    ) -> dict[str, Any]:
        """Create combined file from parts."""
        file_id = f"file-{uuid.uuid4().hex[:8]}"
        file_path = os.path.join(DATA_DIR, f"{file_id}-{upload_obj['filename']}")

        self._combine_part_files(upload_obj["id"], ordered_parts, file_path)
        return self._create_file_object(file_id, total_bytes, upload_obj)

    def _combine_part_files(
        self, upload_id: str, ordered_parts: list[dict[str, Any]], file_path: str
    ) -> None:
        """Combine part files into a single file."""
        with open(file_path, "wb") as output_file:
            for part in ordered_parts:
                part_path = os.path.join(
                    DATA_DIR, f"{upload_id}-part-{part['part_number']}"
                )
                with open(part_path, "rb") as part_file:
                    output_file.write(part_file.read())

    def _create_file_object(
        self, file_id: str, total_bytes: int, upload_obj: dict[str, Any]
    ) -> dict[str, Any]:
        """Create file object."""
        from backend.services.files_service import FILES_METADATA

        file_obj = {
            "id": file_id,
            "object": "file",
            "bytes": total_bytes,
            "created_at": int(time.time()),
            "filename": upload_obj["filename"],
            "purpose": upload_obj["purpose"],
            "status": "uploaded",
            "status_details": None,
        }
        FILES_METADATA[file_id] = file_obj
        return file_obj

    def _update_upload_status(
        self, upload_obj: dict[str, Any], file_obj: dict[str, Any]
    ) -> None:
        """Update upload status and add file reference."""
        upload_obj["status"] = "completed"
        upload_obj["file"] = file_obj

    def _cleanup_part_files(
        self, upload_id: str, all_parts: list[dict[str, Any]]
    ) -> None:
        """Clean up part files after combining."""
        for part in all_parts:
            part_path = os.path.join(
                DATA_DIR, f"{upload_id}-part-{part['part_number']}"
            )
            try:
                os.remove(part_path)
            except FileNotFoundError:
                pass

    def cancel_upload(self, upload_id: str) -> dict[str, Any]:
        """
        Cancels the Upload.

        Args:
            upload_id: The ID of the upload

        Returns:
            Dictionary with cancelled upload object
        """
        try:
            # Check if upload exists
            upload_obj = UPLOADS_METADATA.get(upload_id)
            if not upload_obj:
                raise HTTPException(status_code=404, detail="Upload not found")

            # Check if upload can be cancelled
            if upload_obj["status"] not in ["created", "processing"]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Cannot cancel upload with status: {upload_obj['status']}",
                )

            # Update upload status
            upload_obj["status"] = "cancelled"

            # Clean up part files
            all_parts = UPLOAD_PARTS.get(upload_id, [])
            for part in all_parts:
                part_path = os.path.join(
                    DATA_DIR, f"{upload_id}-part-{part['part_number']}"
                )
                try:
                    os.remove(part_path)
                except FileNotFoundError:
                    pass

            return upload_obj

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to cancel upload: {str(e)}"
            ) from e
