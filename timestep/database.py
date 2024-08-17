import os
import uuid
from abc import ABC, abstractmethod
from typing import List

from pydantic import ConfigDict
from sqlalchemy import (
    ARRAY,
    DDL,
    JSON,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Table,
    create_engine,
    event,
    func,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlmodel import Field, SQLModel, create_engine

from timestep.config import settings

app_dir = settings.app_dir

engine = create_engine(
    # f"sqlite:///{app_dir}/data/database.db", echo=True, echo_pool=True
    f"sqlite:///{app_dir}/data/database.db"
)


class SQLModelMixin(object):
    ## TODO: Investigate inheritance and use cases of TableArtifact from Prefect
    __table_args__ = {"extend_existing": True}

    # created_at = Column(DateTime, server_default=text('NOW()'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class AgentSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "agents"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    description: str | None = None
    instructions: str | None = None
    model: str = Field()
    # models: List[str] = Field(sa_column=Column(JSON), default=[])
    # model_config = ConfigDict(protected_namespaces=())
    # model_id: uuid.UUID = Field(foreign_key="models.id")
    name: str | None = None
    tools: List[dict] = Field(sa_column=Column(JSON), default=[])


class MessageSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "messages"
    __table_args__ = {"extend_existing": True}
    # __sqlmodel_relationships__: dict = {"thread": relationship}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    attachments: List[dict] = Field(sa_column=Column(JSON), default=[])
    content: List[dict] = Field(sa_column=Column(JSON), default=[])
    role: str = Field()
    status: str = Field()  # status: Literal['in_progress', 'incomplete', 'completed']
    thread_id: uuid.UUID = Field(foreign_key="threads.id")
    # thread: "ThreadSQLModel" = relationship("ThreadSQLModel", back_populates="messages")

    # Relationship back to the thread
    # thread = relationship("ThreadSQLModel", back_populates="messages")


# class ModelSQLModel(SQLModel, SQLModelMixin, table=True):
#     __tablename__: str = "models"
#     id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


# class ModelAliasSQLModel(SQLModel, SQLModelMixin, table=True):
#     __tablename__: str = "model_aliases"
#     alias: str = Field(default=None, primary_key=True)
#     model_config = ConfigDict(protected_namespaces=())
#     model_id: uuid.UUID = Field(foreign_key="models.id", ondelete="CASCADE")


class ThreadSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "threads"
    __table_args__ = {"extend_existing": True}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    is_locked: bool = Field(default=False)
    # is_locked = Column(Integer, default=0)
    # is_locked: bool = Field(default=False)

    # messages: List[MessageSQLModel] = relationship("MessageSQLModel", back_populates="thread")

    # Relationship to messages
    # messages = relationship("MessageSQLModel", back_populates="thread")


class VectorSQLModel(SQLModel, SQLModelMixin, table=True):
    __tablename__: str = "vectors"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # distance_to_center: float = Field()
    # metadata: dict = Field(sa_column=Column(JSON), default={})
    vector: List[float] = Field(sa_column=Column(JSON), default=[])


# DDL statements for triggers
trigger_insert_ddl = DDL(
    """
CREATE TRIGGER prevent_insert_on_locked_threads
BEFORE INSERT ON messages
FOR EACH ROW
WHEN EXISTS (
    SELECT 1
    FROM threads
    WHERE threads.id = NEW.thread_id AND threads.is_locked = 1
)
BEGIN
    SELECT RAISE(ABORT, 'Operation not allowed: the thread is locked');
END;
"""
)

trigger_update_ddl = DDL(
    """
CREATE TRIGGER prevent_update_on_locked_threads
BEFORE UPDATE ON messages
FOR EACH ROW
WHEN EXISTS (
    SELECT 1
    FROM threads
    WHERE threads.id = NEW.thread_id AND threads.is_locked = 1
)
BEGIN
    SELECT RAISE(ABORT, 'Operation not allowed: the thread is locked');
END;
"""
)

trigger_delete_ddl = DDL(
    """
CREATE TRIGGER prevent_delete_on_locked_threads
BEFORE DELETE ON messages
FOR EACH ROW
WHEN EXISTS (
    SELECT 1
    FROM threads
    WHERE threads.id = OLD.thread_id AND threads.is_locked = 1
)
BEGIN
    SELECT RAISE(ABORT, 'Operation not allowed: the thread is locked');
END;
"""
)

# Attach triggers to the table creation event
event.listen(MessageSQLModel.__table__, "after_create", trigger_insert_ddl)
event.listen(MessageSQLModel.__table__, "after_create", trigger_update_ddl)
event.listen(MessageSQLModel.__table__, "after_create", trigger_delete_ddl)


def create_db_and_tables():
    # try:
    SQLModel.metadata.create_all(
        bind=engine,
        # checkfirst=False,
        checkfirst=True,
        tables=None,
        # tables=[
        #     AgentSQLModel,
        #     # ModelSQLModel,
        #     # ModelAliasSQLModel,
        #     MessageSQLModel,
        #     ThreadSQLModel,
        # ],
    )

    # except Exception as e:
    #     print(f"Error creating tables: {e}")


if __name__ == "__main__":
    create_db_and_tables()
