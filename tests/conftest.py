import atexit
import glob
import os
import shutil
import subprocess
import threading
import time
from collections.abc import Callable, Generator
from typing import Any

import numpy as np
import psutil
import pytest
import requests
import soundfile as sf
from openai import AsyncOpenAI, OpenAI
from PIL import Image


def pytest_addoption(parser):
    """Add command line options for configuring API settings."""
    parser.addoption(
        "--api-key",
        action="store",
        default=None,
        help="OpenAI API key to use for tests"
    )
    parser.addoption(
        "--base-url", 
        action="store",
        default=None,
        help="Base URL for OpenAI API (e.g., https://api.openai.com/v1 or http://localhost:8000/v1)"
    )
    parser.addoption(
        "--model-name",
        action="store", 
        default=None,
        help="Model name to use for tests"
    )
    parser.addoption(
        "--skip-local-server",
        action="store_true",
        default=False,
        help="Skip starting local server and use external API"
    )

# Default values - can be overridden by environment variables or command line
DEFAULT_BASE_URL = "http://localhost:8000/v1"
DEFAULT_MODEL_NAME = "openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
DEFAULT_API_KEY = "api_key"


def get_test_config(request=None):
    """Get test configuration from command line args, environment variables, or defaults."""
    # Priority: command line args > environment variables > defaults
    
    if request:
        # Get from pytest command line options
        api_key = request.config.getoption("--api-key")
        base_url = request.config.getoption("--base-url") 
        model_name = request.config.getoption("--model-name")
        skip_local_server = request.config.getoption("--skip-local-server")
    else:
        api_key = base_url = model_name = skip_local_server = None
    
    return {
        "api_key": api_key or os.getenv("AGENTS_SDK_API_KEY") or DEFAULT_API_KEY,
        "base_url": base_url or os.getenv("AGENTS_SDK_BASE_URL") or DEFAULT_BASE_URL,
        "model_name": model_name or os.getenv("AGENTS_SDK_MODEL_NAME") or DEFAULT_MODEL_NAME,
        "skip_local_server": skip_local_server or os.getenv("AGENTS_SDK_SKIP_LOCAL_SERVER", "").lower() in ("true", "1", "yes")
    }


# Get global config (will be used by fixtures that don't have request access)
_GLOBAL_CONFIG = get_test_config()
BASE_URL = _GLOBAL_CONFIG["base_url"]
MODEL_NAME = _GLOBAL_CONFIG["model_name"] 
API_KEY = _GLOBAL_CONFIG["api_key"]


def wait_for_server_ready(
    base_url: str,
    timeout_seconds: int = 120,
    server_process: subprocess.Popen[str] | None = None,
) -> bool:
    """Wait for server to be ready by checking the /docs endpoint"""
    server_ready = False
    for attempt in range(timeout_seconds):
        # First check if the server process has exited
        if server_process and server_process.poll() is not None:
            # Server process has exited, check the return code
            return_code = server_process.returncode
            if return_code != 0:
                raise RuntimeError(
                    f"Server process exited with code {return_code} - server failed to start"
                )
            else:
                raise RuntimeError("Server process exited unexpectedly")

        try:
            response = requests.get(f"{base_url}/docs", timeout=1)
            if response.status_code == 200:
                server_ready = True
                break
        except (requests.ConnectionError, requests.Timeout):
            pass
        time.sleep(1)
        if attempt % 10 == 0:
            print(f"⏳ Waiting for server... (attempt {attempt + 1}/{timeout_seconds})")

    if not server_ready:
        raise RuntimeError(f"Server failed to start within {timeout_seconds} seconds")
    return True


@pytest.fixture(scope="session", autouse=True)
def api_server_with_coverage(request) -> Generator[str, None, None]:
    """
    Automatically starts FastAPI server with coverage for all tests.
    Uses OpenAI client to test API endpoints with full coverage tracking.
    Ensures proper cleanup regardless of how tests exit.
    Can be skipped with --skip-local-server flag.
    """
    config = get_test_config(request)
    
    if config["skip_local_server"]:
        print("\n⏭️  Skipping local server startup (using external API)")
        # Extract base URL without /v1 suffix for consistency with other fixtures
        base_url = config["base_url"].rstrip('/v1')
        yield base_url
        return

    print("\n🚀 Starting FastAPI server with coverage...")

    _cleanup_existing_processes()
    _cleanup_coverage_files()
    env = _setup_environment()
    cmd = _create_server_command()
    print(f"🔍 Server command: {' '.join(cmd)}")

    server_process = None

    try:
        server_process = _start_server_process(cmd, env)
        _start_output_thread(
            server_process
        )  # Start output thread but don't store reference
        wait_for_server_ready("http://localhost:8000", server_process=server_process)
        print("✅ FastAPI server is ready at http://localhost:8000")

        cleanup_func = _create_cleanup_function(server_process)
        atexit.register(cleanup_func)

        yield "http://localhost:8000"

    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        _cleanup_on_exception(server_process)
        raise
    finally:
        _final_cleanup(server_process)


def _cleanup_existing_processes() -> None:
    """Clean up any existing processes on port 8000."""
    try:
        for proc in psutil.process_iter():
            try:
                if proc.name() == "uvicorn" and proc.net_connections():
                    for conn in proc.net_connections():
                        if conn.laddr.port == 8000:
                            print(
                                f"🧹 Killing existing process {proc.pid} on port 8000"
                            )
                            proc.terminate()
                            try:
                                proc.wait(timeout=2)
                            except psutil.TimeoutExpired:
                                proc.kill()
                                proc.wait()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
    except Exception as e:
        print(f"⚠️  Could not clean existing processes: {e}")


def _cleanup_coverage_files() -> None:
    """Clean up any existing coverage files."""
    for f in glob.glob(".coverage*"):
        try:
            os.remove(f)
        except Exception as e:
            # Ignore file removal errors during cleanup
            print(f"⚠️  Could not remove coverage file {f}: {e}")


def _setup_environment() -> dict[str, str]:
    """Set up environment for subprocess coverage."""
    env = os.environ.copy()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = os.path.join(project_root, "src")
    env["PYTHONPATH"] = src_path
    return env


def _create_server_command() -> list[str]:
    """Create server command."""
    uv_path = shutil.which("uv")
    if not uv_path:
        raise RuntimeError("Could not find uv executable")

    return [
        uv_path,
        "run",
        "uvicorn",
        "src.backend.main:app",
        "--host",
        "0.0.0.0",  # noqa: S104
        "--port",
        "8000",
    ]


def _start_server_process(cmd: list[str], env: dict[str, str]) -> subprocess.Popen[str]:
    """Start server process."""
    return subprocess.Popen(  # noqa: S603
        cmd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True,
    )


def _start_output_thread(server_process: subprocess.Popen[str]) -> threading.Thread:
    """Start thread to read server output."""

    def read_server_output() -> None:
        try:
            if server_process.stdout is not None:
                for line in iter(server_process.stdout.readline, ""):
                    if line:
                        print(f"[SERVER] {line.rstrip()}")
        except Exception as e:
            # Ignore errors when thread is interrupted
            print(f"⚠️  Server output thread error: {e}")

    output_thread = threading.Thread(target=read_server_output, daemon=True)
    output_thread.start()
    return output_thread


def _create_cleanup_function(
    server_process: subprocess.Popen[str] | None,
) -> Callable[[], None]:
    """Create cleanup function that ALWAYS runs."""

    def cleanup() -> None:
        nonlocal server_process
        print("\n🛑 Stopping FastAPI server...")

        if server_process:
            _terminate_server_process(server_process)
            server_process = None

        _force_cleanup_remaining_processes()
        _generate_coverage_report()

    return cleanup


def _terminate_server_process(server_process: subprocess.Popen[str]) -> None:
    """Terminate server process gracefully."""
    try:
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print("⚠️  Server didn't shut down gracefully, forcing kill...")
            server_process.kill()
            server_process.wait()
    except Exception as e:
        print(f"⚠️  Error during server cleanup: {e}")


def _force_cleanup_remaining_processes() -> None:
    """Force kill any remaining processes on port 8000."""
    try:
        for proc in psutil.process_iter():
            try:
                if proc.name() == "uvicorn" and proc.net_connections():
                    for conn in proc.net_connections():
                        if conn.laddr.port == 8000:
                            print(f"🧹 Force killing remaining process {proc.pid}")
                            proc.kill()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
    except Exception as e:
        print(f"⚠️  Could not force cleanup: {e}")


def _generate_coverage_report() -> None:
    """Generate coverage report."""
    coverage_files = glob.glob(".coverage.*")
    print(f"📋 Found {len(coverage_files)} coverage files: {coverage_files}")

    if coverage_files:
        print("📊 Generating coverage report...")
        _combine_coverage_files()
        _generate_html_report()
        _print_coverage_report()
    else:
        print(
            "❌ No coverage files found - server may not have executed any tracked code"
        )


def _combine_coverage_files() -> None:
    """Combine coverage files."""
    uv_path = shutil.which("uv")
    coverage_path = shutil.which("coverage")

    if not uv_path or not coverage_path:
        print("⚠️  Could not find uv or coverage executables")
        return

    combine_result = subprocess.run(  # noqa: S603
        [uv_path, "run", coverage_path, "combine"], capture_output=True, text=True
    )
    if combine_result.returncode != 0:
        print(f"⚠️  Coverage combine error: {combine_result.stderr}")
    else:
        print("✅ Coverage files combined successfully")


def _generate_html_report() -> None:
    """Generate HTML coverage report."""
    uv_path = shutil.which("uv")
    coverage_path = shutil.which("coverage")

    if not uv_path or not coverage_path:
        print("⚠️  Could not find uv or coverage executables")
        return

    subprocess.run([uv_path, "run", coverage_path, "html"], capture_output=True)  # noqa: S603


def _print_coverage_report() -> None:
    """Print coverage report."""
    uv_path = shutil.which("uv")
    coverage_path = shutil.which("coverage")

    if not uv_path or not coverage_path:
        print("⚠️  Could not find uv or coverage executables")
        return

    result = subprocess.run(  # noqa: S603
        [uv_path, "run", coverage_path, "report"], capture_output=True, text=True
    )
    if result.stdout:
        print(result.stdout)
    else:
        print("⚠️  No coverage data found")
    print("📝 Coverage report saved to htmlcov/index.html")


def _cleanup_on_exception(server_process: subprocess.Popen[str] | None) -> None:
    """Cleanup on exception."""
    if server_process:
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()


def _final_cleanup(server_process: subprocess.Popen[str] | None) -> None:
    """Final cleanup in fixture finally block."""
    if server_process and server_process.poll() is None:
        print("🧹 Final cleanup in fixture finally block...")
        server_process.terminate()
        try:
            server_process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server_process.kill()


@pytest.fixture
def api_base_url(api_server_with_coverage: str) -> str:
    """Convenience fixture for API base URL"""
    return "http://localhost:8000"


@pytest.fixture
def model_name(request) -> str:
    """Fixture for model name that respects configuration"""
    config = get_test_config(request)
    return config["model_name"]


@pytest.fixture
def async_client(api_base_url: str, request) -> AsyncOpenAI:
    """Async OpenAI client configured for the test server"""
    config = get_test_config(request)
    
    # Use configured base_url if provided, otherwise use the local server
    if config["skip_local_server"]:
        base_url = config["base_url"]
    else:
        base_url = f"{api_base_url}/v1"
    
    print(f"🔌 Using API: {base_url} with model: {config['model_name']}")
    return AsyncOpenAI(api_key=config["api_key"], base_url=base_url)


@pytest.fixture
def sync_client(api_base_url: str, request) -> OpenAI:
    """Sync OpenAI client configured for the test server"""
    config = get_test_config(request)
    
    # Use configured base_url if provided, otherwise use the local server
    if config["skip_local_server"]:
        base_url = config["base_url"]
    else:
        base_url = f"{api_base_url}/v1"
    
    print(f"🔌 Using API: {base_url} with model: {config['model_name']}")
    return OpenAI(api_key=config["api_key"], base_url=base_url)


@pytest.fixture
def sample_audio(tmp_path: Any) -> str:
    # Path to a sample audio file in the fixtures directory
    sample_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "audio", "sample.wav"
    )
    # Create a valid silent WAV file if it doesn't exist
    if not os.path.exists(sample_path):
        # Ensure directory exists
        os.makedirs(os.path.dirname(sample_path), exist_ok=True)
        # 1 second of silence at 16kHz, mono
        data = np.zeros(16000, dtype=np.float32)
        sf.write(sample_path, data, 16000, format="WAV")
    return sample_path


@pytest.fixture
def sample_jsonl_file(tmp_path: Any) -> str:
    sample_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "jsonl", "sample.jsonl"
    )
    # Create a minimal valid JSONL file if it doesn't exist
    if not os.path.exists(sample_path):
        # Ensure directory exists
        os.makedirs(os.path.dirname(sample_path), exist_ok=True)
        with open(sample_path, "w") as f:
            f.write('{"prompt": "Say hello", "completion": "Hello!"}\n')
    return sample_path


@pytest.fixture
def sample_image(tmp_path: Any) -> str:
    sample_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "images", "sample.png"
    )
    if not os.path.exists(sample_path):
        # Ensure directory exists
        os.makedirs(os.path.dirname(sample_path), exist_ok=True)
        image = Image.new("RGB", (256, 256), color="blue")
        image.save(sample_path, format="PNG")
    return sample_path


@pytest.fixture
def sample_text_file(tmp_path: Any) -> str:
    sample_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "text", "sample.txt"
    )
    if not os.path.exists(sample_path):
        # Ensure directory exists
        os.makedirs(os.path.dirname(sample_path), exist_ok=True)
        with open(sample_path, "w") as f:
            f.write("This is a sample text file for testing.\n")
    return sample_path


@pytest.fixture
def builtin_tools():
    """Built-in tools for testing."""
    return [
        {
            "type": "function",
            "function": {
                "name": "code_interpreter",
                "description": "Execute Python code to perform calculations or data processing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "The Python code to execute",
                        }
                    },
                    "required": ["code"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "talk_to_user",
                "description": "Communicate with the user by providing a text response",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "response": {
                            "type": "string",
                            "description": "The message to communicate to the user",
                        }
                    },
                    "required": ["response"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "Search the web for information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query to look up",
                        }
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
        },
    ]


@pytest.fixture
def builtin_tool_examples():
    """Built-in tool examples for testing."""
    return {
        "code_interpreter": {
            "user_message": "How many r's are in the word 'strawberry'?",
            "assistant_response": "<observation>The user is asking me to count the letter 'r' in the word 'strawberry'.</observation><thought>I need to count the occurrences of the letter 'r' in 'strawberry'. I can use Python code to do this accurately with the count() method.</thought><tool_call>\n{'name': 'code_interpreter', 'arguments': {'code': \"'strawberry'.count('r')\"}}\n</tool_call>",
            "tool_response": "3",
            "final_response": "<observation>The code execution returned 3, indicating there are 3 r's in 'strawberry'.</observation><thought>I have the answer to the user's question. I should communicate this result clearly to the user.</thought><tool_call>\n{'name': 'talk_to_user', 'arguments': {'response': \"There are 3 r's in the word 'strawberry'.\"}}\n</tool_call>",
        },
        "web_search": {
            "user_message": "What is the answer to the Ultimate Question of Life, the Universe, and Everything?",
            "assistant_response": "<observation>The user is asking about the Ultimate Question of Life, the Universe, and Everything.</observation><thought>This is a reference to Douglas Adams' 'The Hitchhiker's Guide to the Galaxy'. I should search the web to get accurate information about this famous question and its answer.</thought><tool_call>\n{'name': 'web_search', 'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}}\n</tool_call>",
            "tool_response": "The answer to the Ultimate Question of Life, the Universe, and Everything is 42.",
            "final_response": "<observation>The web search returned that the answer to the Ultimate Question of Life, the Universe, and Everything is 42.</observation><thought>I have the answer from the web search. This is the famous answer from Douglas Adams' work. I should communicate this to the user.</thought><tool_call>\n{'name': 'talk_to_user', 'arguments': {'response': '42'}}\n</tool_call>",
        },
    }


@pytest.fixture
def create_base_messages():
    """Fixture that provides the create_base_messages function."""

    def _create_base_messages(tools, builtin_tool_examples):
        """Create the base conversation messages for tool calling demonstrations."""
        import pprint

        messages = [
            {
                "content": f"""You are an AI agent acting as an assistant on behalf of a human user.

You are aware of the following tools available to the human user in this environment:
{pprint.pformat(tools)}

You MUST always respond in exactly this format:
1. <observation></observation> - Your observation of the user message or tool response
2. <thought></thought> - Your reasoning about what to do next
3. <tool_call></tool_call> - A tool call (use talk_to_user to communicate responses)

For tool calls, use this exact JSON format:
{{'name': 'function_name', 'arguments': {{'parameter': 'value'}}}}

To communicate with the user, use:
{{'name': 'talk_to_user', 'arguments': {{'response': 'your message here'}}}}

You will follow this agent-environment cycle of sensing, thinking, and acting consistently.""",
                "role": "system",
            }
        ]

        # Find which built-in tools are present in the tools list (excluding talk_to_user)
        tool_names = {
            tool["function"]["name"] for tool in tools if tool.get("type") == "function"
        }

        # Add 1-shot examples for built-in tools that are present (in a consistent order)
        for tool_name in [
            "code_interpreter",
            "web_search",
        ]:  # Maintain consistent order
            if tool_name in tool_names and tool_name in builtin_tool_examples:
                example = builtin_tool_examples[tool_name]

                # Add the example conversation
                messages.extend(
                    [
                        {
                            "content": example["user_message"],
                            "role": "user",
                        },
                        {
                            "content": example["assistant_response"],
                            "role": "assistant",
                        },
                        {
                            "content": example["tool_response"],
                            "role": "tool",
                        },
                        {
                            "content": example["final_response"],
                            "role": "assistant",
                        },
                    ]
                )

        return messages

    return _create_base_messages
