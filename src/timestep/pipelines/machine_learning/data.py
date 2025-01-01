import json
from typing import Dict, Union

import PIL
import torch
from datasets import interleave_datasets, load_dataset
from datasets.features import Features, Image, Sequence, Value
from transformers import PreTrainedModel, ProcessorMixin

seed = 42
stopping_strategy = "first_exhausted"


def create_conversation_features():
    """
    Creates a Feature object representing a conversation with multi-modal content.
    Format:
    - Each message has a role (user/assistant) and a list of content items
    - Content items can be text or images

    Returns:
        datasets.Features: A Feature object for conversations
    """
    content_list_feature = {
        "type": Value("string"),  # 'text' or 'image'
        "text": Value("string", id=None),  # Used when type is 'text'
        "image": Value(
            "string", id=None
        ),  # Used when type is 'image' - stores image path/url/bytes
    }

    content_string_feature = Value("string")

    tool_call_feature = {
        "function": {
            "arguments": Value("string"),
            "description": Value("string"),
            "name": Value("string"),
        },
        "id": Value("string"),
        "type": Value("string"),
    }

    message_feature = {
        "content": Union[Sequence(content_list_feature), content_string_feature],
        "role": Value("string"),
        "tool_calls": Sequence(tool_call_feature),
    }

    parameters_feature = {
        "properties": Dict,
        "required": Sequence(Value("string")),
        "type": Value("string"),
    }

    tool_feature = {
        "function": {
            "description": Value("string"),
            "name": Value("string"),
            "parameters": parameters_feature,
        },
        "type": Value("string"),
    }

    conversation_features = Features(
        {
            "completion": Sequence(message_feature),
            "images": Sequence(Image()),
            "messages": Sequence(message_feature),
            "prompt": Sequence(message_feature),
            "tools": Sequence(tool_feature),
        }
    )

    return conversation_features


features = create_conversation_features()


def load_and_transform_chat_threads(features):
    # chat_threads_train_dataset = load_dataset(
    #     "mjschock/chat_threads", split="train", streaming=True
    # )

    chat_threads_dataset = load_dataset("mjschock/chat_threads", streaming=True)

    chat_threads_train_dataset = chat_threads_dataset["train"]
    chat_threads_validation_dataset = chat_threads_dataset["validation"]
    chat_threads_test_dataset = chat_threads_dataset["test"]

    def transform_chat_threads(
        sample,
        indices,
    ):
        messages = json.loads(sample["messages"])
        tools = json.loads(sample["tools"])

        # TODO: adjust call_id to call_0, call_1, etc.

        return {
            "messages": messages,
            "tools": tools,
        }

    chat_threads_train_dataset = chat_threads_train_dataset.map(
        transform_chat_threads,
        batched=False,
        features=features,
        # remove_columns=chat_threads_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert chat_threads_train_dataset.column_names == list(
        features.keys()
    ), f"{chat_threads_train_dataset.column_names} != {list(features.keys())}"

    chat_threads_validation_dataset = chat_threads_validation_dataset.map(
        transform_chat_threads,
        batched=False,
        features=features,
        # remove_columns=chat_threads_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert chat_threads_validation_dataset.column_names == list(
        features.keys()
    ), f"{chat_threads_validation_dataset.column_names} != {list(features.keys())}"

    chat_threads_test_dataset = chat_threads_test_dataset.map(
        transform_chat_threads,
        batched=False,
        features=features,
        # remove_columns=chat_threads_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert chat_threads_test_dataset.column_names == list(
        features.keys()
    ), f"{chat_threads_test_dataset.column_names} != {list(features.keys())}"

    return (
        chat_threads_train_dataset,
        chat_threads_validation_dataset,
        chat_threads_test_dataset,
    )


# chat_threads_train_dataset = load_and_transform_chat_threads(features)
(
    chat_threads_train_dataset,
    chat_threads_validation_dataset,
    chat_threads_test_dataset,
) = load_and_transform_chat_threads(features)


def load_and_transform_the_cauldron(features, name):
    the_cauldron_train_dataset = load_dataset(
        "HuggingFaceM4/the_cauldron", name=name, split="train", streaming=True
    )

    def transform_the_cauldron(sample, indices):
        return {"images": sample["images"], "messages": sample["texts"]}

    the_cauldron_train_dataset = the_cauldron_train_dataset.map(
        transform_the_cauldron,
        batched=False,
        features=features,
        remove_columns=the_cauldron_train_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert the_cauldron_train_dataset.column_names == list(
        features.keys()
    ), f"{the_cauldron_train_dataset.column_names} != {list(features.keys())}"

    return (the_cauldron_train_dataset, None, None)


names = [
    "ai2d",
    "aokvqa",
    "chart2text",
    "chartqa",
    "clevr",
    # "clevr_math", # FileNotFoundError: [Errno 2] No such file or directory: '/fsx/m4/datasets/downloads/extracted/3c4c03ad359586cd332583e3a61e1ef5808cc52f30cef52648847fd19d477eac/CLEVR_v1.0/images/train/CLEVR_train_000000.png'
    "cocoqa",
    "datikz",
    "diagram_image_to_text",
    "docvqa",
    "dvqa",
    "figureqa",
    "finqa",
    "geomverse",
    "hateful_memes",
    "hitab",
    "iam",
    "iconqa",
    "infographic_vqa",
    "intergps",
    "localized_narratives",
    "mapqa",
    "mimic_cgd",
    "multihiertt",
    "nlvr2",
    "ocrvqa",
    "okvqa",
    "plotqa",
    "raven",
    "rendered_text",
    "robut_sqa",
    "robut_wikisql",
    "robut_wtq",
    "scienceqa",
    "screen2words",
    "spot_the_diff",
    "st_vqa",
    "tabmwp",
    "tallyqa",
    "tat_qa",
    "textcaps",
    "textvqa",
    "tqa",
    "vistext",
    "visual7w",
    "visualmrc",
    "vqarad",
    "vqav2",
    "vsr",
    "websight",
]

the_cauldron_train_datasets = [
    load_and_transform_the_cauldron(features, name=name)[0] for name in names
]


def load_and_transform_code_act_dataset(features):
    code_act_train_dataset = load_dataset(
        "xingyaoww/code-act",
        split="codeact",
        streaming=True,
    )

    def transform_code_act(
        sample,
        indices,
    ):
        return {
            "messages": sample["conversations"],
        }

    code_act_train_dataset = code_act_train_dataset.map(
        transform_code_act,
        batched=False,
        features=features,
        remove_columns=code_act_train_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert code_act_train_dataset.column_names == list(
        features.keys()
    ), f"{code_act_train_dataset.column_names} != {list(features.keys())}"

    return code_act_train_dataset, None, None


code_act_train_dataset, _, _ = load_and_transform_code_act_dataset(features)


def load_and_transform_latex_dataset(features):
    latex_ocr_train_dataset = load_dataset(
        "unsloth/LaTeX_OCR", split="train", streaming=True
    )

    latex_ocr_validation_dataset = load_dataset(
        "unsloth/LaTeX_OCR", split="test", streaming=True
    )

    def transform_latex_ocr(
        sample,
        indices,
    ):
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Write the LaTeX representation for this image.",
                    },
                    {"type": "image"},
                ],
            },
            {
                "role": "assistant",
                "content": [{"type": "text", "text": sample["text"]}],
            },
        ]

        return {
            "completion": messages[1:],
            "images": [sample["image"]],
            "prompt": messages[:1],
        }

    latex_ocr_train_dataset = latex_ocr_train_dataset.map(
        transform_latex_ocr,
        batched=False,
        features=features,
        remove_columns=latex_ocr_train_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert latex_ocr_train_dataset.column_names == list(
        features.keys()
    ), f"{latex_ocr_train_dataset.column_names} != {list(features.keys())}"

    latex_ocr_validation_dataset = latex_ocr_validation_dataset.map(
        transform_latex_ocr,
        batched=False,
        features=features,
        remove_columns=latex_ocr_validation_dataset.column_names,
        with_indices=True,
        batch_size=1,
    )

    assert latex_ocr_validation_dataset.column_names == list(
        features.keys()
    ), f"{latex_ocr_validation_dataset.column_names} != {list(features.keys())}"

    return latex_ocr_train_dataset, latex_ocr_validation_dataset, None


latex_ocr_train_dataset, latex_ocr_validation_dataset, _ = (
    load_and_transform_latex_dataset(features)
)

train_dataset = interleave_datasets(
    [chat_threads_train_dataset, code_act_train_dataset, latex_ocr_train_dataset],
    seed=seed,
    stopping_strategy=stopping_strategy,
)

assert train_dataset.column_names == list(
    features.keys()
), f"{train_dataset.column_names} != {list(features.keys())}"

validation_dataset = interleave_datasets(
    [chat_threads_validation_dataset, latex_ocr_validation_dataset],
    seed=seed,
    stopping_strategy=stopping_strategy,
)

assert validation_dataset.column_names == list(
    features.keys()
), f"{validation_dataset.column_names} != {list(features.keys())}"

test_dataset = interleave_datasets(
    [chat_threads_test_dataset],
    seed=seed,
    stopping_strategy=stopping_strategy,
)


class MultiModalConversationalDataCollator:
    processor: ProcessorMixin
    model: PreTrainedModel

    def __init__(self, model, processor):
        self.model = model
        self.processor = processor

    def __call__(self, examples):
        conversations = []

        for example in examples:
            completion = self._extract_messages(example, messages_key="completion")
            messages = self._extract_messages(example, messages_key="messages")
            prompt = self._extract_messages(example, messages_key="prompt")
            tools = self._extract_tools(example)

            conversations.append(
                {
                    "completion": completion,
                    "images": example["images"],
                    "prompt": prompt,
                    "messages": prompt + completion if not messages else messages,
                    "tools": tools,
                }
            )

        text_batch = [
            self.processor.apply_chat_template(
                add_generation_prompt=False,
                conversation=conversation["messages"],
                documents=None,
                tokenize=False,
                tools=conversation["tools"],
                # use_cache=False,
            )
            for conversation in conversations
        ]

        tokenized_text_batch = [
            self.processor.apply_chat_template(
                add_generation_prompt=False,
                conversation=conversation["messages"],
                documents=None,
                return_assistant_tokens_mask=True,
                return_dict=True,
                return_tensors="pt",
                tokenize=True,
                tools=conversation["tools"],
                # use_cache=False,
            )
            for conversation in conversations
        ]

        images_batch = [conversation["images"] for conversation in conversations]

        for images in images_batch:
            if images is not None:
                for image in images:
                    assert (
                        type(image) == PIL.PngImagePlugin.PngImageFile
                    ), f"{type(image)} != PIL.PngImagePlugin.PngImageFile"
                    assert image.mode == "RGB", f"{image.mode} != RGB"

                    # width, height = image.size

                    # if width > 384 or height > 384:
                    #     # raise ValueError(
                    #     #     f"Image is too large: {width}x{height} > 384x384"
                    #     # )
                    #     print(f"WARN: Image is too large: {width}x{height} > 384x384")
                    #     print("Resizing image to a maximum of 384 on the longest side")
                    #     image.thumbnail((384, 384))
                    #     print(f"Resized image size: {image.size}")

        # if any images are None in the batch, we need to process them separately
        if any(images is None for images in images_batch):
            batch = {
                "attention_mask": [],
                "input_ids": [],
                "pixel_attention_mask": [],
                "pixel_values": [],
            }

            for text, images in zip(text_batch, images_batch):
                processed = self.processor(  # TODO: Set add_end_of_utterance_token=False here and below? P.S., why is the vocab size 49152 when the end_of_utterance token id is 49154?
                    text=text,
                    images=images,
                    return_tensors="pt",
                    size={"longest_edge": 3 * 384},
                )

                batch["attention_mask"].append(processed["attention_mask"])
                batch["input_ids"].append(processed["input_ids"])

                if "pixel_attention_mask" in processed:
                    batch["pixel_attention_mask"].append(
                        processed["pixel_attention_mask"]
                    )

                else:
                    batch["pixel_attention_mask"].append(torch.tensor([]))

                if "pixel_values" in processed:
                    batch["pixel_values"].append(processed["pixel_values"])

                else:
                    batch["pixel_values"].append(torch.tensor([]))

            for key, value in batch.items():
                batch[key] = torch.cat(value, dim=0)

        else:
            batch = self.processor(
                text=text_batch,
                images=images_batch,
                return_tensors="pt",
                size={"longest_edge": 3 * 384},
            )

        assistant_masks = []
        image_token_id = self.processor.tokenizer.additional_special_tokens_ids[
            self.processor.tokenizer.additional_special_tokens.index("<image>")
        ]

        for i in range(len(batch["input_ids"])):
            assistant_mask = torch.zeros_like(batch["input_ids"][i])
            offset = 0

            for j in range(len(tokenized_text_batch[i]["input_ids"][0])):
                if tokenized_text_batch[i]["input_ids"][0][j] == image_token_id:
                    while (
                        batch["input_ids"][i][j + offset]
                        != tokenized_text_batch[i]["input_ids"][0][j + 1]
                    ):
                        offset += 1

                    offset -= 1

                else:
                    assert (
                        tokenized_text_batch[i]["input_ids"][0][j]
                        == batch["input_ids"][i][j + offset]
                    ), f"{tokenized_text_batch[i]['input_ids'][0][j]} != {batch["input_ids"][i][j+offset]}"

                    if tokenized_text_batch[i]["assistant_masks"][j] == 1:
                        assistant_mask[j + offset] = 1

            decoded_assistant_input_ids = self.processor.tokenizer.decode(
                batch["input_ids"][i][assistant_mask == 1]
            )
            decoded_assistant_tokenized_text_batch_input_ids = (
                self.processor.tokenizer.decode(
                    tokenized_text_batch[i]["input_ids"][0][
                        torch.tensor(tokenized_text_batch[i]["assistant_masks"]) == 1
                    ]
                )
            )

            assert (
                decoded_assistant_input_ids
                == decoded_assistant_tokenized_text_batch_input_ids
            ), f"{decoded_assistant_input_ids} != {decoded_assistant_tokenized_text_batch_input_ids}"

            assistant_masks.append(assistant_mask)

        assistant_masks = torch.stack(assistant_masks)
        labels = torch.where(
            assistant_masks == 1, batch["input_ids"], torch.tensor(-100)
        )

        batch["labels"] = labels

        if len(batch["pixel_attention_mask"]) == 0:
            del batch["pixel_attention_mask"]

        if len(batch["pixel_values"]) == 0:
            del batch["pixel_values"]

        return batch

    def _extract_messages(self, example, messages_key="messages"):
        messages = []

        if example[messages_key] is None:
            return messages

        for role_idx in range(len(example[messages_key]["role"])):
            message = {"role": example[messages_key]["role"][role_idx]}

            contents = example[messages_key]["content"][role_idx]

            if type(contents) == str:
                message["content"] = contents

            elif type(contents) == list:
                message["content"] = contents

            tool_calls = example[messages_key]["tool_calls"][role_idx]

            if tool_calls is not None:
                message["tool_calls"] = []

                for tool_call_idx in range(len(tool_calls["id"])):

                    tool_call = {
                        "function": {
                            "arguments": tool_calls["function"][tool_call_idx][
                                "arguments"
                            ],
                            "description": tool_calls["function"][tool_call_idx][
                                "description"
                            ],
                            "name": tool_calls["function"][tool_call_idx]["name"],
                        },
                        "id": tool_calls["id"][tool_call_idx],
                        "type": tool_calls["type"][tool_call_idx],
                    }

                    message["tool_calls"].append(tool_call)

            messages.append(message)

        return messages

    def _extract_tools(self, example):
        tools = []

        if example["tools"] is None:
            return tools

        for function_idx in range(len(example["tools"]["function"])):
            tool = {
                "function": {
                    "description": example["tools"]["function"][function_idx][
                        "description"
                    ],
                    "name": example["tools"]["function"][function_idx]["name"],
                    "parameters": example["tools"]["function"][function_idx][
                        "parameters"
                    ],
                },
                "type": example["tools"]["type"][function_idx],
            }

            tools.append(tool)

        return tools
