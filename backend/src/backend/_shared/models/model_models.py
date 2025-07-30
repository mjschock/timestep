"""Model registry related data models."""

from sqlmodel import Field, SQLModel


class ModelTable(SQLModel, table=True):
    """SQLModel table for persisting model registry information."""

    __tablename__ = "models"

    id: str = Field(primary_key=True)
    object: str = "model"
    created: int
    owned_by: str = "user"
    model_type: str = "base"  # base, fine_tuned, etc.
    base_model: str | None = None  # For fine-tuned models, reference to base model
    adapter_path: str | None = None  # Path to PEFT adapter for fine-tuned models
