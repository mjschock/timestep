"""Fine-tuning data access operations."""

import json
import time

from openai.types.fine_tuning.fine_tuning_job import (
    FineTuningJob,
    Hyperparameters,
    Method,
)
from openai.types.fine_tuning.supervised_hyperparameters import (
    SupervisedHyperparameters,
)
from openai.types.fine_tuning.supervised_method import SupervisedMethod
from sqlmodel import select

from backend._shared.database import get_session
from backend._shared.logging_config import logger
from backend._shared.models.fine_tuning_models import FineTuningJobTable


class FineTuningJobConverter:
    """Converter between FineTuningJob and FineTuningJobTable."""

    @staticmethod
    def to_table(job: FineTuningJob) -> FineTuningJobTable:
        """Convert FineTuningJob to FineTuningJobTable."""
        return FineTuningJobTable(
            id=job.id,
            object=job.object,
            model=job.model,
            created_at=job.created_at,
            updated_at=getattr(job, "updated_at", None),
            finished_at=getattr(job, "finished_at", None),
            fine_tuned_model=job.fine_tuned_model,
            status=job.status,
            trained_tokens=getattr(job, "trained_tokens", None),
            training_file=job.training_file,
            validation_file=getattr(job, "validation_file", None),
            result_files=json.dumps(job.result_files) if job.result_files else None,
            error=json.dumps(getattr(job, "error", None))
            if getattr(job, "error", None)
            and isinstance(getattr(job, "error", None), dict)
            else getattr(job, "error", None),
            estimated_finish=getattr(job, "estimated_finish", None),
            seed=getattr(job, "seed", None),
            organization_id=getattr(job, "organization_id", "org-default"),
            method_json=json.dumps(job.method.model_dump()) if job.method else None,
            hyperparameters_json=None,  # Deprecated field, hyperparameters now in method
            training_metrics_json=json.dumps(getattr(job, "training_metrics", None))
            if hasattr(job, "training_metrics")
            else None,
        )

    @staticmethod
    def from_table(table: FineTuningJobTable) -> FineTuningJob:
        """Convert FineTuningJobTable to FineTuningJob."""
        # Parse method
        method = None
        if table.method_json:
            method_data = json.loads(table.method_json)
            if "supervised" in method_data:
                supervised_data = method_data["supervised"]
                hyperparams = SupervisedHyperparameters(
                    **supervised_data["hyperparameters"]
                )
                method = Method(
                    type="supervised",
                    supervised=SupervisedMethod(hyperparameters=hyperparams),
                )

        # Create FineTuningJob with required fields
        job = FineTuningJob(
            id=table.id,
            object=table.object,
            model=table.model,
            created_at=table.created_at,
            finished_at=table.finished_at,
            fine_tuned_model=table.fine_tuned_model,
            status=table.status,
            trained_tokens=table.trained_tokens,
            training_file=table.training_file,
            validation_file=table.validation_file,
            result_files=json.loads(table.result_files) if table.result_files else [],
            error=json.loads(table.error)
            if table.error and table.error.startswith("{")
            else table.error,
            estimated_finish=table.estimated_finish,
            seed=table.seed,
            method=method,
            hyperparameters=Hyperparameters(),  # Required field with empty values
            organization_id=table.organization_id,
        )

        # Add training metrics as an extra attribute
        if table.training_metrics_json:
            job.training_metrics = json.loads(table.training_metrics_json)

        return job


class FineTuningJobDAO:
    """Data access object for fine-tuning job operations."""

    def __init__(self):
        self._counter = 0
        # Initialize counter from existing jobs
        with get_session() as session:
            existing_jobs = session.exec(select(FineTuningJobTable)).all()
            if existing_jobs:
                counters = []
                for job in existing_jobs:
                    if "-" in job.id:
                        try:
                            counter_part = job.id.split("-")[-1]
                            counters.append(int(counter_part))
                        except ValueError:
                            pass
                if counters:
                    self._counter = max(counters)

    def create(self, fine_tuning_job: FineTuningJob) -> FineTuningJob:
        """Create and store a new fine-tuning job."""
        if not fine_tuning_job.id or fine_tuning_job.id == "temp-id":
            self._counter += 1
            fine_tuning_job.id = f"ftjob-{int(time.time())}-{self._counter}"

        with get_session() as session:
            table_job = FineTuningJobConverter.to_table(fine_tuning_job)
            session.add(table_job)
            session.commit()
            session.refresh(table_job)

        logger.info(f"📝 Created job {fine_tuning_job.id} in database")
        return fine_tuning_job

    def get_by_id(self, job_id: str) -> FineTuningJob | None:
        """Retrieve a fine-tuning job by ID."""
        with get_session() as session:
            table_job = session.get(FineTuningJobTable, job_id)
            if table_job:
                job = FineTuningJobConverter.from_table(table_job)
                logger.info(f"📖 Retrieved job {job_id} from database")
                return job
            else:
                logger.warning(f"⚠️  Job {job_id} not found in database")
                return None

    def update(
        self, job_id: str, fine_tuning_job: FineTuningJob
    ) -> FineTuningJob | None:
        """Update an existing fine-tuning job."""
        with get_session() as session:
            table_job = session.get(FineTuningJobTable, job_id)
            if table_job:
                updated_table = FineTuningJobConverter.to_table(fine_tuning_job)
                for field, value in updated_table.model_dump().items():
                    setattr(table_job, field, value)
                session.commit()
                session.refresh(table_job)
                logger.info(f"📝 Updated job {job_id} in database")
                return fine_tuning_job
            else:
                logger.error(f"❌ Cannot update job {job_id}: not found in database")
                return None

    def list_all(self) -> list[FineTuningJob]:
        """List all jobs from the database."""
        with get_session() as session:
            table_jobs = session.exec(select(FineTuningJobTable)).all()
            jobs = [
                FineTuningJobConverter.from_table(table_job) for table_job in table_jobs
            ]
            logger.info(f"📋 Listed {len(jobs)} jobs from database")
            return jobs

    def delete(self, job_id: str) -> bool:
        """Delete a fine-tuning job by ID."""
        with get_session() as session:
            table_job = session.get(FineTuningJobTable, job_id)
            if table_job:
                session.delete(table_job)
                session.commit()
                logger.info(f"🗑️  Deleted job {job_id} from database")
                return True
            else:
                logger.warning(f"⚠️  Cannot delete job {job_id}: not found in database")
                return False
