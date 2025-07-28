# mypy: ignore-errors
from fastapi import BackgroundTasks
from openai.types.fine_tuning.fine_tuning_job import FineTuningJob

from backend.logging_config import logger
from backend.services.models_service import get_models_service
from backend.utils.fine_tuning_utils import (
    METHOD_TYPE_DPO,
    METHOD_TYPE_SUPERVISED,
    fine_tuning_db,
)
from backend.utils.fine_tuning_utils import (
    cancel_job as cancel_ft_job_utils,
)
from backend.utils.fine_tuning_utils import (
    create_fine_tuning_job as create_ft_job_utils,
)
from backend.utils.fine_tuning_utils import (
    run_fine_tuning_job as run_ft_job_utils,
)

# Use the global fine_tuning_db from fine_tuning_utils
# FINE_TUNING_JOBS and RUNNING_JOBS are now handled by fine_tuning_db


class FineTuningService:
    def __init__(self) -> None:
        # Use the unified fine tuning database
        self.db = fine_tuning_db

    async def create_fine_tuning_job(self, request, background_tasks: BackgroundTasks):
        """Create a fine-tuning job from a request object (API endpoint)"""
        # Parse the request body
        body = await request.json()

        return self.create_fine_tuning_job_from_params(
            model=body.get("model"),
            training_file=body.get("training_file"),
            validation_file=body.get("validation_file"),
            hyperparameters=body.get("hyperparameters"),
            suffix=body.get("suffix"),
            integrations=body.get("integrations"),
            seed=body.get("seed"),
            method=body.get("method"),
            background_tasks=background_tasks,
        )

    def create_fine_tuning_job_from_params(
        self,
        model,
        training_file,
        validation_file=None,
        hyperparameters=None,
        suffix=None,
        integrations=None,
        seed=None,
        method=None,
        background_tasks=None,
    ):
        """Create a new fine-tuning job"""
        # Determine method type
        method_type = METHOD_TYPE_SUPERVISED  # Default
        if method and isinstance(method, dict):
            method_type = method.get("type", METHOD_TYPE_SUPERVISED)

        # Create the job using fine_tuning_utils
        # Strip 'openai/' prefix if present to match the model ID format expected by fine_tuning_utils
        normalized_model = (
            model.replace("openai/", "") if model.startswith("openai/") else model
        )
        job_id = create_ft_job_utils(
            method_type=method_type,
            training_file_id=training_file,
            model=normalized_model,
        )

        # Get the created job from the database
        job = self.db.get_job(job_id)
        if not job:
            raise RuntimeError(f"Failed to create job {job_id}")

        # Update with additional parameters if provided
        if validation_file:
            job.validation_file = validation_file
        if suffix:
            job.suffix = suffix
        if integrations:
            job.integrations = integrations
        if seed:
            job.seed = seed

        # Update the job in the database
        self.db.update_job(job_id, job)

        # Add background task to run the fine-tuning
        if background_tasks:
            logger.info(f"🔄 Adding background task for job {job_id}")
            background_tasks.add_task(self._run_fine_tuning_background, job_id)
        else:
            # Fallback for synchronous execution (testing)
            logger.info(f"🔄 Running fine-tuning synchronously for job {job_id}")
            self._run_fine_tuning_background(job_id)

        return self._convert_job_to_dict(job)

    def _run_fine_tuning_background(self, job_id: str) -> None:
        """Run fine-tuning job in background using fine_tuning_utils"""
        try:
            logger.info(f"🚀 Starting background fine-tuning for job {job_id}")

            # Check job status before running
            job = self.db.get_job(job_id)
            if job:
                logger.info(
                    f"📊 Job {job_id} current status before training: {job.status}"
                )
            else:
                logger.error(f"❌ Job {job_id} not found in database before training")
                return

            # Use the unified fine tuning runner
            logger.info(f"🔄 Calling run_ft_job_utils for job {job_id}")
            completed_job = run_ft_job_utils(job_id)

            logger.info(
                f"✅ Fine-tuning job {job_id} completed with status: {completed_job.status}"
            )

        except Exception as e:
            logger.error(f"❌ Fine-tuning job {job_id} failed: {str(e)}")
            import traceback

            logger.error(f"📋 Full traceback: {traceback.format_exc()}")
            # The error is already handled by run_ft_job_utils

    def _convert_job_to_dict(self, job: FineTuningJob) -> dict:
        """Convert FineTuningJob object to dictionary for API compatibility."""
        # Extract method details
        method_dict = {"type": "supervised"}
        if job.method:
            method_dict = {
                "type": job.method.type,
            }
            if job.method.type == METHOD_TYPE_SUPERVISED and job.method.supervised:
                method_dict["supervised"] = {
                    "hyperparameters": job.method.supervised.hyperparameters.model_dump()
                    if job.method.supervised.hyperparameters
                    else {}
                }
            elif job.method.type == METHOD_TYPE_DPO and job.method.dpo:
                method_dict["dpo"] = {
                    "hyperparameters": job.method.dpo.hyperparameters.model_dump()
                    if job.method.dpo.hyperparameters
                    else {}
                }

        # Create fine-tuned model name if completed successfully
        fine_tuned_model = None
        if job.status == "succeeded":
            base_model_short = (
                job.model.split("/")[-1] if "/" in job.model else job.model
            )
            suffix = getattr(job, "suffix", None) or "custom"
            fine_tuned_model = f"ft:{base_model_short}:{suffix}:{job.id[:8]}"

        return {
            "id": job.id,
            "object": job.object,
            "model": job.model,
            "created_at": job.created_at,
            "finished_at": getattr(job, "finished_at", None),
            "fine_tuned_model": fine_tuned_model,
            "organization_id": job.organization_id,
            "result_files": job.result_files or [],
            "status": job.status,
            "validation_file": job.validation_file,
            "training_file": job.training_file,
            "hyperparameters": job.hyperparameters.model_dump()
            if job.hyperparameters
            else {},
            "trained_tokens": getattr(job, "trained_tokens", None),
            "integrations": getattr(job, "integrations", []),
            "seed": job.seed,
            "estimated_finish": getattr(job, "estimated_finish", None),
            "metadata": job.metadata,
            "error": job.error.model_dump()
            if job.error and hasattr(job.error, "model_dump")
            else job.error,
            "method": method_dict,
        }

    def list_fine_tuning_jobs(self, limit=20, after=None):
        """List fine-tuning jobs"""
        # Ensure limit is an integer
        if isinstance(limit, str):
            limit = int(limit)

        # Get all jobs from the database
        all_jobs = self.db.list_jobs()
        jobs = [self._convert_job_to_dict(job) for job in all_jobs.values()]
        jobs.sort(key=lambda x: x["created_at"], reverse=True)

        if after:
            # Find the job with the given ID and return jobs after it
            after_index = None
            for i, job in enumerate(jobs):
                if job["id"] == after:
                    after_index = i + 1
                    break
            if after_index:
                jobs = jobs[after_index:]

        jobs = jobs[:limit]

        return {
            "object": "list",
            "data": jobs,
            "has_more": False,  # Simplified for this example
        }

    def retrieve_fine_tuning_job(self, job_id):
        """Retrieve a specific fine-tuning job"""
        job = self.db.get_job(job_id)
        if not job:
            return None

        job_dict = self._convert_job_to_dict(job)
        print(
            f"DEBUG: Retrieving job {job_id}: result_files = {job_dict.get('result_files', [])}"
        )
        return job_dict

    def cancel_fine_tuning_job(self, job_id):
        """Cancel a fine-tuning job"""
        try:
            cancelled_job = cancel_ft_job_utils(job_id)
            return self._convert_job_to_dict(cancelled_job)
        except ValueError:
            return None

    def list_fine_tuning_events(self, job_id, limit=20, after=None):
        """List events for a fine-tuning job"""
        # Ensure limit is an integer
        if isinstance(limit, str):
            limit = int(limit)

        job = self.db.get_job(job_id)
        if not job:
            return None

        # Create events from job status changes
        events = [
            {"timestamp": job.created_at, "message": "Fine-tuning job created"},
        ]

        if job.status == "succeeded":
            events.append(
                {
                    "timestamp": job.finished_at or job.created_at,
                    "message": "Training completed successfully",
                }
            )
        elif job.status == "failed":
            error_msg = (
                job.error.get("message", "Unknown error")
                if job.error
                else "Unknown error"
            )
            events.append(
                {
                    "timestamp": job.finished_at or job.created_at,
                    "message": f"Error: {error_msg}",
                }
            )
        elif job.status == "cancelled":
            events.append(
                {
                    "timestamp": job.finished_at or job.created_at,
                    "message": "Fine-tuning job cancelled",
                }
            )

        events.sort(key=lambda x: x["timestamp"], reverse=True)

        if after:
            # Find the event with the given timestamp and return events after it
            after_index = None
            for i, event in enumerate(events):
                if event["timestamp"] == after:
                    after_index = i + 1
                    break
            if after_index:
                events = events[after_index:]

        events = events[:limit]

        return {
            "object": "list",
            "data": events,
            "has_more": False,  # Simplified for this example
        }

    def get_peft_adapter_path(self, fine_tuned_model_name):
        """Get the path to PEFT adapter for a fine-tuned model"""
        return get_models_service().get_peft_adapter_path(fine_tuned_model_name)

    # Additional methods needed by the API
    def run_grader(self):
        """Run a grader (not implemented)"""
        return {"message": "Grader functionality not implemented"}

    def validate_grader(self):
        """Validate a grader (not implemented)"""
        return {"message": "Grader validation not implemented"}

    def list_fine_tuning_checkpoint_permissions(self):
        """List fine-tuning checkpoint permissions (not implemented)"""
        return {"message": "Checkpoint permissions not implemented"}

    def create_fine_tuning_checkpoint_permission(self):
        """Create fine-tuning checkpoint permission (not implemented)"""
        return {"message": "Checkpoint permission creation not implemented"}

    def delete_fine_tuning_checkpoint_permission(self):
        """Delete fine-tuning checkpoint permission (not implemented)"""
        return {"message": "Checkpoint permission deletion not implemented"}

    def list_paginated_fine_tuning_jobs(self, after=None, limit=None, metadata=None):
        """List paginated fine-tuning jobs"""
        return self.list_fine_tuning_jobs(limit=limit or 20, after=after)

    def list_fine_tuning_job_checkpoints(self, job_id, after=None, limit=None):
        """List checkpoints for a fine-tuning job (not implemented)"""
        return {
            "object": "list",
            "data": [],
            "has_more": False,
        }

    def pause_fine_tuning_job(self):
        """Pause a fine-tuning job (not implemented)"""
        return {"message": "Job pausing not implemented"}

    def resume_fine_tuning_job(self):
        """Resume a fine-tuning job (not implemented)"""
        return {"message": "Job resuming not implemented"}
