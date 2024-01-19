from dotenv import load_dotenv

load_dotenv()
import logging
import os

from llama_index import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
)
from llama_index.vector_stores import PGVectorStore

from app.engine.constants import DATA_DIR
from app.engine.context import create_service_context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def generate_datasource(service_context):
    logger.info("Creating new index")
    # load the documents and create the index
    documents = SimpleDirectoryReader(DATA_DIR).load_data() # TODO: load from MinIO instead
    # store = MongoDBAtlasVectorSearch(
    #     db_name=os.environ["MONGODB_DATABASE"],
    #     collection_name=os.environ["MONGODB_VECTORS"],
    #     index_name=os.environ["MONGODB_VECTOR_INDEX"],
    # )
    store = PGVectorStore.from_params(
        database=os.getenv("POSTGRES_DATABASE"),
        host=os.getenv("POSTGRES_HOSTNAME"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port="5432",
        user=os.getenv("POSTGRES_USERNAME"),
    )
    storage_context = StorageContext.from_defaults(vector_store=store)
    VectorStoreIndex.from_documents(
        documents,
        service_context=service_context,
        storage_context=storage_context,
        show_progress=True,  # this will show you a progress bar as the embeddings are created
    )
    logger.info(
        f"Successfully created embeddings in the PostgreSQL table {store.table_name}"
    )
#     logger.info(
#         """IMPORTANT: You can't query your index yet because you need to create a vector search index in MongoDB's UI now.
# See https://github.com/run-llama/mongodb-demo/tree/main?tab=readme-ov-file#create-a-vector-search-index"""
#     )


if __name__ == "__main__":
    generate_datasource(create_service_context())
