"""
Matplotlib visualization engine for categorical diagrams.

This module handles the actual rendering of categorical diagrams using matplotlib,
including node drawing, edge rendering, and type annotations.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np
from typing import List, Dict, Tuple, Optional
try:
    from .data_types import Node, Edge, AgentStructure, LayoutPositions, COLORS, FLOW_STYLES
except ImportError:
    from data_types import Node, Edge, AgentStructure, LayoutPositions, COLORS, FLOW_STYLES


def draw_node(ax: plt.Axes, node: Node, position: Dict[str, float], 
              show_types: bool = True) -> None:
    """
    Draw a node on the matplotlib axes.
    
    Args:
        ax: Matplotlib axes
        node: Node to draw
        position: Position dictionary with x, y, width, height
        show_types: Whether to show type information
    """
    x, y = position["x"], position["y"]
    width, height = position["width"], position["height"]
    
    # Get color for node type
    color = COLORS.get(node.type, "#6b7280")
    
    # Draw different shapes based on node type
    if node.type == "agent":
        # Rectangle for agents
        rect = FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor="black",
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(rect)
        
    elif node.type == "tool":
        # Ellipse for tools
        ellipse = patches.Ellipse(
            (x, y), width, height,
            facecolor=color,
            edgecolor="black",
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(ellipse)
        
    elif node.type == "guardrail":
        # Diamond for guardrails
        diamond = patches.Polygon([
            (x, y + height/2),
            (x + width/2, y),
            (x, y - height/2),
            (x - width/2, y)
        ], facecolor=color, edgecolor="black", linewidth=2, alpha=0.8)
        ax.add_patch(diamond)
        
    else:
        # Default rectangle for other types
        rect = patches.Rectangle(
            (x - width/2, y - height/2), width, height,
            facecolor=color,
            edgecolor="black",
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(rect)
    
    # Add text label
    ax.text(x, y, node.name, ha='center', va='center', 
            fontsize=10, fontweight='bold', color='black')
    
    # Add type annotation if requested
    if show_types and node.metadata and 'instructions' in node.metadata:
        # Show truncated instructions
        instructions = node.metadata['instructions']
        if len(instructions) > 30:
            instructions = instructions[:30] + "..."
        ax.text(x, y - height/2 - 0.2, instructions, 
                ha='center', va='top', fontsize=8, color='gray')


def draw_edge(ax: plt.Axes, edge: Edge, source_pos: Dict[str, float], 
              target_pos: Dict[str, float], show_types: bool = True) -> None:
    """
    Draw an edge (morphism) on the matplotlib axes.
    
    Args:
        ax: Matplotlib axes
        edge: Edge to draw
        source_pos: Source node position
        target_pos: Target node position
        show_types: Whether to show type annotations
    """
    # Get edge style
    style = FLOW_STYLES.get(edge.flow_type, {})
    color = style.get("color", "#6b7280")
    linestyle = style.get("style", "solid")
    linewidth = style.get("width", 2)
    
    # Convert linestyle string to matplotlib style
    if linestyle == "dashed":
        linestyle = "--"
    elif linestyle == "dotted":
        linestyle = ":"
    else:
        linestyle = "-"
    
    # Calculate arrow positions
    source_x, source_y = source_pos["x"], source_pos["y"]
    target_x, target_y = target_pos["x"], target_pos["y"]
    
    # Draw arrow
    arrow = ConnectionPatch(
        (source_x, source_y), (target_x, target_y),
        "data", "data",
        arrowstyle="->",
        shrinkA=5,
        shrinkB=5,
        mutation_scale=20,
        fc=color,
        ec=color,
        linewidth=linewidth,
        linestyle=linestyle
    )
    ax.add_patch(arrow)
    
    # Add type annotation if available
    if show_types and edge.type_annotation:
        # Position annotation at midpoint
        mid_x = (source_x + target_x) / 2
        mid_y = (source_y + target_y) / 2
        
        # Add background for better readability
        ax.text(mid_x, mid_y, edge.type_annotation,
                ha='center', va='center', fontsize=8, color='black',
                bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))


def add_legend(ax: plt.Axes) -> None:
    """
    Add a legend to the diagram.
    
    Args:
        ax: Matplotlib axes
    """
    legend_elements = []
    legend_labels = []
    
    # Add legend entries for each node type
    for node_type, color in COLORS.items():
        if node_type == "agent":
            element = patches.Rectangle((0, 0), 1, 1, facecolor=color, alpha=0.8)
        elif node_type == "tool":
            element = patches.Ellipse((0, 0), 1, 1, facecolor=color, alpha=0.8)
        elif node_type == "guardrail":
            element = patches.Polygon([(0, 0.5), (0.5, 0), (0, -0.5), (-0.5, 0)], 
                                    facecolor=color, alpha=0.8)
        else:
            element = patches.Rectangle((0, 0), 1, 1, facecolor=color, alpha=0.8)
        
        legend_elements.append(element)
        legend_labels.append(node_type.title())
    
    # Add legend entries for edge types
    for flow_type, style in FLOW_STYLES.items():
        element = plt.Line2D([0], [0], color=style["color"], 
                           linestyle=style["style"], linewidth=style["width"])
        legend_elements.append(element)
        legend_labels.append(f"{flow_type.replace('_', ' ').title()}")
    
    ax.legend(legend_elements, legend_labels, loc='upper right', 
              bbox_to_anchor=(1.15, 1.0))


def add_type_annotations(ax: plt.Axes, edges: List[Edge]) -> None:
    """
    Add type annotations to the diagram.
    
    Args:
        ax: Matplotlib axes
        edges: List of edges
    """
    # This function can be enhanced to show more detailed type information
    # For now, type annotations are handled in draw_edge
    pass


def create_categorical_diagram(agent_structure: AgentStructure, 
                              positions: LayoutPositions,
                              layout: str = "hierarchical",
                              show_types: bool = True,
                              show_flow_direction: bool = True,
                              figsize: Tuple[int, int] = (12, 8)) -> plt.Figure:
    """
    Generate the actual matplotlib visualization.
    
    Args:
        agent_structure: Extracted agent structure
        positions: Node positions
        layout: Layout type used
        show_types: Whether to show type annotations
        show_flow_direction: Whether to show flow direction
        figsize: Figure size
        
    Returns:
        Matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Set up the plot
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Calculate plot bounds
    all_x = [pos["x"] for pos in positions.values()]
    all_y = [pos["y"] for pos in positions.values()]
    
    if all_x and all_y:
        x_min, x_max = min(all_x), max(all_x)
        y_min, y_max = min(all_y), max(all_y)
        
        # Add padding
        x_padding = (x_max - x_min) * 0.1
        y_padding = (y_max - y_min) * 0.1
        
        ax.set_xlim(x_min - x_padding, x_max + x_padding)
        ax.set_ylim(y_min - y_padding, y_max + y_padding)
    
    # Draw edges first (so they appear behind nodes)
    for edge in agent_structure.edges:
        source_pos = positions.get(edge.source)
        target_pos = positions.get(edge.target)
        
        if source_pos and target_pos:
            draw_edge(ax, edge, source_pos, target_pos, show_types)
    
    # Draw nodes
    for node in agent_structure.nodes:
        pos = positions.get(node.id)
        if pos:
            draw_node(ax, node, pos, show_types)
    
    # Add legend
    add_legend(ax)
    
    # Add title
    ax.set_title(f"Categorical Flow Diagram - {layout.title()} Layout", 
                 fontsize=14, fontweight='bold', pad=20)
    
    return fig


def save_diagram(fig: plt.Figure, save_path: Optional[str] = None, 
                 dpi: int = 300) -> None:
    """
    Save the diagram to a file.
    
    Args:
        fig: Matplotlib figure
        save_path: Path to save the file (optional)
        dpi: DPI for saving
    """
    if save_path:
        fig.savefig(save_path, dpi=dpi, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        print(f"Diagram saved to: {save_path}")


def create_interactive_diagram(agent_structure: AgentStructure,
                              positions: LayoutPositions,
                              **kwargs) -> plt.Figure:
    """
    Create an interactive version of the diagram with hover tooltips.
    
    Args:
        agent_structure: Extracted agent structure
        positions: Node positions
        **kwargs: Additional arguments for create_categorical_diagram
        
    Returns:
        Interactive matplotlib figure
    """
    # This is a placeholder for interactive features
    # In a full implementation, this would add hover tooltips and click handlers
    return create_categorical_diagram(agent_structure, positions, **kwargs)