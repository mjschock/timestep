"""File-related data models."""

from sqlmodel import Field, SQLModel


class FileTable(SQLModel, table=True):
    """SQLModel table for persisting file metadata."""

    __tablename__ = "files"

    id: str = Field(primary_key=True)
    object: str = "file"
    bytes: int
    created_at: int
    filename: str
    purpose: str
    status: str = "processed"
    status_details: str | None = None
