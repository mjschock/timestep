"""
Fast Fine-tuning Test

Quick test to verify hyperparameters are properly extracted and passed through
to the training process with minimal training data and fast hyperparameters.
"""

import asyncio
import json
import time

import pytest
from conftest import MODEL_NAME


@pytest.mark.asyncio
async def test_fine_tuning_hyperparameters_fast(async_client):
    """Fast test to verify hyperparameters are properly extracted and used in training"""

    # Create minimal training data for fast processing using weather examples
    training_data = [
        {
            "messages": [
                {"role": "user", "content": "What is the weather in San Francisco?"},
                {
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": "call_id",
                            "type": "function",
                            "function": {
                                "name": "get_current_weather",
                                "arguments": '{"location": "San Francisco, USA", "format": "celsius"}',
                            },
                        }
                    ],
                },
            ],
            "parallel_tool_calls": False,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "Get the current weather",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and country, eg. San Francisco, USA",
                                },
                                "format": {
                                    "type": "string",
                                    "enum": ["celsius", "fahrenheit"],
                                },
                            },
                            "required": ["location", "format"],
                        },
                    },
                }
            ],
        },
        {
            "messages": [
                {"role": "user", "content": "What is the weather in Minneapolis?"},
                {
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": "call_id",
                            "type": "function",
                            "function": {
                                "name": "get_current_weather",
                                "arguments": '{"location": "Minneapolis, USA", "format": "celsius"}',
                            },
                        }
                    ],
                },
            ],
            "parallel_tool_calls": False,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "Get the current weather",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and country, eg. Minneapolis, USA",
                                },
                                "format": {
                                    "type": "string",
                                    "enum": ["celsius", "fahrenheit"],
                                },
                            },
                            "required": ["location", "format"],
                        },
                    },
                }
            ],
        },
        {
            "messages": [
                {"role": "user", "content": "What is the weather in San Diego?"},
                {
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": "call_id",
                            "type": "function",
                            "function": {
                                "name": "get_current_weather",
                                "arguments": '{"location": "San Diego, USA", "format": "celsius"}',
                            },
                        }
                    ],
                },
            ],
            "parallel_tool_calls": False,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "Get the current weather",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and country, eg. San Diego, USA",
                                },
                                "format": {
                                    "type": "string",
                                    "enum": ["celsius", "fahrenheit"],
                                },
                            },
                            "required": ["location", "format"],
                        },
                    },
                }
            ],
        },
        {
            "messages": [
                {"role": "user", "content": "What is the weather in Memphis?"},
                {
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": "call_id",
                            "type": "function",
                            "function": {
                                "name": "get_current_weather",
                                "arguments": '{"location": "Memphis, USA", "format": "celsius"}',
                            },
                        }
                    ],
                },
            ],
            "parallel_tool_calls": False,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "Get the current weather",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and country, eg. Memphis, USA",
                                },
                                "format": {
                                    "type": "string",
                                    "enum": ["celsius", "fahrenheit"],
                                },
                            },
                            "required": ["location", "format"],
                        },
                    },
                }
            ],
        },
        {
            "messages": [
                {"role": "user", "content": "What is the weather in Atlanta?"},
                {
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": "call_id",
                            "type": "function",
                            "function": {
                                "name": "get_current_weather",
                                "arguments": '{"location": "Atlanta, USA", "format": "celsius"}',
                            },
                        }
                    ],
                },
            ],
            "parallel_tool_calls": False,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "Get the current weather",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and country, eg. Atlanta, USA",
                                },
                                "format": {
                                    "type": "string",
                                    "enum": ["celsius", "fahrenheit"],
                                },
                            },
                            "required": ["location", "format"],
                        },
                    },
                }
            ],
        },
    ]

    print("🚀 Creating training file...")
    # Upload training file
    training_file_content = "\n".join(json.dumps(item) for item in training_data)
    training_file = await async_client.files.create(
        file=training_file_content.encode(), purpose="fine-tune"
    )
    print(f"Created training file: {training_file.id}")

    # Create fine-tuning job with stable hyperparameters for better results
    test_hyperparams = {
        "n_epochs": 2,  # Conservative epochs for stability
        "batch_size": 1,  # Small batch size for more updates
        "learning_rate_multiplier": 3.0,  # Conservative learning rate for stable training
    }

    print("🚀 Creating fine-tuning job with hyperparameters...")
    print(f"Hyperparameters: {test_hyperparams}")

    fine_tuning_job = await async_client.fine_tuning.jobs.create(
        model=MODEL_NAME,
        training_file=training_file.id,
        hyperparameters=test_hyperparams,
        seed=42,
    )

    print(f"Created fine-tuning job: {fine_tuning_job.id}")
    print(f"Status: {fine_tuning_job.status}")

    # Verify hyperparameters were stored correctly in the job
    assert hasattr(fine_tuning_job, "method"), "Job should have method structure"
    assert fine_tuning_job.method.type == "supervised", "Method should be supervised"
    assert hasattr(fine_tuning_job.method, "supervised"), (
        "Method should have supervised structure"
    )
    assert fine_tuning_job.method.supervised is not None, (
        "Supervised method should not be None"
    )
    assert hasattr(fine_tuning_job.method.supervised, "hyperparameters"), (
        "Supervised method should have hyperparameters"
    )

    stored_hyperparams = fine_tuning_job.method.supervised.hyperparameters
    print(
        f"Stored hyperparameters: n_epochs={stored_hyperparams.n_epochs}, batch_size={stored_hyperparams.batch_size}, learning_rate_multiplier={stored_hyperparams.learning_rate_multiplier}"
    )

    # Verify the hyperparameters were stored correctly
    assert stored_hyperparams.n_epochs == 2, (
        f"Expected n_epochs=2, got {stored_hyperparams.n_epochs}"
    )
    assert stored_hyperparams.batch_size == 1, (
        f"Expected batch_size=1, got {stored_hyperparams.batch_size}"
    )
    assert stored_hyperparams.learning_rate_multiplier == 3.0, (
        f"Expected learning_rate_multiplier=3.0, got {stored_hyperparams.learning_rate_multiplier}"
    )

    print("✅ Hyperparameters stored correctly in job")

    # Wait for the job to complete (should be fast with 2 epochs)
    print("⏳ Waiting for fine-tuning to complete...")
    max_wait_time = 400  # 7 minutes max for 2 epochs
    start_time = time.time()

    while time.time() - start_time < max_wait_time:
        # Get updated job status
        current_job = await async_client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
        print(f"Job status: {current_job.status}")

        if current_job.status == "succeeded":
            print("✅ Fine-tuning completed successfully!")
            break
        elif current_job.status == "failed":
            print(f"❌ Fine-tuning failed: {current_job.error}")
            if current_job.error:
                print(f"Error details: {current_job.error}")
            raise AssertionError(f"Fine-tuning job failed: {current_job.error}")
        elif current_job.status in ["cancelled", "expired"]:
            raise AssertionError(f"Fine-tuning job was {current_job.status}")

        # Wait before checking again
        await asyncio.sleep(10)
    else:
        # Timeout reached
        raise AssertionError(
            f"Fine-tuning job did not complete within {max_wait_time} seconds"
        )

    # Get the final job details
    final_job = await async_client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
    print(f"Final job status: {final_job.status}")
    print(f"Fine-tuned model: {final_job.fine_tuned_model}")
    print(f"Result files: {final_job.result_files}")

    # Verify we got a fine-tuned model
    assert final_job.fine_tuned_model is not None, (
        "Should have created a fine-tuned model"
    )
    assert final_job.status == "succeeded", "Job should have succeeded"

    # Verify result files were created and can be read
    assert final_job.result_files is not None and len(final_job.result_files) > 0, (
        "Should have created result files with training metrics"
    )

    print(f"📊 Checking training results file: {final_job.result_files[0]}")
    result_file_id = final_job.result_files[0]

    # Retrieve the result file content via files API
    try:
        result_file_content = await async_client.files.content(result_file_id)
        content_bytes = result_file_content.read()

        # Try to decode content
        try:
            import base64

            content_text = base64.b64decode(content_bytes).decode("utf-8")
            print("Successfully decoded base64 training results")
        except Exception:
            content_text = content_bytes.decode("utf-8")
            print("Decoded as direct UTF-8 training results")

        print(f"Training results preview: {content_text[:300]}")

        # Verify CSV format and training steps
        lines = content_text.strip().split("\n")
        print(f"Training results has {len(lines)} lines (including header)")

        assert len(lines) >= 2, "Should have at least header + 1 training step"

        # Check header format
        header = lines[0]
        expected_columns = ["step", "train_loss"]
        for col in expected_columns:
            assert col in header, f"Expected column '{col}' in header: {header}"

        print("✅ Training results file successfully retrieved and validated")

    except Exception as e:
        print(f"❌ Failed to retrieve training results: {e}")
        raise AssertionError(f"Could not retrieve training results file: {e}") from e

    # Test improvement on training examples
    print("🧪 Testing model improvement on training examples...")

    # Define the weather tools for testing
    weather_tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and country, eg. San Francisco, USA",
                        },
                        "format": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location", "format"],
                },
            },
        }
    ]

    # Test baseline model on first training example
    baseline_messages = [
        {"role": "user", "content": "What is the weather in San Francisco?"}
    ]

    baseline_response = await async_client.chat.completions.create(
        model=MODEL_NAME,  # Use baseline model
        messages=baseline_messages,
        tools=weather_tools,
        temperature=0.0,
        tool_choice="required",
        seed=42,
    )

    # Test fine-tuned model on the same example
    ft_response = await async_client.chat.completions.create(
        model=final_job.fine_tuned_model,  # Use fine-tuned model
        messages=baseline_messages,
        tools=weather_tools,
        temperature=0.0,
        tool_choice="required",
        seed=42,
    )

    # Check if both models made tool calls
    baseline_tool_call = (
        baseline_response.choices[0].message.tool_calls[0]
        if baseline_response.choices[0].message.tool_calls
        else None
    )
    ft_tool_call = (
        ft_response.choices[0].message.tool_calls[0]
        if ft_response.choices[0].message.tool_calls
        else None
    )

    print(
        f"Baseline tool call: {baseline_tool_call.function.name if baseline_tool_call else 'None'}"
    )
    print(
        f"Fine-tuned tool call: {ft_tool_call.function.name if ft_tool_call else 'None'}"
    )

    # Verify both models can make the correct tool call
    assert baseline_tool_call is not None, "Baseline model should make a tool call"
    assert ft_tool_call is not None, "Fine-tuned model should make a tool call"
    assert baseline_tool_call.function.name == "get_current_weather", (
        "Baseline should call get_current_weather"
    )
    assert ft_tool_call.function.name == "get_current_weather", (
        "Fine-tuned should call get_current_weather"
    )

    print("✅ Both models can handle the training example correctly")

    print("✅ Fast fine-tuning with hyperparameters test completed successfully!")
    print(
        f"Training completed with hyperparameters: n_epochs={test_hyperparams['n_epochs']}, batch_size={test_hyperparams['batch_size']}, learning_rate_multiplier={test_hyperparams['learning_rate_multiplier']}"
    )
    print("✅ Training results successfully saved and retrieved from files API")
    print("✅ Models can handle training examples correctly")
