import logging
from typing import Any, Optional, Sequence

import torch
from llama_index.bridge.pydantic import Field
from llama_index.constants import (
    DEFAULT_TEMPERATURE,
)
from llama_index.core.llms.types import (
    ChatMessage,
    ChatResponse,
    ChatResponseAsyncGen,
    ChatResponseGen,
    CompletionResponse,
    CompletionResponseAsyncGen,
    CompletionResponseGen,
)
from llama_index.llms import HuggingFaceLLM
from llama_index.llms.openai_utils import (
    from_openai_message,
    to_openai_message_dicts,
)
from llama_index.multi_modal_llms import MultiModalLLM, MultiModalLLMMetadata
from llama_index.prompts import PromptTemplate
from llama_index.schema import ImageDocument
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    LocalAgent,
)

logger = logging.getLogger(__name__)


class HuggingFaceMultiModalLLM(MultiModalLLM):
    """Hugging Face Multi-Modal LLM interface."""

    checkpoint: str = Field(description="The Hugging Face checkpoint to use.")
    # model: str = Field(description="The Multi-Modal model to use from OpenAI.")
    # model: Optional[Any] = Field(description="The Multi-Modal model to use from Hugging Face.")
    # tokenizer: Optional[Any] = Field(description="The Multi-Modal tokenizer to use from Hugging Face.")
    # llm: Optional[HuggingFaceLLM] = Field(description="The Hugging Face LLM to use.")
    # temperature: float = Field(description="The temperature to use for sampling.")
    # max_new_tokens: Optional[int] = Field(
    #     description=" The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt",
    #     gt=0,
    # )
    # additional_kwargs: dict[str, Any] = Field(
    #     default_factory=dict, description="Additional kwargs for the OpenAI API."
    # )

    def __init__(
        self,
        checkpoint: str,
        # model: str = "gpt-4-vision-preview",
        # model: Optional[Any] = None,
        # tokenizer: Optional[Any] = None,
        # temperature: float = DEFAULT_TEMPERATURE,
        # max_new_tokens: Optional[int] = 300,
        # additional_kwargs: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            checkpoint=checkpoint,
            # model=model,
            # tokenizer=tokenizer,
            # temperature=temperature,
            # max_new_tokens=max_new_tokens,
            # additional_kwargs=additional_kwargs or {},
            **kwargs,
        )

        # SYSTEM_PROMPT = """You are an AI assistant that answers questions in a friendly manner, based on the given source documents. Here are some rules you always follow:
        # - Generate human readable output, avoid creating output with gibberish text.
        # - Generate only the requested output, don't include any other language before or after the requested output.
        # - Never say thank you, that you are happy to help, that you are an AI agent, etc. Just answer directly.
        # - Generate professional language typically used in business documents in North America.
        # - Never generate offensive or foul language.
        # """  # noqa: E501, N806

        # query_wrapper_prompt = PromptTemplate(
        #     "[INST]<<SYS>>\n" + SYSTEM_PROMPT + "<</SYS>>\n\n{query_str}[/INST] "
        # )

        # self.llm = HuggingFaceLLM(
        #     model=model,
        #     tokenizer=tokenizer,
        #     max_new_tokens=max_new_tokens,
        #     # context_window
        #     is_chat_model=True,
        #     # **kwargs,
        # )

        model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)  # noqa: E501
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)

        self.agent = LocalAgent(model, tokenizer)

        # self.llm = HuggingFaceLLM(
        #     model_name=checkpoint,
        #     tokenizer_name=checkpoint,
        #     # context_window=4096,
        #     # max_new_tokens=2048,
        #     # generate_kwargs={"temperature": 0.0, "do_sample": False},
        #     # query_wrapper_prompt=query_wrapper_prompt,
        #     # tokenizer_name=checkpoint,
        #     # model_name=checkpoint,
        #     # device_map="auto",
        #     # change these settings below depending on your GPU
        #     # model_kwargs={"torch_dtype": torch.float16, "load_in_8bit": True},
        # )

    class Config:
        arbitrary_types_allowed = True

    @property
    def metadata(self) -> MultiModalLLMMetadata:
        """Multi-Modal LLM metadata."""

    # def _get_model_kwargs(self, **kwargs: Any) -> dict[str, Any]:
    #     base_kwargs = {"model": self.model, "temperature": self.temperature, **kwargs}

    #     if self.max_new_tokens is not None:
    #         # If max_tokens is None, don't include in the payload:
    #         # https://platform.openai.com/docs/api-reference/chat
    #         # https://platform.openai.com/docs/api-reference/completions
    #         base_kwargs["max_tokens"] = self.max_new_tokens

    #     return {**base_kwargs, **self.additional_kwargs}

    # def _get_response_token_counts(self, raw_response: Any) -> dict:
    #     """Get the token usage reported by the response."""
    #     if not isinstance(raw_response, dict):
    #         return {}

    #     usage = raw_response.get("usage", {})
    #     # NOTE: other model providers that use the OpenAI client may not report usage
    #     if usage is None:
    #         return {}

    #     return {
    #         "prompt_tokens": usage.get("prompt_tokens", 0),
    #         "completion_tokens": usage.get("completion_tokens", 0),
    #         "total_tokens": usage.get("total_tokens", 0),
    #     }

    def complete(
        self, prompt: str, image_documents: Sequence[ImageDocument], **kwargs: Any
    ) -> CompletionResponse:
        """Completion endpoint for Multi-Modal LLM."""

    def stream_complete(
        self, prompt: str, image_documents: Sequence[ImageDocument], **kwargs: Any
    ) -> CompletionResponseGen:
        """Streaming completion endpoint for Multi-Modal LLM."""

    def chat(
        self,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> ChatResponse:
        """Chat endpoint for Multi-Modal LLM."""

        logger.info("Chatting with LLM...")
        logger.info(f"Chat messages: {messages}")
        print(f"Chat messages: {messages}")
        print('kwargs: ', kwargs)

        return self.llm.chat(messages, **kwargs)

        # all_kwargs = self._get_model_kwargs(**kwargs)
        # message_dicts = to_openai_message_dicts(messages)
        # # response = self._client.chat.completions.create(
        # #     messages=message_dicts,
        # #     stream=False,
        # #     **all_kwargs,
        # # )
        # print('all_kwargs:', all_kwargs)
        # print('message_dicts:', message_dicts)

        # response = self.llm.complete(
        #     prompt=message_dicts,
        #     # image_documents=image_documents, # TODO: add image_documents
        #     stream=False,
        #     **all_kwargs,
        # )

        # openai_message = response.choices[0].message
        # message = from_openai_message(openai_message)

        # return ChatResponse(
        #     message=message,
        #     raw=response,
        #     delta=None,
        #     additional_kwargs=self._get_response_token_counts(response),
        # )

    def stream_chat(
        self,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> ChatResponseGen:
        """Stream chat endpoint for Multi-Modal LLM."""

    # ===== Async Endpoints =====

    async def acomplete(
        self, prompt: str, image_documents: Sequence[ImageDocument], **kwargs: Any
    ) -> CompletionResponse:
        """Async completion endpoint for Multi-Modal LLM."""

    async def astream_complete(
        self, prompt: str, image_documents: Sequence[ImageDocument], **kwargs: Any
    ) -> CompletionResponseAsyncGen:
        """Async streaming completion endpoint for Multi-Modal LLM."""

    async def achat(
        self,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> ChatResponse:
        """Async chat endpoint for Multi-Modal LLM."""

    async def astream_chat(
        self,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> ChatResponseAsyncGen:
        """Async streaming chat endpoint for Multi-Modal LLM."""
