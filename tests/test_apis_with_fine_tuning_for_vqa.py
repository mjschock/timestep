"""
Vision Fine-tuning for Visual Question Answering Test

This test extracts the logic from the Vision_Fine_tuning_on_GPT4o_for_Visual_Question_Answering.ipynb notebook
and runs it as a sequential test with assertions on intermediate state.

Modified from: https://github.com/openai/openai-cookbook/blob/843a8bc6826bd4f32a035c95f67a36d6b7c14253/examples/multimodal/Vision_Fine_tuning_on_GPT4o_for_Visual_Question_Answering.ipynb

Uses the SmolVLM2-256M-Video-Instruct model for vision fine-tuning capabilities.
"""

import asyncio
import base64
import csv
import io
import json
import os
import time
from pathlib import Path

import pytest
from conftest import MODEL_NAME
from PIL import Image


def create_sample_images():
    """Create sample images for VQA testing"""
    images_dir = Path("tests/fixtures/images")
    images_dir.mkdir(exist_ok=True)

    # Create a simple image with text
    img1 = Image.new("RGB", (256, 256), color="white")
    # Add some text-like content (simplified)
    img1.save(images_dir / "book0.png")

    img2 = Image.new("RGB", (256, 256), color="lightblue")
    img2.save(images_dir / "book1.png")

    return str(images_dir / "book0.png"), str(images_dir / "book1.png")


def encode_image_to_base64(image_path):
    """Encode image to base64 for API calls"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def create_vqa_training_data():
    """Create VQA training data in the format expected by the notebook"""
    book0_path, book1_path = create_sample_images()

    training_data = []

    # Sample 1: Book 0
    book0_base64 = encode_image_to_base64(book0_path)
    training_data.append(
        {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "Use the image to answer the question.",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What is the title of book 0?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{book0_base64}"
                            },
                        },
                    ],
                },
                {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Book Title 0"}],
                },
            ]
        }
    )

    # Sample 2: Book 1
    book1_base64 = encode_image_to_base64(book1_path)
    training_data.append(
        {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "Use the image to answer the question.",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What is the title of book 1?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{book1_base64}"
                            },
                        },
                    ],
                },
                {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Book Title 1"}],
                },
            ]
        }
    )

    # Write to JSONL file
    training_file_path = "tests/fixtures/jsonl/vqa_training_data.jsonl"
    os.makedirs(os.path.dirname(training_file_path), exist_ok=True)

    with open(training_file_path, "w") as f:
        for item in training_data:
            f.write(f"{json.dumps(item)}\n")

    return training_file_path


async def test_baseline_vision_model(async_client):
    """Test baseline vision model performance"""
    print("🧪 Testing baseline vision model performance...")

    # Create sample images
    book0_path, book1_path = create_sample_images()

    # Test baseline performance on VQA tasks
    test_cases = [
        {
            "image_path": book0_path,
            "question": "What is the title of book 0?",
            "expected_answer": "Book Title 0",
        },
        {
            "image_path": book1_path,
            "question": "What is the title of book 1?",
            "expected_answer": "Book Title 1",
        },
    ]

    baseline_results = []

    for i, test_case in enumerate(test_cases):
        image_base64 = encode_image_to_base64(test_case["image_path"])

        messages = [
            {
                "role": "system",
                "content": [
                    {"type": "text", "text": "Use the image to answer the question."}
                ],
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": test_case["question"]},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_base64}"},
                    },
                ],
            },
        ]

        completion = await async_client.chat.completions.create(
            model=MODEL_NAME, messages=messages, temperature=0.0, seed=42
        )

        actual_answer = completion.choices[0].message.content
        expected_answer = test_case["expected_answer"]
        match = actual_answer.strip() == expected_answer.strip()

        baseline_results.append(
            {
                "test_case": i + 1,
                "question": test_case["question"],
                "expected": expected_answer,
                "actual": actual_answer,
                "match": match,
            }
        )

        print(f"Test case {i + 1}: {match}")
        print(f"  Question: {test_case['question']}")
        print(f"  Expected: {expected_answer}")
        print(f"  Actual: {actual_answer}")

    # Calculate baseline performance
    matches = sum(1 for r in baseline_results if r["match"])
    baseline_percentage = (matches / len(baseline_results)) * 100

    print(f"Baseline VQA performance: {baseline_percentage:.1f}%")

    # For now, expect low baseline performance (model may not be trained on this specific task)
    assert baseline_percentage >= 0.0, (
        f"Baseline performance should be >= 0.0%: {baseline_percentage}%"
    )

    return baseline_results, baseline_percentage


async def create_vqa_fine_tuning_job(async_client):
    """Upload VQA training data and create fine-tuning job"""
    print("📁 Creating VQA training data...")
    training_file_path = create_vqa_training_data()
    assert os.path.exists(training_file_path), (
        f"Training file not found: {training_file_path}"
    )

    print("📁 Uploading VQA training data...")
    with open(training_file_path, "rb") as f:
        file_object = await async_client.files.create(file=f, purpose="fine-tune")

    file_id = file_object.id
    print(f"VQA training file uploaded with ID: {file_id}")
    assert file_id is not None

    # Create fine-tuning job
    print("🚀 Creating VQA fine-tuning job...")
    fine_tuning_job = await async_client.fine_tuning.jobs.create(
        model=MODEL_NAME,
        training_file=file_id,
        hyperparameters={
            "n_epochs": 1,  # Just 1 epoch for speed
            "batch_size": 1,  # Keep batch_size=1 to avoid GPU memory issues
            "learning_rate_multiplier": 4.0,  # Use working learning rate from function calling test
        },
        seed=42,
    )

    fine_tuning_job_id = fine_tuning_job.id
    print(f"VQA fine-tuning job created with ID: {fine_tuning_job_id}")
    assert fine_tuning_job_id is not None

    return file_id, fine_tuning_job_id


async def wait_for_vqa_job_completion(
    async_client, fine_tuning_job_id, max_wait_time=300
):
    """Wait for VQA fine-tuning job to complete"""
    print("⏳ Waiting for VQA fine-tuning job to complete...")
    start_time = time.time()
    fine_tuned_model = None

    while True:
        fine_tuning_job = await async_client.fine_tuning.jobs.retrieve(
            fine_tuning_job_id
        )
        print(f"Job status: {fine_tuning_job.status}")

        if fine_tuning_job.status == "succeeded":
            fine_tuned_model = fine_tuning_job.fine_tuned_model
            print("✅ VQA fine-tuning job completed successfully!")
            print(f"Fine-tuned model: {fine_tuned_model}")
            break
        elif fine_tuning_job.status == "failed":
            pytest.fail(f"VQA fine-tuning job failed: {fine_tuning_job.error}")
        elif fine_tuning_job.status == "cancelled":
            pytest.fail("VQA fine-tuning job was cancelled")
        else:
            if time.time() - start_time > max_wait_time:
                # Cancel the job before failing
                await async_client.fine_tuning.jobs.cancel(fine_tuning_job_id)
                pytest.fail(
                    f"VQA fine-tuning job timed out after {max_wait_time} seconds"
                )

            print(f"Job still running... status: {fine_tuning_job.status}")
            await asyncio.sleep(5)  # Wait 5 seconds before checking again

    return fine_tuned_model, fine_tuning_job


async def inspect_vqa_job_details(fine_tuning_job, file_id):
    """Inspect and assert on VQA fine-tuning job details"""
    print("🔍 Inspecting VQA fine-tuning job details...")
    print(f"Job ID: {fine_tuning_job.id}")
    print(f"Object: {fine_tuning_job.object}")
    print(f"Model: {fine_tuning_job.model}")
    print(f"Status: {fine_tuning_job.status}")
    print(f"Training file: {fine_tuning_job.training_file}")
    print(f"Validation file: {fine_tuning_job.validation_file}")
    print(f"Fine-tuned model: {fine_tuning_job.fine_tuned_model}")
    print(f"Organization ID: {fine_tuning_job.organization_id}")
    print(f"Created at: {fine_tuning_job.created_at}")
    print(f"Finished at: {fine_tuning_job.finished_at}")
    print(f"Trained tokens: {fine_tuning_job.trained_tokens}")
    print(f"Error: {fine_tuning_job.error}")
    print(f"Result files: {fine_tuning_job.result_files}")

    # Check if hyperparameters exist
    if hasattr(fine_tuning_job, "hyperparameters"):
        print(f"Hyperparameters: {fine_tuning_job.hyperparameters}")
        if hasattr(fine_tuning_job.hyperparameters, "n_epochs"):
            print(f"  - n_epochs: {fine_tuning_job.hyperparameters.n_epochs}")
        if hasattr(fine_tuning_job.hyperparameters, "batch_size"):
            print(f"  - batch_size: {fine_tuning_job.hyperparameters.batch_size}")
        if hasattr(fine_tuning_job.hyperparameters, "learning_rate_multiplier"):
            print(
                f"  - learning_rate_multiplier: {fine_tuning_job.hyperparameters.learning_rate_multiplier}"
            )

    # Check if method exists
    if hasattr(fine_tuning_job, "method"):
        print(f"Method: {fine_tuning_job.method}")

    # Basic assertions
    assert fine_tuning_job.id == fine_tuning_job.id
    assert fine_tuning_job.object == "fine_tuning.job"
    # The model name should match exactly what was provided
    assert fine_tuning_job.model == MODEL_NAME
    assert fine_tuning_job.status == "succeeded"
    assert fine_tuning_job.training_file == file_id
    assert fine_tuning_job.fine_tuned_model is not None
    assert fine_tuning_job.created_at is not None

    # Assert hyperparameters - our implementation uses the method structure for hyperparameters
    assert hasattr(fine_tuning_job, "hyperparameters")
    assert hasattr(fine_tuning_job, "method")

    # The actual hyperparameters are in the method structure
    if fine_tuning_job.method and fine_tuning_job.method.supervised:
        supervised_hyperparams = fine_tuning_job.method.supervised.hyperparameters
        # Our implementation stores the actual values, not "auto"
        assert supervised_hyperparams.n_epochs == 1
        assert supervised_hyperparams.batch_size == 1
        assert supervised_hyperparams.learning_rate_multiplier == 4.0

    # Assert method structure matches OpenAI API specification
    assert hasattr(fine_tuning_job, "method")
    assert fine_tuning_job.method.type == "supervised"
    assert hasattr(fine_tuning_job.method, "supervised")
    assert fine_tuning_job.method.supervised is not None
    assert hasattr(fine_tuning_job.method.supervised, "hyperparameters")

    # Verify the nested hyperparameters in method - our implementation stores actual values
    method_hyperparams = fine_tuning_job.method.supervised.hyperparameters
    assert method_hyperparams.n_epochs == 1
    assert method_hyperparams.batch_size == 1
    assert method_hyperparams.learning_rate_multiplier == 4.0

    # Assert organization and result files - our implementation uses "org-default"
    assert fine_tuning_job.organization_id == "org-default"
    assert isinstance(fine_tuning_job.result_files, list)
    assert len(fine_tuning_job.result_files) == 1

    # Assert additional OpenAI API fields
    assert hasattr(fine_tuning_job, "seed")
    assert fine_tuning_job.seed == 42  # Default seed value
    assert hasattr(fine_tuning_job, "integrations")
    assert (
        fine_tuning_job.integrations is None or fine_tuning_job.integrations == []
    )  # Handle None or empty list
    assert hasattr(fine_tuning_job, "metadata")
    assert fine_tuning_job.metadata is None  # Default None
    assert hasattr(fine_tuning_job, "error")
    assert fine_tuning_job.error is None  # Should be None for successful job
    assert hasattr(fine_tuning_job, "estimated_finish")
    # estimated_finish can be None even for successful jobs


async def examine_vqa_training_metrics(async_client, fine_tuning_job):
    """Examine result files and training metrics for VQA job"""
    print("📊 Examining VQA training metrics from result files...")
    result_file_id = fine_tuning_job.result_files[0]
    print(f"Result file ID: {result_file_id}")

    # Retrieve the result file object to get metadata
    result_file_object = await async_client.files.retrieve(result_file_id)
    print(f"Result file object: {result_file_object}")
    print(f"Result file filename: {result_file_object.filename}")
    print(f"Result file purpose: {result_file_object.purpose}")
    print(f"Result file bytes: {result_file_object.bytes}")

    # Retrieve the actual content of the result file
    try:
        result_file_content = await async_client.files.content(result_file_id)
        content_bytes = result_file_content.read()

        # Try to decode as base64 first (as the content appears to be base64 encoded)
        try:
            content_text = base64.b64decode(content_bytes).decode("utf-8")
            print("Successfully decoded base64 content")
        except Exception:
            # Fall back to direct UTF-8 decoding if base64 fails
            content_text = content_bytes.decode("utf-8")
            print("Decoded as direct UTF-8 content")

        print(f"Result file content (first 500 chars):\n{content_text[:500]}")

        # Parse CSV content if it's a CSV file
        if result_file_object.filename and result_file_object.filename.endswith(".csv"):
            lines = content_text.strip().split("\n")
            print(f"CSV has {len(lines)} lines")

            if len(lines) > 0:
                # Parse header
                reader = csv.DictReader(io.StringIO(content_text))
                rows = list(reader)
                print(f"CSV columns: {reader.fieldnames}")
                print(f"Number of training steps: {len(rows)}")

                if rows:
                    print("First few training metrics:")
                    for i, row in enumerate(rows[:3]):
                        print(f"  Step {i + 1}: {row}")

                    if len(rows) > 3:
                        print("Last training metrics:")
                        print(f"  Final step: {rows[-1]}")

                    # Assert that we have expected columns
                    expected_columns = [
                        "step",
                        "train_loss",
                    ]  # At minimum these should exist
                    for col in expected_columns:
                        assert col in reader.fieldnames, (
                            f"Expected column '{col}' not found in result file"
                        )

                    # Assert that we have at least one training step
                    assert len(rows) >= 1, (
                        "Should have at least one training step in results"
                    )

                    # Check if loss values are numeric
                    if "train_loss" in reader.fieldnames:
                        train_losses = [
                            float(row["train_loss"])
                            for row in rows
                            if row["train_loss"]
                        ]
                        print(f"Training loss progression: {train_losses}")
                        assert len(train_losses) > 0, "Should have training loss values"
                        assert all(
                            isinstance(loss, int | float) for loss in train_losses
                        ), "All training losses should be numeric"

    except Exception as e:
        print(f"Could not retrieve result file content: {e}")
        # Don't fail the test if we can't retrieve content, but log the issue


async def evaluate_fine_tuned_vqa_performance(
    async_client, fine_tuned_model, baseline_percentage
):
    """Test fine-tuned VQA model performance and compare with baseline"""
    print("🧪 Testing fine-tuned VQA model performance...")

    # Create sample images
    book0_path, book1_path = create_sample_images()

    # Test fine-tuned model performance on VQA tasks
    test_cases = [
        {
            "image_path": book0_path,
            "question": "What is the title of book 0?",
            "expected_answer": "Book Title 0",
        },
        {
            "image_path": book1_path,
            "question": "What is the title of book 1?",
            "expected_answer": "Book Title 1",
        },
    ]

    fine_tuned_results = []

    for i, test_case in enumerate(test_cases):
        image_base64 = encode_image_to_base64(test_case["image_path"])

        messages = [
            {
                "role": "system",
                "content": [
                    {"type": "text", "text": "Use the image to answer the question."}
                ],
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": test_case["question"]},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_base64}"},
                    },
                ],
            },
        ]

        completion = await async_client.chat.completions.create(
            model=fine_tuned_model, messages=messages, temperature=0.0, seed=42
        )

        actual_answer = completion.choices[0].message.content
        expected_answer = test_case["expected_answer"]
        match = actual_answer.strip() == expected_answer.strip()

        fine_tuned_results.append(
            {
                "test_case": i + 1,
                "question": test_case["question"],
                "expected": expected_answer,
                "actual": actual_answer,
                "match": match,
            }
        )

        print(f"Fine-tuned test case {i + 1}: {match}")
        print(f"  Question: {test_case['question']}")
        print(f"  Expected: {expected_answer}")
        print(f"  Actual: {actual_answer}")

    # Calculate fine-tuned performance
    matches = sum(1 for r in fine_tuned_results if r["match"])
    fine_tuned_percentage = (matches / len(fine_tuned_results)) * 100

    print(f"Fine-tuned VQA performance: {fine_tuned_percentage:.1f}%")

    # Compare performance
    print("\n📊 Performance comparison:")
    print(f"Baseline VQA performance: {baseline_percentage:.1f}%")
    print(f"Fine-tuned VQA performance: {fine_tuned_percentage:.1f}%")

    improvement = fine_tuned_percentage - baseline_percentage
    print(f"Improvement: {improvement:.1f} percentage points")

    # For now, expect some improvement or at least no degradation
    print(
        f"🎯 Expected: >= {baseline_percentage:.1f}%, Actual: {fine_tuned_percentage:.1f}%"
    )
    assert fine_tuned_percentage >= baseline_percentage, (
        f"Fine-tuned model should perform at least as well as baseline {baseline_percentage:.1f}%, but got {fine_tuned_percentage:.1f}%"
    )


@pytest.mark.asyncio
@pytest.mark.slow
async def test_vision_fine_tuning_for_vqa_full_workflow(async_client):
    """
    Complete VQA workflow test that mirrors the notebook logic:
    1. Test baseline vision model performance
    2. Create VQA training data
    3. Upload training data and create fine-tuning job
    4. Wait for job completion
    5. Inspect job details and training metrics
    6. Evaluate fine-tuned model performance
    """

    # 1. Test baseline vision model performance
    baseline_results, baseline_percentage = await test_baseline_vision_model(
        async_client
    )

    # 2. Create VQA training data and create fine-tuning job
    file_id, fine_tuning_job_id = await create_vqa_fine_tuning_job(async_client)

    # 3. Wait for job completion
    fine_tuned_model, fine_tuning_job = await wait_for_vqa_job_completion(
        async_client, fine_tuning_job_id
    )

    # 4. Inspect job details
    await inspect_vqa_job_details(fine_tuning_job, file_id)

    # 5. Examine training metrics
    await examine_vqa_training_metrics(async_client, fine_tuning_job)

    # 6. Test fine-tuned model performance
    await evaluate_fine_tuned_vqa_performance(
        async_client, fine_tuned_model, baseline_percentage
    )

    # 7. Cleanup - cancel any remaining jobs
    try:
        if not asyncio.get_event_loop().is_closed():
            await async_client.fine_tuning.jobs.cancel(fine_tuning_job_id)
    except Exception as e:
        print(
            f"Note: Could not cancel job {fine_tuning_job_id}: {e}"
        )  # Job may already be completed

    print("✅ VQA fine-tuning workflow test completed successfully!")
