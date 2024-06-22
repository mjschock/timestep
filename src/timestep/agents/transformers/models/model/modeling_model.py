from __future__ import annotations

from transformers import PreTrainedModel

from timestep.agents.transformers.models.model.configuration_model import ModelConfig


class ModelModel(PreTrainedModel):  # type: ignore[misc]
    config_class = ModelConfig
