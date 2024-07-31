import enum
import uuid
from typing import List, Optional

from openai.types.fine_tuning.fine_tuning_job import FineTuningJob
from pydantic import BaseModel

# from sqlalchemy import JSON
# import sqlalchemy
from sqlalchemy import Column, Enum

# from sqlalchemy.dialects.sqlite.json import JSON
from sqlalchemy.types import JSON
from sqlmodel import Field, Session, SQLModel

# from timestep.database import InstanceStoreSingleton


# class FineTuningJobErrorSQLModel(Error, Column(JSON)):
#   pass
#   __tablename__: str = "fine_tuning_job_errors"

#   id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class FineTuningJobStatus(str, enum.Enum):
    cancelled = "cancelled"
    failed = "failed"
    queued = "queued"
    running = "running"
    succeeded = "succeeded"
    validating_files = "validating_files"


# TODO: can i just use the flow run plus artifacts for this?
class FineTuningJobSQLModel(FineTuningJob, SQLModel, table=True):
    __tablename__: str = "fine_tuning_jobs"
    object: str = "fine_tuning.job"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # id: uuid.uuid4 = Field(default_factory=uuid.uuid4, primary_key=True)

    error: Optional[dict] = Field(sa_column=Column(JSON), default=JSON.NULL)
    integrations: Optional[List[dict]] = Field(
        sa_column=Column(JSON), default=JSON.NULL
    )
    hyperparameters: dict = Field(sa_column=Column(JSON), default={})
    result_files: List[str] = Field(sa_column=Column(JSON), default=[])
    status: FineTuningJobStatus = Field(
        sa_column=Column(Enum(FineTuningJobStatus)), default=FineTuningJobStatus.queued
    )


class ModelInstanceStoreSingleton(object):
    models: dict[uuid.UUID] = {}
    _shared_instance_state = {
        "models": {},
    }

    def __new__(cls, *args, **kwargs):
        obj = super(ModelInstanceStoreSingleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_instance_state

        return obj

    def insert(self, base_model: BaseModel):
        if type(base_model) is FineTuningJob:
            print("=== insert ===")
            print("id: ", base_model.id)
            print('base_model.model_dump()["id"]', base_model.model_dump()["id"])
            fine_tuning_job = FineTuningJobSQLModel.model_validate(
                base_model.model_dump()
            )
            print("fine_tuning_job.id: ", fine_tuning_job.id)

            with Session(engine) as session:
                session.add(fine_tuning_job)
                session.commit()

        else:
            raise NotImplementedError(f"Type {type(base_model)} is not yet implemented")

    def select(self, base_model_class, id: str):
        print("=== select ===")
        print("id: ", id)

        if issubclass(base_model_class, FineTuningJob):
            with Session(engine) as session:
                fine_tuning_job = session.get(
                    FineTuningJobSQLModel, ident=uuid.UUID(id, version=4)
                )
                print("fine_tuning_job.id: ", fine_tuning_job.id)

                assert (
                    type(fine_tuning_job.id) == uuid.UUID
                ), f"{type(fine_tuning_job.id)} != uuid.UUID"

                # m = base_model_class.model_validate(fine_tuning_job, strict=True)
                # print('type(m): ', type(m))
                #

                return FineTuningJob(**fine_tuning_job.model_dump(mode="json"))

                # raise NotImplementedError

        else:
            raise NotImplementedError(f"Type {base_model_class} is not yet implemented")


model_instance_store = InstanceStoreSingleton()
model_instance_store.shared_variable = "Shared Variable"
