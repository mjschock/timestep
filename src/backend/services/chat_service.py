# mypy: ignore-errors
import json
import pprint
import time
import uuid
from typing import Any

import torch
from datasets import Dataset, DatasetDict
from fastapi import HTTPException

from backend._shared.logging_config import logger
from backend._shared.utils.model_utils import (
    prepare_model_inputs,
    process_model_inputs,
    process_model_outputs,
)
from backend.services.models_service import get_models_service


class ChatService:
    # Class-level storage for chat completions to persist across instances
    _stored_completions: dict[str, dict[str, Any]] = {} # TODO: Persist to DB

    def _create_non_streaming_response_from_model_utils(
        self,
        results,
        model_name,
        max_tokens,
        temperature,
        top_p,
        n,
        stop,
        user,
    ):
        """Create a non-streaming response from model_utils results."""
        # Get the response text from model_utils
        response_text = results.get("response", "")

        # Parse tool calls from the response text
        tool_calls = self._parse_tool_calls_from_text(response_text)

        # Create the message
        message = {
            "role": "assistant",
        }

        # According to OpenAI spec: when tool_calls are present, content should be null
        if tool_calls:
            message["tool_calls"] = tool_calls
            message["content"] = None
        else:
            message["content"] = response_text

        # Create choice
        choice = {
            "index": 0,
            "message": message,
            "finish_reason": "stop",
        }

        # Calculate usage (simplified - model_utils doesn't return detailed usage info yet)
        usage = {
            "prompt_tokens": 0,  # TODO: Get from model_utils if needed
            "completion_tokens": len(response_text.split()) if response_text else 0,
            "total_tokens": len(response_text.split()) if response_text else 0,
        }

        # Build final response
        return self._build_non_streaming_response(model_name, [choice], usage)

    def _create_streaming_response_from_model_utils(
        self,
        results,
        model_name,
        max_tokens,
        temperature,
        top_p,
        stop,
        logprobs=False,
        top_logprobs=5,
        tool_choice=None,
        tools=None,
    ):
        """Create a streaming response from model_utils results."""
        from fastapi.responses import StreamingResponse

        # Get the response stream from model_utils
        response_stream = results.get("response_stream")

        return StreamingResponse(
            self._streaming_event_generator_from_model_utils(
                response_stream,
                model_name,
                logprobs,
                tool_choice,
                tools,
            ),
            media_type="text/event-stream",
        )

    def _streaming_event_generator_from_model_utils(
        self,
        response_stream,
        model_name,
        logprobs,
        tool_choice,
        tools,
    ):
        """Generate streaming events from model_utils response stream."""
        generated_text = ""

        # Stream tokens from model_utils TextIteratorStreamer
        for token in response_stream:
            if token:
                generated_text += token
                yield self._create_token_chunk(token, model_name, logprobs)

        # Handle tool choice fallback if needed
        tool_calls = self._handle_streaming_tool_choice_fallback(
            generated_text, tool_choice, tools
        )

        # Send final chunk
        yield self._create_final_chunk(model_name, tool_calls)
        yield "data: [DONE]\n\n"

    def list_chat_completions(
        self, model=None, metadata=None, after=None, limit=None, order=None
    ):
        """List stored Chat Completions."""
        try:
            # Filter stored completions
            completions = list(self._stored_completions.values())

            # Apply filters
            if model:
                completions = [c for c in completions if c.get("model") == model]

            if metadata:
                # Simple metadata filtering - could be enhanced
                completions = [
                    c for c in completions if metadata in str(c.get("metadata", ""))
                ]

            if after:
                # Filter by creation time after the specified timestamp
                try:
                    after_time = int(after)
                    completions = [
                        c for c in completions if c.get("created", 0) > after_time
                    ]
                except ValueError:
                    pass

            # Apply ordering
            if order == "desc":
                completions.sort(key=lambda x: x.get("created", 0), reverse=True)
            else:
                completions.sort(key=lambda x: x.get("created", 0))

            # Apply limit
            if limit:
                try:
                    limit_int = int(limit)
                    completions = completions[:limit_int]
                except ValueError:
                    pass

            return {
                "object": "list",
                "data": completions,
                "first_id": completions[0]["id"] if completions else None,
                "last_id": completions[-1]["id"] if completions else None,
                "has_more": False,  # Simple implementation
            }
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to list chat completions: {str(e)}"
            ) from e

    async def create_chat_completion(self, completion_create_params: dict[str, Any]):
        """Creates a model response for the given chat conversation."""
        try:
            logger.info("create_chat_completion called!")
            logger.debug(f"Request params:\n{pprint.pformat(completion_create_params, width=100)}")

            # Extract parameters directly from validated OpenAI request
            model_name = completion_create_params.get("model", "HuggingFaceTB/SmolVLM2-256M-Video-Instruct")
            messages = completion_create_params["messages"]
            stream = completion_create_params.get("stream", False)
            max_tokens = completion_create_params.get("max_tokens", 100)
            temperature = completion_create_params.get("temperature", 1.0)
            top_p = completion_create_params.get("top_p", 1.0)
            n = completion_create_params.get("n", 1)
            stop = completion_create_params.get("stop", None)
            tools = completion_create_params.get("tools", [])
            tool_choice = completion_create_params.get("tool_choice", None)
            parallel_tool_calls = completion_create_params.get("parallel_tool_calls", True)
            logprobs = completion_create_params.get("logprobs", False)
            top_logprobs = completion_create_params.get("top_logprobs", None)
            store = completion_create_params.get("store", False)
            user = completion_create_params.get("user", None)

            # Get model and processor instances
            models_service = get_models_service()
            model = models_service.get_model(model_name)
            processor = models_service.get_processor(model_name)
            logger.info(
                f"Model: {model_name}, max_tokens: {max_tokens}, temperature: {temperature}, n: {n}"
            )

            # Log messages for debugging
            logger.debug(f"Messages:\n{pprint.pformat(messages, width=120)}")

            # Create DatasetDict directly for model_utils
            dataset = DatasetDict({"test": Dataset.from_list([{
                "messages": messages,
                "tools": tools or [],
                "parallel_tool_calls": None,
            }])})

            # Use model_utils for inference
            model_inputs = prepare_model_inputs(
                dataset=dataset,
                model=model,
                processor=processor,
                stream=stream,
            )
            
            # Debug: Check what messages are actually sent to the model (including few-shot examples)
            if "test_dataset" in model_inputs and len(model_inputs["test_dataset"]) > 0:
                actual_messages = model_inputs["test_dataset"][0].get("messages", [])
                
                # Assert that we have proper chat messages (not formatted strings with <end_of_utterance>)
                assert isinstance(actual_messages, list), f"Expected messages to be a list, got {type(actual_messages)}"
                for i, msg in enumerate(actual_messages):
                    assert isinstance(msg, dict), f"Message {i} should be a dict, got {type(msg)}"
                    assert "role" in msg, f"Message {i} missing 'role' field: {msg}"
                    assert msg["role"] in ["system", "user", "assistant", "tool"], f"Message {i} has invalid role: {msg['role']}"
                
                logger.debug(f"Final messages sent to model (including few-shot examples):\n{pprint.pformat(actual_messages, width=120)}")
            else:
                logger.debug("No test_dataset found in model_inputs")

            model_outputs = process_model_inputs(
                data_collator=model_inputs["data_collator"],
                eval_dataset=model_inputs["eval_dataset"],
                model=model,
                processor=processor,
                stream=stream,
                test_dataset=model_inputs["test_dataset"],
                train_dataset=model_inputs["train_dataset"],
            )

            results = process_model_outputs(
                model_outputs=model_outputs, processor=processor, stream=stream
            )

            if stream:
                return self._create_streaming_response_from_model_utils(
                    results,
                    model_name,
                    max_tokens,
                    temperature,
                    top_p,
                    stop,
                    logprobs,
                    top_logprobs,
                    tool_choice,
                    tools,
                )
            else:
                response = self._create_non_streaming_response_from_model_utils(
                    results,
                    model_name,
                    max_tokens,
                    temperature,
                    top_p,
                    n,
                    stop,
                    user,
                )
                logger.debug(f"Model response:\n{pprint.pformat(response, width=120)}")
                logger.debug("DEBUG: Response validation:")
                logger.debug(f"  - Has 'choices' key: {'choices' in response}")
                if "choices" in response and response["choices"]:
                    choice = response["choices"][0]
                    logger.debug(f"  - First choice keys: {list(choice.keys())}")
                    if "message" in choice:
                        message = choice["message"]
                        logger.debug(f"  - Message keys: {list(message.keys())}")
                        logger.debug(f"  - Has tool_calls: {'tool_calls' in message}")
                        if "tool_calls" in message and message["tool_calls"]:
                            logger.debug(
                                f"  - Tool calls count: {len(message['tool_calls'])}"
                            )
                            logger.debug(
                                f"  - First tool call: {json.dumps(message['tool_calls'][0], indent=4)}"
                            )
                else:
                    logger.debug("  - No choices in response!")

                # Handle tool_choice="required" - must have tool calls
                if tool_choice == "required" and tools:
                    self._ensure_tool_call_in_response(response, tools)

                logger.debug(
                    "DEBUG: Skipping _parse_tool_call_from_response, using standard response format"
                )

                if store:
                    self._stored_completions[response["id"]] = {
                        **response,
                        "metadata": completion_create_params.get("metadata", {}),
                        "messages": messages,
                    }
                return response

        except Exception as e:
            logger.error(f"Exception in create_chat_completion: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Failed to create chat completion: {str(e)}"
            ) from e

    def get_chat_completion(self, completion_id):
        """Get a stored chat completion."""
        try:
            if completion_id not in self._stored_completions:
                raise HTTPException(status_code=404, detail="Chat completion not found")

            return self._stored_completions[completion_id]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get chat completion: {str(e)}"
            ) from e

    def update_chat_completion(self, completion_id, body=None):
        """Modify a stored chat completion."""
        try:
            if completion_id not in self._stored_completions:
                raise HTTPException(status_code=404, detail="Chat completion not found")

            if not body:
                body = {}

            # Currently only support updating metadata
            if "metadata" in body:
                self._stored_completions[completion_id]["metadata"] = body["metadata"]

            return self._stored_completions[completion_id]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to update chat completion: {str(e)}"
            ) from e

    def delete_chat_completion(self, completion_id):
        """Delete a stored chat completion."""
        try:
            if completion_id not in self._stored_completions:
                raise HTTPException(status_code=404, detail="Chat completion not found")

            deleted_completion = self._stored_completions.pop(completion_id)
            return {
                "id": deleted_completion["id"],
                "object": "chat.completion.deleted",
                "deleted": True,
            }
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to delete chat completion: {str(e)}"
            ) from e

    def get_chat_completion_messages(
        self, completion_id, after=None, limit=None, order=None
    ):
        """Get the messages in a stored chat completion."""
        try:
            if completion_id not in self._stored_completions:
                raise HTTPException(status_code=404, detail="Chat completion not found")

            completion = self._stored_completions[completion_id]
            messages = completion.get("messages", [])

            # Apply filters and ordering (similar to list_chat_completions)
            if after:
                try:
                    int(after)
                    # Filter messages by some timestamp if available
                    # For now, just return all messages
                    pass
                except ValueError:
                    pass

            # Apply ordering
            if order == "desc":
                messages = list(reversed(messages))

            # Apply limit
            if limit:
                try:
                    limit_int = int(limit)
                    messages = messages[:limit_int]
                except ValueError:
                    pass

            return {
                "object": "list",
                "data": messages,
                "first_id": messages[0].get("id") if messages else None,
                "last_id": messages[-1].get("id") if messages else None,
                "has_more": False,
            }
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to get chat completion messages: {str(e)}",
            ) from e

    def _create_streaming_response(
        self,
        model,
        processor,
        inputs,
        model_name,
        max_tokens,
        temperature,
        top_p,
        stop,
        logprobs=False,
        top_logprobs=5,
        tool_choice=None,
        tools=None,
    ):
        """Create a streaming response for chat completion."""
        from fastapi.responses import StreamingResponse

        return StreamingResponse(
            self._streaming_event_generator(
                model,
                processor,
                inputs,
                model_name,
                max_tokens,
                temperature,
                top_p,
                stop,
                logprobs,
                tool_choice,
                tools,
            ),
            media_type="text/event-stream",
        )

    def _streaming_event_generator(
        self,
        model,
        processor,
        inputs,
        model_name,
        max_tokens,
        temperature,
        top_p,
        stop,
        logprobs,
        tool_choice,
        tools,
    ):
        """Generate streaming events for chat completion."""
        import threading

        from transformers import TextIteratorStreamer

        # Initialize streaming setup
        input_ids = inputs["input_ids"]
        input_ids.clone()
        generated_text = ""

        # Setup generation parameters
        generation_kwargs = self._prepare_generation_kwargs(
            processor, model, max_tokens, temperature, top_p
        )

        # Setup streamer and start generation
        streamer = TextIteratorStreamer(processor, skip_prompt=True, timeout=10)
        generation_kwargs["streamer"] = streamer

        generation_thread = threading.Thread(
            target=lambda: model.generate(**inputs, **generation_kwargs)
        )
        generation_thread.start()

        # Stream tokens
        for token in streamer:
            if token:
                generated_text += token
                yield self._create_token_chunk(token, model_name, logprobs)

        # Wait for generation to complete
        generation_thread.join()

        # Handle tool choice fallback
        tool_calls = self._handle_streaming_tool_choice_fallback(
            generated_text, tool_choice, tools
        )

        # Send final chunk
        yield self._create_final_chunk(model_name, tool_calls)
        yield "data: [DONE]\n\n"

    def _prepare_generation_kwargs(
        self, processor, model, max_tokens, temperature, top_p
    ):
        """Prepare generation parameters for streaming."""
        eos_token_id = getattr(processor, "eos_token_id", None)
        if eos_token_id is None and hasattr(model, "config"):
            eos_token_id = getattr(model.config, "eos_token_id", None)

        generation_kwargs = {
            "max_new_tokens": max_tokens,
            "do_sample": temperature > 0,
            "temperature": temperature if temperature > 0 else 1.0,
            "top_p": top_p,
            "pad_token_id": getattr(processor, "pad_token_id", None),
            "eos_token_id": eos_token_id,
        }

        return {k: v for k, v in generation_kwargs.items() if v is not None}

    def _create_token_chunk(self, token, model_name, logprobs) -> str:
        """Create a streaming chunk for a single token."""
        import json
        import uuid

        delta_data = {"content": token}

        logprobs_data = None
        if logprobs:
            logprobs_data = {
                "content": [
                    {
                        "token": token,
                        "logprob": -0.01,  # Dummy logprob value
                        "bytes": list(token.encode("utf-8")),
                        "top_logprobs": [],
                    }
                ]
            }

        chunk_data = {
            "id": f"chatcmpl-{uuid.uuid4().hex[:8]}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model_name,
            "choices": [
                {
                    "index": 0,
                    "delta": delta_data,
                    "logprobs": logprobs_data,
                    "finish_reason": None,
                }
            ],
        }

        return f"data: {json.dumps(chunk_data)}\n\n"

    def _handle_streaming_tool_choice_fallback(
        self, generated_text, tool_choice, tools
    ):
        """Handle tool_choice='required' fallback for streaming."""
        if tool_choice != "required" or not tools:
            return None

        has_tool_calls = self._detect_tool_calls_in_text(generated_text)

        logger.debug(
            f"🔍 STREAMING TOOL_CHOICE=required check: has_tool_calls={has_tool_calls}"
        )
        logger.debug(f"🔍 Generated text: {generated_text[:200]}...")

        if not has_tool_calls:
            return self._create_fallback_tool_call(tools)

        return None

    def _create_fallback_tool_call(self, tools):
        """Create a deterministic fallback tool call."""
        import json
        import uuid

        logger.warning(
            "⚠️  WARNING: streaming tool_choice='required' but no tool calls found. Creating deterministic fallback tool call."
        )
        logger.debug(f"🛠️  Available tools for fallback: {len(tools)}")

        fallback_tool = tools[0]
        fallback_tool_name = fallback_tool["function"]["name"]
        fallback_tool_parameters = fallback_tool["function"].get("parameters", {})

        fallback_arguments = {"__fallback_reason": "model_did_not_call_tool"}

        if fallback_tool_parameters and "properties" in fallback_tool_parameters:
            for param, _spec in fallback_tool_parameters["properties"].items():
                if param not in fallback_arguments:
                    fallback_arguments[param] = ""

        tool_calls = [
            {
                "id": f"call_{uuid.uuid4().hex[:8]}",
                "type": "function",
                "function": {
                    "name": fallback_tool_name,
                    "arguments": json.dumps(fallback_arguments),
                },
            }
        ]

        logger.info(
            f"✅ Added deterministic fallback tool call for streaming: {fallback_tool_name}"
        )

        return tool_calls

    def _create_final_chunk(self, model_name, tool_calls) -> str:
        """Create the final streaming chunk."""
        import json
        import uuid

        final_chunk = {
            "id": f"chatcmpl-{uuid.uuid4().hex[:8]}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model_name,
            "choices": [
                {
                    "index": 0,
                    "delta": {},
                    "logprobs": None,
                    "finish_reason": "stop",
                }
            ],
        }

        if tool_calls:
            final_chunk["choices"][0]["delta"]["tool_calls"] = tool_calls

        return f"data: {json.dumps(final_chunk)}\n\n"

    def _create_non_streaming_response(
        self,
        model,
        processor,
        inputs,
        model_name,
        max_tokens,
        temperature,
        top_p,
        n,
        stop,
        user,
    ):
        """Create a non-streaming response for chat completion."""
        # Prepare stop sequences
        stop_sequences = self._prepare_stop_sequences(stop)

        # Prepare generation parameters
        generation_kwargs = self._prepare_non_streaming_generation_kwargs(
            processor, max_tokens, temperature, top_p, n
        )

        logger.debug(f"Generation kwargs: {generation_kwargs}")
        logger.debug(f"Stop sequences: {stop_sequences}")

        # Generate response
        generated_ids = self._generate_model_response(model, inputs, generation_kwargs)

        # Decode responses
        generated_texts = processor.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )

        # Debug: print raw model output
        self._log_raw_model_output(generated_texts)

        # Create choices
        choices = self._create_choices_from_responses(
            generated_texts, processor, inputs, stop_sequences
        )

        # Calculate usage and return response
        usage = self._calculate_usage(inputs, generated_ids)

        return self._build_non_streaming_response(model_name, choices, usage)

    def _prepare_stop_sequences(self, stop):
        """Prepare stop sequences for generation."""
        stop_sequences = []
        if stop:
            if isinstance(stop, str):
                stop_sequences.append(stop)
            elif isinstance(stop, list):
                stop_sequences.extend(stop)
        # Always add </tool_call> as a stop sequence
        if "</tool_call>" not in stop_sequences:
            stop_sequences.append("</tool_call>")
        return stop_sequences

    def _prepare_non_streaming_generation_kwargs(
        self, processor, max_tokens, temperature, top_p, n
    ):
        """Prepare generation parameters for non-streaming response."""
        if temperature == 0.0:
            generation_kwargs = {
                "do_sample": False,
                "max_new_tokens": max_tokens,
            }
        else:
            generation_kwargs = {
                "max_new_tokens": max_tokens,
                "do_sample": True,
                "temperature": temperature,
                "top_p": top_p,
                "num_return_sequences": n,
                "pad_token_id": getattr(processor, "pad_token_id", None),
                "eos_token_id": getattr(processor, "eos_token_id", None),
            }

        return {k: v for k, v in generation_kwargs.items() if v is not None}

    def _generate_model_response(self, model, inputs, generation_kwargs):
        """Generate model response with error handling."""
        logger.info("Starting model generation...")
        with torch.no_grad():
            try:
                generated_ids = model.generate(**inputs, **generation_kwargs)
                logger.info("Model generation completed successfully")
                return generated_ids
            except Exception as e:
                logger.error(f"Model generation failed: {e}", exc_info=True)
                raise

    def _log_raw_model_output(self, generated_texts) -> None:
        """Log raw model output for debugging."""
        logger.debug("\n==================== RAW MODEL OUTPUT ====================")
        for i, text in enumerate(generated_texts):
            logger.debug(
                f"Response {i}: {repr(text)}"
            )  # Use repr to see exact characters
            logger.debug(f"Response {i} length: {len(text)}")
        logger.debug("================== END RAW MODEL OUTPUT =================\n")

    def _create_choices_from_responses(
        self, generated_texts, processor, inputs, stop_sequences
    ):
        """Create choices from generated responses."""
        choices = []
        for i, response_text in enumerate(generated_texts):
            # Remove the input text from the response
            input_text = processor.decode(
                inputs["input_ids"][0], skip_special_tokens=True
            )
            if response_text.startswith(input_text):
                response_text = response_text[len(input_text) :].strip()

            # Check for stop sequences and truncate if found
            response_text, finish_reason = self._apply_stop_sequences(
                response_text, stop_sequences
            )

            # Parse tool calls from <tool_call> tags if present
            tool_calls = self._parse_tool_calls_from_text(response_text)

            message = {
                "role": "assistant",
            }

            # According to OpenAI spec: when tool_calls are present, content should be null
            if tool_calls:
                message["tool_calls"] = tool_calls
                message["content"] = None
            else:
                message["content"] = response_text

            choices.append(
                {
                    "index": i,
                    "message": message,
                    "finish_reason": finish_reason,
                }
            )

        return choices

    def _apply_stop_sequences(self, response_text, stop_sequences):
        """Apply stop sequences to response text."""
        finish_reason = "stop"
        if stop_sequences:
            for stop_seq in stop_sequences:
                if isinstance(stop_seq, str) and stop_seq in response_text:
                    # Find the position and truncate
                    stop_pos = response_text.find(stop_seq)
                    if stop_pos != -1:
                        response_text = response_text[: stop_pos + len(stop_seq)]
                        finish_reason = "stop"
                        break
        return response_text, finish_reason

    def _calculate_usage(self, inputs, generated_ids):
        """Calculate token usage."""
        prompt_tokens = len(inputs["input_ids"][0]) if "input_ids" in inputs else 0
        completion_tokens = (
            len(generated_ids[0]) - prompt_tokens if generated_ids is not None else 0
        )
        total_tokens = prompt_tokens + completion_tokens

        return {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
        }

    def _build_non_streaming_response(self, model_name, choices, usage):
        """Build the final non-streaming response."""
        import uuid

        return {
            "id": f"chatcmpl-{uuid.uuid4().hex[:8]}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model_name,
            "choices": choices,
            "usage": usage,
        }

    def _parse_tool_calls_from_text(self, text):
        """
        Parse tool calls from <tool_call> tags in the response text.

        Expected format: reasoning text followed by <tool_call>function_name(param="value")</tool_call>

        Returns list of tool calls in OpenAI format.
        """
        import re

        tool_calls = []

        # Pattern to match <tool_call>function_call</tool_call>
        pattern = r"<tool_call>(.*?)</tool_call>"
        matches = re.findall(pattern, text, re.DOTALL)

        logger.debug(f"Found {len(matches)} tool_call blocks in response")

        for i, match in enumerate(matches):
            try:
                # Extract function call from the tool_call block
                function_call = match.strip()

                logger.debug(f"Tool call block {i + 1}: {repr(function_call[:100])}...")

                # Try to parse as JSON format first (new format)
                if function_call.startswith("{") and function_call.endswith("}"):
                    try:
                        import ast

                        # Use ast.literal_eval for safe evaluation of Python dict literals
                        tool_call_dict = ast.literal_eval(function_call)
                        function_name = tool_call_dict.get("name")
                        arguments = tool_call_dict.get("arguments", {})

                        if not function_name:
                            logger.warning(
                                f"JSON tool call missing 'name' field: {function_call}"
                            )
                            continue

                        logger.debug(
                            f"Parsed JSON tool call: {function_name} with args {arguments}"
                        )
                    except (ValueError, SyntaxError) as e:
                        logger.warning(
                            f"Failed to parse JSON tool call '{function_call}': {e}"
                        )
                        continue
                else:
                    # Parse function name and arguments using regex (legacy format)
                    # Pattern: function_name(arg1="value1", arg2="value2")
                    func_pattern = r"(\w+)\((.*?)\)"
                    func_match = re.match(func_pattern, function_call, re.DOTALL)

                    if not func_match:
                        logger.warning(
                            f"Could not parse function call: {function_call}"
                        )
                        continue

                    function_name = func_match.group(1)
                    args_string = func_match.group(2).strip()

                    # Parse arguments - simple approach for key="value" pairs
                    arguments = {}
                    if args_string:
                        # Split by comma but handle quoted strings
                        arg_pattern = r'(\w+)=(["\'])(.*?)\2'
                        arg_matches = re.findall(arg_pattern, args_string)
                        for arg_name, _quote, arg_value in arg_matches:
                            arguments[arg_name] = arg_value

                # Create OpenAI-style tool call
                tool_call = {
                    "id": f"call_{uuid.uuid4().hex[:8]}",
                    "type": "function",
                    "function": {
                        "name": function_name,
                        "arguments": json.dumps(arguments),
                    },
                }

                tool_calls.append(tool_call)

            except Exception as e:
                # Log parsing error but don't fail
                logger.warning(f"Failed to parse tool_call block '{match}': {e}")
                continue

        return tool_calls if tool_calls else None

    def _parse_tool_call_from_response(self, response, tool_choice):
        """
        Detects and returns a ToolCallItem if tool_choice is 'required' and a tool call is present.
        Supports both OpenAI and HuggingFace unified tool use formats.
        """
        if tool_choice != "required":
            return None
        # Check for OpenAI function_call/tool_calls in choices
        choices = response.get("choices", [])
        for choice in choices:
            # OpenAI function_call (single tool call)
            message = choice.get("message", {})
            if "function_call" in message:
                fc = message["function_call"]
                return {
                    "type": "function",
                    "call_id": fc.get("call_id") or str(uuid.uuid4()),
                    "name": fc.get("name"),
                    "arguments": (
                        json.loads(fc.get("arguments", "{}"))
                        if isinstance(fc.get("arguments"), str)
                        else fc.get("arguments", {})
                    ),
                }
            # OpenAI tool_calls (multiple tool calls)
            if "tool_calls" in message:
                tool_calls = message["tool_calls"]
                if isinstance(tool_calls, list) and tool_calls:
                    tc = tool_calls[0]
                    return {
                        "type": tc.get("type", "function"),
                        "call_id": tc.get("id", str(uuid.uuid4())),
                        "name": tc.get("function", {}).get("name"),
                        "arguments": (
                            json.loads(tc.get("function", {}).get("arguments", "{}"))
                            if isinstance(tc.get("function", {}).get("arguments"), str)
                            else tc.get("function", {}).get("arguments", {})
                        ),
                    }
        # HuggingFace unified tool use: look for tool_calls at top level
        if "tool_calls" in response:
            tool_calls = response["tool_calls"]
            if isinstance(tool_calls, list) and tool_calls:
                tc = tool_calls[0]
                return {
                    "type": tc.get("type", "function"),
                    "call_id": tc.get("id", str(uuid.uuid4())),
                    "name": tc.get("function", {}).get("name"),
                    "arguments": tc.get("function", {}).get("arguments", {}),
                }
        return None


    def _detect_tool_calls_in_text(self, text) -> bool:
        """
        Detect if the generated text contains tool calls.
        This is a simple check for common tool call patterns.
        """
        if not text:
            return False

        # Check for common tool call patterns
        tool_call_indicators = [
            "<tool_call>",
            "function_call",
            '"name":',
            '"arguments":',
        ]

        text_lower = text.lower()
        for indicator in tool_call_indicators:
            if indicator.lower() in text_lower:
                return True

        return False




    def _ensure_tool_call_in_response(self, response, tools) -> None:
        # Handle tool_choice="required" - must have tool calls
        import uuid

        if not response.get("choices"):
            return
        has_tool_calls = any(
            choice.get("message", {}).get("tool_calls")
            for choice in response.get("choices", [])
        )
        if not has_tool_calls:
            fallback_tool = tools[0]
            fallback_tool_name = fallback_tool["function"]["name"]
            fallback_tool_parameters = fallback_tool["function"].get("parameters", {})
            fallback_arguments = {"__fallback_reason": "model_did_not_call_tool"}
            if fallback_tool_parameters and "properties" in fallback_tool_parameters:
                for param, _spec in fallback_tool_parameters["properties"].items():
                    if param not in fallback_arguments:
                        fallback_arguments[param] = ""
            fallback_tool_call = {
                "id": f"call_{uuid.uuid4().hex[:8]}",
                "type": "function",
                "function": {
                    "name": fallback_tool_name,
                    "arguments": json.dumps(fallback_arguments),
                },
            }
            first_choice = response["choices"][0]
            if "message" in first_choice:
                first_choice["message"]["tool_calls"] = [fallback_tool_call]
                # According to OpenAI spec: when tool_calls are present, content should be null
                first_choice["message"]["content"] = None
                logger.info(
                    f"✅ Added deterministic fallback tool call: {fallback_tool_call['function']['name']}"
                )


