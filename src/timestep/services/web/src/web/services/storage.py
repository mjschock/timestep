import os

import requests
from minio import Minio

# import databases

# from passlib.hash import bcrypt
# from sqlalchemy import TIMESTAMP, Column, MetaData, String, Table, text
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = os.getenv("POSTGRES_CONNECTION_STRING")

# database = databases.Database(DATABASE_URL)
# metadata = MetaData()
# users = Table(
#     "users",
#     metadata,
#     Column(
#         "id",
#         UUID(as_uuid=True),
#         # default=uuid.uuid4,
#         index=True,
#         primary_key=True,
#         server_default=text("gen_random_uuid()"),
#         unique=True,
#     ),
#     Column(
#         "created",
#         TIMESTAMP(timezone=True),
#         nullable=False,
#         server_default=text("CURRENT_TIMESTAMP"),
#     ),
#     Column(
#         "updated",
#         TIMESTAMP(timezone=True),
#         nullable=False,
#         server_default=text("CURRENT_TIMESTAMP"),
#         onupdate=text("CURRENT_TIMESTAMP"),
#     ),
#     Column(
#         "email",
#         String,
#         index=True,
#         nullable=False,
#         unique=True,
#     ),
#     Column(
#         "hashed_password",
#         String,
#         nullable=False,
#     ),
# )

# Base = declarative_base()


# class User(Base):
#     __table__ = users


# class UserService:
#     def __init__(self, database):
#         self.database = database

#     async def create_user(self, email: str, password: str):
#         # hashed_password = bcrypt.hash(password)
#         hashed_password = password
#         query = users.insert().values(email=email, hashed_password=hashed_password)
#         await database.execute(query)

#     async def get_user_by_email(self, email: str):
#         query = users.select().where(users.c.email == email)
#         return await database.fetch_one(query)


class StorageService:
    def __init__(self):
        minio_endpoint = os.getenv("MINIO_ENDPOINT")

        self.minio_client = Minio(
            minio_endpoint,
            access_key=os.getenv("MINIO_ROOT_USER"),
            secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            secure=False,
        )

    async def create_bucket(self, bucket_name: str, ignore_exists: bool = False):
        if self.minio_client.bucket_exists(bucket_name):
            if ignore_exists:
                return

            else:
                raise Exception(f"Bucket {bucket_name} already exists")

        self.minio_client.make_bucket(bucket_name)


async def init_storage_service():  # noqa: C901
    # engine = create_async_engine(
    #     DATABASE_URL,
    #     echo=True,
    # )

    # async with engine.begin() as conn:
    #     await conn.run_sync(metadata.create_all)

    # return UserService(database)

    storage_service = StorageService()

    await storage_service.create_bucket("default", ignore_exists=True)

    # TODO: do this ad-hoc or somewhere else
    # Get all users from database
    # For each user:
    # create a bucket with the user id as the bucket_name
    # set permissions to allow the user CRUD on their own bucket
    #     transport = AIOHTTPTransport(url="http://hasura-graphql-engine:8080/v1/graphql")

    #     async with Client(
    #         transport=transport,
    #         fetch_schema_from_transport=True,
    #     ) as session:
    #         query = gql(
    #             """
    #   query MyQuery {
    #     users {
    #       id
    #     }
    #   }
    #         """
    #         )

    #         result = await session.execute(query)
    #         print(result)

    url = "http://hasura-graphql-engine:8080/v1/graphql"

    async def fetch_graphql(operations_doc, operation_name, variables):
        data = {
            "operationName": operation_name,
            "query": operations_doc,
            "variables": variables,
        }

        response = requests.post(
            url,
            json=data,
            headers={
                "Content-Type": "application/json",
                # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
            },
        )

        print(response.status_code)
        print(response.text)

        return response.json()["data"]

    operations_doc = """
    query MyQuery {
      users {
        id
      }
    }
    """
    operation_name = "MyQuery"
    variables = {}

    data = await fetch_graphql(operations_doc, operation_name, variables)

    print("data: ", data)

    for user in data["users"]:
        await storage_service.create_bucket(user["id"], ignore_exists=True)

        await fetch_graphql(
            """
            mutation MyMutation($id: String) {
                insertBucket(object: {id: $id}, on_conflict: { constraint: buckets_pkey }) {
                    id
                }
            }
            """,  # noqa: E501
            "MyMutation",
            {"id": user["id"]},
        )

        async def pg_drop_files_insert_permission():
            data = {
                "args": {
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_drop_insert_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_drop_insert_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_drop_files_insert_permission()

        async def pg_create_files_insert_permission():
            data = {
                "args": {
                    "permission": {
                        "check": {
                            # "bucket_id": {
                            #     "_eq": "X-HASURA-USER-ID"
                            # }
                        },
                        "columns": "*",
                        "filter": {},
                        # "set": {
                        #     # "bucket_id": "X-Hasura-User-Id"
                        #     # "bucket": {
                        #     #     "id": "X-Hasura-User-Id"
                        #     # }
                        # },
                        # "set": {
                        #     "bucket_id": "X-HASURA-USER-ID"
                        #     # "bucketId": "X-Hasura-User-Id"
                        # },
                    },
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_create_insert_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_create_insert_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_create_files_insert_permission()

        async def pg_drop_buckets_select_permission():
            data = {
                "args": {
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "buckets",
                        "schema": "storage",
                    },
                },
                "type": "pg_drop_select_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_drop_select_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_drop_buckets_select_permission()

        async def pg_drop_files_select_permission():
            data = {
                "args": {
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_drop_select_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_drop_select_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_drop_files_select_permission()

        async def pg_create_buckets_select_permission():
            data = {
                "args": {
                    "permission": {
                        "allow_aggregations": True,
                        "columns": "*",
                        # "filter": {},
                        # "mutation_root_fields": ["insertFile"],
                        "filter": {
                            # "id": {
                            #     "_eq": "X-Hasura-User-Id"
                            # }
                        },
                    },
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "buckets",
                        "schema": "storage",
                    },
                },
                "type": "pg_create_select_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_create_select_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_create_buckets_select_permission()

        async def pg_create_files_select_permission():
            data = {
                "args": {
                    "permission": {
                        "allow_aggregations": True,
                        "columns": "*",
                        # "filter": {},
                        # "mutation_root_fields": ["insertFile"],
                        "filter": {"bucket_id": {"_eq": "X-Hasura-User-Id"}},
                    },
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_create_select_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_create_select_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_create_files_select_permission()

        async def pg_drop_buckets_update_permission():
            data = {
                "args": {
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "buckets",
                        "schema": "storage",
                    },
                },
                "type": "pg_drop_update_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_drop_update_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_drop_buckets_update_permission()

        async def pg_create_buckets_update_permission():
            data = {
                "args": {
                    "permission": {
                        "columns": "*",
                        # "filter": {},
                        # "mutation_root_fields": ["insertFile"],
                        "filter": {"id": {"_eq": "X-Hasura-User-Id"}},
                    },
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "buckets",
                        "schema": "storage",
                    },
                },
                "type": "pg_create_update_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_create_update_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_create_buckets_update_permission()

        async def pg_drop_files_update_permission():
            data = {
                "args": {
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_drop_update_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_drop_update_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_drop_files_update_permission()

        async def pg_create_files_update_permission():
            data = {
                "args": {
                    "permission": {
                        "columns": "*",
                        # "filter": {},
                        # "mutation_root_fields": ["*"],
                        "filter": {"bucket_id": {"_eq": "X-Hasura-User-Id"}},
                        "set": {"bucket_id": "X-Hasura-User-Id"},
                    },
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_create_update_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    # "x-hasura-admin-secret": os.getenv("HASURA_GRAPHQL_ADMIN_SECRET"),
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_create_update_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_create_files_update_permission()

        async def pg_drop_files_delete_permission():
            data = {
                "args": {
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_drop_delete_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_drop_delete_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_drop_files_delete_permission()

        async def pg_create_files_delete_permission():
            data = {
                "args": {
                    "permission": {
                        "columns": "*",
                        # "filter": {},
                        # "mutation_root_fields": ["*"],
                        "filter": {"bucket_id": {"_eq": "X-Hasura-User-Id"}},
                    },
                    "role": "user",
                    "source": "default",
                    "table": {
                        "name": "files",
                        "schema": "storage",
                    },
                },
                "type": "pg_create_delete_permission",
            }

            response = requests.post(
                "http://hasura-graphql-engine:8080/v1/metadata",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    "x-hasura-admin-secret": "*8C25%@5z6$c5ZN",
                },
            )

            print("pg_create_delete_permission")
            print(response.status_code)
            print(response.text)

            # return response.json()['data']

        await pg_create_files_delete_permission()

    return storage_service
