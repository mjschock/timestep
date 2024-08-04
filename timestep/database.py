import uuid
from typing import List

# from llama_cpp.llama_tokenizer import LlamaHFTokenizer
from sqlalchemy import JSON, Column, DateTime, func
from sqlmodel import Field, SQLModel, create_engine

from timestep.config import Settings

settings = Settings()

app_dir = settings.app_dir
engine = create_engine(f"sqlite:///{app_dir}/database.db")


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()


# class AgentSQLModel(Assistant, SQLModel, table=True):
class AgentSQLModel(SQLModel, TimestampMixin, table=True):
    __tablename__: str = "agents"
    # object: str = "fine_tuning.job"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    instructions: str = Field()
    model: str = Field()
    name: str = Field()
    tools: List[dict] = Field(sa_column=Column(JSON), default=[])

    # error: Optional[dict] = Field(sa_column=Column(JSON), default=JSON.NULL)
    # integrations: Optional[List[dict]] = Field(
    #     sa_column=Column(JSON), default=JSON.NULL
    # )
    # hyperparameters: dict = Field(sa_column=Column(JSON), default={})
    # result_files: List[str] = Field(sa_column=Column(JSON), default=[])
    # status: FineTuningJobStatus = Field(
    #     sa_column=Column(Enum(FineTuningJobStatus)), default=FineTuningJobStatus.queued
    # )


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


def create_db_and_tables():
    SQLModel.metadata.create_all(
        bind=engine,
        checkfirst=True,
        tables=None,
    )
