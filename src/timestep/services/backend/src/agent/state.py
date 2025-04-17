"""Define the state structures for the agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class Message:
    """Represents a message in the chat."""
    role: str  # "user" or "assistant"
    content: str


@dataclass
class State:
    """Defines the input state for the agent.
    
    This class is used to define the initial state and structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    for more information.
    """
    # Store the current user message as the changeme field for backward compatibility
    changeme: str = ""
    
    # Add support for conversation history to maintain context across turns
    messages: List[Message] = field(default_factory=list)
    
    # Store agent execution history for debugging
    agent_history: Optional[List[Dict[str, Any]]] = field(default_factory=list)
