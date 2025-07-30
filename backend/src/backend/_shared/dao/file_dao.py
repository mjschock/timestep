"""File data access operations."""

from openai.types.file_object import FileObject
from sqlmodel import select

from backend._shared.database import get_session
from backend._shared.logging_config import logger
from backend._shared.models.file_models import FileTable


class FileConverter:
    """Converter between FileObject and FileTable."""

    @staticmethod
    def to_table(file_obj: FileObject) -> FileTable:
        """Convert FileObject to FileTable."""
        return FileTable(
            id=file_obj.id,
            object=file_obj.object,
            bytes=file_obj.bytes,
            created_at=file_obj.created_at,
            filename=file_obj.filename,
            purpose=file_obj.purpose,
            status=getattr(file_obj, "status", "processed"),
            status_details=getattr(file_obj, "status_details", None),
        )

    @staticmethod
    def from_table(table: FileTable) -> FileObject:
        """Convert FileTable to FileObject."""
        return FileObject(
            id=table.id,
            object=table.object,
            bytes=table.bytes,
            created_at=table.created_at,
            filename=table.filename,
            purpose=table.purpose,
            status=table.status,
            status_details=table.status_details,
        )


class FileDAO:
    """Data access object for file operations."""

    def create(self, file_obj: FileObject) -> FileObject:
        """Create a new file record."""
        with get_session() as session:
            table_file = FileConverter.to_table(file_obj)
            session.add(table_file)
            session.commit()
            session.refresh(table_file)
            logger.info(f"📝 Created file {file_obj.id} in database")
            return FileConverter.from_table(table_file)

    def get_by_id(self, file_id: str) -> FileObject | None:
        """Get a file by ID."""
        with get_session() as session:
            table_file = session.get(FileTable, file_id)
            if table_file:
                logger.info(f"📖 Retrieved file {file_id} from database")
                return FileConverter.from_table(table_file)
            return None

    def list_all(
        self,
        purpose: str | None = None,
        limit: int | None = None,
        order: str = "asc",
        after: str | None = None,
    ) -> list[FileObject]:
        """List files with optional filtering and pagination."""
        with get_session() as session:
            query = select(FileTable)

            # Filter by purpose
            if purpose:
                query = query.where(FileTable.purpose == purpose)

            # Apply ordering
            if order == "desc":
                query = query.order_by(FileTable.created_at.desc())
            else:
                query = query.order_by(FileTable.created_at.asc())

            table_files = session.exec(query).all()

            # Apply pagination
            if after:
                after_index = None
                for i, table_file in enumerate(table_files):
                    if table_file.id == after:
                        after_index = i + 1
                        break
                if after_index is not None:
                    table_files = table_files[after_index:]

            if limit:
                table_files = table_files[:limit]

            files = [FileConverter.from_table(table_file) for table_file in table_files]
            logger.info(f"📋 Listed {len(files)} files from database")
            return files

    def delete(self, file_id: str) -> bool:
        """Delete a file by ID."""
        with get_session() as session:
            table_file = session.get(FileTable, file_id)
            if table_file:
                session.delete(table_file)
                session.commit()
                logger.info(f"🗑️  Deleted file {file_id} from database")
                return True
            return False
