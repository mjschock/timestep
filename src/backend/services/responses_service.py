# mypy: ignore-errors
import json
import time
import uuid
from typing import Any, Never

from fastapi import HTTPException

from backend._shared.logging_config import logger
from backend.services.chat_service import ChatService


class ResponsesService:
    def _convert_responses_tools_to_chat_completion_tools(
        self, responses_tools: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Convert tools from Responses API format to Chat Completions API format.
        Args:
            responses_tools: Tools in Responses API format (FunctionToolParam)
        Returns:
            Tools in Chat Completions API format (ChatCompletionTool)
        """
        chat_completion_tools = []
        for tool in responses_tools:
            # Responses API format is flattened, Chat Completions API format is nested
            chat_completion_tool = {
                "type": "function",
                "function": {
                    "name": tool.get("name"),
                    "description": tool.get("description", ""),
                    "parameters": tool.get("parameters", {}),
                },
            }
            chat_completion_tools.append(chat_completion_tool)
        return chat_completion_tools

    def _convert_chat_completion_tools_to_responses_tools(
        self, chat_completion_tools: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Convert tools from Chat Completions API format to Responses API format.
        Args:
            chat_completion_tools: Tools in Chat Completions API format (ChatCompletionTool)
        Returns:
            Tools in Responses API format (FunctionToolParam)
        """
        responses_tools = []
        for tool in chat_completion_tools:
            if tool.get("type") == "function" and "function" in tool:
                function_data = tool["function"]
                # Chat Completions API format is nested, Responses API format is flattened
                responses_tool = {
                    "type": "function",
                    "name": function_data.get("name"),
                    "description": function_data.get("description", ""),
                    "parameters": function_data.get("parameters", {}),
                }
                responses_tools.append(responses_tool)
        return responses_tools

    async def create_response(self, response_create_params: dict[str, Any]):
        # Reuse chat completion logic for responses
        logger.info("Creating response")
        chat_service = ChatService()
        stream = response_create_params.get("stream", False)
        
        # Convert responses format to chat completions format
        completion_create_params = self._convert_responses_to_chat_format(response_create_params)
        logger.debug("Converting responses to chat format:")
        logger.debug(
            f"  Original params: {json.dumps(response_create_params, indent=2)}"
        )
        logger.debug(f"  Converted chat params: {json.dumps(completion_create_params, indent=2)}")
        
        if stream:
            from fastapi.responses import StreamingResponse

            return StreamingResponse(
                self._response_event_stream(chat_service, completion_create_params, response_create_params),
                media_type="text/event-stream",
            )
        else:
            chat_result = await chat_service.create_chat_completion(completion_create_params)
            logger.debug("Chat service result:")
            logger.debug(
                f"  Result: {json.dumps(chat_result, indent=2) if chat_result else 'None'}"
            )
            tool_calls = self._extract_tool_calls(chat_result)
            if tool_calls:
                return self._format_tool_call_response(
                    chat_result, completion_create_params, tool_calls, response_create_params
                )
            return self._format_standard_response(chat_result, completion_create_params, response_create_params)

    def _extract_tool_calls(self, chat_result):
        if chat_result and "choices" in chat_result and chat_result["choices"]:
            first_choice = chat_result["choices"][0]
            message = first_choice.get("message", {})
            if "tool_calls" in message and message["tool_calls"]:
                logger.debug(
                    f"Found tool calls: {json.dumps(message['tool_calls'], indent=2)}"
                )
                return message["tool_calls"]
        return None

    def _format_tool_call_response(self, chat_result, completion_create_params, tool_calls, response_create_params):
        usage = chat_result.get("usage", {}) if chat_result else {}
        input_tokens = usage.get("prompt_tokens", 0) if usage else 0
        output_tokens = usage.get("completion_tokens", 0) if usage else 0
        total_tokens = (
            usage.get("total_tokens", input_tokens + output_tokens)
            if usage
            else (input_tokens + output_tokens)
        )
        usage_obj = {
            "input_tokens": input_tokens,
            "input_tokens_details": {
                "audio_tokens": None,
                "cached_tokens": 0,
                "text_tokens": input_tokens,
            },
            "output_tokens": output_tokens,
            "output_tokens_details": {
                "reasoning_tokens": 0,
                "text_tokens": output_tokens,
            },
            "total_tokens": total_tokens,
        }
        assistant_text = None
        if chat_result and "choices" in chat_result and chat_result["choices"]:
            assistant_text = chat_result["choices"][0]["message"]["content"]
        response = {
            "id": f"resp_{uuid.uuid4().hex[:16]}",
            "object": "response",
            "created_at": int(time.time()),
            "model": completion_create_params.get("model", "unknown-model"),
            "status": "completed",
            "parallel_tool_calls": response_create_params.get("parallel_tool_calls", True),
            "tool_choice": response_create_params.get("tool_choice", "auto"),
            "tools": response_create_params.get("tools", []),
            "output": [
                {
                    "id": f"msg_{uuid.uuid4().hex[:16]}",
                    "type": "message",
                    "status": "completed",
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": assistant_text or "",
                            "annotations": [],
                        }
                    ],
                    "tool_calls": tool_calls,
                }
            ],
            "usage": usage_obj,
        }
        return response

    def _format_standard_response(self, chat_result, completion_create_params, response_create_params):
        assistant_text = None
        if chat_result and "choices" in chat_result and chat_result["choices"]:
            assistant_text = chat_result["choices"][0]["message"]["content"]
        usage = chat_result.get("usage", {})
        input_tokens = usage.get("prompt_tokens", 0)
        output_tokens = usage.get("completion_tokens", 0)
        total_tokens = usage.get("total_tokens", input_tokens + output_tokens)
        usage_obj = {
            "input_tokens": input_tokens,
            "input_tokens_details": {
                "audio_tokens": None,
                "cached_tokens": 0,
                "text_tokens": input_tokens,
            },
            "output_tokens": output_tokens,
            "output_tokens_details": {
                "reasoning_tokens": 0,
                "text_tokens": output_tokens,
            },
            "total_tokens": total_tokens,
        }
        response = {
            "id": f"resp_{uuid.uuid4().hex[:16]}",
            "object": "response",
            "created_at": int(time.time()),
            "model": completion_create_params.get("model", "unknown-model"),
            "status": "completed",
            "parallel_tool_calls": response_create_params.get("parallel_tool_calls", True),
            "tool_choice": response_create_params.get("tool_choice", "auto"),
            "tools": response_create_params.get("tools", []),
            "output": [
                {
                    "id": f"msg_{uuid.uuid4().hex[:16]}",
                    "type": "message",
                    "status": "completed",
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": assistant_text or "",
                            "annotations": [],
                        }
                    ],
                }
            ],
            "usage": usage_obj,
        }
        return response

    def _response_event_stream(self, chat_service, completion_create_params, response_create_params):
        async def event_stream():
            # Initialize response parameters
            response_params = self._initialize_response_params(completion_create_params, response_create_params)

            # Send initial events
            yield self._create_response_created_event(response_params)
            yield self._create_response_in_progress_event(response_params)
            yield self._create_output_item_added_event(response_params)
            yield self._create_content_part_added_event(response_params)

            # Stream content
            output_text, tool_calls, content_index = await self._stream_content(
                chat_service, completion_create_params, response_params
            )

            # Send completion events
            yield self._create_output_text_done_event(
                response_params, output_text, content_index
            )
            yield self._create_content_part_done_event(
                response_params, output_text, content_index
            )
            yield self._create_output_item_done_event(
                response_params, output_text, tool_calls
            )
            yield self._create_response_completed_event(
                response_params, output_text, tool_calls
            )

        return event_stream()

    def _initialize_response_params(self, completion_create_params, response_create_params):
        """Initialize response parameters."""
        model_name = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
        if response_create_params and isinstance(response_create_params, dict):
            model_name = response_create_params.get("model", model_name)

        messages = completion_create_params.get("messages", [])
        if not messages:
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What is the capital of France?",
                        }
                    ],
                }
            ]

        response_id = f"resp_{uuid.uuid4().hex[:16]}"
        message_id = f"msg_{uuid.uuid4().hex[:16]}"
        created_at = int(time.time())
        model = model_name

        # Extract tools and tool_choice from the request body
        tools = body.get("tools", []) if body else []
        tool_choice = body.get("tool_choice", "auto") if body else "auto"

        return {
            "response_id": response_id,
            "message_id": message_id,
            "created_at": created_at,
            "model": model,
            "tools": tools,
            "tool_choice": tool_choice,
            "body": body,
        }

    def _create_response_created_event(self, params):
        """Create response.created event."""
        return self._create_response_event(
            "response.created", params, status="in_progress", output=[]
        )

    def _create_response_in_progress_event(self, params):
        """Create response.in_progress event."""
        return self._create_response_event(
            "response.in_progress", params, status="in_progress", output=[]
        )

    def _create_response_event(self, event_type, params, status, output):
        """Create a generic response event."""
        return (
            f"event: {event_type}\ndata: "
            + json.dumps(
                {
                    "type": event_type,
                    "response": self._build_response_data(params, status, output),
                }
            )
            + "\n\n"
        )

    def _build_response_data(self, params, status, output):
        """Build response data structure."""
        return {
            "id": params["response_id"],
            "object": "response",
            "created_at": params["created_at"],
            "status": status,
            "error": None,
            "incomplete_details": None,
            "instructions": params["body"].get(
                "instructions", "You are a helpful assistant."
            )
            if params["body"]
            else "You are a helpful assistant.",
            "model": params["model"],
            "output": output,
            "parallel_tool_calls": False,
            "previous_response_id": None,
            "reasoning": {"effort": None, "summary": None},
            "store": True,
            "temperature": params["body"].get("temperature", 1.0)
            if params["body"]
            else 1.0,
            "text": {"format": {"type": "text"}},
            "tool_choice": params["tool_choice"],
            "tools": params["tools"],
            "top_p": params["body"].get("top_p", 1.0) if params["body"] else 1.0,
            "truncation": "disabled",
            "usage": None,
            "user": None,
            "metadata": {},
        }

    def _create_output_item_added_event(self, params):
        """Create response.output_item.added event."""
        return (
            "event: response.output_item.added\ndata: "
            + json.dumps(
                {
                    "type": "response.output_item.added",
                    "output_index": 0,
                    "item": {
                        "id": params["message_id"],
                        "type": "message",
                        "status": "in_progress",
                        "role": "assistant",
                        "content": [],
                    },
                }
            )
            + "\n\n"
        )

    def _create_content_part_added_event(self, params):
        """Create response.content_part.added event."""
        return (
            "event: response.content_part.added\ndata: "
            + json.dumps(
                {
                    "type": "response.content_part.added",
                    "item_id": params["message_id"],
                    "output_index": 0,
                    "content_index": 0,
                    "part": {
                        "type": "output_text",
                        "text": "",
                        "annotations": [],
                    },
                }
            )
            + "\n\n"
        )

    async def _stream_content(self, chat_service, completion_create_params, params):
        """Stream content from chat service."""
        content_index = 0
        output_text = ""
        tool_calls = []

        # Get the streaming response from chat service for text streaming
        streaming_response = await chat_service.create_chat_completion(completion_create_params)

        # Stream through the chat service's streaming response for text content
        if hasattr(streaming_response, "body_iterator"):
            async for chunk in streaming_response.body_iterator:
                if chunk:
                    chunk_str = self._decode_chunk(chunk)
                    if chunk_str.startswith("data: "):
                        result = await self._process_chunk_data(
                            chunk_str, params, content_index, output_text, tool_calls
                        )
                        if result is None:  # [DONE] signal
                            break
                        content_index, output_text, tool_calls = result

        return output_text, tool_calls, content_index

    def _create_delta_event(self, params, token, content_index):
        """Create delta event for streaming text."""
        return (
            "event: response.output_text.delta\ndata: "
            + json.dumps(
                {
                    "type": "response.output_text.delta",
                    "item_id": params["message_id"],
                    "output_index": 0,
                    "content_index": content_index,
                    "delta": {
                        "type": "output_text",
                        "text": token,
                        "annotations": [],
                    },
                }
            )
            + "\n\n"
        )

    def _decode_chunk(self, chunk):
        """Decode chunk to string."""
        return chunk.decode("utf-8") if isinstance(chunk, bytes) else str(chunk)

    async def _process_chunk_data(
        self, chunk_str, params, content_index, output_text, tool_calls
    ):
        """Process chunk data and return updated state."""
        try:
            data_str = chunk_str[6:]  # Remove 'data: ' prefix
            if data_str.strip() == "[DONE]":
                return None  # Signal to break

            data = json.loads(data_str)
            return await self._extract_delta_content(
                data, params, content_index, output_text, tool_calls
            )

        except json.JSONDecodeError:
            # Skip non-JSON chunks
            return content_index, output_text, tool_calls

    async def _extract_delta_content(
        self, data, params, content_index, output_text, tool_calls
    ):
        """Extract delta content from chat completion data."""
        if "choices" not in data or not data["choices"]:
            return content_index, output_text, tool_calls

        choice = data["choices"][0]
        if "delta" not in choice:
            return content_index, output_text, tool_calls

        delta = choice["delta"]

        # Handle text content
        if "content" in delta and delta["content"]:
            content_index, output_text = await self._handle_text_content(
                delta["content"], params, content_index, output_text
            )

        # Handle tool calls in the delta (usually in final chunk)
        if "tool_calls" in delta and delta["tool_calls"]:
            tool_calls = delta["tool_calls"]
            logger.debug(
                f"Found tool calls in streaming delta: {json.dumps(tool_calls, indent=2)}"
            )

        return content_index, output_text, tool_calls

    async def _handle_text_content(self, token, params, content_index, output_text):
        """Handle text content from delta."""
        output_text += token
        content_index += 1
        return content_index, output_text

    def _create_output_text_done_event(self, params, output_text, content_index):
        """Create response.output_text.done event."""
        return (
            "event: response.output_text.done\ndata: "
            + json.dumps(
                {
                    "type": "response.output_text.done",
                    "item_id": params["message_id"],
                    "output_index": 0,
                    "content_index": max(content_index - 1, 0),
                    "text": output_text,
                }
            )
            + "\n\n"
        )

    def _create_content_part_done_event(self, params, output_text, content_index):
        """Create response.content_part.done event."""
        return (
            "event: response.content_part.done\ndata: "
            + json.dumps(
                {
                    "type": "response.content_part.done",
                    "item_id": params["message_id"],
                    "output_index": 0,
                    "content_index": max(content_index - 1, 0),
                    "part": {
                        "type": "output_text",
                        "text": output_text,
                        "annotations": [],
                    },
                }
            )
            + "\n\n"
        )

    def _create_output_item_done_event(self, params, output_text, tool_calls):
        """Create response.output_item.done event."""
        item_data = {
            "id": params["message_id"],
            "type": "message",
            "status": "completed",
            "role": "assistant",
            "content": [
                {
                    "type": "output_text",
                    "text": output_text,
                    "annotations": [],
                }
            ],
        }
        # Add tool calls if present
        if tool_calls:
            item_data["tool_calls"] = tool_calls

        return (
            "event: response.output_item.done\ndata: "
            + json.dumps(
                {
                    "type": "response.output_item.done",
                    "output_index": 0,
                    "item": item_data,
                }
            )
            + "\n\n"
        )

    def _create_response_completed_event(self, params, output_text, tool_calls):
        """Create response.completed event."""
        # Note: usage_obj is defined but not used in current implementation
        # TODO: Implement usage tracking if needed
        # usage_obj = {
        #     "input_tokens": 0,
        #     "input_tokens_details": {
        #         "audio_tokens": None,
        #         "cached_tokens": 0,
        #         "text_tokens": None,
        #     },
        #     "output_tokens": 0,
        #     "output_tokens_details": {
        #         "reasoning_tokens": 0,
        #         "text_tokens": None,
        #     },
        #     "total_tokens": 0,
        # }

        response_output = [
            {
                "id": params["message_id"],
                "type": "message",
                "status": "completed",
                "role": "assistant",
                "content": [
                    {
                        "type": "output_text",
                        "text": output_text,
                        "annotations": [],
                    }
                ],
            }
        ]
        # Add tool calls if present
        if tool_calls:
            response_output[0]["tool_calls"] = tool_calls

        return (
            "event: response.completed\ndata: "
            + json.dumps(
                {
                    "type": "response.completed",
                    "response": self._build_response_data(
                        params, "completed", response_output
                    ),
                }
            )
            + "\n\n"
        )

    def get_response(self, response_id, include, stream, starting_after) -> Never:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_response(self, response_id) -> Never:
        raise HTTPException(status_code=501, detail="Not implemented")

    def cancel_response(self, response_id) -> Never:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_input_items(
        self, response_id, limit, order, after, before, include
    ) -> Never:
        raise HTTPException(status_code=501, detail="Not implemented")

    def _convert_responses_to_chat_format(self, body):
        """Convert responses API format to chat completions format."""
        if not body or not isinstance(body, dict):
            return {"messages": []}

        chat_body = self._copy_common_fields(body)
        messages = self._convert_input_to_messages(body)
        messages = self._add_instructions_as_system_message(body, messages)

        chat_body["messages"] = messages
        return chat_body

    def _copy_common_fields(self, body):
        """Copy common fields from body to chat_body."""
        chat_body = {}
        common_fields = [
            "model",
            "stream",
            "temperature",
            "top_p",
            "max_tokens",
            "tool_choice",
        ]

        for field in common_fields:
            if field in body:
                chat_body[field] = body[field]

        # Handle tools separately for format conversion
        if "tools" in body and body["tools"]:
            # Convert from Responses API format (flattened) to Chat Completions API format (nested)
            chat_body["tools"] = self._convert_responses_tools_to_chat_completion_tools(
                body["tools"]
            )

        return chat_body

    def _convert_input_to_messages(self, body):
        """Convert different input formats to messages."""
        if "messages" in body:
            return body["messages"]
        elif "input" in body:
            return self._convert_input_data_to_messages(body["input"])
        elif "prompt" in body:
            return [{"role": "user", "content": body["prompt"]}]
        else:
            return []

    def _convert_input_data_to_messages(self, input_data):
        """Convert input data to messages format."""
        if isinstance(input_data, list):
            return self._convert_input_list_to_messages(input_data)
        elif isinstance(input_data, str):
            return [{"role": "user", "content": input_data}]
        else:
            return []

    def _convert_input_list_to_messages(self, input_data):
        """Convert input list to messages."""
        messages = []
        for item in input_data:
            if isinstance(item, dict):
                if "type" in item and item["type"] == "text":
                    messages.append({"role": "user", "content": item.get("text", "")})
                elif "role" in item and "content" in item:
                    messages.append(item)
        return messages

    def _add_instructions_as_system_message(self, body, messages):
        """Add instructions as system message if present."""
        if "instructions" in body and body["instructions"]:
            messages.insert(0, {"role": "system", "content": body["instructions"]})
        return messages
