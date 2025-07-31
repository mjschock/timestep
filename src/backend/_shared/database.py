#!/usr/bin/env python3
"""
Centralized database setup for the backend application.
"""

import os

from sqlmodel import Session, SQLModel, create_engine

# Import all models to ensure they're registered with SQLModel
from backend._shared.models import (  # noqa: F401
    FileTable,
    FineTuningJobTable,
    ModelTable,
    UploadPartTable,
    UploadTable,
)


# Database Engine and Session Management
def get_database_path() -> str:
    """Get the path to the database file."""
    # Use data/database.db relative to the project root
    # __file__ is src/backend/_shared/database.py, so go up 4 levels to get to project root
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
    )
    db_path = os.path.join(project_root, "data", "database.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return db_path


def create_db_engine():
    """Create the database engine."""
    db_path = get_database_path()
    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    return engine


def init_database():
    """Initialize the database by creating all tables."""
    engine = create_db_engine()
    SQLModel.metadata.create_all(engine)
    return engine


def get_session():
    """Get a database session."""
    engine = create_db_engine()
    return Session(engine)


# Global engine instance
engine = init_database()
