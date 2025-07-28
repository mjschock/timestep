# VLM-Based Embeddings

This implementation replaces traditional embedding models with embeddings extracted from Vision Language Models (VLMs). Instead of using dedicated embedding models like sentence-transformers, we now extract latent representations directly from the VLM's encoder after text and vision tokens are merged.

## 🎯 Key Benefits

1. **Unified Representation Space**: Text and image embeddings are generated in the same latent space, enabling better multimodal understanding
2. **Rich Contextual Information**: VLM embeddings capture both visual and textual context
3. **Flexible Extraction Strategies**: Multiple ways to extract embeddings from different layers
4. **Multimodal Capabilities**: Support for both text-only and text+image embeddings

## 🏗️ Architecture

### Traditional Approach
```
Text Input → Sentence Transformer → Embedding Vector
```

### VLM-Based Approach
```
Text Input → VLM Encoder → Extract Latent Representations → Embedding Vector
```

The key insight is extracting embeddings from the VLM's encoder after the text and vision tokens are merged, as you suggested. This provides a unified representation space that captures both textual and visual understanding.

## 🔧 Implementation Details

### Embedding Extraction Strategies

1. **CLS Token (`cls`)**: Uses the first token's representation from the last layer
   - Good for sentence-level embeddings
   - Captures global context

2. **Mean Pooling (`mean`)**: Averages all token representations (excluding padding)
   - Good for longer texts
   - More stable for variable-length inputs

3. **Last Layer (`last_layer`)**: Uses the entire last hidden state
   - Maximum information but larger dimensions
   - Good for detailed analysis

4. **Multi-Layer (`multi_layer`)**: Concatenates CLS tokens from multiple layers
   - Captures information from different abstraction levels
   - More expressive but larger dimensions

### API Endpoints

#### Text Embeddings
```bash
POST /v1/embeddings
{
    "input": "A cat sitting on a windowsill",
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
}
```

#### Multimodal Embeddings
```bash
POST /v1/embeddings/multimodal
{
    "text": "A red square image",
    "image": "base64_encoded_image_data",
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
}
```

## 🚀 Usage Examples

### Python Client

```python
import requests
import base64
from PIL import Image
import io

# Text embedding
response = requests.post("http://localhost:8000/v1/embeddings", json={
    "input": "A beautiful sunset over the ocean",
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
})

embedding = response.json()["data"][0]["embedding"]
print(f"Embedding dimension: {len(embedding)}")

# Multimodal embedding
image = Image.open("cat.jpg")
buffer = io.BytesIO()
image.save(buffer, format='PNG')
image_base64 = base64.b64encode(buffer.getvalue()).decode()

response = requests.post("http://localhost:8000/v1/embeddings/multimodal", json={
    "text": "A cat sitting on a windowsill",
    "image": image_base64,
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
})

embedding = response.json()["data"][0]["embedding"]
print(f"Multimodal embedding dimension: {len(embedding)}")
```

### cURL Examples

```bash
# Text embedding
curl -X POST "http://localhost:8000/v1/embeddings" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "A cat sitting on a windowsill",
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
  }'

# Multimodal embedding
curl -X POST "http://localhost:8000/v1/embeddings/multimodal" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "A red square image",
    "image": "base64_encoded_image_data",
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
  }'
```

## 🔬 Technical Details

### Model Architecture

The implementation uses `AutoModelForImageTextToText` from Hugging Face Transformers, which provides:

- **Unified Encoder**: Processes both text and image inputs
- **Hidden States Access**: Allows extraction from any layer
- **Flexible Input Processing**: Handles text-only or multimodal inputs

### Embedding Extraction Process

1. **Input Processing**: Text and/or image inputs are processed by the VLM's processor
2. **Forward Pass**: Model generates hidden states for all layers
3. **Embedding Extraction**: Selected strategy extracts embeddings from appropriate layers
4. **Post-processing**: Convert to numpy arrays and flatten to lists

### Memory and Performance

- **GPU Memory**: VLM models are larger than traditional embedding models
- **Inference Time**: Slightly slower due to full model forward pass
- **Embedding Quality**: Potentially higher quality due to richer context

## 🧪 Testing

Run the test script to verify the implementation:

```bash
cd backend
python test_vlm_embeddings.py
```

This will test:
- Text-only embeddings
- Multimodal embeddings
- Different embedding extraction strategies
- Comparison with traditional embeddings

## 🔄 Migration from Traditional Embeddings

### Before (Traditional)
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L3-v2')
embedding = model.encode("Your text here")
```

### After (VLM-Based)
```python
# Use the API endpoint
response = requests.post("/v1/embeddings", json={
    "input": "Your text here",
    "model": "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "embedding_type": "cls"
})
embedding = response.json()["data"][0]["embedding"]
```

## 🎯 Use Cases

1. **Semantic Search**: Find similar documents or images
2. **Recommendation Systems**: Content-based recommendations
3. **Clustering**: Group similar content together
4. **Anomaly Detection**: Identify unusual content
5. **Multimodal Applications**: Applications requiring both text and image understanding

## 🔧 Configuration

### Supported Models
- `HuggingFaceTB/SmolVLM2-256M-Video-Instruct` (default)

### Embedding Types
- `cls`: CLS token from last layer (recommended)
- `mean`: Mean pooling across tokens
- `last_layer`: Full last layer representation
- `multi_layer`: Concatenated multi-layer CLS tokens

### Parameters
- `max_length`: Maximum sequence length (default: 512)
- `padding`: Whether to pad sequences (default: True)
- `truncation`: Whether to truncate long sequences (default: True)

## 🚨 Limitations and Considerations

1. **Model Size**: VLM models are larger than traditional embedding models
2. **Inference Speed**: Slower than dedicated embedding models
3. **Memory Usage**: Higher GPU memory requirements
4. **Model Compatibility**: Depends on specific VLM architecture

## 🔮 Future Enhancements

1. **Layer Selection**: Allow users to specify which layers to extract from
2. **Attention Weights**: Extract attention-based embeddings
3. **Custom Aggregation**: Allow custom pooling strategies
4. **Batch Processing**: Optimize for batch inference
5. **Model Quantization**: Reduce memory footprint

## 📊 Performance Comparison

| Aspect | Traditional Embeddings | VLM Embeddings |
|--------|----------------------|----------------|
| Model Size | ~100MB | ~1-2GB |
| Inference Speed | Fast | Moderate |
| Embedding Quality | Good | Potentially Better |
| Multimodal Support | No | Yes |
| Context Understanding | Limited | Rich |

## 🤝 Contributing

To extend this implementation:

1. Add new VLM models to `supported_vlm_models`
2. Implement new embedding extraction strategies
3. Add support for different input modalities
4. Optimize for specific use cases

## 📚 References

- [SmolVLM2 Paper](https://arxiv.org/abs/2401.10108)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Vision Language Models](https://arxiv.org/abs/2202.10461)