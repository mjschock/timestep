"""Model registry data access operations."""

import time

from backend._shared.database import get_session
from backend._shared.logging_config import logger
from backend._shared.models.model_models import ModelTable


class ModelDAO:
    """Data access object for model registry operations."""

    def create(self, model_data: dict) -> ModelTable:
        """Create a new model record."""
        with get_session() as session:
            model_table = ModelTable(**model_data)
            session.add(model_table)
            session.commit()
            session.refresh(model_table)
            logger.info(f"📝 Created model {model_data['id']} in database")
            return model_table

    def get_by_id(self, model_id: str) -> ModelTable | None:
        """Get a model by ID."""
        with get_session() as session:
            model_table = session.get(ModelTable, model_id)
            if model_table:
                logger.info(f"📖 Retrieved model {model_id} from database")
            return model_table

    def list_all(self, model_type: str | None = None) -> list[ModelTable]:
        """List all models, optionally filtered by type."""
        with get_session() as session:
            if model_type:
                models = (
                    session.query(ModelTable)
                    .filter(ModelTable.model_type == model_type)
                    .all()
                )
            else:
                models = session.query(ModelTable).all()
            logger.info(f"📋 Listed {len(models)} models from database")
            return models

    def update(self, model_id: str, model_data: dict) -> ModelTable | None:
        """Update a model record."""
        with get_session() as session:
            model_table = session.get(ModelTable, model_id)
            if model_table:
                for key, value in model_data.items():
                    if hasattr(model_table, key):
                        setattr(model_table, key, value)
                session.commit()
                session.refresh(model_table)
                logger.info(f"📝 Updated model {model_id} in database")
                return model_table
            return None

    def delete(self, model_id: str) -> bool:
        """Delete a model by ID."""
        with get_session() as session:
            model_table = session.get(ModelTable, model_id)
            if model_table:
                session.delete(model_table)
                session.commit()
                logger.info(f"🗑️  Deleted model {model_id} from database")
                return True
            return False

    def register_fine_tuned_model(
        self, model_id: str, base_model: str, adapter_path: str
    ) -> ModelTable:
        """Register a fine-tuned model with its adapter path."""
        model_data = {
            "id": model_id,
            "object": "model",
            "created": int(time.time()),
            "owned_by": "user",
            "model_type": "fine_tuned",
            "base_model": base_model,
            "adapter_path": adapter_path,
        }
        return self.create(model_data)
