"""
Common utility functions shared across the backend.
"""

from typing import Any, Type, TypeVar
from pydantic import TypeAdapter

T = TypeVar('T')


def convert_validator_iterators(obj: Any) -> Any:
    """
    Recursively convert ValidatorIterators to plain Python types for serialization.
    
    ValidatorIterator objects are returned by pydantic TypeAdapter.validate_python()
    for list fields, but they cannot be serialized by libraries like HuggingFace datasets.
    This function converts them to regular Python lists while preserving all nested data.
    
    Args:
        obj: The object to convert (can be ValidatorIterator, dict, list, or primitive)
        
    Returns:
        The same object with ValidatorIterators converted to plain Python lists
    """
    if type(obj).__name__ == 'ValidatorIterator':
        return [convert_validator_iterators(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_validator_iterators(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_validator_iterators(item) for item in obj]
    else:
        return obj


def validate_and_convert_openai_request(
    request_data: dict, 
    openai_type: Type[T], 
    type_name: str = None
) -> T:
    """
    Validate request data against OpenAI types and convert ValidatorIterators.
    
    This function combines TypeAdapter validation with ValidatorIterator conversion
    to provide a clean, serializable result that matches OpenAI specification exactly.
    
    Args:
        request_data: Raw request data to validate
        openai_type: OpenAI TypedDict type to validate against
        type_name: Optional name for the type (used in variable naming)
        
    Returns:
        Validated and converted data with proper type annotation
        
    Raises:
        ValidationError: If request_data doesn't match OpenAI specification
    """
    # Create TypeAdapter for the OpenAI type
    adapter = TypeAdapter(openai_type)
    
    # Validate with strict mode for maximum compliance (can explore other parameters later)
    validated_data = adapter.validate_python(request_data, strict=True)
    
    # Convert ValidatorIterators to plain Python types
    converted_data = convert_validator_iterators(validated_data)
    
    # Type assertion for clarity
    assert isinstance(converted_data, dict), f"Expected dict, got {type(converted_data)}"
    
    return converted_data