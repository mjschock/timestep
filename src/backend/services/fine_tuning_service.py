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
        _, processed_messages, _ = prepare_model_inputs(
            messages=dataset[0]["messages"],  # First example
            processor=processor,
            train=True,
        )

        processed_dataset = [{"messages": processed_messages}]

        # Get collate function
        collate_fn = process_model_inputs(
            processed_dataset, model, processor, train=True
        )

        # Run training
        training_result = process_model_outputs(
            processed_dataset,
            collate_fn,
            model,
            train=processor,
            conversation_idx=0,
        )

        self.logger.info("Fine-tuning completed successfully")
        return training_result


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
