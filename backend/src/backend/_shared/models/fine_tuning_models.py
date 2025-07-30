"""Fine-tuning related data models."""

from sqlmodel import Field, SQLModel


class FineTuningJobTable(SQLModel, table=True):
    """SQLModel table for persisting FineTuningJob objects."""

    __tablename__ = "fine_tuning_jobs"

    id: str = Field(primary_key=True)
    object: str = "fine_tuning.job"
    model: str
    created_at: int
    updated_at: int | None = None
    finished_at: int | None = None
    fine_tuned_model: str | None = None
    status: str = "queued"
    trained_tokens: int | None = None
    training_file: str
    validation_file: str | None = None
    result_files: str | None = None  # JSON string of list
    error: str | None = None
    estimated_finish: int | None = None
    seed: int | None = None
    organization_id: str = "org-default"

    # Store method and hyperparameters as JSON strings
    method_json: str | None = None
    hyperparameters_json: str | None = None

    # Store training metrics as JSON string
    training_metrics_json: str | None = None
