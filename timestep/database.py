import uuid
from typing import List

from sqlalchemy import JSON, Column, DateTime, func
from sqlmodel import Field, SQLModel, create_engine

from timestep.config import Settings


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()


class AgentSQLModel(SQLModel, TimestampMixin, table=True):
    __tablename__: str = "agents"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    instructions: str = Field()
    model: str = Field()
    name: str = Field()
    tools: List[dict] = Field(sa_column=Column(JSON), default=[])


class ThreadSQLModel(SQLModel, TimestampMixin, table=True):
    __tablename__: str = "threads"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class MessageSQLModel(SQLModel, TimestampMixin, table=True):
    __tablename__: str = "messages"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    attachments: List[dict] = Field(sa_column=Column(JSON), default=[])
    content: List[dict] = Field(sa_column=Column(JSON), default=[])
    role: str = Field()
    status: str = Field()  # status: Literal['in_progress', 'incomplete', 'completed']
    thread_id: uuid.UUID = Field(foreign_key="threads.id")


settings = Settings()
app_dir = settings.app_dir
engine = create_engine(f"sqlite:///{app_dir}/database.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(
        bind=engine,
        checkfirst=True,
        tables=None,
    )


if __name__ == "__main__":
    create_db_and_tables()
