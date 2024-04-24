from transformers import (
    AutoFeatureExtractor,
    AutoImageProcessor,
    AutoProcessor,
    AutoTokenizer,
    FeatureExtractionMixin,
    ImageProcessingMixin,
    PreTrainedTokenizerBase,
    ProcessorMixin,
)

class ModelFeatureExtractor(FeatureExtractionMixin):
    _auto_class = "AutoFeatureExtractor"

class ModelImageProcessor(ImageProcessingMixin):
    _auto_class = "AutoImageProcessor"

class ModelTokenizer(PreTrainedTokenizerBase):
    _auto_class = "AutoTokenizer"

class ModelProcessor(ProcessorMixin):
    _auto_class = "AutoProcessor"

    attributes = [
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
