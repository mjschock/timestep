# Test Fixtures

This directory contains test assets and fixtures used across the test suite.

## Organization

- `audio/` - Audio files for testing audio APIs
- `images/` - Image files for testing vision APIs  
- `jsonl/` - JSONL files for testing fine-tuning APIs
- `text/` - Text files for testing text-based APIs

## Usage

Fixtures are automatically created by `conftest.py` if they don't exist. You can also manually add test files to these directories.

## File Types

- **Audio**: `.wav` files for audio processing tests
- **Images**: `.png`, `.jpg` files for vision model tests
- **JSONL**: `.jsonl` files for fine-tuning data tests
- **Text**: `.txt` files for text processing tests

## Adding New Fixtures

1. Place files in the appropriate subdirectory
2. Update `conftest.py` if you need new fixture functions
3. Use the fixture in your tests via dependency injection
