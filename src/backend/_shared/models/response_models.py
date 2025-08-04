"""Response models for storing responses in the database."""

import json
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class ResponseTable(SQLModel, table=True):
    """Database table for storing responses."""
    
    __tablename__ = "responses"
    
    id: str = Field(primary_key=True, description="Unique response ID")
    object: str = Field(default="response", description="Object type")
    created_at: int = Field(description="Unix timestamp when response was created")
    model: str = Field(description="Model used for the response")
    status: str = Field(description="Response status (completed, in_progress, etc.)")
    parallel_tool_calls: bool = Field(default=True, description="Whether parallel tool calls are enabled")
    tool_choice: str = Field(default="auto", description="Tool choice setting")
    tools: str = Field(description="JSON string of tools used")
    previous_response_id: Optional[str] = Field(default=None, description="ID of previous response")
    output: str = Field(description="JSON string of response output")
    usage: str = Field(description="JSON string of usage statistics")
    instructions: Optional[str] = Field(default=None, description="Instructions used")
    temperature: float = Field(default=1.0, description="Temperature setting")
    top_p: float = Field(default=1.0, description="Top-p setting")
    max_tokens: Optional[int] = Field(default=None, description="Maximum tokens")
    user: Optional[str] = Field(default=None, description="User ID")
    # TODO: SQLAlchemy reserves 'metadata' as a field name, so we use 'response_metadata'
    # Consider if we can work around this limitation or if this naming is acceptable
    response_metadata: str = Field(default="{}", description="JSON string of metadata")
    
    created: datetime = Field(default_factory=datetime.utcnow, description="Database creation timestamp")
    updated: datetime = Field(default_factory=datetime.utcnow, description="Database update timestamp")
    
    def to_dict(self) -> dict:
        """Convert the response to a dictionary format matching OpenAI's response format."""
        return {
            "id": self.id,
            "object": self.object,
            "created_at": self.created_at,
            "model": self.model,
            "status": self.status,
            "parallel_tool_calls": self.parallel_tool_calls,
            "tool_choice": self.tool_choice,
            "tools": json.loads(self.tools) if self.tools else [],
            "previous_response_id": self.previous_response_id,
            "output": json.loads(self.output) if self.output else [],
            "usage": json.loads(self.usage) if self.usage else {},
            "instructions": self.instructions,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_tokens": self.max_tokens,
            "user": self.user,
            "metadata": json.loads(self.response_metadata) if self.response_metadata else {},
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "ResponseTable":
        """Create a ResponseTable from a dictionary."""
        return cls(
            id=data.get("id"),
            object=data.get("object", "response"),
            created_at=data.get("created_at"),
            model=data.get("model"),
            status=data.get("status"),
            parallel_tool_calls=data.get("parallel_tool_calls", True),
            tool_choice=data.get("tool_choice", "auto"),
            tools=json.dumps(data.get("tools", [])),
            previous_response_id=data.get("previous_response_id"),
            output=json.dumps(data.get("output", [])),
            usage=json.dumps(data.get("usage", {})),
            instructions=data.get("instructions"),
            temperature=data.get("temperature", 1.0),
            top_p=data.get("top_p", 1.0),
            max_tokens=data.get("max_tokens"),
            user=data.get("user"),
            response_metadata=json.dumps(data.get("metadata", {})),
        ) 