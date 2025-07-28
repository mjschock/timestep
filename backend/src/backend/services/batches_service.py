# mypy: ignore-errors
import time
import uuid
from enum import Enum
from typing import Any

from fastapi import HTTPException

from backend.services.chat_service import ChatService


class BatchStatus(str, Enum):
    VALIDATING = "validating"
    VALIDATION_FAILED = "validation_failed"
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    FINALIZING = "finalizing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"


class BatchesService:
    # Class-level storage for batches to persist across instances
    _batches: dict[str, dict[str, Any]] = {}
    _batch_results: dict[str, list[dict[str, Any]]] = {}

    def __init__(self) -> None:
        pass

    def create_batch(self, body: dict[str, Any]):
        """Creates and executes a batch from an uploaded file of requests"""
        try:
            # Extract required parameters
            input_file_id = body.get("input_file_id")
            endpoint = body.get("endpoint")
            completion_window = body.get("completion_window", "24h")

            # Optional parameters
            metadata = body.get("metadata", {})

            # Validate required parameters
            if not input_file_id:
                raise HTTPException(status_code=400, detail="input_file_id is required")
            if not endpoint:
                raise HTTPException(status_code=400, detail="endpoint is required")

            # Validate endpoint
            if endpoint not in ["/v1/chat/completions"]:
                raise HTTPException(
                    status_code=400, detail="endpoint must be /v1/chat/completions"
                )

            # Validate completion_window
            if completion_window not in ["24h"]:
                raise HTTPException(
                    status_code=400, detail="completion_window must be 24h"
                )

            # Generate batch ID
            batch_id = f"batch_{uuid.uuid4().hex[:8]}"

            # Create batch record
            batch = {
                "id": batch_id,
                "object": "batch",
                "endpoint": endpoint,
                "errors": None,
                "input_file_id": input_file_id,
                "completion_window": completion_window,
                "status": BatchStatus.VALIDATING,
                "created_at": int(time.time()),
                "in_progress_at": None,
                "expires_at": int(time.time()) + (24 * 60 * 60),  # 24 hours from now
                "finalizing_at": None,
                "completed_at": None,
                "request_counts": {"total": 0, "completed": 0, "failed": 0},
                "metadata": metadata,
            }

            # Store the batch
            self._batches[batch_id] = batch
            self._batch_results[batch_id] = []

            # Simulate validation process
            # In a real implementation, this would validate the input file
            # For now, we'll simulate a successful validation
            batch["status"] = BatchStatus.PENDING

            return batch

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to create batch: {str(e)}"
            ) from e

    def list_batches(self, after: str | None = None, limit: str | None = None):
        """List your organization's batches."""
        try:
            # Get all batches
            batches = list(self._batches.values())

            # Apply after filter
            if after:
                try:
                    after_time = int(after)
                    batches = [
                        b for b in batches if b.get("created_at", 0) > after_time
                    ]
                except ValueError:
                    pass

            # Sort by creation time (newest first)
            batches.sort(key=lambda x: x.get("created_at", 0), reverse=True)

            # Apply limit
            if limit:
                try:
                    limit_int = int(limit)
                    batches = batches[:limit_int]
                except ValueError:
                    pass

            return {
                "object": "list",
                "data": batches,
                "first_id": batches[0]["id"] if batches else None,
                "last_id": batches[-1]["id"] if batches else None,
                "has_more": False,
            }

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to list batches: {str(e)}"
            ) from e

    def retrieve_batch(self, batch_id: str):
        """Retrieves a batch."""
        try:
            if batch_id not in self._batches:
                raise HTTPException(status_code=404, detail="Batch not found")

            return self._batches[batch_id]

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to retrieve batch: {str(e)}"
            ) from e

    def cancel_batch(self, batch_id: str):
        """Cancels an in-progress batch."""
        try:
            if batch_id not in self._batches:
                raise HTTPException(status_code=404, detail="Batch not found")

            batch = self._batches[batch_id]

            # Check if batch can be cancelled
            if batch["status"] not in [BatchStatus.PENDING, BatchStatus.IN_PROGRESS]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Cannot cancel batch in status: {batch['status']}",
                )

            # Update batch status
            batch["status"] = BatchStatus.CANCELLING

            # Simulate cancellation process
            # In a real implementation, this would stop the batch processing
            batch["status"] = BatchStatus.CANCELLED

            return batch

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to cancel batch: {str(e)}"
            ) from e

    async def process_batch(self, batch_id: str, input_data: list[dict[str, Any]]):
        """Process a batch of requests (internal method)"""
        try:
            if batch_id not in self._batches:
                raise HTTPException(status_code=404, detail="Batch not found")

            batch = self._batches[batch_id]

            # Update status to in progress
            batch["status"] = BatchStatus.IN_PROGRESS
            batch["in_progress_at"] = int(time.time())
            batch["request_counts"]["total"] = len(input_data)

            results = []
            chat_service = ChatService()

            # Process each request in the batch
            for i, request_data in enumerate(input_data):
                try:
                    # Process the request based on the endpoint
                    if batch["endpoint"] == "/v1/chat/completions":
                        result = await chat_service.create_chat_completion(request_data)
                        results.append(
                            {
                                "id": f"batch_{batch_id}_{i}",
                                "custom_id": request_data.get("custom_id"),
                                "response": result,
                                "error": None,
                            }
                        )
                        batch["request_counts"]["completed"] += 1
                    else:
                        # Unsupported endpoint
                        results.append(
                            {
                                "id": f"batch_{batch_id}_{i}",
                                "custom_id": request_data.get("custom_id"),
                                "response": None,
                                "error": {
                                    "code": "unsupported_endpoint",
                                    "message": f"Endpoint {batch['endpoint']} is not supported",
                                },
                            }
                        )
                        batch["request_counts"]["failed"] += 1

                except Exception as e:
                    # Handle individual request errors
                    results.append(
                        {
                            "id": f"batch_{batch_id}_{i}",
                            "custom_id": request_data.get("custom_id"),
                            "response": None,
                            "error": {"code": "request_failed", "message": str(e)},
                        }
                    )
                    batch["request_counts"]["failed"] += 1

            # Store results
            self._batch_results[batch_id] = results

            # Update batch status
            if batch["request_counts"]["failed"] == batch["request_counts"]["total"]:
                batch["status"] = BatchStatus.FAILED
            else:
                batch["status"] = BatchStatus.FINALIZING
                batch["finalizing_at"] = int(time.time())
                batch["status"] = BatchStatus.COMPLETED
                batch["completed_at"] = int(time.time())

            return results

        except HTTPException:
            raise
        except Exception as e:
            # Update batch status to failed
            if batch_id in self._batches:
                self._batches[batch_id]["status"] = BatchStatus.FAILED
            raise HTTPException(
                status_code=500, detail=f"Failed to process batch: {str(e)}"
            ) from e

    def get_batch_results(self, batch_id: str):
        """Get results for a completed batch (internal method)"""
        try:
            if batch_id not in self._batch_results:
                raise HTTPException(status_code=404, detail="Batch results not found")

            return self._batch_results[batch_id]

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get batch results: {str(e)}"
            ) from e
