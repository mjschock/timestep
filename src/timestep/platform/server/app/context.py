import logging
import os
from typing import Optional

from llama_index import BasePromptTemplate, ServiceContext
from llama_index.callbacks import CallbackManager
from llama_index.llms import OpenAI
from llama_index.multi_modal_llms import OpenAIMultiModal
from llama_index.types import (
    PydanticProgramMode,
)
from pydantic import Field

logger = logging.getLogger("uvicorn")

def create_base_context():
    model = os.getenv("MODEL", "gpt-3.5-turbo")
    logger.info(f"model: {model}")
    assert model == "gpt-4-vision-preview", f"{model} != gpt-4-vision-preview"

    llm = OpenAI(model=model)
    mm_llm = OpenAIMultiModal(model="gpt-4-vision-preview", max_new_tokens=1000)

    class OpenAIMultiModalExtended(OpenAIMultiModal):
        callback_manager: Optional[CallbackManager] = None,
        pydantic_program_mode: PydanticProgramMode = PydanticProgramMode.DEFAULT
        # deprecated
        query_wrapper_prompt: Optional[BasePromptTemplate] = Field(
            description="Query wrapper prompt for LLM calls.",
            default=None,
            exclude=True,
        )
        system_prompt: Optional[str] = Field(
            default=None, description="System prompt for LLM calls."
        )

    lmm = OpenAIMultiModalExtended(model="gpt-4-vision-preview", max_new_tokens=1000)

    # react_step_engine = MultimodalReActAgentWorker.from_tools(
    #     [query_tool],
    #     # [],
    #     multi_modal_llm=mm_llm,
    #     verbose=True,
    # )
    # agent = AgentRunner(react_step_engine)

    return ServiceContext.from_defaults(
        # llm=llm,
        # llm=mm_llm,
        llm=lmm,
    )
