import json
import os
import time
import uuid
from typing import Any

from fastapi import HTTPException, Request, UploadFile
from openai.types.file_object import FileObject

from backend._shared.dao.file_dao import FileDAO
from backend._shared.logging_config import logger

DATA_DIR = os.path.join("data", "files")
os.makedirs(DATA_DIR, exist_ok=True)


def validate_openai_messages_format(file_content: bytes) -> None:
    """Validate that every row in the file content follows the OpenAI messages format exactly.

    Args:
        file_content: The file content as bytes

    Raises:
        ValueError: If any row doesn't follow the OpenAI messages format
    """
    content_text = file_content.decode("utf-8")
    lines = content_text.strip().split("\n")

    for line_num, line in enumerate(lines, 1):
        if not line.strip():  # Skip empty lines
            continue

        try:
            # Parse the JSON line
            example = json.loads(line.strip())

            # Check that it has a 'messages' field
            if "messages" not in example:
                raise ValueError(f"Line {line_num}: Missing 'messages' field")

            messages = example["messages"]

            # Check that messages is a list
            if not isinstance(messages, list):
                raise ValueError(
                    f"Line {line_num}: 'messages' must be a list, got {type(messages)}"
                )

            # Check that messages is not empty
            if len(messages) == 0:
                raise ValueError(f"Line {line_num}: 'messages' list cannot be empty")

            # Validate each message
            for msg_idx, message in enumerate(messages):
                if not isinstance(message, dict):
                    raise ValueError(
                        f"Line {line_num}, message {msg_idx}: Message must be a dict, got {type(message)}"
                    )

                # Check required 'role' field
                if "role" not in message:
                    raise ValueError(
                        f"Line {line_num}, message {msg_idx}: Missing 'role' field"
                    )

                role = message["role"]
                if role not in ["system", "user", "assistant"]:
                    raise ValueError(
                        f"Line {line_num}, message {msg_idx}: Invalid role '{role}'. Must be 'system', 'user', or 'assistant'"
                    )

                # Check content or tool_calls
                has_content = "content" in message and message["content"] is not None
                has_tool_calls = (
                    "tool_calls" in message and message["tool_calls"] is not None
                )

                if not has_content and not has_tool_calls:
                    raise ValueError(
                        f"Line {line_num}, message {msg_idx}: Message must have either 'content' or 'tool_calls'"
                    )

                # Only assistant messages can have tool_calls
                if has_tool_calls and role != "assistant":
                    raise ValueError(
                        f"Line {line_num}, message {msg_idx}: Only assistant messages can have 'tool_calls'"
                    )

                # Validate content if present
                if has_content:
                    content = message["content"]
                    if content is None:
                        raise ValueError(
                            f"Line {line_num}, message {msg_idx}: 'content' cannot be None"
                        )

                    # Content can be string or list (for multimodal)
                    if not isinstance(content, str | list):
                        raise ValueError(
                            f"Line {line_num}, message {msg_idx}: 'content' must be string or list, got {type(content)}"
                        )

                    # If content is a list, validate each item
                    if isinstance(content, list):
                        for content_idx, content_item in enumerate(content):
                            if not isinstance(content_item, dict):
                                raise ValueError(
                                    f"Line {line_num}, message {msg_idx}, content item {content_idx}: Content item must be a dict, got {type(content_item)}"
                                )

                            if "type" not in content_item:
                                raise ValueError(
                                    f"Line {line_num}, message {msg_idx}, content item {content_idx}: Content item missing 'type' field"
                                )

                            content_type = content_item["type"]
                            if content_type not in [
                                "text",
                                "image_url",
                                "video_url",
                            ]:
                                raise ValueError(
                                    f"Line {line_num}, message {msg_idx}, content item {content_idx}: Invalid content type '{content_type}'. Must be 'text', 'image_url', or 'video_url'"
                                )

                            # Validate based on content type
                            if content_type == "text":
                                if "text" not in content_item:
                                    raise ValueError(
                                        f"Line {line_num}, message {msg_idx}, content item {content_idx}: Text content missing 'text' field"
                                    )
                            elif content_type in ["image_url", "video_url"]:
                                if (
                                    "image_url" not in content_item
                                    and "video_url" not in content_item
                                ):
                                    raise ValueError(
                                        f"Line {line_num}, message {msg_idx}, content item {content_idx}: {content_type} content missing '{content_type}' field"
                                    )

                                url_obj = content_item.get(
                                    "image_url"
                                ) or content_item.get("video_url")
                                if (
                                    not isinstance(url_obj, dict)
                                    or "url" not in url_obj
                                ):
                                    raise ValueError(
                                        f"Line {line_num}, message {msg_idx}, content item {content_idx}: {content_type} must have 'url' field in object"
                                    )

                # Validate tool_calls if present
                if has_tool_calls:
                    tool_calls = message["tool_calls"]
                    if not isinstance(tool_calls, list):
                        raise ValueError(
                            f"Line {line_num}, message {msg_idx}: 'tool_calls' must be a list, got {type(tool_calls)}"
                        )

                    for tool_idx, tool_call in enumerate(tool_calls):
                        if not isinstance(tool_call, dict):
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Tool call must be a dict, got {type(tool_call)}"
                            )

                        if "id" not in tool_call:
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Tool call missing 'id' field"
                            )

                        if "type" not in tool_call or tool_call["type"] != "function":
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Tool call must have type 'function'"
                            )

                        if "function" not in tool_call:
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Tool call missing 'function' field"
                            )

                        function = tool_call["function"]
                        if not isinstance(function, dict):
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Function must be a dict, got {type(function)}"
                            )

                        if "name" not in function:
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Function missing 'name' field"
                            )

                        if "arguments" not in function:
                            raise ValueError(
                                f"Line {line_num}, message {msg_idx}, tool call {tool_idx}: Function missing 'arguments' field"
                            )

        except json.JSONDecodeError as e:
            raise ValueError(f"Line {line_num}: Invalid JSON - {e}") from e
        except Exception as e:
            raise ValueError(f"Line {line_num}: {e}") from e

    logger.info(f"✅ Validated {len(lines)} examples successfully")


class FilesService:
    def __init__(self):
        self.dao = FileDAO()

    def list_files(
        self,
        purpose: str | None = None,
        limit: str | None = None,
        order: str | None = None,
        after: str | None = None,
    ) -> dict[str, Any]:
        limit_int = int(limit) if limit else None
        order_str = order or "asc"

        files = self.dao.list_all(
            purpose=purpose, limit=limit_int, order=order_str, after=after
        )

        files_data = [file_obj.model_dump() for file_obj in files]
        return {"object": "list", "data": files_data}

    async def create_file_with_upload(
        self, upload: UploadFile, purpose: str
    ) -> dict[str, Any]:
        """Create a file from an UploadFile object."""
        logger.info(f"Creating file: {upload.filename}, purpose: {purpose}")
        file_id = f"file-{uuid.uuid4().hex[:8]}"
        filename = upload.filename or "unknown"
        file_path = os.path.join(DATA_DIR, file_id + "-" + filename)

        # Read file content
        content = await upload.read()

        # Validate OpenAI messages format for fine-tune and vision purposes
        if purpose in ["fine-tune", "vision"]:
            logger.info(f"Validating OpenAI messages format for {purpose} purpose")
            try:
                validate_openai_messages_format(content)
                logger.info(f"✅ File validation passed for {purpose} purpose")
            except ValueError as e:
                logger.error(f"❌ File validation failed for {purpose} purpose: {e}")
                raise HTTPException(
                    status_code=400, detail=f"File validation failed: {str(e)}"
                ) from e

        # For evals and user_data purposes, perform basic JSONL validation
        elif purpose in ["evals", "user_data"]:
            logger.info(f"Validating JSONL format for {purpose} purpose")
            try:
                # Basic JSONL validation - each line should be valid JSON
                content_text = content.decode("utf-8")
                lines = content_text.strip().split("\n")
                import json

                for line_num, line in enumerate(lines, 1):
                    if line.strip():  # Skip empty lines
                        try:
                            json.loads(line.strip())
                        except json.JSONDecodeError as e:
                            raise ValueError(
                                f"Line {line_num}: Invalid JSON - {e}"
                            ) from e
                logger.info(f"✅ File validation passed for {purpose} purpose")
            except ValueError as e:
                logger.error(f"❌ File validation failed for {purpose} purpose: {e}")
                raise HTTPException(
                    status_code=400, detail=f"File validation failed: {str(e)}"
                ) from e

        # Save file
        with open(file_path, "wb") as f:
            f.write(content)
        logger.info(f"File uploaded: {filename} as {file_id}")

        # Create file record in database
        file_obj = FileObject(
            id=file_id,
            object="file",
            bytes=len(content),
            created_at=int(time.time()),
            filename=filename,
            purpose=purpose,
            status="uploaded",
            status_details=None,
        )

        created_file = self.dao.create(file_obj)
        return created_file.model_dump()

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

        # Read file content
        content = await upload.read()

        # Validate OpenAI messages format for fine-tune and vision purposes
        if purpose in ["fine-tune", "vision"]:
            logger.info(f"Validating OpenAI messages format for {purpose} purpose")
            try:
                validate_openai_messages_format(content)
                logger.info(f"✅ File validation passed for {purpose} purpose")
            except ValueError as e:
                logger.error(f"❌ File validation failed for {purpose} purpose: {e}")
                raise HTTPException(
                    status_code=400, detail=f"File validation failed: {str(e)}"
                ) from e

        # For evals and user_data purposes, perform basic JSONL validation
        elif purpose in ["evals", "user_data"]:
            logger.info(f"Validating JSONL format for {purpose} purpose")
            try:
                # Basic JSONL validation - each line should be valid JSON
                content_text = content.decode("utf-8")
                lines = content_text.strip().split("\n")
                import json

                for line_num, line in enumerate(lines, 1):
                    if line.strip():  # Skip empty lines
                        try:
                            json.loads(line.strip())
                        except json.JSONDecodeError as e:
                            raise ValueError(
                                f"Line {line_num}: Invalid JSON - {e}"
                            ) from e
                logger.info(f"✅ File validation passed for {purpose} purpose")
            except ValueError as e:
                logger.error(f"❌ File validation failed for {purpose} purpose: {e}")
                raise HTTPException(
                    status_code=400, detail=f"File validation failed: {str(e)}"
                ) from e

        # Save file
        with open(file_path, "wb") as f:
            f.write(content)
        logger.info(f"File uploaded: {filename} as {file_id}")
        # Create file record in database
        file_obj = FileObject(
            id=file_id,
            object="file",
            bytes=len(content),
            created_at=int(time.time()),
            filename=filename,
            purpose=purpose,
            status="uploaded",
            status_details=None,
        )

        created_file = self.dao.create(file_obj)
        return created_file.model_dump()

    def delete_file(self, file_id: str) -> dict[str, Any]:
        # Get file info before deletion
        file_obj = self.dao.get_by_id(file_id)
        if not file_obj:
            logger.error(f"File deletion failed: {file_id} not found")
            raise HTTPException(status_code=404, detail="File not found")

        # Delete file from disk
        file_path = os.path.join(DATA_DIR, file_id + "-" + file_obj.filename)
        try:
            os.remove(file_path)
            logger.info(f"File deleted: {file_id}")
        except FileNotFoundError:
            logger.warning(f"File not found on disk during deletion: {file_id}")

        # Delete from database
        if self.dao.delete(file_id):
            return {"id": file_id, "object": "file", "deleted": True}
        else:
            raise HTTPException(
                status_code=500, detail="Failed to delete file from database"
            )

    def retrieve_file(self, file_id: str) -> dict[str, Any]:
        file_obj = self.dao.get_by_id(file_id)
        if not file_obj:
            raise HTTPException(status_code=404, detail="File not found")
        return file_obj.model_dump()

    def download_file(self, file_id: str) -> str:
        file_obj = self.dao.get_by_id(file_id)
        if not file_obj:
            raise HTTPException(status_code=404, detail="File not found")

        file_path = os.path.join(DATA_DIR, file_id + "-" + file_obj.filename)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found on disk")
        return file_path  # The API layer should stream this file

    async def get_file_content(self, file_id: str) -> bytes:
        """Get the content of a file as bytes."""
        file_path = self.download_file(file_id)
        with open(file_path, "rb") as f:
            return f.read()


def get_files_metadata_dict() -> dict[str, dict[str, Any]]:
    """Get all files as a dictionary for backward compatibility with FILES_METADATA."""
    files_service = FilesService()
    files_data = files_service.list_files()
    return {file["id"]: file for file in files_data["data"]}


# Backward compatibility: provide FILES_METADATA as a property
class FilesMetadataDict:
    """Backward compatibility wrapper for FILES_METADATA."""

    def get(self, key: str, default=None):
        files_service = FilesService()
        try:
            return files_service.retrieve_file(key)
        except HTTPException:
            return default

    def __getitem__(self, key: str):
        files_service = FilesService()
        return files_service.retrieve_file(key)

    def __setitem__(self, key: str, value: dict[str, Any]):
        # For setting, we assume it's a new file creation
        files_service = FilesService()
        file_obj = FileObject(**value)
        files_service.dao.create(file_obj)
        logger.info(
            f"📝 Created file {key} in database via FILES_METADATA compatibility"
        )

    def items(self):
        files_dict = get_files_metadata_dict()
        return files_dict.items()

    def __len__(self):
        files_dict = get_files_metadata_dict()
        return len(files_dict)


# Provide backward compatibility
FILES_METADATA = FilesMetadataDict()
