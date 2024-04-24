from mamba_ssm import Mamba
import timm
import torch
from transformers import PreTrainedModel

from timestep.agents.transformers.models.model.configuration_model import ModelConfig

class ModelModel(PreTrainedModel):
    config_class = ModelConfig
