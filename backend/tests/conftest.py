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

BASE_URL = "http://localhost:8000/v1"
MODEL_NAME = "openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct"


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
def api_server_with_coverage() -> Generator[str, None, None]:
    """
    Automatically starts FastAPI server with coverage for all tests.
    Uses OpenAI client to test API endpoints with full coverage tracking.
    Ensures proper cleanup regardless of how tests exit.
    """
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
def async_client(api_base_url: str) -> AsyncOpenAI:
    """Async OpenAI client configured for the test server"""
    return AsyncOpenAI(api_key="api_key", base_url=f"{api_base_url}/v1")


@pytest.fixture
def sync_client(api_base_url: str) -> OpenAI:
    """Sync OpenAI client configured for the test server"""
    return OpenAI(api_key="api_key", base_url=f"{api_base_url}/v1")


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
