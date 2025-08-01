# Basic models service stub using new model_utils
from typing import Any

from backend._shared.dao.model_dao import ModelDAO
from backend._shared.utils.model_utils import get_model, get_processor


class ModelsService:
    def __init__(self) -> None:
        # Model registry/cache to avoid reloading models
        self._model_cache = {}
        self._processor_cache = {}
        self.model_dao = ModelDAO()

    def get_model(self, model_name: str = None) -> Any:
        """Get a model instance."""
        if model_name in self._model_cache:
            return self._model_cache[model_name]

        model = get_model()
        self._model_cache[model_name] = model
        return model

    def get_processor(self, model_name: str = None) -> Any:
        """Get a processor instance."""
        if model_name in self._processor_cache:
            return self._processor_cache[model_name]

        processor = get_processor()
        self._processor_cache[model_name] = processor
        return processor


# Global service instance
_models_service = None
_lock = None


def get_models_service() -> ModelsService:
    """Get the global models service instance."""
    global _models_service, _lock
    if _models_service is None:
        import threading

        if _lock is None:
            _lock = threading.Lock()
        with _lock:
            if _models_service is None:
                _models_service = ModelsService()
    return _models_service
