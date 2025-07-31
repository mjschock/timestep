"""Fine-tuning worker for background job execution."""

import time
from typing import Any

from openai.types.fine_tuning.fine_tuning_job import FineTuningJob

from backend._shared.dao.fine_tuning_dao import FineTuningJobDAO
from backend._shared.logging_config import logger
from backend._shared.utils.fine_tuning_utils import (
    METHOD_TYPE_DPO,
    METHOD_TYPE_SUPERVISED,
    PEFT_METHOD_LORA,
    PEFT_METHOD_QLORA,
    UnifiedFineTuner,
    _create_training_metrics_file,
    validate_and_load_dataset,
)
from backend.services.models_service import get_models_service


class FineTuningWorker:
    """Worker class for executing fine-tuning jobs in the background."""

    def __init__(self):
        self.dao = FineTuningJobDAO()
        self.models_service = get_models_service()

    def execute_job(self, job_id: str, **kwargs) -> FineTuningJob:
        """Execute a fine-tuning job with comprehensive error handling and monitoring."""
        logger.info(f"🔧 Starting fine-tuning job execution for {job_id}")

        # Retrieve the job from the database
        fine_tuning_job = self.dao.get_by_id(job_id)
        if not fine_tuning_job:
            logger.error(f"❌ Job {job_id} not found in database")
            raise ValueError(f"Job {job_id} not found in database")

        logger.info(f"📊 Found job {job_id} with status: {fine_tuning_job.status}")

        # Validate job status
        if not self._validate_job_status(fine_tuning_job):
            return fine_tuning_job

        try:
            # Stage 1: Validate files
            train_dataset = self._validate_files(fine_tuning_job)

            # Stage 2: Run training
            training_results = self._run_training(
                fine_tuning_job, train_dataset, **kwargs
            )

            # Stage 3: Complete job
            return self._complete_job(fine_tuning_job, training_results)

        except Exception as e:
            logger.error(f"❌ Job {job_id} failed: {str(e)}")
            return self._fail_job(fine_tuning_job, e)

    def _validate_job_status(self, job: FineTuningJob) -> bool:
        """Validate that the job can be executed."""
        if job.status == "running":
            logger.error(f"❌ Job {job.id} is already running")
            raise ValueError("Resuming a fine-tuning job is not yet supported")
        elif job.status not in ["queued"]:
            logger.error(
                f"❌ Job {job.id} cannot be run in status '{job.status}' - expected 'queued'"
            )
            raise ValueError(f"Job {job.id} cannot be run in status '{job.status}'")
        return True

    def _validate_files(self, job: FineTuningJob):
        """Validate and load the training dataset."""
        # Update status to validating_files
        job.status = "validating_files"
        self.dao.update(job.id, job)
        logger.info(f"🔍 Job {job.id} status updated to 'validating_files'")

        # Validate dataset file and load it
        logger.info(f"📁 Starting dataset validation for job {job.id}")
        method_type = job.method.type if job.method else METHOD_TYPE_SUPERVISED
        logger.info(f"⚙️  Method type for job {job.id}: {method_type}")

        train_dataset = validate_and_load_dataset(job.training_file)
        logger.info(f"✅ Dataset validation completed for job {job.id}")
        return train_dataset

    def _run_training(
        self, job: FineTuningJob, train_dataset, **kwargs
    ) -> dict[str, Any]:
        """Execute the actual training process."""
        # Update status to running
        job.status = "running"
        self.dao.update(job.id, job)
        logger.info(f"🔄 Job {job.id} status updated to 'running'")

        # Set random seed if provided
        if job.seed is not None:
            import torch

            torch.manual_seed(job.seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed(job.seed)

        # Determine PEFT method based on method type
        method_type = job.method.type if job.method else METHOD_TYPE_SUPERVISED
        if method_type == METHOD_TYPE_SUPERVISED:
            peft_method = PEFT_METHOD_QLORA  # Default to QLoRA for supervised
        elif method_type == METHOD_TYPE_DPO:
            peft_method = PEFT_METHOD_LORA  # Default to LoRA for DPO
        else:
            peft_method = PEFT_METHOD_QLORA  # Default fallback

        # Extract training parameters from kwargs - optimized for ultra-fast convergence
        max_steps = kwargs.get("max_steps", 25)  # Ultra-fast optimization
        eval_steps = kwargs.get("eval_steps", 5)  # Very frequent evaluation

        # Create enhanced fine-tuner instance with pre-prepared dataset
        fine_tuner = UnifiedFineTuner(
            train_dataset=train_dataset,
            fine_tuning_job=job,
            peft_method=peft_method,
            max_steps=max_steps,
            eval_steps=eval_steps,
        )

        # Run enhanced training
        training_results = fine_tuner.run_training()
        logger.info(f"✅ Training completed for job {job.id}")
        return training_results

    def _complete_job(
        self, job: FineTuningJob, training_results: dict[str, Any]
    ) -> FineTuningJob:
        """Complete the job successfully and register the model."""
        # Create a training metrics CSV file for the result
        result_file_id = _create_training_metrics_file(training_results)

        # Update the job with results
        job.status = "succeeded"
        job.finished_at = int(time.time())
        job.result_files = [result_file_id]
        job.trained_tokens = training_results.get("total_flos", 0)

        # Generate fine-tuned model name following OpenAI convention
        base_model_short = job.model.split("/")[-1] if "/" in job.model else job.model
        suffix = getattr(job, "suffix", None) or "custom"
        fine_tuned_model_name = f"ft:{base_model_short}:{suffix}:{job.id[:8]}"
        job.fine_tuned_model = fine_tuned_model_name

        # Register the fine-tuned model with the models service
        try:
            # Get PEFT adapter path from training results
            adapter_path = training_results.get("adapter_path")
            if adapter_path:
                self.models_service.register_fine_tuned_model(
                    fine_tuned_model_name, job.model, adapter_path
                )
                logger.info(f"📝 Registered fine-tuned model {fine_tuned_model_name}")
            else:
                logger.warning(
                    f"⚠️  No adapter path found in training results for job {job.id}"
                )
        except Exception as e:
            logger.error(f"❌ Failed to register fine-tuned model: {str(e)}")
            # Don't fail the job, just log the error

        # Update job in database
        updated_job = self.dao.update(job.id, job)
        logger.info(f"✅ Job {job.id} completed successfully")
        return updated_job or job

    def _fail_job(self, job: FineTuningJob, error: Exception) -> FineTuningJob:
        """Mark the job as failed with error details."""
        job.status = "failed"
        job.finished_at = int(time.time())
        job.error = {
            "code": "training_failed",
            "message": str(error),
            "param": None,
            "type": "server_error",
        }

        updated_job = self.dao.update(job.id, job)
        logger.error(f"❌ Job {job.id} marked as failed")
        return updated_job or job

    def cancel_job(self, job_id: str) -> FineTuningJob:
        """Cancel a running fine-tuning job."""
        logger.info(f"⏹️  Attempting to cancel job {job_id}")

        job = self.dao.get_by_id(job_id)
        if not job:
            raise ValueError(f"Job {job_id} not found")

        if job.status not in ["queued", "validating_files", "running"]:
            raise ValueError(f"Cannot cancel job in status '{job.status}'")

        job.status = "cancelled"
        job.finished_at = int(time.time())

        updated_job = self.dao.update(job_id, job)
        logger.info(f"⏹️  Job {job_id} cancelled successfully")
        return updated_job or job
