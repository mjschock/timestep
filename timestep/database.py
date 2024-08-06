import os
import uuid
from abc import ABC, abstractmethod
from typing import List

from pydantic import ConfigDict
from sqlalchemy import JSON, Column, DateTime, func
from sqlmodel import Field, SQLModel, create_engine

from timestep.config import Settings

settings = Settings()
app_dir = settings.app_dir
os.makedirs(app_dir, exist_ok=True)
engine = create_engine(f"sqlite:///{app_dir}/database.db", echo=True, echo_pool=True)


class SQLModelMixin(object):
    ## TODO: Investigate inheritance and use cases of TableArtifact from Prefect
    __table_args__ = {"extend_existing": True}

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class AgentSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "agents"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    instructions: str = Field()
    # model: str = Field()
    # models: List[str] = Field(sa_column=Column(JSON), default=[])
    model_config = ConfigDict(protected_namespaces=())
    model_id: uuid.UUID = Field(foreign_key="models.id")
    name: str = Field()
    tools: List[dict] = Field(sa_column=Column(JSON), default=[])


class MessageSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "messages"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    attachments: List[dict] = Field(sa_column=Column(JSON), default=[])
    content: List[dict] = Field(sa_column=Column(JSON), default=[])
    role: str = Field()
    status: str = Field()  # status: Literal['in_progress', 'incomplete', 'completed']
    thread_id: uuid.UUID = Field(foreign_key="threads.id")


class ModelSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "models"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class ModelAliasSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "model_aliases"
    alias: str = Field(default=None, primary_key=True)
    model_config = ConfigDict(protected_namespaces=())
    model_id: uuid.UUID = Field(foreign_key="models.id", ondelete="CASCADE")


class ThreadSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "threads"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(
            bind=engine,
            checkfirst=True,
            tables=None,
        )

    except Exception as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    create_db_and_tables()
