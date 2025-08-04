"""Data Access Object for responses."""

from typing import Optional

from sqlmodel import Session, select

from backend._shared.models.response_models import ResponseTable


class ResponseDAO:
    """Data Access Object for response operations."""
    
    def __init__(self, session: Session):
        self.session = session
    
    def create_response(self, response_data: dict) -> ResponseTable:
        """Create a new response in the database."""
        response = ResponseTable.from_dict(response_data)
        self.session.add(response)
        self.session.commit()
        self.session.refresh(response)
        return response
    
    def get_response_by_id(self, response_id: str) -> Optional[ResponseTable]:
        """Get a response by its ID."""
        statement = select(ResponseTable).where(ResponseTable.id == response_id)
        return self.session.exec(statement).first()
    
    def update_response(self, response_id: str, response_data: dict) -> Optional[ResponseTable]:
        """Update an existing response."""
        response = self.get_response_by_id(response_id)
        if not response:
            return None
        
        # Update fields from response_data
        for key, value in response_data.items():
            if hasattr(response, key):
                if key in ["tools", "output", "usage", "metadata"]:
                    # These fields are stored as JSON strings
                    setattr(response, key, value if isinstance(value, str) else str(value))
                else:
                    setattr(response, key, value)
        
        self.session.commit()
        self.session.refresh(response)
        return response
    
    def delete_response(self, response_id: str) -> bool:
        """Delete a response by its ID."""
        response = self.get_response_by_id(response_id)
        if not response:
            return False
        
        self.session.delete(response)
        self.session.commit()
        return True
    
    def list_responses(self, limit: int = 100, offset: int = 0) -> list[ResponseTable]:
        """List responses with pagination."""
        statement = select(ResponseTable).offset(offset).limit(limit)
        return self.session.exec(statement).all() 