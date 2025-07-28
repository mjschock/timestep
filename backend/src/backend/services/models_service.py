# mypy: ignore-errors
import os
import threading
from pathlib import Path
from typing import Any

from fastapi import HTTPException

try:
    from transformers import (
        AutoModelForImageTextToText,
        AutoProcessor,
        pipeline,
    )
except ImportError:
    AutoModelForImageTextToText = Any  # type: ignore
    AutoProcessor = Any  # type: ignore
    pipeline = Any  # type: ignore

from backend.logging_config import logger
from backend.utils.model_utils import validate_chat_template

# Store PEFT adapter paths by fine-tuned model name
PEFT_ADAPTERS = {}


class ModelsService:
    def __init__(self) -> None:
        # Model registry/cache to avoid reloading models
        self._model_cache = {}
        self._processor_cache = {}
        self._pipeline_cache = {}

        # PEFT adapter management
        self._current_adapter = None  # Currently loaded adapter path
        self._model_lock = threading.RLock()  # Thread-safe model access
        self._base_model_instance = None  # Single base model instance

        # Define supported models
        self.supported_embedding_models = [
            "sentence-transformers/paraphrase-MiniLM-L3-v2",
        ]
        self.supported_image_models: list[str] = [
            "text-image-gpt2",
            # "stable-diffusion-v1-5/stable-diffusion-v1-5",
        ]
        self.supported_vlm_models = [
            "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
        ]
        self.supported_stt_models = [
            "openai/whisper-tiny",
        ]
        self.supported_tts_models = [
            "microsoft/speecht5_tts",
        ]

        self.supported_models = (
            self.supported_embedding_models
            + self.supported_image_models
            + self.supported_stt_models
            + self.supported_tts_models
            + self.supported_vlm_models
        )

        # Load chat template
        self.chat_template = self._load_chat_template()

        # Load all models as singletons during initialization
        logger.info("🚀 Initializing ModelsService - Loading all models...")
        self._load_all_models()
        logger.info("✅ All models loaded successfully!")

    def _load_chat_template(self) -> None:
        """Load the custom chat template."""
        template_path = (
            Path(__file__).parent.parent.parent.parent / "chat_template.jinja"
        )
        if template_path.exists():
            with open(template_path) as f:
                return f.read()
        else:
            logger.warning("No custom chat template found, using default")
            return None

    def _load_all_models(self) -> None:
        """
        Load all supported models as singletons during initialization.
        This ensures we can detect any loading issues upfront.
        Models are loaded in alphabetical order by category.
        """
        model_categories = [
            (
                "🔍 Loading embedding models...",
                self.supported_embedding_models,
                self.get_embedding_model,
            ),
            (
                "🎨 Loading image generation models...",
                self.supported_image_models,
                self.get_image_pipeline,
            ),
            (
                "🔊 Loading speech-to-text models...",
                self.supported_stt_models,
                self.get_stt_pipeline,
            ),
            (
                "🎵 Loading text-to-speech models...",
                self.supported_tts_models,
                self.get_tts_pipeline,
            ),
            (
                "📦 Loading VLM models...",
                self.supported_vlm_models,
                self.get_model_instance,
            ),
        ]

        for category_log, model_list, loader_func in model_categories:
            self._load_model_category(category_log, model_list, loader_func)

    def _load_model_category(
        self, category_log: str, model_list: list, loader_func
    ) -> None:
        """Load a category of models."""
        logger.info(category_log)
        for model_name in model_list:
            self._load_single_model(model_name, loader_func)

    def _load_single_model(self, model_name: str, loader_func) -> None:
        """Load a single model with error handling."""
        try:
            logger.info(f"  Loading {model_name}...")
            loader_func(model_name, use_cache=True)
            logger.info(f"  ✅ {model_name} loaded successfully")
        except Exception as e:
            logger.error(f"  ❌ Failed to load {model_name}: {e}")
            raise

    def list_models(self) -> dict[str, Any]:
        # Return a list of supported models in OpenAI-compatible format
        import time

        now = int(time.time())
        models = [
            {
                "id": model_id,
                "object": "model",
                "created": now,
                "owned_by": "system",
                "permission": [],
            }
            for model_id in self.supported_models
        ]
        return {
            "object": "list",
            "data": models,
        }

    def retrieve_model(self, model: str) -> dict[str, Any]:
        # Normalize model name by stripping 'openai/' prefix if present
        if model.startswith("openai/"):
            model = model[len("openai/") :]
        import time

        now = int(time.time())
        if model not in self.supported_models:
            raise HTTPException(status_code=404, detail=f"Model {model} not supported.")
        return {
            "id": model,
            "object": "model",
            "created": now,
            "owned_by": "system",
        }

    def delete_model(self, model: str) -> dict[str, str]:
        raise HTTPException(status_code=501, detail="Not implemented")

    def _override_chat_template(self, processor: Any, cache: bool = False) -> Any:
        if not cache:
            """Backup the original chat template."""
            original_chat_template = processor.chat_template

            with open(
                Path(__file__).parent.parent.parent.parent
                / "default_chat_template.jinja",
                "w",
            ) as f:
                f.write(original_chat_template)

        """Override the processor's chat template with our custom template."""
        template_path = (
            Path(__file__).parent.parent.parent.parent / "chat_template.jinja"
        )

        if template_path.exists():
            with open(template_path) as f:
                custom_template = f.read()

            # Load the original chat template for validation
            default_template_path = (
                Path(__file__).parent.parent.parent.parent
                / "default_chat_template.jinja"
            )
            original_chat_template = ""
            if default_template_path.exists():
                with open(default_template_path) as f:
                    original_chat_template = f.read()

            processor.chat_template = custom_template
            print(
                f"DEBUG: Chat template overridden with code act format (contains 'execute': {'execute' in custom_template})"
            )

            # Validate both the original and custom chat templates
            try:
                validate_chat_template(processor, original_chat_template)
                logger.info("✅ Chat template validation completed successfully")
            except Exception as e:
                logger.error(f"❌ Chat template validation failed: {e}")
                logger.error(
                    "🛑 Halting application due to chat template validation failure"
                )
                # Exit the process immediately to halt the entire application
                import sys

                sys.exit(1)
        else:
            print("DEBUG: No custom chat template found")

        return processor

    def get_model_instance(
        self, model_name: str, use_cache: bool = True
    ) -> tuple[Any, Any]:
        """
        Get model and processor instances with PEFT adapter support and blocking.
        """
        logger.info(f"Getting model instance for: {model_name}")
        with self._model_lock:
            # Handle fine-tuned models with PEFT adapters
            if model_name.startswith("ft:"):
                return self._handle_fine_tuned_model(model_name, use_cache)

            # Check cache first
            if use_cache and model_name in self._model_cache:
                logger.info(f"Found model in cache: {model_name}")
                return self._get_cached_model(model_name)

            # Normalize and validate model name
            normalized_model_name = self._normalize_model_name(model_name)
            logger.info(f"Normalized model name: {normalized_model_name}")
            self._validate_model_support(normalized_model_name)

            # Check cache again after normalization
            if use_cache and normalized_model_name in self._model_cache:
                logger.info(f"Found normalized model in cache: {normalized_model_name}")
                return self._get_cached_model(normalized_model_name)

        # Load model if not cached
        logger.info(f"Loading model instance: {normalized_model_name}")
        return self._load_model_instance(normalized_model_name, use_cache)

    def _handle_fine_tuned_model(
        self, model_name: str, use_cache: bool
    ) -> tuple[Any, Any]:
        """Handle fine-tuned models with PEFT adapters."""
        logger.info(f"Loading fine-tuned PEFT model {model_name}")

        # Get the PEFT adapter path from the global storage
        adapter_path = PEFT_ADAPTERS.get(model_name)

        if adapter_path and os.path.exists(adapter_path):
            return self._load_peft_model(adapter_path, use_cache)
        else:
            logger.warning(
                f"No PEFT adapter found for {model_name}, falling back to base model"
            )
            return self._fallback_to_base_model(use_cache)

    def _load_peft_model(self, adapter_path: str, use_cache: bool) -> tuple[Any, Any]:
        """Load PEFT model with adapter."""
        logger.info(f"Loading PEFT adapter from {adapter_path}")

        if self.load_peft_adapter(adapter_path):
            # Get processor from base model
            base_model_name = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
            _, processor = self.get_model_instance(base_model_name, use_cache=True)

            # Override template if available
            if self.chat_template:
                processor.chat_template = self.chat_template
            return self._base_model_instance, processor
        else:
            logger.warning("Failed to load PEFT adapter, falling back to base model")
            return self._fallback_to_base_model(use_cache)

    def _fallback_to_base_model(self, use_cache: bool) -> tuple[Any, Any]:
        """Fall back to base model when PEFT loading fails."""
        base_model_name = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
        return self.get_model_instance(base_model_name, use_cache)

    def _get_cached_model(self, model_name: str) -> tuple[Any, Any]:
        """Get cached model and processor."""
        model = self._model_cache[model_name]
        processor = self._processor_cache[model_name]
        logger.info(
            f"Retrieved cached processor for {model_name}: {processor is not None}"
        )
        # Always override template for consistency (this will also validate the template)
        if self.chat_template:
            processor = self._override_chat_template(processor, cache=True)
            logger.info(
                f"After template override for {model_name}: {processor is not None}"
            )
        return model, processor

    def _normalize_model_name(self, model_name: str) -> str:
        """Normalize model name by stripping 'openai/' prefix if present."""
        if model_name.startswith("openai/"):
            return model_name[len("openai/") :]
        return model_name

    def _validate_model_support(self, model_name: str) -> None:
        """Validate that the model is supported."""
        if model_name not in self.supported_models:
            raise HTTPException(
                status_code=404, detail=f"Model {model_name} not supported."
            )

    def _load_model_instance(self, model_name: str, use_cache: bool) -> tuple[Any, Any]:
        """Load model instance from scratch."""
        try:
            if model_name in self.supported_vlm_models:
                model, processor = self._load_vlm_model(model_name)
            else:
                raise HTTPException(
                    status_code=404, detail=f"Model {model_name} not supported."
                )

            # Cache the instances if caching is enabled
            if use_cache:
                self._model_cache[model_name] = model
                self._processor_cache[model_name] = processor

            # Override chat template if available (this will also validate the template)
            if self.chat_template:
                processor = self._override_chat_template(processor, cache=use_cache)

            return model, processor

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to load model: {e}"
            ) from e

    def _load_vlm_model(self, model_name: str) -> tuple[Any, Any]:
        """Load vision-language model."""
        import torch

        processor = AutoProcessor.from_pretrained(model_name)  # type: ignore
        model = AutoModelForImageTextToText.from_pretrained(
            model_name, torch_dtype=torch.bfloat16
        ).to("cuda")
        return model, processor

    def get_stt_pipeline(
        self, model_name: str = "openai/whisper-tiny", use_cache: bool = True
    ) -> Any:
        """
        Get a speech-to-text pipeline for transcription.

        Args:
            model_name: The name of the STT model to load
            use_cache: Whether to use cached instances (default: True)

        Returns:
            pipeline: The STT pipeline
        """
        # Check if model is supported
        if model_name not in self.supported_stt_models:
            raise HTTPException(
                status_code=404, detail=f"STT model {model_name} not supported."
            )

        # Return cached pipeline if available and caching is enabled
        cache_key = f"stt_{model_name}"
        if use_cache and cache_key in self._pipeline_cache:
            return self._pipeline_cache[cache_key]

        try:
            import torch

            pipe = pipeline(
                "automatic-speech-recognition",
                model=model_name,
                device=0 if torch.cuda.is_available() else -1,
            )

            # Cache the pipeline if caching is enabled
            if use_cache:
                self._pipeline_cache[cache_key] = pipe

            return pipe

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to load STT model: {e}"
            ) from e

    def get_tts_pipeline(
        self, model_name: str = "microsoft/speecht5_tts", use_cache: bool = True
    ) -> Any:
        """
        Get a text-to-speech pipeline for speech synthesis.

        Args:
            model_name: The name of the TTS model to load
            use_cache: Whether to use cached instances (default: True)

        Returns:
            pipeline: The TTS pipeline
        """
        # Check if model is supported
        if model_name not in self.supported_tts_models:
            raise HTTPException(
                status_code=404, detail=f"TTS model {model_name} not supported."
            )

        # Return cached pipeline if available and caching is enabled
        cache_key = f"tts_{model_name}"
        if use_cache and cache_key in self._pipeline_cache:
            return self._pipeline_cache[cache_key]

        try:
            import torch

            if model_name == "microsoft/speecht5_tts":
                # For SpeechT5, we need to handle speaker embeddings
                from transformers import SpeechT5ForTextToSpeech, SpeechT5Processor

                processor = SpeechT5Processor.from_pretrained(model_name)
                model = SpeechT5ForTextToSpeech.from_pretrained(model_name)

                # Create a simple pipeline function that handles the speaker embeddings
                def tts_pipeline(text):
                    inputs = processor(text=text, return_tensors="pt")
                    # Use a default speaker embedding (zeros) for simplicity
                    speaker_embeddings = torch.zeros(
                        1, 512
                    )  # Default size for SpeechT5
                    speech = model.generate_speech(
                        inputs["input_ids"], speaker_embeddings, vocoder=None
                    )
                    return speech

                pipe = tts_pipeline
            else:
                raise HTTPException(
                    status_code=404, detail=f"TTS model {model_name} not supported."
                )

            # Cache the pipeline if caching is enabled
            if use_cache:
                self._pipeline_cache[cache_key] = pipe

            return pipe

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to load TTS model: {e}"
            ) from e

    def get_image_pipeline(
        self, model_name="text-image-gpt2", use_cache=True
    ):
        """
        Get an image generation pipeline for creating images.

        Args:
            model_name: The name of the image model to load
            use_cache: Whether to use cached instances (default: True)

        Returns:
            pipeline: The image generation pipeline
        """
        # Check if model is supported
        if model_name not in self.supported_image_models:
            raise HTTPException(
                status_code=404, detail=f"Image model {model_name} not supported."
            )

        # Return cached pipeline if available and caching is enabled
        cache_key = f"image_{model_name}"
        if use_cache and cache_key in self._pipeline_cache:
            return self._pipeline_cache[cache_key]

        try:
            if model_name == "text-image-gpt2":
                # Import text-based image generation components
                from .text_image_generator import generate_image_with_fallback
                from .text_image_trainer import train_model
                
                # Create a pipeline-like interface
                class TextImagePipeline:
                    def __init__(self):
                        self.train_model = train_model
                        self.generate_image = generate_image_with_fallback
                    
                    def __call__(self, prompt, width=28, height=28, **kwargs):
                        """Generate image from prompt"""
                        img_array, img = self.generate_image(prompt)
                        if img_array is not None:
                            # Resize to requested dimensions
                            img = img.resize((width, height))
                            return type('Result', (), {'images': [img]})()
                        else:
                            # Return a blank image if generation fails
                            blank_img = Image.new('RGB', (width, height), color='white')
                            return type('Result', (), {'images': [blank_img]})()

                pipe = TextImagePipeline()

            else:
                # Fallback to Stable Diffusion for other models
                import torch
                from diffusers import StableDiffusionPipeline

                # Load pipeline without device map to avoid meta tensor issues
                pipe = StableDiffusionPipeline.from_pretrained(  # type: ignore
                    model_name,
                    torch_dtype=(
                        torch.float16 if torch.cuda.is_available() else torch.float32
                    ),
                    device_map=None,  # Disable device map to avoid meta tensor issues
                )

                # Move to device after loading
                if torch.cuda.is_available():
                    pipe = pipe.to("cuda")
                else:
                    pipe = pipe.to("cpu")

            # Cache the pipeline if caching is enabled
            if use_cache:
                self._pipeline_cache[cache_key] = pipe

            return pipe

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to load image model: {e}"
            ) from e

    def get_embedding_model(
        self,
        model_name: str = "sentence-transformers/paraphrase-MiniLM-L3-v2",
        use_cache: bool = True,
    ) -> Any:
        """
        Get an embedding model for creating text embeddings.

        Args:
            model_name: The name of the embedding model to load
            use_cache: Whether to use cached instances (default: True)

        Returns:
            model: The embedding model
        """
        # Check if model is supported
        if model_name not in self.supported_embedding_models:
            raise HTTPException(
                status_code=404, detail=f"Embedding model {model_name} not supported."
            )

        # Return cached model if available and caching is enabled
        cache_key = f"embedding_{model_name}"
        if use_cache and cache_key in self._model_cache:
            return self._model_cache[cache_key]

        try:
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer(model_name)

            # Cache the model if caching is enabled
            if use_cache:
                self._model_cache[cache_key] = model

            return model

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to load embedding model: {e}"
            ) from e

    def get_model_for_fine_tuning(
        self, model_name: str, device: str = "cuda", torch_dtype: Any = None
    ) -> tuple[Any, Any]:
        """
        Get a model instance specifically for fine-tuning with device and dtype settings.

        Args:
            model_name: The name of the model to load
            device: Device to load the model on (default: "cuda")
            torch_dtype: Torch dtype for the model (default: None)

        Returns:
            tuple: (model_instance, processor)
        """
        model_instance, processor = self.get_model_instance(model_name, use_cache=False)

        # Move model to specified device and dtype
        if hasattr(model_instance, "to"):
            model_instance = model_instance.to(device)
            if torch_dtype:
                model_instance = model_instance.to(torch_dtype)

        return model_instance, processor

    def clear_cache(self) -> None:
        """Clear the model and processor cache."""
        self._model_cache.clear()
        self._processor_cache.clear()
        self._pipeline_cache.clear()

    def get_cached_models(self) -> dict[str, Any]:
        """Get list of currently cached model names."""
        return list(self._model_cache.keys())

    def load_peft_adapter(
        self, adapter_path: str, model_name: str | None = None
    ) -> bool:
        """
        Load a PEFT adapter onto the base model with blocking.

        Args:
            adapter_path: Path to the PEFT adapter directory
            model_name: Optional model name (for compatibility)

        Returns:
            bool: True if adapter loaded successfully
        """
        with self._model_lock:
            try:
                logger.info(f"Loading PEFT adapter from {adapter_path}")

                # Unload current adapter if any
                if self._current_adapter:
                    self.unload_peft_adapter()

                # Get base model instance
                base_model_name = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
                if self._base_model_instance is None:
                    self._base_model_instance, processor = self.get_model_instance(
                        base_model_name, use_cache=True
                    )

                # Load PEFT adapter
                if os.path.exists(adapter_path):
                    from peft import PeftModel

                    # Load adapter on top of base model
                    self._base_model_instance = PeftModel.from_pretrained(
                        self._base_model_instance, adapter_path
                    )
                    self._current_adapter = adapter_path

                    logger.info(f"Successfully loaded PEFT adapter: {adapter_path}")
                    return True
                else:
                    logger.error(f"Adapter path does not exist: {adapter_path}")
                    return False

            except Exception as e:
                logger.error(f"Failed to load PEFT adapter: {e}")
                return False

    def unload_peft_adapter(self) -> bool:
        """
        Unload the current PEFT adapter and return to base model.

        Returns:
            bool: True if adapter unloaded successfully
        """
        with self._model_lock:
            try:
                if self._current_adapter is None:
                    logger.info("No PEFT adapter currently loaded")
                    return True

                logger.info(f"Unloading PEFT adapter: {self._current_adapter}")

                # Reset to base model (reload from cache)
                base_model_name = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
                self._base_model_instance, _ = self.get_model_instance(
                    base_model_name, use_cache=True
                )

                self._current_adapter = None
                logger.info("Successfully unloaded PEFT adapter")
                return True

            except Exception as e:
                logger.error(f"Failed to unload PEFT adapter: {e}")
                return False

    def get_current_adapter(self) -> str | None:
        """Get the currently loaded adapter path."""
        return self._current_adapter

    def is_adapter_loaded(self) -> bool:
        """Check if a PEFT adapter is currently loaded."""
        return self._current_adapter is not None

    def register_peft_adapter(self, model_name: str, adapter_path: str) -> None:
        """
        Register a PEFT adapter path for a fine-tuned model.

        This method allows the fine-tuning service to register adapter paths
        without creating a circular dependency.

        Args:
            model_name: The fine-tuned model name (e.g., "ft:model:suffix:jobid")
            adapter_path: Path to the PEFT adapter directory
        """
        PEFT_ADAPTERS[model_name] = adapter_path
        logger.info(f"Registered PEFT adapter for {model_name}: {adapter_path}")

    def get_peft_adapter_path(self, model_name: str) -> str | None:
        """
        Get the PEFT adapter path for a fine-tuned model.

        Args:
            model_name: The fine-tuned model name

        Returns:
            The adapter path if found, None otherwise
        """
        return PEFT_ADAPTERS.get(model_name)


# Create a private singleton instance
_models_service = ModelsService()


def get_models_service() -> ModelsService:
    """Get the singleton ModelsService instance for dependency injection."""
    return _models_service
