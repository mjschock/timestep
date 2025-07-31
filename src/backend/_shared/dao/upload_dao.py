"""Upload data access operations."""

from typing import Any

from sqlmodel import select

from backend._shared.database import get_session
from backend._shared.logging_config import logger
from backend._shared.models.upload_models import UploadPartTable, UploadTable


class UploadDAO:
    """Data access object for upload operations."""

    def create_upload(self, upload_data: dict[str, Any]) -> UploadTable:
        """Create a new upload record."""
        with get_session() as session:
            upload_table = UploadTable(**upload_data)
            session.add(upload_table)
            session.commit()
            session.refresh(upload_table)
            logger.info(f"📝 Created upload {upload_data['id']} in database")
            return upload_table

    def get_upload_by_id(self, upload_id: str) -> UploadTable | None:
        """Get an upload by ID."""
        with get_session() as session:
            upload_table = session.get(UploadTable, upload_id)
            if upload_table:
                logger.info(f"📖 Retrieved upload {upload_id} from database")
            return upload_table

    def update_upload_status(self, upload_id: str, status: str) -> bool:
        """Update upload status."""
        with get_session() as session:
            upload_table = session.get(UploadTable, upload_id)
            if upload_table:
                upload_table.status = status
                session.commit()
                logger.info(f"📝 Updated upload {upload_id} status to {status}")
                return True
            return False

    def delete_upload(self, upload_id: str) -> bool:
        """Delete an upload by ID."""
        with get_session() as session:
            upload_table = session.get(UploadTable, upload_id)
            if upload_table:
                session.delete(upload_table)
                session.commit()
                logger.info(f"🗑️  Deleted upload {upload_id} from database")
                return True
            return False

    def create_upload_part(self, part_data: dict[str, Any]) -> UploadPartTable:
        """Create a new upload part record."""
        with get_session() as session:
            part_table = UploadPartTable(**part_data)
            session.add(part_table)
            session.commit()
            session.refresh(part_table)
            logger.info(f"📝 Created upload part {part_data['id']} in database")
            return part_table

    def get_upload_parts(self, upload_id: str) -> list[UploadPartTable]:
        """Get all parts for an upload."""
        with get_session() as session:
            parts = session.exec(
                select(UploadPartTable).where(UploadPartTable.upload_id == upload_id)
            ).all()
            logger.info(f"📋 Retrieved {len(parts)} parts for upload {upload_id}")
            return list(parts)

    def get_upload_part_by_number(
        self, upload_id: str, part_number: int
    ) -> UploadPartTable | None:
        """Get a specific upload part by upload ID and part number."""
        with get_session() as session:
            part = session.exec(
                select(UploadPartTable).where(
                    UploadPartTable.upload_id == upload_id,
                    UploadPartTable.part_number == part_number,
                )
            ).first()
            return part

    def delete_upload_parts(self, upload_id: str) -> int:
        """Delete all parts for an upload. Returns count of deleted parts."""
        with get_session() as session:
            parts = session.exec(
                select(UploadPartTable).where(UploadPartTable.upload_id == upload_id)
            ).all()
            count = len(parts)
            for part in parts:
                session.delete(part)
            session.commit()
            logger.info(f"🗑️  Deleted {count} parts for upload {upload_id}")
            return count
