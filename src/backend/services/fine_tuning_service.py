# Basic fine-tuning service stub using new model_utils
from typing import Any

from backend._shared.logging_config import logger
from backend._shared.utils.model_utils import (
    get_model,
    get_processor,
    prepare_model_inputs,
    process_model_inputs,
    process_model_outputs,
)


class FineTuningService:
    def __init__(self) -> None:
        self.logger = logger

    def start_fine_tuning(
        self, dataset: list, model_name: str = None
    ) -> dict[str, Any]:
        """Start a fine-tuning job."""
        self.logger.info(f"Starting fine-tuning for model: {model_name}")

        # Load model for training
        model = get_model(train=True)
        processor = get_processor()

        # Process training data
        model_inputs = prepare_model_inputs(
            messages=dataset[0]["messages"],  # First example
            processor=processor,
            train=True,
        )

        # Get collate function and run training
        model_outputs = process_model_inputs(
            data_collator=model_inputs["data_collator"],
            model=model,
            processor=processor,
            train_dataset=model_inputs["train_dataset"],
        )

        # Run training
        results = process_model_outputs(
            model_outputs=model_outputs,
            processor=processor,
        )

        self.logger.info("Fine-tuning completed successfully")
        return results


# Global service instance
_fine_tuning_service = None
_lock = None


def get_fine_tuning_service() -> FineTuningService:
    """Get the global fine-tuning service instance."""
    global _fine_tuning_service, _lock
    if _fine_tuning_service is None:
        import threading

        if _lock is None:
            _lock = threading.Lock()
        with _lock:
            if _fine_tuning_service is None:
                _fine_tuning_service = FineTuningService()
    return _fine_tuning_service
