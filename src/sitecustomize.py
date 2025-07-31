"""
This file automatically starts coverage when imported.
It needs to be in the Python path to enable subprocess coverage.
"""

import atexit
import sys

import coverage

# Start coverage for uvicorn processes
if "uvicorn" in " ".join(sys.argv):
    # Initialize coverage
    cov = coverage.Coverage(
        config_file="pyproject.toml",
        data_suffix=True,
        auto_data=True,
    )
    cov.start()

    # Register cleanup
    def save_coverage():
        try:
            cov.stop()
            cov.save()
        except Exception as e:
            # Log the exception but don't fail during shutdown
            print(f"Warning: Could not save coverage data: {e}")
            pass

    atexit.register(save_coverage)

    # Also register signal handlers for graceful shutdown
    import signal

    def signal_handler(signum, frame):
        save_coverage()
        sys.exit(0)

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
