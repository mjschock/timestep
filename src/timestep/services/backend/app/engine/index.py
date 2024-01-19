import logging
import os

from llama_index import VectorStoreIndex
from llama_index.agent import (
    AgentRunner,
    MultimodalReActAgentWorker,
    OpenAIAgent,
    OpenAIAgentWorker,
    ParallelAgentRunner,
)
from llama_index.chat_engine.types import BaseChatEngine, ChatMode
from llama_index.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index.vector_stores import PGVectorStore

from app.engine.context import create_service_context


def get_chat_engine() -> BaseChatEngine:
    service_context = create_service_context()
    logger = logging.getLogger("uvicorn")

    logger.info("Connecting to index from PostgreSQL...")
    vector_store = PGVectorStore.from_params(
        database=os.getenv("POSTGRES_DATABASE"),
        host=os.getenv("POSTGRES_HOSTNAME"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port="5432",
        user=os.getenv("POSTGRES_USERNAME"),
    )

    index = VectorStoreIndex.from_vector_store(vector_store, service_context)
    # index = MultiModalVectorStoreIndex.from_vector_store(vector_store, service_context)
    # ImportError: ClipEmbedding requires `pip install git+https://github.com/openai/CLIP.git` and torch
    logger.info("Finished connecting to index from PostgreSQL.")
    logger.info(f'\tDatabase: {os.getenv("POSTGRES_DATABASE")}')
    logger.info(f"\tSchema: {vector_store.schema_name}")
    logger.info(f"\tTable: {vector_store.table_name}")
    # logger.info(f"store._is_initialized: {store._is_initialized}")

    # return index.as_chat_engine(similarity_top_k=5)
    # return index.as_chat_engine(chat_mode = ChatMode.REACT, similarity_top_k=5) # ReActAgent  # noqa: E501
    return index.as_chat_engine(chat_mode=ChatMode.CONTEXT, similarity_top_k=5) # ContextChatEngine # noqa: E501
