"""Upload-related data models."""

from sqlmodel import Field, SQLModel


class UploadTable(SQLModel, table=True):
    """SQLModel table for persisting upload metadata."""

    __tablename__ = "uploads"

    id: str = Field(primary_key=True)
    object: str = "upload"
    bytes: int
    purpose: str
    filename: str
    created_at: int
    expires_at: int
    status: str = "pending"


class UploadPartTable(SQLModel, table=True):
    """SQLModel table for persisting upload parts."""

    __tablename__ = "upload_parts"

    id: str = Field(primary_key=True)
    upload_id: str = Field(foreign_key="uploads.id")
    part_number: int
    bytes: int
    created_at: int
    etag: str | None = None
