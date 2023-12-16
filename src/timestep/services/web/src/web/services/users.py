import os

import databases

# from passlib.hash import bcrypt
from sqlalchemy import TIMESTAMP, Column, MetaData, String, Table, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.getenv("POSTGRES_CONNECTION_STRING")

database = databases.Database(DATABASE_URL)
metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        # default=uuid.uuid4,
        index=True,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        unique=True,
    ),
    Column(
        "created",
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ),
    Column(
        "updated",
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column(
        "email",
        String,
        index=True,
        nullable=False,
        unique=True,
    ),
    Column(
        "hashed_password",
        String,
        nullable=False,
    ),
)

Base = declarative_base()


class User(Base):
    __table__ = users


class UserService:
    def __init__(self, database):
        self.database = database

    async def create_user(self, email: str, password: str):
        # hashed_password = bcrypt.hash(password)
        # hashed_password = password
        # query = users.insert().values(email=email, hashed_password=hashed_password)
        # await database.execute(query)

        raise NotImplementedError

    async def get_user_by_email(self, email: str):
        # query = users.select().where(users.c.email == email)
        # return await database.fetch_one(query)

        raise NotImplementedError


async def init():
    engine = create_async_engine(
        DATABASE_URL,
        echo=True,
    )

    async with engine.begin() as conn:
        # await conn.run_sync(metadata.create_all)
        await conn.run_sync(metadata.drop_all)

    return UserService(database)
