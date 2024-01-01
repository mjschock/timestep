import datetime
import logging
import os
import tempfile
from typing import Any, Callable, Dict, List, Optional, Union

from llama_index import (
    Document,
    ServiceContext,
    SimpleDirectoryReader,
)
from llama_index.embeddings.utils import EmbedType

# from llama_index.llms import OpenAI
from llama_index.llms import Ollama
from llama_index.llms.utils import LLMType
from llama_index.readers.base import BaseReader
from minio import Minio

# from llama_index.readers.schema.base import Document

STORAGE_DIR = "./storage"  # directory to cache the generated index
DATA_DIR = "./data"  # directory containing the documents to index

# service_context = ServiceContext.from_defaults(
#     embed_model="local",
#     # llm=OpenAI(model="gpt-3.5-turbo")
#     llm=Ollama(
#         base_url="http://ollama.default.svc.cluster.local:80",
#         model="phi:latest",
#     )
# )


async def get_service_context() -> ServiceContext:
    embed_model: EmbedType = "local"
    llm: LLMType = Ollama(
        base_url="http://ollama.default.svc.cluster.local:80",
        model="phi:latest",
    )

    # service_context = None

    # ServiceContext
    # See: https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/service_context.html
    service_context: ServiceContext = ServiceContext.from_defaults(
        # The embedding model used to generate vector representations of text.
        # If not provided, defaults to text-embedding-ada-002
        # If your OpenAI key is not set, defaults to BAAI/bge-small-en
        # embed_model: BaseEmbedding
        embed_model=embed_model,
        # The LLM used to generate natural language responses to queries.
        # If not provided, defaults to gpt-3.5-turbo from OpenAI
        # If your OpenAI key is not set, defaults to llama2-chat-13B from Llama.cpp
        # llm: LLM
        llm=llm,
    )

    return service_context


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


def get_file_metadata(file_path: str) -> Dict:
    # assert os.path.getsize(file_path) == user_files[0]['size'], f"{os.path.getsize(file_path)} != {user_files[0]['size']}"  # noqa: E501

    now = datetime.datetime.now()
    creation_date = datetime.datetime.strptime(
        user_files[0]["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z"  # noqa: F821
    ).strftime("%Y-%m-%d")
    last_accessed_date = now.strftime("%Y-%m-%d")
    last_modified_date = datetime.datetime.strptime(
        user_files[0]["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z"  # noqa: F821
    ).strftime("%Y-%m-%d")

    file_metadata = {
        "file_path": file_path,
        "file_name": user_files[0]["name"],  # noqa: F821
        "file_type": user_files[0]["mime_type"],  # noqa: F821
        "file_size": user_files[0]["size"],  # noqa: F821
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


async def load_documents():
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


async def get_index(service_context: ServiceContext):
    logging.getLogger("uvicorn")

    # check if storage already exists
    # if not os.path.exists(STORAGE_DIR):
    #     logger.info("Creating new index")
    #     # load the documents and create the index
    #     documents = SimpleDirectoryReader(DATA_DIR).load_data() # TODO: load from minio  # noqa: E501
    #     index = VectorStoreIndex.from_documents( # TODO: pgvector vector store index
    #         documents,
    #         service_context=service_context
    #     )
    #     # store it for later
    #     index.storage_context.persist(STORAGE_DIR)
    #     logger.info(f"Finished creating new index. Stored in {STORAGE_DIR}")

    # else:
    #     # load the existing index
    #     logger.info(f"Loading index from {STORAGE_DIR}...")
    #     storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
    #     index = load_index_from_storage(
    #         storage_context,
    #         service_context=service_context
    #     )
    #     logger.info(f"Finished loading index from {STORAGE_DIR}")

    return index  # noqa: F821
