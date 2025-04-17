"""Define the configurable parameters for the agent."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Optional, List

from langchain_core.runnables import RunnableConfig


@dataclass(kw_only=True)
class Configuration:
    """The configuration for the agent with smolagents integration."""

    # Model parameters
    model_id: str = "llama2"  # Default model ID for Ollama
    model_provider: str = "ollama"  # Options: "huggingface", "openai", "litellm", "ollama"
    ollama_base_url: str = "http://host.docker.internal:11434"  # Ollama API URL
    
    # Tool configuration
    enabled_tools: List[str] = field(default_factory=lambda: ["web_search"])

    @classmethod
    def from_runnable_config(
        cls, config: Optional[RunnableConfig] = None
    ) -> Configuration:
        """Create a Configuration instance from a RunnableConfig object."""
        configurable = (config.get("configurable") or {}) if config else {}
        _fields = {f.name for f in fields(cls) if f.init}
        return cls(**{k: v for k, v in configurable.items() if k in _fields})
