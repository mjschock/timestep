"""
Layout algorithms for categorical visualization.

This module provides different layout algorithms for positioning nodes
in the categorical diagram, including linear, hierarchical, and temporal layouts.
"""

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    # Mock networkx for basic functionality
    class MockNetworkx:
        class DiGraph:
            def __init__(self):
                self.nodes = []
                self.edges = []
            
            def add_node(self, node_id, **kwargs):
                self.nodes.append((node_id, kwargs))
            
            def add_edge(self, source, target, **kwargs):
                self.edges.append((source, target, kwargs))
        
        @staticmethod
        def spring_layout(G, **kwargs):
            return {node_id: (0.0, 0.0) for node_id, _ in G.nodes}
    
    nx = MockNetworkx()

from typing import List, Dict, Tuple
try:
    from .data_types import Node, Edge, AgentStructure, LayoutPositions, LayoutType
except ImportError:
    from data_types import Node, Edge, AgentStructure, LayoutPositions, LayoutType


def layout_linear(nodes: List[Node], edges: List[Edge]) -> LayoutPositions:
    """
    Left-to-right flow: input → agent → tools → output
    
    Args:
        nodes: List of nodes to position
        edges: List of edges for connectivity
        
    Returns:
        Dictionary mapping node IDs to positions
    """
    positions = {}
    
    # Group nodes by type for positioning
    start_nodes = [n for n in nodes if n.type == "start"]
    agent_nodes = [n for n in nodes if n.type == "agent"]
    tool_nodes = [n for n in nodes if n.type == "tool"]
    guardrail_nodes = [n for n in nodes if n.type == "guardrail"]
    session_nodes = [n for n in nodes if n.type == "session"]
    
    # Calculate positions
    x_spacing = 2.0
    y_spacing = 1.5
    
    # Position start nodes (leftmost)
    for i, node in enumerate(start_nodes):
        positions[node.id] = {
            "x": 0,
            "y": i * y_spacing,
            "width": 1.0,
            "height": 0.8
        }
    
    # Position agent nodes
    for i, node in enumerate(agent_nodes):
        positions[node.id] = {
            "x": x_spacing,
            "y": i * y_spacing,
            "width": 1.5,
            "height": 1.0
        }
    
    # Position tool nodes (to the right of agents)
    for i, node in enumerate(tool_nodes):
        positions[node.id] = {
            "x": 2 * x_spacing,
            "y": i * y_spacing,
            "width": 1.2,
            "height": 0.8
        }
    
    # Position guardrail nodes (above and below main flow)
    for i, node in enumerate(guardrail_nodes):
        if "input" in node.id:
            # Input guardrails above
            positions[node.id] = {
                "x": x_spacing,
                "y": (i + 1) * y_spacing,
                "width": 1.0,
                "height": 0.6
            }
        else:
            # Output guardrails below
            positions[node.id] = {
                "x": x_spacing,
                "y": -(i + 1) * y_spacing,
                "width": 1.0,
                "height": 0.6
            }
    
    # Position session nodes (rightmost)
    for i, node in enumerate(session_nodes):
        positions[node.id] = {
            "x": 3 * x_spacing,
            "y": i * y_spacing,
            "width": 1.0,
            "height": 0.8
        }
    
    return positions


def layout_hierarchical(nodes: List[Node], edges: List[Edge]) -> LayoutPositions:
    """
    Tree structure showing agent-tool-handoff relationships.
    
    Args:
        nodes: List of nodes to position
        edges: List of edges for connectivity
        
    Returns:
        Dictionary mapping node IDs to positions
    """
    # Create networkx graph for layout
    G = nx.DiGraph()
    
    # Add nodes
    for node in nodes:
        G.add_node(node.id, type=node.type, name=node.name)
    
    # Add edges
    for edge in edges:
        G.add_edge(edge.source, edge.target, flow_type=edge.flow_type)
    
    # Use hierarchical layout
    pos = nx.spring_layout(G, k=3, iterations=50)
    
    # Convert to our format
    positions = {}
    for node_id, (x, y) in pos.items():
        node = next(n for n in nodes if n.id == node_id)
        
        # Adjust size based on node type
        if node.type == "agent":
            width, height = 1.5, 1.0
        elif node.type == "tool":
            width, height = 1.2, 0.8
        elif node.type == "guardrail":
            width, height = 1.0, 0.6
        else:
            width, height = 1.0, 0.8
        
        positions[node_id] = {
            "x": float(x * 3),  # Scale for better spacing
            "y": float(y * 2),
            "width": width,
            "height": height
        }
    
    return positions


def layout_temporal(nodes: List[Node], edges: List[Edge]) -> LayoutPositions:
    """
    Time-based layout for session evolution.
    
    Args:
        nodes: List of nodes to position
        edges: List of edges for connectivity
        
    Returns:
        Dictionary mapping node IDs to positions
    """
    positions = {}
    
    # Group nodes by temporal order
    start_nodes = [n for n in nodes if n.type == "start"]
    input_guardrails = [n for n in nodes if n.type == "guardrail" and "input" in n.id]
    agent_nodes = [n for n in nodes if n.type == "agent"]
    tool_nodes = [n for n in nodes if n.type == "tool"]
    output_guardrails = [n for n in nodes if n.type == "guardrail" and "output" in n.id]
    session_nodes = [n for n in nodes if n.type == "session"]
    
    # Temporal positioning (left to right = time progression)
    x_spacing = 2.0
    y_spacing = 1.5
    
    # Time step 0: Start
    for i, node in enumerate(start_nodes):
        positions[node.id] = {
            "x": 0,
            "y": i * y_spacing,
            "width": 1.0,
            "height": 0.8
        }
    
    # Time step 1: Input guardrails
    for i, node in enumerate(input_guardrails):
        positions[node.id] = {
            "x": x_spacing,
            "y": i * y_spacing,
            "width": 1.0,
            "height": 0.6
        }
    
    # Time step 2: Main agents
    for i, node in enumerate(agent_nodes):
        positions[node.id] = {
            "x": 2 * x_spacing,
            "y": i * y_spacing,
            "width": 1.5,
            "height": 1.0
        }
    
    # Time step 3: Tools (can happen in parallel)
    for i, node in enumerate(tool_nodes):
        positions[node.id] = {
            "x": 3 * x_spacing,
            "y": i * y_spacing,
            "width": 1.2,
            "height": 0.8
        }
    
    # Time step 4: Output guardrails
    for i, node in enumerate(output_guardrails):
        positions[node.id] = {
            "x": 4 * x_spacing,
            "y": i * y_spacing,
            "width": 1.0,
            "height": 0.6
        }
    
    # Time step 5: Session output
    for i, node in enumerate(session_nodes):
        positions[node.id] = {
            "x": 5 * x_spacing,
            "y": i * y_spacing,
            "width": 1.0,
            "height": 0.8
        }
    
    return positions


def calculate_layout(nodes: List[Node], edges: List[Edge], layout_type: LayoutType) -> LayoutPositions:
    """
    Calculate node positions based on layout type.
    
    Args:
        nodes: List of nodes to position
        edges: List of edges for connectivity
        layout_type: Type of layout to use
        
    Returns:
        Dictionary mapping node IDs to positions
    """
    if layout_type == "linear":
        return layout_linear(nodes, edges)
    elif layout_type == "hierarchical":
        return layout_hierarchical(nodes, edges)
    elif layout_type == "temporal":
        return layout_temporal(nodes, edges)
    else:
        raise ValueError(f"Unknown layout type: {layout_type}")


def optimize_layout(positions: LayoutPositions, edges: List[Edge]) -> LayoutPositions:
    """
    Optimize layout to minimize edge crossings and improve readability.
    
    Args:
        positions: Current node positions
        edges: List of edges
        
    Returns:
        Optimized positions
    """
    # Simple optimization: adjust positions to reduce edge crossings
    # This is a basic implementation - could be enhanced with more sophisticated algorithms
    
    # Calculate center of mass
    center_x = sum(pos["x"] for pos in positions.values()) / len(positions)
    center_y = sum(pos["y"] for pos in positions.values()) / len(positions)
    
    # Adjust positions to be more centered
    optimized = {}
    for node_id, pos in positions.items():
        optimized[node_id] = {
            "x": pos["x"] - center_x,
            "y": pos["y"] - center_y,
            "width": pos["width"],
            "height": pos["height"]
        }
    
    return optimized