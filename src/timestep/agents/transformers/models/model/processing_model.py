from __future__ import annotations

from transformers import (  # type: ignore[import-not-found]
    FeatureExtractionMixin,
    ImageProcessingMixin,
    PreTrainedTokenizerBase,
    ProcessorMixin,
)


class ModelFeatureExtractor(FeatureExtractionMixin):  # type: ignore[misc]
    _auto_class = "AutoFeatureExtractor"


class ModelImageProcessor(ImageProcessingMixin):  # type: ignore[misc]
    _auto_class = "AutoImageProcessor"


class ModelTokenizer(PreTrainedTokenizerBase):  # type: ignore[misc]
    _auto_class = "AutoTokenizer"


class ModelProcessor(ProcessorMixin):  # type: ignore[misc]
    _auto_class = "AutoProcessor"

    attributes = [  # noqa: RUF012
        "feature_extractor",
        "image_processor",
        "tokenizer",
    ]

    # Names need to be attr_class for attr in attributes
    # feature_extractor_class = "ModelFeatureExtractor"
    feature_extractor_class = "AutoFeatureExtractor"
    # image_processor_class = "ModelImageProcessor"
    image_processor_class = "AutoImageProcessor"
    # tokenizer_class = "ModelTokenizer"
    tokenizer_class = "AutoTokenizer"
