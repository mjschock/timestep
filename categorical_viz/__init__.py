"""
Categorical Flow Visualization for OpenAI Agents SDK.

This module provides enhanced visualization capabilities that complement the existing
`draw_graph()` function by adding information flow arrows, type annotations,
compositional structure, and temporal flow visualization.

Example:
    >>> from agents import Agent, function_tool
    >>> from categorical_viz import draw_categorical_flow
    >>> 
    >>> @function_tool
    >>> def calculator(expression: str) -> str:
    >>>     return f"Result: {eval(expression)}"
    >>> 
    >>> agent = Agent(
    >>>     name="Math Tutor",
    >>>     instructions="Help with math problems",
    >>>     tools=[calculator]
    >>> )
    >>> 
    >>> fig = draw_categorical_flow(agent, layout="hierarchical", show_types=True)
    >>> fig.show()
"""

from .core import (
    draw_categorical_flow,
    draw_categorical_flow_comparison,
    validate_agent_composition,
    get_flow_statistics,
    draw_linear_flow,
    draw_hierarchical_flow,
    draw_temporal_flow
)

from .data_types import (
    Node,
    Edge,
    AgentStructure,
    TypeInfo,
    NodeType,
    FlowType,
    LayoutType,
    COLORS,
    FLOW_STYLES
)

from .extractor import (
    extract_agent_structure,
    get_tool_signature,
    validate_composition,
    extract_type_information,
    get_agent_metadata
)

from .layouts import (
    calculate_layout,
    layout_linear,
    layout_hierarchical,
    layout_temporal,
    optimize_layout
)

from .visualizer import (
    create_categorical_diagram,
    save_diagram,
    create_interactive_diagram
)

__version__ = "1.0.0"
__author__ = "OpenAI Agents SDK Team"

__all__ = [
    # Main public API
    "draw_categorical_flow",
    "draw_categorical_flow_comparison",
    "validate_agent_composition",
    "get_flow_statistics",
    
    # Layout convenience functions
    "draw_linear_flow",
    "draw_hierarchical_flow", 
    "draw_temporal_flow",
    
    # Core types
    "Node",
    "Edge", 
    "AgentStructure",
    "TypeInfo",
    "NodeType",
    "FlowType",
    "LayoutType",
    
    # Constants
    "COLORS",
    "FLOW_STYLES",
    
    # Internal utilities (exposed for advanced usage)
    "extract_agent_structure",
    "get_tool_signature",
    "validate_composition",
    "extract_type_information",
    "get_agent_metadata",
    "calculate_layout",
    "layout_linear",
    "layout_hierarchical",
    "layout_temporal",
    "optimize_layout",
    "create_categorical_diagram",
    "save_diagram",
    "create_interactive_diagram"
]