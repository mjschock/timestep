import datetime
import logging
import mimetypes
import os
import tempfile
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union

from llama_index import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.readers.base import BaseReader
from llama_index.readers.schema.base import Document
from llama_index.vector_stores import PGVectorStore
from minio import Minio
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# from sqlalchemy import make_url
from sqlalchemy_utils import create_database, database_exists

# STORAGE_DIR = "./storage"  # directory to cache the generated index
# DATA_DIR = "./data"  # directory containing the documents to index

# service_context = ServiceContext.from_defaults(
#     llm=OpenAI(model="gpt-3.5-turbo")
# )
# service_context = ServiceContext.from_defaults(
#     embed_model='local',
#     llm=None,
# )

# MinioReader = download_loader("MinioReader")


class MinioReader(BaseReader):
    """General reader for any Minio file or directory."""

    def __init__(
        self,
        *args: Any,
        bucket: str,
        key: Optional[str] = None,
        prefix: Optional[str] = "",
        file_extractor: Optional[Dict[str, Union[str, BaseReader]]] = None,
        required_exts: Optional[List[str]] = None,
        filename_as_id: bool = False,
        num_files_limit: Optional[int] = None,
        file_metadata: Optional[Callable[[str], Dict]] = None,
        minio_endpoint: Optional[str] = None,
        minio_secure: bool = False,
        minio_access_key: Optional[str] = None,
        minio_secret_key: Optional[str] = None,
        minio_session_token: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize Minio bucket and key, along with credentials if needed.

        If key is not set, the entire bucket (filtered by prefix) is parsed.

        Args:
        bucket (str): the name of your Minio bucket
        key (Optional[str]): the name of the specific file. If none is provided,
            this loader will iterate through the entire bucket.
        prefix (Optional[str]): the prefix to filter by in the case that the loader
            iterates through the entire bucket. Defaults to empty string.
        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file
            extension to a BaseReader class that specifies how to convert that file
            to text. See `SimpleDirectoryReader` for more details.
        required_exts (Optional[List[str]]): List of required extensions.
            Default is None.
        num_files_limit (Optional[int]): Maximum number of files to read.
            Default is None.
        file_metadata (Optional[Callable[str, Dict]]): A function that takes
            in a filename and returns a Dict of metadata for the Document.
            Default is None.
        minio_endpoint (Optional[str]): The Minio endpoint. Default is None.
        minio_port (Optional[int]): The Minio port. Default is None.
        minio_access_key (Optional[str]): The Minio access key. Default is None.
        minio_secret_key (Optional[str]): The Minio secret key. Default is None.
        minio_session_token (Optional[str]): The Minio session token.
        """
        super().__init__(*args, **kwargs)

        self.bucket = bucket
        self.key = key
        self.prefix = prefix

        self.file_extractor = file_extractor
        self.required_exts = required_exts
        self.filename_as_id = filename_as_id
        self.num_files_limit = num_files_limit
        self.file_metadata = file_metadata

        self.minio_endpoint = minio_endpoint
        self.minio_secure = minio_secure
        self.minio_access_key = minio_access_key
        self.minio_secret_key = minio_secret_key
        self.minio_session_token = minio_session_token

    def load_data(self) -> List[Document]:
        """Load file(s) from Minio."""
        minio_client = Minio(
            self.minio_endpoint,
            secure=self.minio_secure,
            access_key=self.minio_access_key,
            secret_key=self.minio_secret_key,
            session_token=self.minio_session_token,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            # suffix = Path(self.key).suffix
            suffix = self.file_metadata(self.key)["file_type"]
            filepath = f"{temp_dir}/{next(tempfile._get_candidate_names())}{suffix}"
            minio_client.fget_object(
                bucket_name=self.bucket, object_name=self.key, file_path=filepath
            )

            # try:
            #     from llama_index import SimpleDirectoryReader
            # except ImportError:
            #     SimpleDirectoryReader = download_loader("SimpleDirectoryReader")

            loader = SimpleDirectoryReader(
                temp_dir,
                file_extractor=self.file_extractor,
                required_exts=self.required_exts,
                filename_as_id=self.filename_as_id,
                num_files_limit=self.num_files_limit,
                file_metadata=self.file_metadata,
            )

            return loader.load_data()


def default_file_metadata_func(file_path: str) -> Dict:
    """Get some handy metadate from filesystem.

    Args:
        file_path: str: file path in str
    """
    return {
        "file_path": file_path,
        "file_name": os.path.basename(file_path),
        "file_type": mimetypes.guess_type(file_path)[0],
        "file_size": os.path.getsize(file_path),
        "creation_date": datetime.fromtimestamp(
            Path(file_path).stat().st_ctime
        ).strftime("%Y-%m-%d"),
        "last_modified_date": datetime.fromtimestamp(
            Path(file_path).stat().st_mtime
        ).strftime("%Y-%m-%d"),
        "last_accessed_date": datetime.fromtimestamp(
            Path(file_path).stat().st_atime
        ).strftime("%Y-%m-%d"),
    }


class UserIndexService:
    # async def initialize_index(self):
    # global index
    # storage_context = StorageContext.from_defaults()

    # if os.path.exists(index_dir):
    #     index = load_index_from_storage(storage_context)

    # else:
    #     documents = SimpleDirectoryReader("./documents").load_data()
    #     index = VectorStoreIndex.from_documents(
    #         documents, storage_context=storage_context
    #     )
    #     storage_context.persist(index_dir)

    async def get_index(self):
        logger = logging.getLogger("uvicorn")

        postgres_database = "vector_db"
        postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
        postgres_password = os.environ.get("POSTGRES_PASSWORD")
        postgres_username = "postgres"
        # connection_string = f"postgresql://{postgres_username}:{postgres_password}@{postgres_hostname}:5432"  # noqa: E501
        # url = make_url(connection_string)
        url: URL = URL(
            # drivername="postgresql+psycopg2",
            # drivername="postgresql",
            # drivername="postgresql+asyncpg",
            drivername="postgresql+pg8000",
            username=postgres_username,
            password=postgres_password,
            host=postgres_hostname,
            port=5432,
            database=postgres_database,
        )

        vector_store = PGVectorStore.from_params(
            database=url.database,
            host=url.host,
            password=url.password,
            port=url.port,
            user=url.username,
            table_name="paul_graham_essay",
            embed_dim=1536,  # openai embedding dimension
        )

        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        logger.info("Loading index ...")
        # storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        index = load_index_from_storage(
            storage_context,
            index_id=None,
            service_context=service_context,  # noqa: F821, E501
        )  # noqa: E501, F821
        logger.info("Finished loading index")

        # check if storage already exists
        # if not os.path.exists(STORAGE_DIR):
        logger.info("Creating new index")
        # load the documents and create the index
        # loader = SimpleDirectoryReader(DATA_DIR)

        minio_endpoint = os.getenv("MINIO_ENDPOINT")
        s3_root_folder = os.getenv(
            "S3_ROOT_FOLDER", "f215cf48-7458-4596-9aa5-2159fc6a3caf"
        )  # noqa: E501

        user_files = [
            {
                "id": "28598384-5189-418c-a4f0-3470f5f9c403",
                "bucket_id": "4ac528d3-92c8-4cba-8a0c-a3b18ba3fc48",
                "created_at": "2023-12-10T15:16:48.626964+00:00",
                "updated_at": "2023-12-10T15:16:48.644634+00:00",
                "mime_type": "text/plain",
                "name": "paul_graham_essay.txt",
                "size": 75042,
            }
        ]

        user_file_id = user_files[0]["id"]

        def get_file_metadata(file_path: str) -> Dict:
            # assert os.path.getsize(file_path) == user_files[0]['size'], f"{os.path.getsize(file_path)} != {user_files[0]['size']}"  # noqa: E501

            now = datetime.datetime.now()
            creation_date = datetime.datetime.strptime(
                user_files[0]["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
            ).strftime("%Y-%m-%d")
            last_accessed_date = now.strftime("%Y-%m-%d")
            last_modified_date = datetime.datetime.strptime(
                user_files[0]["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
            ).strftime("%Y-%m-%d")

            file_metadata = {
                "file_path": file_path,
                "file_name": user_files[0]["name"],
                "file_type": user_files[0]["mime_type"],
                "file_size": user_files[0]["size"],
                "creation_date": creation_date,
                "last_modified_date": last_modified_date,
                # "last_accessed_date": user_files[0]['updated_at'],
                "last_accessed_date": last_accessed_date,
                # "creation_date": datetime.fromtimestamp(
                #     Path(file_path).stat().st_ctime
                # ).strftime("%Y-%m-%d"),
                # "last_modified_date": datetime.fromtimestamp(
                #     Path(file_path).stat().st_mtime
                # ).strftime("%Y-%m-%d"),
                # "last_accessed_date": datetime.fromtimestamp(
                #     Path(file_path).stat().st_atime
                # ).strftime("%Y-%m-%d"),
            }

            print("file_metadata", file_metadata)

            return file_metadata

        loader = MinioReader(
            # bucket="documents",
            bucket="default",
            # file_extractor,
            # file_metadata=default_file_metadata_func,
            file_metadata=get_file_metadata,
            filename_as_id=True,
            key=f"{s3_root_folder}/{user_file_id}",
            minio_endpoint=minio_endpoint,
            minio_access_key=os.getenv("MINIO_ROOT_USER"),
            minio_secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            minio_secure=False,
        )

        # TODO: pass in user_id and only load documents for that user
        documents = loader.load_data()
        print("documents", documents)

        index = VectorStoreIndex.from_documents(
            documents, service_context=service_context  # noqa: F821
        )  # noqa: F821, E501
        # store it for later
        # index.storage_context.persist(STORAGE_DIR)
        # logger.info(f"Finished creating new index. Stored in {STORAGE_DIR}")

        # else:
        #     # load the existing index
        #     logger.info(f"Loading index from {STORAGE_DIR}...")
        #     storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        #     index = load_index_from_storage(storage_context,service_context=service_context)  # noqa: E501
        #     logger.info(f"Finished loading index from {STORAGE_DIR}")

        return index

    async def query_index(self, query_text):
        # global index
        # query_text = request.args.get("text", None)
        # if query_text is None:
        #     return (
        #         "No text found, please include a ?text=blah parameter in the URL",
        #         400,
        #     )
        # index: VectorStoreIndex = Depends(get_index),
        index: VectorStoreIndex = await self.get_index()
        query_engine = index.as_query_engine()
        response = query_engine.query(query_text)

        print("response", response)

        return response


async def init_user_index_service():
    user_index_service = UserIndexService()

    # await user_index_service.initialize_index()

    print("OPENAI_API_KEY", os.environ.get("OPENAI_API_KEY"))

    # DATABASE_URL = os.getenv("POSTGRES_CONNECTION_STRING")

    postgres_database = "vector_db"
    postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
    # postgres_password = config.postgresql_password.get_secret_value()
    postgres_password = os.environ.get("POSTGRES_PASSWORD")
    postgres_username = "postgres"

    # connection_string = f"postgresql://{postgres_username}:{postgres_password}@{postgres_hostname}:5432"  # noqa: E501
    # url = make_url(connection_string)
    url: URL = URL(
        # drivername="postgresql+psycopg2",
        # drivername="postgresql",
        # drivername="postgresql+asyncpg",
        drivername="postgresql+pg8000",
        username=postgres_username,
        password=postgres_password,
        host=postgres_hostname,
        port=5432,
        database=postgres_database,
    )

    engine = create_engine(url)

    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))

    return user_index_service
