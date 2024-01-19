from llama_index.tools import FunctionTool


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)

def divide(a: int, b: int) -> float:
    """Divide two integers and returns the result float"""
    return a / b

divide_tool = FunctionTool.from_defaults(fn=divide)

def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)
