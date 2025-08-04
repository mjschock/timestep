# mypy: ignore-errors
import json
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
            raise NotImplementedError("TODO: Streaming through the chat service, converting the stream to the responses API format")

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
                    messages.append(item)
        return messages

    def _add_instructions_as_system_message(self, body, messages):
        """Add instructions as system message if present."""
        if "instructions" in body and body["instructions"]:
            messages.insert(0, {"role": "system", "content": body["instructions"]})
        return messages
