# 🚀 Timestep

> **One API to rule them all** - A unified AI service that adapts to your resources

Timestep is a FastAPI-based AI gateway that provides a single, OpenAI-compatible interface to multiple AI providers. Whether you're running on a modest GTX 1050 Ti or accessing powerful cloud models, Timestep seamlessly adapts to your setup.

## ✨ Key Features

- 🔄 **Multi-Provider Support** - OpenAI, Anthropic, GitHub Models, and local inference
- 💡 **Resource-Aware** - Optimized for limited hardware while supporting cloud scaling  
- 🛠️ **Fine-Tuning Pipeline** - Complete model training and evaluation toolkit
- 📊 **Comprehensive APIs** - Chat, embeddings, images, audio, vector stores, and more
- 🔌 **OpenAI Compatible** - Drop-in replacement for existing OpenAI integrations
- ⚡ **Streaming Support** - Real-time responses for chat and completions

## 🚧 Status: Experimental Hobby Project - Paused for Academic Focus

**⚠️ This is an experimental, hobby project that implements the full OpenAI API spec locally using a SmolVLM model on limited compute hardware (GTX 1050 Ti). It is NOT production-grade and will require significant fine-tuning to be useful. The project can optionally proxy to external providers.**

**This project is currently paused to prioritize the final semester of a master's program. It has been left in a clean, working state for future development.**

## 🏃‍♂️ Quick Start

1. **Clone and install**:
   ```bash
   git clone <repository-url>
   cd timestep
   uv sync
   ```

2. **Configure providers** in `config.yaml`:
   ```yaml
   providers:
     openai:
       api_key: "${OPENAI_API_KEY}"
       base_url: "https://api.openai.com/v1"
       type: "proxy"
     local:
       type: "local"
   ```

3. **Start the server**:
   ```bash
   uv run uvicorn src.backend.main:app --reload
   ```

4. **Use any provider** through a unified interface:

   **Using OpenAI SDK:**
   ```python
   from openai import AsyncOpenAI
   
   # Connect to Timestep gateway
   client = AsyncOpenAI(
       api_key="your-key",  # Provider-specific API key
       base_url="http://localhost:8000/api/openai/v1"  # or /api/anthropic/v1, etc.
   )
   
   # Standard OpenAI API calls work unchanged
   response = await client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[
           {"role": "system", "content": "You are a helpful assistant."},
           {"role": "user", "content": "What is the capital of France?"}
       ]
   )
   ```

   **Using OpenAI Agents SDK:**
   ```python
   from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, function_tool
   
   @function_tool
   def get_weather(city: str):
       return f"The weather in {city} is sunny."
   
   # Create agent pointing to Timestep
   client = AsyncOpenAI(
       api_key="your-key",
       base_url="http://localhost:8000/api/local/v1"  # Use local models
   )
   
   agent = Agent(
       name="Weather Assistant",
       instructions="You are a helpful weather assistant.",
       model=OpenAIChatCompletionsModel(
           model="openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
           openai_client=client
       ),
       tools=[get_weather]
   )
   
   result = await Runner.run(agent, "What's the weather in Oakland?")
   ```

   **Or with curl:**
   ```bash
   # OpenAI via proxy
   curl -X POST http://localhost:8000/api/openai/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "Hello!"}]}'
   
   # Local inference
   curl -X POST http://localhost:8000/api/local/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"model": "openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct", "messages": [{"role": "user", "content": "Hello!"}]}'
   ```

## 🎯 Use Cases

- **Development**: Switch between local testing and production providers seamlessly
- **Cost Optimization**: Use local models for development, cloud for production
- **Multi-Model Workflows**: Compare responses across different providers
- **Fine-Tuning**: Train and evaluate custom models with comprehensive tooling
- **Resource Constraints**: Run AI workloads on modest hardware (tested on GTX 1050 Ti)

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   Your App     │────▶│   Timestep   │────▶│   Providers     │
│                │    │   Gateway    │    │                 │
└─────────────────┘    └──────────────┘    │ • OpenAI        │
                                           │ • Anthropic     │
                                           │ • GitHub Models │
                                           │ • Local Models  │
                                           └─────────────────┘
```

## 📋 Available APIs

| Endpoint | Description |
|----------|-------------|
| `/v1/chat/completions` | Chat completions with streaming |
| `/v1/embeddings` | Text embeddings |
| `/v1/images/generations` | Image generation |
| `/v1/audio/transcriptions` | Speech-to-text |
| `/v1/fine_tuning/jobs` | Model fine-tuning |
| `/v1/evals` | Model evaluation |
| `/v1/files` | File management |
| `/v1/vector_stores` | Vector database operations |

## 🧪 Development

```bash
# Run full test suite (includes formatting, linting, and coverage)
uv run pytest

# Or run individual components
uv run ruff format .
uv run ruff check --fix .
uv run pytest tests/ --cov=src/backend --cov-fail-under=42

# Start development server
uv run uvicorn src.backend.main:app --reload --host 0.0.0.0 --port 8000

# Alternative: Run with make (same as pytest but includes additional setup)
make
```

## 🤝 Contributing

This is an active WIP! Contributions welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

*Built with ❤️ for developers who need AI flexibility without the complexity*
