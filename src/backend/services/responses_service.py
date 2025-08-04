# mypy: ignore-errors
import json
import sys
import time
import uuid
from typing import Any, Never

from fastapi import HTTPException

from backend._shared.dao.response_dao import ResponseDAO
from backend._shared.database import get_session
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
        logger.debug("=== RESPONSES SERVICE DEBUG ===")
        logger.debug(f"  Input params: {json.dumps(response_create_params, indent=2)}")

        chat_service = ChatService()
        stream = response_create_params.get("stream", False)
        logger.debug(f"  Stream: {stream}")

        # Convert responses format to chat completions format
        logger.debug("  Converting responses to chat format...")
        completion_create_params = self._convert_responses_to_chat_format(
            response_create_params
        )
        logger.debug("Converting responses to chat format:")
        logger.debug(
            f"  Original params: {json.dumps(response_create_params, indent=2)}"
        )
        logger.debug(
            f"  Converted chat params: {json.dumps(completion_create_params, indent=2)}"
        )

        if stream:
            from fastapi.responses import StreamingResponse

            return StreamingResponse(
                self._stream_response_events(
                    chat_service, completion_create_params, response_create_params
                ),
                media_type="text/event-stream",
            )

        else:
            chat_result = await chat_service.create_chat_completion(
                completion_create_params
            )
            logger.debug("=== CHAT SERVICE RESULT ===")
            logger.debug(
                f"  Raw result: {json.dumps(chat_result, indent=2) if chat_result else 'None'}"
            )

            # Debug: Extract and log key parts
            if chat_result and "choices" in chat_result and chat_result["choices"]:
                first_choice = chat_result["choices"][0]
                message = first_choice.get("message", {})
                content = message.get("content", "")
                tool_calls = message.get("tool_calls", [])
                logger.debug(f"  Content: '{content}'")
                logger.debug(f"  Tool calls: {json.dumps(tool_calls, indent=2)}")
                logger.debug(f"  Message keys: {list(message.keys())}")
            else:
                logger.debug("  No choices found in chat result")

            # Create response and store in database
            response_data = self._create_simple_response(
                chat_result, response_create_params
            )

            # Store in database
            with get_session() as session:
                response_dao = ResponseDAO(session)
                stored_response = response_dao.create_response(response_data)
                logger.debug(
                    f"  Stored response in database with ID: {stored_response.id}"
                )

            return response_data

    def _create_simple_response(self, chat_result, response_create_params):
        """Create a simple responses API response from chat result."""
        logger.debug("=== CREATING SIMPLE RESPONSE ===")

        # Extract content and tool calls
        content = ""
        tool_calls = []
        usage = {}

        if chat_result and "choices" in chat_result and chat_result["choices"]:
            first_choice = chat_result["choices"][0]
            message = first_choice.get("message", {})
            content = message.get("content", "")
            tool_calls = message.get("tool_calls", [])
            usage = chat_result.get("usage", {})
            logger.debug(f"  Extracted content: '{content}'")
            logger.debug(f"  Extracted tool calls: {json.dumps(tool_calls, indent=2)}")

        # Ensure content is a string, not None
        if content is None:
            content = ""

        # Create usage object
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

        # Create response
        response = {
            "id": f"resp_{uuid.uuid4().hex[:16]}",
            "object": "response",
            "created_at": int(time.time()),
            "model": response_create_params.get("model", "unknown-model"),
            "status": "completed",
            "parallel_tool_calls": response_create_params.get(
                "parallel_tool_calls", True
            ),
            "tool_choice": response_create_params.get("tool_choice", "auto"),
            "tools": response_create_params.get("tools", []),
            "previous_response_id": response_create_params.get("previous_response_id"),
            "output": [],
            "usage": usage_obj,
        }

        # Add message output if there's content
        if content:
            response["output"].append(
                {
                    "id": f"msg_{uuid.uuid4().hex[:16]}",
                    "type": "message",
                    "status": "completed",
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": content,
                            "annotations": [],
                        }
                    ],
                }
            )

        # Add tool calls as proper ResponseFunctionToolCall format
        for tool_call in tool_calls:
            response["output"].append(
                {
                    "type": "function_call",
                    "call_id": tool_call.get("id", f"call_{uuid.uuid4().hex[:16]}"),
                    "name": tool_call["function"]["name"],
                    "arguments": tool_call["function"]["arguments"],
                    "status": "incomplete",
                }
            )

        logger.debug(f"  Final response: {json.dumps(response, indent=2)}")
        return response

    def get_response(
        self, response_id: str, include: list[str], stream: str, starting_after: str
    ) -> dict:
        """Get a response by its ID."""
        logger.info(f"Getting response with ID: {response_id}")

        with get_session() as session:
            response_dao = ResponseDAO(session)
            response = response_dao.get_response_by_id(response_id)

            if not response:
                raise HTTPException(
                    status_code=404, detail=f"Response with ID {response_id} not found"
                )

            return response.to_dict()

    def delete_response(self, response_id: str) -> dict:
        """Delete a response by its ID."""
        logger.info(f"Deleting response with ID: {response_id}")

        with get_session() as session:
            response_dao = ResponseDAO(session)
            success = response_dao.delete_response(response_id)

            if not success:
                raise HTTPException(
                    status_code=404, detail=f"Response with ID {response_id} not found"
                )

            return {"id": response_id, "object": "response", "deleted": True}

    def cancel_response(self, response_id) -> Never:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_input_items(
        self, response_id, limit, order, after, before, include
    ) -> Never:
        raise HTTPException(status_code=501, detail="Not implemented")

    def _convert_responses_to_chat_format(self, body):
        """Convert responses API format to chat completions format."""
        logger.debug("  _convert_responses_to_chat_format called")
        logger.debug(f"    Input body: {json.dumps(body, indent=2)}")

        if not body or not isinstance(body, dict):
            logger.debug("    Body is empty or not dict, returning empty messages")
            return {"messages": []}

        chat_body = self._copy_common_fields(body)
        logger.debug(f"    Common fields: {json.dumps(chat_body, indent=2)}")

        messages = self._convert_input_to_messages(body)
        logger.debug(f"    Converted messages: {json.dumps(messages, indent=2)}")

        messages = self._add_instructions_as_system_message(body, messages)
        logger.debug(
            f"    Messages with instructions: {json.dumps(messages, indent=2)}"
        )

        chat_body["messages"] = messages
        logger.debug(f"    Final chat body: {json.dumps(chat_body, indent=2)}")
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
                    # Handle responses API format where content can be a list or string
                    content = item["content"]
                    if isinstance(content, list):
                        # Extract text from content list (responses API format)
                        text_parts = []
                        for content_item in content:
                            if (
                                isinstance(content_item, dict)
                                and content_item.get("type") == "output_text"
                            ):
                                text_parts.append(content_item.get("text", ""))
                        content = "".join(text_parts)
                    messages.append({"role": item["role"], "content": content})
        return messages

    def _add_instructions_as_system_message(self, body, messages):
        """Add instructions as system message if present."""
        if "instructions" in body and body["instructions"]:
            messages.insert(0, {"role": "system", "content": body["instructions"]})
        return messages

    async def _stream_response_events(
        self, chat_service, completion_create_params, response_create_params
    ):
        """Stream response events by delegating to chat service and converting format."""
        # Initialize response parameters
        response_id = f"resp_{uuid.uuid4().hex[:16]}"
        message_id = f"msg_{uuid.uuid4().hex[:16]}"
        created_at = int(time.time())

        print(
            f"[DEBUG] Streaming: response_id={response_id}, message_id={message_id}",
            file=sys.stderr,
        )
        yield self._create_response_created_event(
            response_id, created_at, response_create_params
        )
        yield self._create_response_in_progress_event(
            response_id, created_at, response_create_params
        )
        yield self._create_output_item_added_event(message_id)
        yield self._create_content_part_added_event(message_id)

        # Get streaming response from chat service
        streaming_response = await chat_service.create_chat_completion(
            completion_create_params
        )

        # Process the chat completions stream and convert to responses API format
        output_text = ""
        tool_calls = []

        if hasattr(streaming_response, "body_iterator"):
            async for chunk in streaming_response.body_iterator:
                print(f"[DEBUG] Received chunk: {chunk}", file=sys.stderr)
                if chunk:
                    chunk_str = self._decode_chunk(chunk)
                    if chunk_str.startswith("data: "):
                        data_str = chunk_str[6:]  # Remove 'data: ' prefix
                        if data_str.strip() == "[DONE]":
                            print("[DEBUG] Received [DONE] chunk", file=sys.stderr)
                            break

                        try:
                            data = json.loads(data_str)
                            print(f"[DEBUG] Decoded data: {data}", file=sys.stderr)
                            if "choices" in data and data["choices"]:
                                choice = data["choices"][0]
                                delta = choice.get("delta", {})

                                # Handle content tokens
                                if "content" in delta and delta["content"]:
                                    token = delta["content"]
                                    output_text += token
                                    print(
                                        f"[DEBUG] Accumulated token: '{token}', output_text now: '{output_text}'",
                                        file=sys.stderr,
                                    )
                                    # Send delta event for content
                                    yield self._create_delta_event(message_id, token)

                                # Handle tool calls
                                if "tool_calls" in delta and delta["tool_calls"]:
                                    print(
                                        f"[DEBUG] Tool calls found: {delta['tool_calls']}",
                                        file=sys.stderr,
                                    )
                                    if isinstance(delta["tool_calls"], list):
                                        tool_calls.extend(delta["tool_calls"])
                                    else:
                                        tool_calls.append(delta["tool_calls"])

                                    # Yield function_call events for each tool call
                                    for tool_call in delta["tool_calls"]:
                                        if (
                                            isinstance(tool_call, dict)
                                            and "function" in tool_call
                                        ):
                                            function_call_event = {
                                                "type": "function_call",
                                                "call_id": tool_call.get(
                                                    "id",
                                                    f"call_{uuid.uuid4().hex[:16]}",
                                                ),
                                                "name": tool_call["function"]["name"],
                                                "arguments": tool_call["function"][
                                                    "arguments"
                                                ],
                                                "status": "incomplete",
                                            }
                                            yield f"event: response.function_call\ndata: {json.dumps({'type': 'response.function_call', 'function_call': function_call_event})}\n\n"

                        except json.JSONDecodeError:
                            print(
                                "[DEBUG] Skipping invalid JSON chunk", file=sys.stderr
                            )
                            continue  # Skip invalid JSON

        print(f"[DEBUG] Final output_text: '{output_text}'", file=sys.stderr)
        print(f"[DEBUG] Final tool_calls: {tool_calls}", file=sys.stderr)
        # Send completion events
        yield self._create_output_text_done_event(message_id, output_text)
        yield self._create_content_part_done_event(message_id, output_text)
        yield self._create_output_item_done_event(message_id, output_text, tool_calls)
        yield self._create_response_completed_event(
            response_id, output_text, tool_calls
        )

    def _create_response_created_event(
        self, response_id, created_at, response_create_params
    ):
        """Create response.created event."""
        return f"event: response.created\ndata: {json.dumps({'type': 'response.created', 'response': {'id': response_id, 'created_at': created_at, 'model': response_create_params.get('model', 'unknown'), 'status': 'in_progress'}})}\n\n"

    def _create_response_in_progress_event(
        self, response_id, created_at, response_create_params
    ):
        """Create response.in_progress event."""
        return f"event: response.in_progress\ndata: {json.dumps({'type': 'response.in_progress', 'response': {'id': response_id, 'created_at': created_at, 'model': response_create_params.get('model', 'unknown'), 'status': 'in_progress'}})}\n\n"

    def _create_output_item_added_event(self, message_id):
        """Create response.output_item.added event."""
        return f"event: response.output_item.added\ndata: {json.dumps({'type': 'response.output_item.added', 'output_index': 0, 'item': {'id': message_id, 'type': 'message', 'role': 'assistant', 'status': 'in_progress'}})}\n\n"

    def _create_content_part_added_event(self, message_id):
        """Create response.content_part.added event."""
        return f"event: response.content_part.added\ndata: {json.dumps({'type': 'response.content_part.added', 'output_index': 0, 'item_id': message_id, 'content_index': 0, 'part': {'type': 'output_text', 'text': '', 'annotations': []}})}\n\n"

    def _create_delta_event(self, message_id, token):
        """Create response.output_text.delta event."""
        return f"event: response.output_text.delta\ndata: {json.dumps({'type': 'response.output_text.delta', 'output_index': 0, 'item_id': message_id, 'content_index': 0, 'delta': {'type': 'output_text', 'text': token, 'annotations': []}})}\n\n"

    def _create_output_text_done_event(self, message_id, output_text):
        """Create response.output_text.done event."""
        return f"event: response.output_text.done\ndata: {json.dumps({'type': 'response.output_text.done', 'output_index': 0, 'item_id': message_id, 'content_index': 0, 'text': output_text})}\n\n"

    def _create_content_part_done_event(self, message_id, output_text):
        """Create response.content_part.done event."""
        return f"event: response.content_part.done\ndata: {json.dumps({'type': 'response.content_part.done', 'output_index': 0, 'item_id': message_id, 'content_index': 0, 'part': {'type': 'output_text', 'text': output_text, 'annotations': []}})}\n\n"

    def _create_output_item_done_event(self, message_id, output_text, tool_calls):
        """Create response.output_item.done event."""
        item_data = {
            "id": message_id,
            "type": "message",
            "status": "completed",
            "role": "assistant",
            "content": [
                {"type": "output_text", "text": output_text, "annotations": []}
            ],
        }

        # Add tool calls if present
        if tool_calls:
            item_data["tool_calls"] = tool_calls

        return f"event: response.output_item.done\ndata: {json.dumps({'type': 'response.output_item.done', 'output_index': 0, 'item': item_data})}\n\n"

    def _create_response_completed_event(self, response_id, output_text, tool_calls):
        """Create response.completed event."""
        response_data = {
            "id": response_id,
            "object": "response",
            "created_at": int(time.time()),
            "status": "completed",
            "output": [
                {
                    "id": f"msg_{uuid.uuid4().hex[:16]}",
                    "type": "message",
                    "status": "completed",
                    "role": "assistant",
                    "content": [
                        {"type": "output_text", "text": output_text, "annotations": []}
                    ],
                }
            ],
        }

        # Add tool calls as proper ResponseFunctionToolCall format
        if tool_calls:
            for tool_call in tool_calls:
                response_data["output"].append(
                    {
                        "type": "function_call",
                        "call_id": tool_call.get("id", f"call_{uuid.uuid4().hex[:16]}"),
                        "name": tool_call["function"]["name"],
                        "arguments": tool_call["function"]["arguments"],
                        "status": "incomplete",
                    }
                )

        return f"event: response.completed\ndata: {json.dumps({'type': 'response.completed', 'response': response_data})}\n\n"

    def _decode_chunk(self, chunk):
        """Decode chunk to string."""
        return chunk.decode("utf-8") if isinstance(chunk, bytes) else str(chunk)
