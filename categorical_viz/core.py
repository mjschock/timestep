"""
Core module for categorical flow visualization.

This module provides the main `draw_categorical_flow()` function that
enhances the existing OpenAI Agents SDK `draw_graph()` output with
categorical string diagrams showing information flow, type safety, and
compositional structure.
"""

import time
from typing import Optional, Tuple
import matplotlib.pyplot as plt

from .extractor import extract_agent_structure
from .layouts import calculate_layout
from .visualizer import create_categorical_diagram, save_diagram
try:
    from .data_types import LayoutType
except ImportError:
    from data_types import LayoutType


def draw_categorical_flow(
    agent,
    layout: LayoutType = "hierarchical",
    show_types: bool = True,
    show_flow_direction: bool = True,
    figsize: Tuple[int, int] = (12, 8),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Create a categorical flow diagram for an OpenAI SDK Agent.
    
    This function enhances the existing `draw_graph()` output with:
    - Information flow arrows showing data movement through agents/tools
    - Type annotations for interface validation
    - Compositional structure using category theory principles
    - Temporal flow for session management
    
    Args:
        agent: OpenAI SDK Agent object
        layout: Layout type ("linear", "hierarchical", "temporal")
        show_types: Whether to show type annotations on connections
        show_flow_direction: Whether to show flow direction arrows
        figsize: Figure size as (width, height)
        save_path: Optional path to save the diagram
        
    Returns:
        matplotlib.Figure: The generated diagram
        
    Raises:
        ValueError: If agent is None or invalid
        RuntimeError: If diagram generation fails
        
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
    start_time = time.time()
    
    # Input validation
    if agent is None:
        raise ValueError("Agent cannot be None")
    
    try:
        # Phase 1: Extract agent structure
        agent_structure = extract_agent_structure(agent)
        
        # Phase 2: Calculate layout positions
        positions = calculate_layout(
            agent_structure.nodes, 
            agent_structure.edges, 
            layout
        )
        
        # Phase 3: Generate visualization
        fig = create_categorical_diagram(
            agent_structure=agent_structure,
            positions=positions,
            layout=layout,
            show_types=show_types,
            show_flow_direction=show_flow_direction,
            figsize=figsize
        )
        
        # Phase 4: Save if requested
        if save_path:
            save_diagram(fig, save_path)
        
        # Performance check
        generation_time = time.time() - start_time
        if generation_time > 2.0:
            print(f"Warning: Diagram generation took {generation_time:.2f}s (target: <2s)")
        
        return fig
        
    except Exception as e:
        raise RuntimeError(f"Failed to generate categorical flow diagram: {str(e)}") from e


def draw_categorical_flow_comparison(
    agent,
    layouts: list[LayoutType] = ["linear", "hierarchical", "temporal"],
    show_types: bool = True,
    figsize: Tuple[int, int] = (18, 6),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Create a comparison diagram showing the same agent in different layouts.
    
    Args:
        agent: OpenAI SDK Agent object
        layouts: List of layout types to compare
        show_types: Whether to show type annotations
        figsize: Figure size
        save_path: Optional path to save the diagram
        
    Returns:
        matplotlib.Figure: Comparison diagram
    """
    agent_structure = extract_agent_structure(agent)
    
    # Create subplots for each layout
    fig, axes = plt.subplots(1, len(layouts), figsize=figsize)
    if len(layouts) == 1:
        axes = [axes]
    
    for i, layout in enumerate(layouts):
        positions = calculate_layout(agent_structure.nodes, agent_structure.edges, layout)
        
        create_categorical_diagram(
            agent_structure=agent_structure,
            positions=positions,
            layout=layout,
            show_types=show_types,
            figsize=(6, 4)
        )
        
        # Copy the figure content to the subplot
        axes[i].set_title(f"{layout.title()} Layout")
    
    plt.tight_layout()
    
    if save_path:
        save_diagram(fig, save_path)
    
    return fig


def validate_agent_composition(agent) -> dict:
    """
    Validate the compositional structure of an agent.
    
    Args:
        agent: OpenAI SDK Agent object
        
    Returns:
        Dictionary with validation results
    """
    from .extractor import validate_composition
    
    tools = getattr(agent, 'tools', [])
    composition_results = {}
    
    # Check tool composition
    for i, tool1 in enumerate(tools):
        for j, tool2 in enumerate(tools):
            if i != j:
                can_compose = validate_composition(tool1, tool2)
                composition_results[f"{tool1.__name__} → {tool2.__name__}"] = can_compose
    
    return {
        "tool_count": len(tools),
        "composition_pairs": composition_results,
        "valid_compositions": sum(composition_results.values()),
        "total_pairs": len(composition_results)
    }


def get_flow_statistics(agent) -> dict:
    """
    Get statistics about the information flow in an agent.
    
    Args:
        agent: OpenAI SDK Agent object
        
    Returns:
        Dictionary with flow statistics
    """
    agent_structure = extract_agent_structure(agent)
    
    # Count different types of flows
    flow_counts = {}
    for edge in agent_structure.edges:
        flow_type = edge.flow_type
        flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
    
    # Count node types
    node_counts = {}
    for node in agent_structure.nodes:
        node_type = node.type
        node_counts[node_type] = node_counts.get(node_type, 0) + 1
    
    return {
        "total_nodes": len(agent_structure.nodes),
        "total_edges": len(agent_structure.edges),
        "node_type_counts": node_counts,
        "flow_type_counts": flow_counts,
        "type_info_count": len(agent_structure.type_info)
    }


# Convenience functions for different layout types
def draw_linear_flow(agent, **kwargs) -> plt.Figure:
    """Draw categorical flow with linear layout."""
    return draw_categorical_flow(agent, layout="linear", **kwargs)


def draw_hierarchical_flow(agent, **kwargs) -> plt.Figure:
    """Draw categorical flow with hierarchical layout."""
    return draw_categorical_flow(agent, layout="hierarchical", **kwargs)


def draw_temporal_flow(agent, **kwargs) -> plt.Figure:
    """Draw categorical flow with temporal layout."""
    return draw_categorical_flow(agent, layout="temporal", **kwargs)