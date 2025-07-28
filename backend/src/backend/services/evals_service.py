import time
import uuid
from enum import Enum
from typing import Any

from fastapi import HTTPException


class EvalStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class EvalRunStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class EvalsService:
    # Class-level storage for evals to persist across instances
    _evals: dict[str, dict[str, Any]] = {}
    _eval_runs: dict[str, dict[str, Any]] = {}
    _eval_run_output_items: dict[str, list[dict[str, Any]]] = {}

    def __init__(self) -> None:
        pass

    def list_evals(
        self,
        after: str | None = None,
        limit: str | None = None,
        order: str | None = None,
        order_by: str | None = None,
    ) -> dict[str, Any]:
        """List evaluations for a project."""
        try:
            # Get all evals
            evals = list(self._evals.values())

            # Apply after filter
            if after:
                try:
                    after_time = int(after)
                    evals = [e for e in evals if e.get("created_at", 0) > after_time]
                except ValueError:
                    pass

            # Apply sorting
            if order_by:
                reverse = order == "desc" if order else False
                if order_by == "created_at":
                    evals.sort(key=lambda x: x.get("created_at", 0), reverse=reverse)
                elif order_by == "name":
                    evals.sort(key=lambda x: x.get("name", ""), reverse=reverse)

            # Default sort by creation time (newest first)
            if not order_by:
                evals.sort(key=lambda x: x.get("created_at", 0), reverse=True)

            # Apply limit
            if limit:
                try:
                    limit_int = int(limit)
                    evals = evals[:limit_int]
                except ValueError:
                    pass

            return {
                "object": "list",
                "data": evals,
                "first_id": evals[0]["id"] if evals else None,
                "last_id": evals[-1]["id"] if evals else None,
                "has_more": False,
            }

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to list evals: {str(e)}"
            ) from e

    def create_eval(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create the structure of an evaluation."""
        try:
            # Extract required parameters
            name = body.get("name")
            data_source_config = body.get("data_source_config")
            testing_criteria = body.get("testing_criteria")

            # Optional parameters
            description = body.get("description", "")
            metadata = body.get("metadata", {})
            dataset_id = body.get("dataset_id")
            dataset_slice = body.get("dataset_slice")
            grader_config = body.get("grader_config", {})
            model_config = body.get("model_config", {})

            # Validate required parameters
            if not name:
                raise HTTPException(status_code=400, detail="name is required")
            if not data_source_config:
                raise HTTPException(
                    status_code=400, detail="data_source_config is required"
                )
            if not testing_criteria:
                raise HTTPException(
                    status_code=400, detail="testing_criteria is required"
                )

            # Extract eval_type from testing_criteria
            eval_type = testing_criteria.get("type", "accuracy")

            # Validate eval_type
            valid_eval_types = ["accuracy", "exact_match", "f1", "custom"]
            if eval_type not in valid_eval_types:
                raise HTTPException(
                    status_code=400,
                    detail=f"eval_type must be one of: {valid_eval_types}",
                )

            # Generate eval ID
            eval_id = f"eval_{uuid.uuid4().hex[:8]}"

            # Create eval record
            eval_record = {
                "id": eval_id,
                "object": "eval",
                "name": name,
                "description": description,
                "data_source_config": data_source_config,
                "testing_criteria": testing_criteria,
                "eval_type": eval_type,
                "dataset_id": dataset_id,
                "dataset_slice": dataset_slice,
                "grader_config": grader_config,
                "model_config": model_config,
                "status": EvalStatus.PENDING,
                "created_at": int(time.time()),
                "updated_at": int(time.time()),
                "metadata": metadata,
            }

            # Store the eval
            self._evals[eval_id] = eval_record

            return eval_record

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to create eval: {str(e)}"
            ) from e

    def get_eval(self, eval_id: str) -> dict[str, Any]:
        """Get an evaluation by ID."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            return self._evals[eval_id]

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get eval: {str(e)}"
            ) from e

    def update_eval(self, eval_id: str, body: dict[str, Any]) -> dict[str, Any]:
        """Update certain properties of an evaluation."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            eval_record = self._evals[eval_id]

            # Update allowed fields
            allowed_fields = [
                "name",
                "description",
                "prompt_template",
                "grader_config",
                "model_config",
                "metadata",
            ]
            for field in allowed_fields:
                if field in body:
                    eval_record[field] = body[field]

            # Update timestamp
            eval_record["updated_at"] = int(time.time())

            return eval_record

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to update eval: {str(e)}"
            ) from e

    def delete_eval(self, eval_id: str) -> dict[str, Any]:
        """Delete an evaluation."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            # Check if eval has runs
            eval_runs = [
                run for run in self._eval_runs.values() if run.get("eval_id") == eval_id
            ]
            if eval_runs:
                raise HTTPException(
                    status_code=400, detail="Cannot delete eval with existing runs"
                )

            # Delete the eval
            del self._evals[eval_id]

            return {"deleted": True}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to delete eval: {str(e)}"
            ) from e

    def get_eval_runs(
        self,
        eval_id: str,
        after: str | None = None,
        limit: str | None = None,
        order: str | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        """Get a list of runs for an evaluation."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            # Get runs for this eval
            runs = [
                run for run in self._eval_runs.values() if run.get("eval_id") == eval_id
            ]

            # Apply status filter
            if status:
                runs = [run for run in runs if run.get("status") == status]

            # Apply after filter
            if after:
                try:
                    after_time = int(after)
                    runs = [r for r in runs if r.get("created_at", 0) > after_time]
                except ValueError:
                    pass

            # Apply sorting
            if order:
                reverse = order == "desc"
                runs.sort(key=lambda x: x.get("created_at", 0), reverse=reverse)
            else:
                # Default sort by creation time (newest first)
                runs.sort(key=lambda x: x.get("created_at", 0), reverse=True)

            # Apply limit
            if limit:
                try:
                    limit_int = int(limit)
                    runs = runs[:limit_int]
                except ValueError:
                    pass

            return {
                "object": "list",
                "data": runs,
                "first_id": runs[0]["id"] if runs else None,
                "last_id": runs[-1]["id"] if runs else None,
                "has_more": False,
            }

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get eval runs: {str(e)}"
            ) from e

    def create_eval_run(self, eval_id: str, body: dict[str, Any]) -> dict[str, Any]:
        """Kicks off a new run for a given evaluation."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            # Extract parameters
            model = body.get(
                "model", "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
            )  # Default model

            # Optional parameters
            metadata = body.get("metadata", {})
            dataset_slice = body.get("dataset_slice")
            model_config = body.get("model_config", {})

            # Generate run ID
            run_id = f"run_{uuid.uuid4().hex[:8]}"

            # Create run record
            run_record = {
                "id": run_id,
                "object": "eval_run",
                "eval_id": eval_id,
                "model": model,
                "dataset_slice": dataset_slice,
                "model_config": model_config,
                "status": EvalRunStatus.PENDING,
                "created_at": int(time.time()),
                "started_at": None,
                "completed_at": None,
                "metadata": metadata,
                "results": None,
                "error": None,
            }

            # Store the run
            self._eval_runs[run_id] = run_record
            self._eval_run_output_items[run_id] = []

            # Simulate starting the run
            run_record["status"] = EvalRunStatus.IN_PROGRESS
            run_record["started_at"] = int(time.time())

            return run_record

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to create eval run: {str(e)}"
            ) from e

    def get_eval_run(self, eval_id: str, run_id: str) -> dict[str, Any]:
        """Get an evaluation run by ID."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            if run_id not in self._eval_runs:
                raise HTTPException(status_code=404, detail="Eval run not found")

            run = self._eval_runs[run_id]
            if run.get("eval_id") != eval_id:
                raise HTTPException(
                    status_code=404, detail="Eval run not found for this eval"
                )

            return run

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get eval run: {str(e)}"
            ) from e

    def cancel_eval_run(self, eval_id: str, run_id: str) -> dict[str, Any]:
        """Cancel an ongoing evaluation run."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            if run_id not in self._eval_runs:
                raise HTTPException(status_code=404, detail="Eval run not found")

            run = self._eval_runs[run_id]
            if run.get("eval_id") != eval_id:
                raise HTTPException(
                    status_code=404, detail="Eval run not found for this eval"
                )

            # Check if run can be cancelled
            if run["status"] not in [EvalRunStatus.PENDING, EvalRunStatus.IN_PROGRESS]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Cannot cancel run in status: {run['status']}",
                )

            # Update run status
            run["status"] = EvalRunStatus.CANCELLED
            run["completed_at"] = int(time.time())

            return run

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to cancel eval run: {str(e)}"
            ) from e

    def delete_eval_run(self, eval_id: str, run_id: str) -> dict[str, Any]:
        """Delete an eval run."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            if run_id not in self._eval_runs:
                raise HTTPException(status_code=404, detail="Eval run not found")

            run = self._eval_runs[run_id]
            if run.get("eval_id") != eval_id:
                raise HTTPException(
                    status_code=404, detail="Eval run not found for this eval"
                )

            # Delete the run and its output items
            del self._eval_runs[run_id]
            if run_id in self._eval_run_output_items:
                del self._eval_run_output_items[run_id]

            return {"deleted": True}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to delete eval run: {str(e)}"
            ) from e

    def get_eval_run_output_items(
        self,
        eval_id: str,
        run_id: str,
        after: str | None = None,
        limit: str | None = None,
        status: str | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:
        """Get a list of output items for an evaluation run."""
        try:
            # Validate eval and run existence
            self._validate_eval_and_run(eval_id, run_id)

            # Get and filter output items
            output_items = self._get_filtered_output_items(
                run_id, status, after, order, limit
            )

            # Build response
            return self._build_output_items_response(output_items)

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get eval run output items: {str(e)}"
            ) from e

    def _validate_eval_and_run(self, eval_id: str, run_id: str) -> None:
        """Validate that eval and run exist and are related."""
        if eval_id not in self._evals:
            raise HTTPException(status_code=404, detail="Eval not found")

        if run_id not in self._eval_runs:
            raise HTTPException(status_code=404, detail="Eval run not found")

        run = self._eval_runs[run_id]
        if run.get("eval_id") != eval_id:
            raise HTTPException(
                status_code=404, detail="Eval run not found for this eval"
            )

    def _get_filtered_output_items(
        self,
        run_id: str,
        status: str | None,
        after: str | None,
        order: str | None,
        limit: str | None,
    ):
        """Get and filter output items for a run."""
        # Get output items for this run
        output_items = self._eval_run_output_items.get(run_id, [])

        # Apply status filter
        if status:
            output_items = [
                item for item in output_items if item.get("status") == status
            ]

        # Apply after filter
        if after:
            output_items = self._apply_after_filter(output_items, after)

        # Apply sorting
        output_items = self._apply_sorting(output_items, order)

        # Apply limit
        if limit:
            output_items = self._apply_limit(output_items, limit)

        return output_items

    def _apply_after_filter(self, output_items: list, after: str) -> list:
        """Apply after filter to output items."""
        try:
            after_time = int(after)
            return [
                item for item in output_items if item.get("created_at", 0) > after_time
            ]
        except ValueError:
            return output_items

    def _apply_sorting(self, output_items: list, order: str | None) -> list:
        """Apply sorting to output items."""
        if order:
            reverse = order == "desc"
            output_items.sort(key=lambda x: x.get("created_at", 0), reverse=reverse)
        else:
            # Default sort by creation time (newest first)
            output_items.sort(key=lambda x: x.get("created_at", 0), reverse=True)
        return output_items

    def _apply_limit(self, output_items: list, limit: str) -> list:
        """Apply limit to output items."""
        try:
            limit_int = int(limit)
            return output_items[:limit_int]
        except ValueError:
            return output_items

    def _build_output_items_response(self, output_items: list) -> dict[str, Any]:
        """Build the response for output items."""
        return {
            "object": "list",
            "data": output_items,
            "first_id": output_items[0]["id"] if output_items else None,
            "last_id": output_items[-1]["id"] if output_items else None,
            "has_more": False,
        }

    def get_eval_run_output_item(
        self, eval_id: str, run_id: str, output_item_id: str
    ) -> dict[str, Any]:
        """Get an evaluation run output item by ID."""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            if run_id not in self._eval_runs:
                raise HTTPException(status_code=404, detail="Eval run not found")

            run = self._eval_runs[run_id]
            if run.get("eval_id") != eval_id:
                raise HTTPException(
                    status_code=404, detail="Eval run not found for this eval"
                )

            # Get output items for this run
            output_items = self._eval_run_output_items.get(run_id, [])

            # Find the specific output item
            output_item = next(
                (item for item in output_items if item.get("id") == output_item_id),
                None,
            )
            if not output_item:
                raise HTTPException(status_code=404, detail="Output item not found")

            return output_item

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get eval run output item: {str(e)}"
            ) from e

    def process_eval_run(
        self, eval_id: str, run_id: str, test_data: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Process an eval run with test data (internal method)"""
        try:
            if eval_id not in self._evals:
                raise HTTPException(status_code=404, detail="Eval not found")

            if run_id not in self._eval_runs:
                raise HTTPException(status_code=404, detail="Eval run not found")

            self._evals[eval_id]
            run_record = self._eval_runs[run_id]

            if run_record.get("eval_id") != eval_id:
                raise HTTPException(
                    status_code=404, detail="Eval run not found for this eval"
                )

            # Update run status to in progress
            run_record["status"] = EvalRunStatus.IN_PROGRESS
            run_record["started_at"] = int(time.time())

            output_items = []

            # Process each test item
            for i, test_item in enumerate(test_data):
                try:
                    # Create output item
                    output_item = {
                        "id": f"output_{run_id}_{i}",
                        "object": "eval_run_output_item",
                        "eval_id": eval_id,
                        "run_id": run_id,
                        "input": test_item.get("input", {}),
                        "output": test_item.get("output", {}),
                        "expected_output": test_item.get("expected_output", {}),
                        "score": test_item.get("score", 0.0),
                        "status": "completed",
                        "created_at": int(time.time()),
                        "metadata": test_item.get("metadata", {}),
                    }

                    output_items.append(output_item)

                except Exception as e:
                    # Handle individual item errors
                    output_item = {
                        "id": f"output_{run_id}_{i}",
                        "object": "eval_run_output_item",
                        "eval_id": eval_id,
                        "run_id": run_id,
                        "input": test_item.get("input", {}),
                        "output": None,
                        "expected_output": test_item.get("expected_output", {}),
                        "score": None,
                        "status": "failed",
                        "created_at": int(time.time()),
                        "metadata": test_item.get("metadata", {}),
                        "error": str(e),
                    }
                    output_items.append(output_item)

            # Store output items
            self._eval_run_output_items[run_id] = output_items

            # Calculate overall results
            completed_items = [
                item for item in output_items if item["status"] == "completed"
            ]
            if completed_items:
                avg_score = sum(item["score"] for item in completed_items) / len(
                    completed_items
                )
                run_record["results"] = {
                    "average_score": avg_score,
                    "total_items": len(output_items),
                    "completed_items": len(completed_items),
                    "failed_items": len(output_items) - len(completed_items),
                }
                run_record["status"] = EvalRunStatus.COMPLETED
            else:
                run_record["status"] = EvalRunStatus.FAILED
                run_record["error"] = "No items completed successfully"

            run_record["completed_at"] = int(time.time())

            return output_items

        except HTTPException:
            raise
        except Exception as e:
            # Update run status to failed
            if run_id in self._eval_runs:
                self._eval_runs[run_id]["status"] = EvalRunStatus.FAILED
                self._eval_runs[run_id]["error"] = str(e)
            raise HTTPException(
                status_code=500, detail=f"Failed to process eval run: {str(e)}"
            ) from e
