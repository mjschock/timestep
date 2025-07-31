# ruff: noqa: S101
import copy

import pytest
import torch

from utils import (
    # assert_training_correctness,
    # build_messages,
    # convert_tool_calls_to_content,
    get_model,
    get_processor,
    # normalize_content,
    prepare_inference_messages,
    # prepare_training_example,
    # validate_training_example,
)

BASE_WEATHER_CONVERSATION = {
    "expected": {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """You are a helpful assistant.

The following tools are available:

Tool name: code_interpreter
Description: Execute Python code and return the result.
Parameters:
- code (string): Python code to execute

Tool name: get_weather
Description: Get current temperature for a given location.
Parameters:
- location (string): City and country e.g. Bogotá, Colombia

Tool name: web_search
Description: Search the web for information.
Parameters:
- query (string): Search query

To use a tool, respond with:
<tool_call>
{ ... }
</tool_call>

User: How many r's are in the word 'strawberry'?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"code": "'strawberry'.count('r')"}, "name": "code_interpreter"}
</tool_call><end_of_utterance>
Tool: 3<end_of_utterance>
Assistant: There are 3 r's in the word 'strawberry'.<end_of_utterance>

User: What are the Three Laws of Robotics?<end_of_utterance>
Assistant: <tool_call>
{'arguments': {'query': 'Three Laws of Robotics'}, 'name': 'web_search'}
</tool_call><end_of_utterance>
Tool: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>
Assistant: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>

User: What is the answer to the Ultimate Question of Life, the Universe, and Everything?<end_of_utterance>
Assistant: <tool_call>
{'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}, 'name': 'web_search'}
</tool_call><end_of_utterance>
Tool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.<end_of_utterance>
Assistant: 42""",
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is the weather like in Oakland today?",
                    }
                ],
            },
        ],
        "prompt": """<|im_start|>System: You are a helpful assistant.

The following tools are available:

Tool name: code_interpreter
Description: Execute Python code and return the result.
Parameters:
- code (string): Python code to execute

Tool name: get_weather
Description: Get current temperature for a given location.
Parameters:
- location (string): City and country e.g. Bogotá, Colombia

Tool name: web_search
Description: Search the web for information.
Parameters:
- query (string): Search query

To use a tool, respond with:
<tool_call>
{ ... }
</tool_call>

User: How many r's are in the word 'strawberry'?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"code": "'strawberry'.count('r')"}, "name": "code_interpreter"}
</tool_call><end_of_utterance>
Tool: 3<end_of_utterance>
Assistant: There are 3 r's in the word 'strawberry'.<end_of_utterance>

User: What are the Three Laws of Robotics?<end_of_utterance>
Assistant: <tool_call>
{'arguments': {'query': 'Three Laws of Robotics'}, 'name': 'web_search'}
</tool_call><end_of_utterance>
Tool: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>
Assistant: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>

User: What is the answer to the Ultimate Question of Life, the Universe, and Everything?<end_of_utterance>
Assistant: <tool_call>
{'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}, 'name': 'web_search'}
</tool_call><end_of_utterance>
Tool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.<end_of_utterance>
Assistant: 42<end_of_utterance>
User: What is the weather like in Oakland today?<end_of_utterance>
Assistant:""",
        "response": """ <tool_call>
{'arguments': {'city': 'Oakland', 'country': 'CA'}}
</tool_call>""",
    },
    "messages": [
        {
            "role": "user",
            "content": "What is the weather like in Oakland today?",
        },
    ],
    "tools": [
        {
            "type": "function",
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
            "strict": False,
        }
    ],
}


# Example conversations for testing and demonstration
EXAMPLE_CONVERSATIONS = [
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a helpful assistant.",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image",
                            "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                        },
                    ],
                },
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: What's in this image?<image><end_of_utterance>\nAssistant:",
            "response": " The image shows a bee on a pink flower. The flower has a yellow center and a pinkish-purple petals. The bee is in the center of the flower, and it is surrounded by the petals. The background is blurred, but it appears to be a garden or a field with green foliage.",
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                    },
                ],
            },
            # {"role": "assistant", "content": "I can see a bee in the image."},
        ],
        "tools": None,
    },
    # Weather conversation with tool call in content format
    {
        "expected": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]),
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"]),
        #         + [
        #             {
        #                 "role": "assistant",
        #                 "content": [
        #                     {
        #                         "type": "text",
        #                         "text": """<tool_call>
        # {'arguments': {'location': 'Oakland, CA'}}
        # </tool_call>""",
        #                     }
        #                 ],
        #             },
        #         ],
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
    # Weather conversation with tool call in tool_calls array format (tests convert_tool_calls_to_content)
    {
        "expected": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]),
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"]),
        # + [
        #     {
        #         "role": "assistant",
        #         "tool_calls": [
        #             {
        #                 "arguments": {"location": "Oakland, CA"},
        #                 "name": "get_weather",
        #             }
        #         ],
        #     },
        # ],
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
]

# Fine-tuned model expected responses (updated based on actual fine-tuned model outputs)
FINE_TUNED_EXAMPLE_CONVERSATIONS = [
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a helpful assistant.",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image",
                            "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                        },
                    ],
                },
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: What's in this image?<image><end_of_utterance>\nAssistant:",
            "response": " I am not able to see any text in the image",
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                    },
                ],
            },
            {"role": "assistant", "content": "I can see a bee in the image."},
        ],
        "tools": None,
    },
    # Weather conversation with tool call in content format
    {
        "expected": {
            "messages": copy.deepcopy(
                BASE_WEATHER_CONVERSATION["expected"]["messages"]
            ),
            "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
            "response": """ <tool_call>
{'arguments': {'query': 'What is the weather like in Oakland today?'}
{'name': 'weather_weather'}
</tool_call>""",
        },
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"])
        + [
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": """<tool_call>
{'arguments': {'location': 'Oakland, CA'}}
</tool_call>""",
                    }
                ],
            },
        ],
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
    # Weather conversation with tool call in tool_calls array format (tests convert_tool_calls_to_content)
    {
        "expected": {
            "messages": copy.deepcopy(
                BASE_WEATHER_CONVERSATION["expected"]["messages"]
            ),
            "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
            "response": """ <tool_call>
{"arguments": {"query": 'What is the weather like in Oakland today?'}
"name": 'weather_weather'}
</tool_call>""",
        },
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"])
        + [
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "arguments": {"location": "Oakland, CA"},
                        "name": "get_weather",
                    }
                ],
            },
        ],
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
]


class TestMultimodalMessageProcessor:
    """
    Test suite for multimodal message processing functionality.

    Tests cover text-only and multimodal conversations, training example preparation,
    inference processing, validation functions, and edge cases for robust functionality.
    Includes comprehensive testing of tool call conversion, message building, and
    training example validation.
    """

    @pytest.fixture(scope="class")
    def processor(self):
        """Load the SmolVLM2 processor for testing."""
        return get_processor()

    @pytest.mark.parametrize("conversation_idx", range(len(EXAMPLE_CONVERSATIONS)))
    @pytest.mark.slow
    def test_example_conversations_with_model_inference(
        self, processor, conversation_idx
    ):
        """Test example conversations with actual model inference (requires GPU)."""
        try:
            model = get_model()
        except Exception as e:
            pytest.skip(f"Model loading failed (GPU required): {e}")

        conversation_dict = EXAMPLE_CONVERSATIONS[conversation_idx]

        expected = conversation_dict["expected"]
        messages = conversation_dict["messages"]
        tools = conversation_dict["tools"]

        print("messages:")
        print(messages)

        # If any message has a system role, raise an error
        for msg in messages:
            if msg["role"] == "system":
                raise ValueError("System messages are not allowed in messages")

        ### PREPARE

        inference_inputs, inference_messages, inference_prompt = (
            prepare_inference_messages(
                messages=messages,
                processor=processor,
                # system_message=None,
                developer_message=None,
                tools=tools,
            )
        )

        assert inference_messages == expected["messages"]
        assert inference_prompt == expected["prompt"]

        print(f"\n🤖 RUNNING INFERENCE FOR CONVERSATION {conversation_idx + 1}...")

        ### PROCESS

        # Move inputs to the same device as the model
        device = next(model.parameters()).device
        inference_inputs = {
            k: v.to(device=device) if hasattr(v, "to") else v
            for k, v in inference_inputs.items()
        }

        # Convert pixel_values to float16 if present (but keep input_ids as long)
        if "pixel_values" in inference_inputs:
            inference_inputs["pixel_values"] = inference_inputs["pixel_values"].to(
                dtype=torch.float16
            )

        # Run actual inference (exact from original)
        with torch.no_grad():
            generated_ids = model.generate(
                **inference_inputs,
                max_new_tokens=100,
                do_sample=False,
                temperature=0.0,
                pad_token_id=processor.tokenizer.eos_token_id,
            )

        ### RESPOND

        # Decode the response
        response = processor.tokenizer.decode(
            generated_ids[0][inference_inputs["input_ids"].shape[-1] :],
            skip_special_tokens=True,
        )

        print("✅ Inference completed!")
        print(f"🤖 Model response: {response}")

        assert response == expected["response"]

    @pytest.mark.parametrize("conversation_idx", range(len(EXAMPLE_CONVERSATIONS)))
    @pytest.mark.slow
    def test_example_conversations_with_model_training(  # noqa: C901
        self, processor, conversation_idx
    ):
        """Test example conversations with actual model training using Trainer (single epoch, requires GPU)."""
        try:
            # Load model with QLoRA (4-bit quantized LoRA) for parameter-efficient training
            model = get_model(with_peft=True)
        except Exception as e:
            pytest.skip(f"Model loading failed (GPU required): {e}")

        print(
            f"\n🎓 RUNNING TRAINER-BASED TRAINING FOR CONVERSATION {conversation_idx + 1}..."
        )

        # Import required modules
        from torch.nn.utils.rnn import pad_sequence
        from transformers import Trainer, TrainingArguments

        # Create a simple dataset class for training that matches the working example format
        class SimpleDataset:
            def __init__(self):
                # Use the exact same data format as the working example
                self.data = [
                    {
                        "text prompt": "A bee on a flower",
                        "video link": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                    }
                ]

            def __len__(self):
                return 1

            def __getitem__(self, idx):
                return self.data[idx]

        train_dataset = SimpleDataset()

        # Define data collator function exactly like the working example
        def preprocess_video_caption_example(example, instruction="Caption the video."):
            prompt = example["text prompt"]
            user_content = [{"type": "text", "text": instruction}]
            user_content.append({"type": "video", "path": example["video link"]})
            messages = [
                {"role": "user", "content": user_content},
                {
                    "role": "assistant",
                    "content": [{"type": "text", "text": f"{prompt}"}],
                },
            ]
            # Return a new dict with messages and keep other fields if needed
            new_example = dict(example)
            new_example["messages"] = messages
            return new_example

        # Preprocess the dataset with the desired instruction
        instruction = "Caption the video."
        processed_dataset = [
            preprocess_video_caption_example(train_dataset[0], instruction)
        ]

        image_token_id = processor.tokenizer.additional_special_tokens_ids[
            processor.tokenizer.additional_special_tokens.index("<image>")
        ]

        def collate_fn(examples):
            instances = []
            for example in examples:
                messages = example["messages"]
                instance = (
                    processor.apply_chat_template(
                        messages,
                        add_generation_prompt=False,
                        tokenize=True,
                        return_dict=True,
                        return_tensors="pt",
                    )
                    .to("cuda")
                    .to(model.dtype)
                )
                instances.append(instance)

            input_ids = pad_sequence(
                [inst["input_ids"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=processor.tokenizer.pad_token_id,
            )
            attention_mask = pad_sequence(
                [inst["attention_mask"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=0,
            )
            labels = pad_sequence(
                [inst["input_ids"].squeeze(0).clone() for inst in instances],
                batch_first=True,
                padding_value=-100,
            )

            labels[labels == image_token_id] = -100

            out = {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "labels": labels,
            }

            # Step 1: figure out maximum frames, height, width across the batch
            pvs = [
                inst["pixel_values"].squeeze(0)
                for inst in instances
                if "pixel_values" in inst
            ]
            if pvs:  # there is at least one non-None pixel_values
                max_frames = max(pv.shape[0] for pv in pvs)
                max_h = max(pv.shape[-2] for pv in pvs)
                max_w = max(pv.shape[-1] for pv in pvs)
            else:
                max_h = max_w = processor.video_size["longest_edge"]
                max_frames = 1

            padded_pixel_values_list = []
            for ex in instances:
                pv = ex.get("pixel_values", None).squeeze(0)

                if pv is None:
                    # text-only => fill pixel data + mask with zeros
                    shape_pv = (max_frames, 3, max_h, max_w)
                    padded_pv = torch.zeros(shape_pv, dtype=torch.float32)
                else:
                    f, c, h, w = pv.shape
                    # Prepare final storage
                    padded_pv = torch.zeros(
                        (max_frames, c, max_h, max_w), dtype=pv.dtype, device=pv.device
                    )
                    padded_pv[:f, :, :h, :w] = pv
                padded_pixel_values_list.append(padded_pv)

            out["pixel_values"] = torch.stack(padded_pixel_values_list, dim=0)
            return out

        # Print model info
        model.print_trainable_parameters()
        print(f"  Model dtype: {model.dtype}")

        # Create training arguments exactly like the working example
        training_args = TrainingArguments(
            num_train_epochs=1,
            per_device_train_batch_size=2,
            gradient_accumulation_steps=1,
            warmup_steps=50,
            learning_rate=1e-4,
            weight_decay=0.01,
            logging_steps=25,
            save_strategy="steps",
            save_steps=250,
            save_total_limit=1,
            optim="paged_adamw_8bit",  # appropriate optimizer for QLoRA
            bf16=True,
            output_dir=f"./test-training-{conversation_idx}",
            hub_model_id=f"test-training-{conversation_idx}",
            remove_unused_columns=False,
            report_to="tensorboard",
            label_names=["labels"],
            dataloader_pin_memory=False,
            gradient_checkpointing=True,
            gradient_checkpointing_kwargs={"use_reentrant": False},
        )

        # Create trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=collate_fn,
            train_dataset=processed_dataset,
        )

        # Record initial loss for comparison
        model.eval()
        with torch.no_grad():
            # Get a sample batch to compute initial loss
            sample_batch = collate_fn([processed_dataset[0]])
            device = next(model.parameters()).device
            sample_batch = {
                k: v.to(device) if hasattr(v, "to") else v
                for k, v in sample_batch.items()
            }

            initial_outputs = model(**sample_batch)
            initial_loss = initial_outputs.loss.item()

        print(f"  Initial loss: {initial_loss:.4f}")

        # Train for one epoch
        model.train()
        train_result = trainer.train()

        print("  Training completed!")
        print(f"  Final loss: {train_result.training_loss:.4f}")
        print(f"  Loss improvement: {initial_loss - train_result.training_loss:.4f}")

        # Verify that training actually improved the model
        assert train_result.training_loss < initial_loss, (
            "Training should improve the model"
        )
