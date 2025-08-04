import json
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Any

LOG_DIR = os.environ.get("LOG_DIR", "logs")
LOG_FILE = os.path.join(LOG_DIR, "server.log")
os.makedirs(LOG_DIR, exist_ok=True)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record: dict[str, Any] = {
            "level": record.levelname,
            "time": self.formatTime(record, self.datefmt),
            "name": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_record)


class ConsoleFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        # Simple console format for readability with timestamp
        timestamp = self.formatTime(record, "%H:%M:%S")
        return f"[{timestamp}] {record.levelname}: {record.getMessage()}"


logger = logging.getLogger("timestep")
# Set log level from environment variable, default to INFO
log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
logger.setLevel(getattr(logging, log_level, logging.INFO))

# Clear any existing handlers
logger.handlers = []

# File handler with JSON format
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5)
file_handler.setFormatter(JsonFormatter())
logger.addHandler(file_handler)

# Console handler - only show clean messages
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(ConsoleFormatter())

# In test/development mode, only show INFO+ to console, DEBUG goes to file
# In production, show all levels to console if LOG_LEVEL is set
console_level = os.environ.get("CONSOLE_LOG_LEVEL", "INFO").upper()
console_handler.setLevel(getattr(logging, console_level, logging.INFO))
logger.addHandler(console_handler)
