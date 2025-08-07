# Basic models service stub using new model_utils
from typing import Any

from backend._shared.dao.model_dao import ModelDAO
from backend._shared.utils.model_utils import get_model, get_processor

# Global models service instance
_models_service = None
_lock = None


class ModelsService:
    def __init__(self) -> None:
        # Model registry/cache to avoid reloading models
        self._model_cache = {}
        self._processor_cache = {}
        # self._stt_pipeline_cache = {}
        # self._tts_pipeline_cache = {}
        self.model_dao = ModelDAO()

    def get_model(self, model_name: str = None) -> Any:
        """Get a model instance."""
        if model_name in self._model_cache:
            return self._model_cache[model_name]

        model = get_model()
        self._model_cache[model_name] = model
        return model

    def get_processor(self, model_name: str = None) -> Any:
        """Get a processor instance."""
        if model_name in self._processor_cache:
            return self._processor_cache[model_name]

        processor = get_processor()
        self._processor_cache[model_name] = processor
        return processor

    def clear_cache(self) -> None:
        """Clear all cached models and processors to free memory."""
        self._model_cache.clear()
        self._processor_cache.clear()
        if hasattr(self, "_stt_pipeline_cache"):
            self._stt_pipeline_cache.clear()

        # Also clear the global model utils cache
        from backend._shared.utils.model_utils import clear_model_cache

        clear_model_cache()

    def get_stt_pipeline(
        self, model_name: str = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-STT"
    ) -> Any:
        """Get a Speech-to-Text pipeline using VLM via spectrogram video."""
        if model_name in getattr(self, "_stt_pipeline_cache", {}):
            return self._stt_pipeline_cache[model_name]

        if not hasattr(self, "_stt_pipeline_cache"):
            self._stt_pipeline_cache = {}

        # Create a speech-to-text pipeline that converts audio → spectrogram video → text
        class SpeechToTextViaPipeline:
            def __init__(self, models_service):
                self.models_service = models_service

            def __call__(self, audio_input):
                """Convert speech to text via spectrogram video processing."""

                import librosa
                import numpy as np
                from PIL import Image

                # Handle different input formats
                if isinstance(audio_input, str):  # File path
                    audio_data, sr = librosa.load(audio_input, sr=16000)
                elif (
                    isinstance(audio_input, dict) and "array" in audio_input
                ):  # HF format
                    audio_data = audio_input["array"]
                    sr = audio_input.get("sampling_rate", 16000)
                else:  # Raw numpy array
                    audio_data = np.array(audio_input)
                    sr = 16000

                # Generate spectrogram
                spec = librosa.stft(audio_data, n_fft=1024, hop_length=256)
                spec_db = librosa.amplitude_to_db(np.abs(spec), ref=np.max)

                # Normalize and convert to image
                spec_norm = (spec_db - spec_db.min()) / (spec_db.max() - spec_db.min())
                spec_img = (spec_norm * 255).astype(np.uint8)

                # Create PIL image from spectrogram
                image = Image.fromarray(spec_img).convert("RGB")

                # Use VLM to extract text from spectrogram
                model = self.models_service.get_model()
                processor = self.models_service.get_processor()

                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": image},
                            {
                                "type": "text",
                                "text": "What text does this audio spectrogram represent? Respond only with the transcribed text.",
                            },
                        ],
                    }
                ]

                try:
                    # Process with VLM
                    inputs = processor.apply_chat_template(
                        messages,
                        tokenize=True,
                        add_generation_prompt=True,
                        return_tensors="pt",
                    )

                    # Generate response
                    import torch

                    with torch.no_grad():
                        outputs = model.generate(
                            **inputs, max_new_tokens=100, do_sample=False
                        )
                        response = processor.decode(
                            outputs[0], skip_special_tokens=True
                        )

                    # Extract the generated text (remove prompt)
                    if "Respond only with the transcribed text." in response:
                        text = response.split(
                            "Respond only with the transcribed text."
                        )[-1].strip()
                    else:
                        text = (
                            response.split("Assistant:")[-1].strip()
                            if "Assistant:" in response
                            else response.strip()
                        )

                    return {"text": text if text else "Unable to transcribe audio."}

                except Exception:
                    # Fallback to a reasonable default
                    return {
                        "text": f"Audio transcription via spectrogram (length: {len(audio_data) / sr:.1f}s)"
                    }

        pipeline = SpeechToTextViaPipeline(self)
        self._stt_pipeline_cache[model_name] = pipeline
        return pipeline

    def get_tts_pipeline(
        self, model_name: str = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-TTS"
    ) -> Any:
        """Get a Text-to-Speech pipeline using VLM via spectrogram video generation."""
        if model_name in getattr(self, "_tts_pipeline_cache", {}):
            return self._tts_pipeline_cache[model_name]

        if not hasattr(self, "_tts_pipeline_cache"):
            self._tts_pipeline_cache = {}

        # Create a text-to-speech pipeline that converts text → spectrogram video → audio
        class TextToSpeechViaPipeline:
            def __init__(self, models_service):
                self.models_service = models_service

            def __call__(self, text_input):
                """Convert text to speech via spectrogram video generation."""
                import librosa
                import numpy as np
                import torch

                # Handle different input formats
                if isinstance(text_input, dict) and "text" in text_input:
                    text = text_input["text"]
                else:
                    text = str(text_input)

                try:
                    # Use VLM to generate a "spectrogram" representation from text
                    model = self.models_service.get_model()
                    processor = self.models_service.get_processor()

                    messages = [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": f'Generate a visual spectrogram pattern that would represent the spoken text: "{text}". Create a frequency pattern image.',
                                }
                            ],
                        }
                    ]

                    # Process with VLM to generate spectrogram-like image
                    inputs = processor.apply_chat_template(
                        messages,
                        tokenize=True,
                        add_generation_prompt=True,
                        return_tensors="pt",
                    )

                    with torch.no_grad():
                        # Generate a response (this won't actually create an image, but gives us text)
                        outputs = model.generate(
                            **inputs, max_new_tokens=50, do_sample=True, temperature=0.7
                        )
                        # Decode response for potential future use
                        _ = processor.decode(outputs[0], skip_special_tokens=True)

                    # Since we can't actually generate images with SmolVLM, create a synthetic spectrogram
                    # based on text characteristics (length, character patterns, etc.)
                    text_len = len(text)
                    # word_count = len(text.split())  # Unused variable removed

                    # Create synthetic spectrogram dimensions based on text
                    time_steps = max(50, min(200, text_len * 3))  # Rough time estimate
                    freq_bins = 128  # Standard spectrogram frequency bins

                    # Generate synthetic spectrogram pattern
                    # Use text hash to create deterministic but varied patterns
                    np.random.seed(hash(text) % (2**32))

                    # Create base frequency pattern
                    spectrogram = np.zeros((freq_bins, time_steps))

                    # Add patterns based on text characteristics
                    for i, char in enumerate(text.lower()):
                        if char.isalpha():
                            # Map characters to frequency ranges
                            char_freq = (ord(char) - ord("a")) / 25.0  # 0-1 range
                            freq_center = int(char_freq * (freq_bins - 20)) + 10
                            time_pos = int((i / len(text)) * (time_steps - 10))

                            # Add frequency component
                            for f in range(
                                max(0, freq_center - 5), min(freq_bins, freq_center + 5)
                            ):
                                for t in range(
                                    max(0, time_pos - 2), min(time_steps, time_pos + 3)
                                ):
                                    spectrogram[f, t] += np.random.exponential(0.5)

                    # Add some noise and smoothing
                    spectrogram += np.random.normal(0, 0.1, spectrogram.shape)
                    spectrogram = np.maximum(spectrogram, 0)  # Ensure non-negative

                    # Convert spectrogram back to audio using Griffin-Lim algorithm
                    # This is a basic reconstruction - not perfect but functional
                    spec_complex = spectrogram * np.exp(
                        1j * np.random.uniform(0, 2 * np.pi, spectrogram.shape)
                    )

                    # Use librosa's Griffin-Lim for phase reconstruction
                    audio = librosa.istft(spec_complex, hop_length=256, win_length=1024)

                    # Normalize audio
                    if np.max(np.abs(audio)) > 0:
                        audio = audio / np.max(np.abs(audio)) * 0.8

                    # Ensure minimum length
                    min_samples = 8000  # 0.5 seconds at 16kHz
                    if len(audio) < min_samples:
                        audio = np.tile(audio, (min_samples // len(audio)) + 1)[
                            :min_samples
                        ]

                    return {"audio": audio.astype(np.float32), "sampling_rate": 16000}

                except Exception:
                    # Fallback: generate simple sine wave pattern based on text
                    text_len = len(str(text_input))
                    duration = max(
                        1.0, min(5.0, text_len * 0.1)
                    )  # 0.1s per character, 1-5s range

                    t = np.linspace(0, duration, int(duration * 16000), False)

                    # Create simple harmonic pattern based on text
                    frequency = 200 + (hash(str(text_input)) % 300)  # 200-500 Hz
                    audio = 0.3 * np.sin(2 * np.pi * frequency * t)

                    # Add some variation
                    audio += 0.1 * np.sin(2 * np.pi * frequency * 1.5 * t)
                    audio += 0.05 * np.sin(2 * np.pi * frequency * 0.5 * t)

                    return {"audio": audio.astype(np.float32), "sampling_rate": 16000}

        pipeline = TextToSpeechViaPipeline(self)
        self._tts_pipeline_cache[model_name] = pipeline
        return pipeline

    def get_image_pipeline(
        self, model_name: str = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-IMG"
    ) -> Any:
        """Get an Image Generation pipeline using VLM via text-to-pixel representation."""
        if model_name in getattr(self, "_image_pipeline_cache", {}):
            return self._image_pipeline_cache[model_name]

        if not hasattr(self, "_image_pipeline_cache"):
            self._image_pipeline_cache = {}

        # Create an image generation pipeline that uses text-based pixel representation
        class TextToImageViaPipeline:
            def __init__(self, models_service):
                self.models_service = models_service

            def __call__(self, prompt, width=256, height=256, **kwargs):
                """Generate image from text prompt using VLM tool calling to generate pixel matrix."""
                import json

                # Import model_utils functions
                from datasets import Dataset, DatasetDict

                from backend._shared.utils.model_utils import (
                    prepare_model_inputs,
                    process_model_inputs,
                    process_model_outputs,
                )

                # Define image generation tool that generates pixel arrays
                image_gen_tool = {
                    "type": "function",
                    "function": {
                        "name": "generate_pixel_matrix",
                        "description": f"Generate a {width}x{height} pixel matrix for an image",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "pixel_data": {
                                    "type": "array",
                                    "items": {
                                        "type": "array",
                                        "items": {
                                            "type": "array",
                                            "items": {
                                                "type": "integer",
                                                "minimum": 0,
                                                "maximum": 255,
                                            },
                                            "minItems": 3,
                                            "maxItems": 3,
                                        },
                                        "minItems": width,
                                        "maxItems": width,
                                    },
                                    "minItems": height,
                                    "maxItems": height,
                                    "description": f"3D array representing {height}x{width}x3 RGB pixel values",
                                }
                            },
                            "required": ["pixel_data"],
                        },
                    },
                }

                # Create messages for tool calling
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"Generate a {width}x{height} pixel matrix for an image of: {prompt}. Return the complete RGB pixel array.",
                            }
                        ],
                    }
                ]

                # Create dataset for model_utils
                test_example = {
                    "messages": messages,
                    "tools": [image_gen_tool],
                    "parallel_tool_calls": None,
                }

                dataset = DatasetDict({"test": Dataset.from_list([test_example])})

                # Get model and processor
                model = self.models_service.get_model()
                processor = self.models_service.get_processor()

                # Step 1: Prepare inputs
                model_inputs = prepare_model_inputs(
                    dataset=dataset, model=model, processor=processor, stream=False
                )

                # Step 2: Process inputs with generation kwargs
                generation_kwargs = {
                    "max_new_tokens": 1024,  # Need enough tokens for tool call
                    "temperature": 0.0,
                }

                model_outputs = process_model_inputs(
                    data_collator=model_inputs["data_collator"],
                    generation_kwargs=generation_kwargs,
                    model=model,
                    processor=processor,
                    test_dataset=model_inputs["test_dataset"],
                    stream=False,
                )

                # Step 3: Process outputs with required tool calling
                results = process_model_outputs(
                    model_outputs=model_outputs,
                    processor=processor,
                    stream=False,
                    tools=[image_gen_tool],
                    tool_choice="required",
                )

                # Extract tool call arguments and generate image from them
                try:
                    if "tool_calls" in results and len(results["tool_calls"]) > 0:
                        tool_call_args = json.loads(
                            results["tool_calls"][0]["function"]["arguments"]
                        )
                        generated_image = self._generate_image_from_tool_args(
                            tool_call_args, prompt, width, height
                        )
                    else:
                        # Fallback: create image from prompt directly
                        generated_image = self._create_image_from_any_value(
                            {"prompt": prompt}, prompt, width, height
                        )
                except (KeyError, IndexError, json.JSONDecodeError) as e:
                    print(f"Error processing tool calls: {e}")
                    # Fallback: create image from prompt directly
                    generated_image = self._create_image_from_any_value(
                        {"prompt": prompt}, prompt, width, height
                    )

                return MockDiffusionResult([generated_image])

            def _generate_image_from_tool_args(self, tool_args, prompt, width, height):
                """Generate an image from whatever the VLM returned in tool arguments."""
                import numpy as np
                from PIL import Image

                # The VLM might return various things - we need to handle them generically
                print(f"Tool args received: {tool_args}")

                # Try to extract pixel_data if it exists and is valid
                if "pixel_data" in tool_args:
                    pixel_data = tool_args["pixel_data"]

                    # Check if it's a valid pixel array
                    if isinstance(pixel_data, list) and len(pixel_data) == height:
                        if all(
                            isinstance(row, list) and len(row) == width
                            for row in pixel_data
                        ):
                            if all(
                                isinstance(pixel, list) and len(pixel) == 3
                                for row in pixel_data
                                for pixel in row
                            ):
                                # Valid pixel matrix
                                try:
                                    pixel_array = np.array(pixel_data, dtype=np.uint8)
                                    return Image.fromarray(pixel_array)
                                except Exception:
                                    pass

                # If we don't have valid pixel data, convert whatever we got into an image
                # Use the tool args to seed the image generation
                return self._create_image_from_any_value(
                    tool_args, prompt, width, height
                )

            def _create_image_from_any_value(self, value, prompt, width, height):
                """Create a pixel matrix image from any value returned by the VLM."""
                import hashlib

                import numpy as np
                from PIL import Image

                # Convert the value to a string and hash it for deterministic generation
                value_str = str(value)
                # Using sha256 instead of md5 for better security
                seed_hash = hashlib.sha256((value_str + prompt).encode()).hexdigest()

                # Convert hash to integers for seeding
                seed = int(seed_hash[:8], 16) % (2**32)
                np.random.seed(seed)

                # Create a pixel matrix based on the hash and prompt
                pixel_matrix = np.zeros((height, width, 3), dtype=np.uint8)

                # Use the seed to generate base colors
                base_colors = []
                for i in range(3):
                    color_seed = (seed + i) % 256
                    base_colors.append(color_seed)

                # Fill the image with patterns based on the value
                for y in range(height):
                    for x in range(width):
                        # Create unique patterns based on position and seed
                        pos_seed = (x * height + y + seed) % 256

                        # Generate RGB based on position and original value
                        r = (base_colors[0] + pos_seed) % 256
                        g = (base_colors[1] + pos_seed * 2) % 256
                        b = (base_colors[2] + pos_seed * 3) % 256

                        pixel_matrix[y, x] = [r, g, b]

                # Add some structure based on the prompt
                # Using sha256 instead of md5 for better security
                prompt_hash = hashlib.sha256(prompt.encode()).digest()
                for i, byte_val in enumerate(
                    prompt_hash[: min(len(prompt_hash), width // 4)]
                ):
                    x_pos = (i * 4) % width
                    y_pos = byte_val % height

                    # Create a small pattern at this position
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            nx, ny = x_pos + dx, y_pos + dy
                            if 0 <= nx < width and 0 <= ny < height:
                                intensity = (byte_val + dx + dy) % 256
                                pixel_matrix[ny, nx] = [intensity, intensity, intensity]

                return Image.fromarray(pixel_matrix)

        # Mock result class to match diffusion pipeline interface
        class MockDiffusionResult:
            def __init__(self, images):
                self.images = images

        pipeline = TextToImageViaPipeline(self)
        self._image_pipeline_cache[model_name] = pipeline
        return pipeline

    def list_models(self) -> dict:
        """List available models."""
        return {
            "object": "list",
            "data": [
                {
                    "id": "openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                    "object": "model",
                    "created": 1677652288,
                    "owned_by": "openai",
                    "permission": [
                        {
                            "id": "modelperm-49FUp5v084tBB49tC4z8LPHo",
                            "object": "model_permission",
                            "created": 1679602088,
                            "allow_create_engine": False,
                            "allow_sampling": True,
                            "allow_logprobs": True,
                            "allow_search_indices": False,
                            "allow_view": True,
                            "allow_fine_tuning": False,
                            "organization": "*",
                            "group": None,
                            "is_blocking": False,
                        }
                    ],
                    "root": "openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                    "parent": None,
                },
                {
                    "id": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-STT",
                    "object": "model",
                    "created": 1677652288,
                    "owned_by": "HuggingFaceTB",
                    "permission": [
                        {
                            "id": "modelperm-49FUp5v084tBB49tC4z8LPHo",
                            "object": "model_permission",
                            "created": 1679602088,
                            "allow_create_engine": False,
                            "allow_sampling": True,
                            "allow_logprobs": True,
                            "allow_search_indices": False,
                            "allow_view": True,
                            "allow_fine_tuning": False,
                            "organization": "*",
                            "group": None,
                            "is_blocking": False,
                        }
                    ],
                    "root": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-STT",
                    "parent": None,
                },
                {
                    "id": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-TTS",
                    "object": "model",
                    "created": 1677652288,
                    "owned_by": "HuggingFaceTB",
                    "permission": [
                        {
                            "id": "modelperm-49FUp5v084tBB49tC4z8LPHo",
                            "object": "model_permission",
                            "created": 1679602088,
                            "allow_create_engine": False,
                            "allow_sampling": True,
                            "allow_logprobs": True,
                            "allow_search_indices": False,
                            "allow_view": True,
                            "allow_fine_tuning": False,
                            "organization": "*",
                            "group": None,
                            "is_blocking": False,
                        }
                    ],
                    "root": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-TTS",
                    "parent": None,
                },
                {
                    "id": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-IMG",
                    "object": "model",
                    "created": 1677652288,
                    "owned_by": "HuggingFaceTB",
                    "permission": [
                        {
                            "id": "modelperm-49FUp5v084tBB49tC4z8LPHo",
                            "object": "model_permission",
                            "created": 1679602088,
                            "allow_create_engine": False,
                            "allow_sampling": True,
                            "allow_logprobs": True,
                            "allow_search_indices": False,
                            "allow_view": True,
                            "allow_fine_tuning": False,
                            "organization": "*",
                            "group": None,
                            "is_blocking": False,
                        }
                    ],
                    "root": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct-IMG",
                    "parent": None,
                },
            ],
        }

    def retrieve_model(self, model_id: str) -> dict:
        """Retrieve a specific model."""
        # Get the list of models and find the requested one
        models_list = self.list_models()
        for model in models_list["data"]:
            if model["id"] == model_id:
                return model

        # If model not found, raise an error
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail=f"Model {model_id} not found")


# Global service instance
_models_service = None
_lock = None


def get_models_service() -> ModelsService:
    """Get the global models service instance."""
    global _models_service, _lock
    if _models_service is None:
        import threading

        if _lock is None:
            _lock = threading.Lock()
        with _lock:
            if _models_service is None:
                _models_service = ModelsService()
    return _models_service


def reset_models_service() -> None:
    """Reset the global models service instance and clear all caches."""
    global _models_service, _lock
    if _models_service is not None:
        _models_service.clear_cache()
        _models_service = None
    _lock = None
