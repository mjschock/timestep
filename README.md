# Timestep-OAI-Compatible-App

A universal OpenAI-compatible proxy that supports both local models (SmolVLM2) and external AI providers through a unified API interface.

## Features

✅ **Local Model Support**: Run SmolVLM2 and other local models  
✅ **External Provider Proxy**: Proxy requests to OpenAI, Anyscale, Together, Anthropic, and more  
✅ **Unified API**: Same OpenAI client works for all providers  
✅ **Fine-tuning Support**: Local fine-tuning capabilities  
✅ **File Management**: Upload and manage training files  
✅ **Health Monitoring**: Built-in health checks and provider status  

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Running the Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

## API Usage Examples

### Local Models (SmolVLM2)

```python
import openai

# Local fine-tuning and inference
local_client = openai.OpenAI(
    api_key="anything",  # Not needed for local
    base_url="http://localhost:8000/local/v1"
)

# Chat completion with local model
response = local_client.chat.completions.create(
    model="SmolVLM2-1.7B-Instruct",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Fine-tuning with local model
job = local_client.fine_tuning.jobs.create(
    model="SmolVLM2-1.7B-Instruct",
    training_file="file-abc123"
)
```

### External Providers (Proxied)

```python
import openai

# OpenAI (proxied)
openai_client = openai.OpenAI(
    api_key="sk-your-real-openai-key",
    base_url="http://localhost:8000/openai/v1"
)

# Anyscale (proxied)
anyscale_client = openai.OpenAI(
    api_key="esecret_your_anyscale_key",
    base_url="http://localhost:8000/anyscale/v1"
)

# Together (proxied)
together_client = openai.OpenAI(
    api_key="your_together_key",
    base_url="http://localhost:8000/together/v1"
)

# All use the same API calls!
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or any model supported by the provider
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
```

## API Endpoints

### Root Information
- `GET /` - API information and usage guide
- `GET /health` - Health check
- `GET /providers` - List all available providers

### Local APIs (`/local/v1`)
- `POST /local/v1/chat/completions` - Chat completions
- `GET /local/v1/models` - List local models
- `POST /local/v1/fine_tuning/jobs` - Create fine-tuning job
- `GET /local/v1/fine_tuning/jobs` - List fine-tuning jobs
- `POST /local/v1/files` - Upload files
- `GET /local/v1/files` - List files

### External Provider Proxies
- `/{provider}/v1/*` - Proxy to external providers
  - `openai` → OpenAI API
  - `anyscale` → Anyscale API
  - `together` → Together API
  - `anthropic` → Anthropic API

## Available Local Models

- `SmolVLM2-1.7B-Instruct` - Vision-capable instruction model
- `SmolVLM2-1.7B` - Base text generation model
- `SmolVLM2-1.7B-Instruct-finetuned` - Fine-tuned instruction model

## External Providers

| Provider | Base URL | API Key Format |
|----------|----------|----------------|
| OpenAI | `/openai/v1` | `sk-...` |
| Anyscale | `/anyscale/v1` | `esecret_...` |
| Together | `/together/v1` | `your_key` |
| Anthropic | `/anthropic/v1` | `sk-ant-...` |

## Adding New Providers

Simply add to the `EXTERNAL_PROVIDERS` dict in `main.py`:

```python
EXTERNAL_PROVIDERS = {
    "openai": "https://api.openai.com/v1",
    "anyscale": "https://api.endpoints.anyscale.com/v1",
    "together": "https://api.together.xyz/v1",
    "anthropic": "https://api.anthropic.com/v1",
    
    # Add new providers here:
    "huggingface": "https://api-inference.huggingface.co/v1",
    "fireworks": "https://api.fireworks.ai/inference/v1",
}
```

## Deployment

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "main.py"]
```

### Environment Variables

- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)

### Production Considerations

1. **Database**: Replace in-memory storage with persistent database
2. **Authentication**: Add API key validation for local endpoints
3. **Rate Limiting**: Implement rate limiting per provider
4. **Logging**: Add comprehensive logging
5. **Monitoring**: Add metrics and monitoring
6. **SSL**: Use HTTPS in production

## Development

### Project Structure

```
├── main.py              # Main FastAPI application
├── APIs/                # API routers
│   ├── __init__.py
│   ├── chat.py         # Chat completions
│   ├── files.py        # File management
│   ├── fine_tuning.py  # Fine-tuning jobs
│   └── models.py       # Model listing
├── requirements.txt     # Dependencies
└── README.md          # This file
```

### Testing

```bash
# Test local endpoints
curl http://localhost:8000/local/v1/models

# Test external proxy
curl -H "Authorization: Bearer sk-test" \
     http://localhost:8000/openai/v1/models
```

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions, please open an issue on GitHub.
