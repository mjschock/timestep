from __future__ import annotations

from transformers import PretrainedConfig


class ModelConfig(PretrainedConfig):  # type: ignore[misc]
    model_type = "model"
