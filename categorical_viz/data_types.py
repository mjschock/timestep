"""
Type definitions and data structures for categorical visualization.

This module defines the core types used in the categorical flow visualization
system, including nodes, edges, and flow types.
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional, Literal, Any
import inspect
try:
    from typing_extensions import TypedDict
except ImportError:
    from typing import TypedDict


# Node types (Objects in Category)
NodeType = Literal["agent", "tool", "guardrail", "session", "start"]

# Flow types (Morphisms in Category)  
FlowType = Literal["input", "output", "tool_call", "tool_result", 
                  "handoff", "guardrail", "session"]

# Layout types
LayoutType = Literal["linear", "hierarchical", "temporal"]


@dataclass
class Node:
    """Represents a node in the categorical diagram."""
    id: str
    type: NodeType
    name: str
    metadata: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class Edge:
    """Represents an edge (morphism) in the categorical diagram."""
    source: str
    target: str
    flow_type: FlowType
    type_annotation: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class TypeInfo:
    """Type information extracted from function signatures."""
    inputs: List[str]
    output: str
    
    @classmethod
    def from_function(cls, func) -> 'TypeInfo':
        """Extract type information from a function."""
        sig = inspect.signature(func)
        inputs = []
        for param in sig.parameters.values():
            if param.annotation == inspect.Parameter.empty:
                inputs.append("Any")
            else:
                inputs.append(param.annotation.__name__)
        
        if sig.return_annotation == inspect.Signature.empty:
            output = "Any"
        else:
            output = sig.return_annotation.__name__
            
        return cls(inputs=inputs, output=output)


# Color schemes (compatible with current SDK)
COLORS = {
    "agent": "#fbbf24",     # Yellow (matches current draw_graph)
    "tool": "#10b981",      # Green (matches current draw_graph)  
    "guardrail": "#ef4444", # Red
    "session": "#8b5cf6",   # Purple
    "start": "#374151"      # Gray
}

# Arrow styles for different flow types
FLOW_STYLES = {
    "input": {"color": "#3b82f6", "style": "solid", "width": 3},
    "output": {"color": "#dc2626", "style": "solid", "width": 3},
    "tool_call": {"color": "#10b981", "style": "solid", "width": 2},
    "tool_result": {"color": "#10b981", "style": "dashed", "width": 2},
    "handoff": {"color": "#f59e0b", "style": "dashed", "width": 2.5},
    "guardrail": {"color": "#ef4444", "style": "dotted", "width": 2},
    "session": {"color": "#8b5cf6", "style": "dotted", "width": 1.5}
}


@dataclass
class AgentStructure:
    """Complete structure extracted from an Agent object."""
    nodes: List[Node]
    edges: List[Edge]
    type_info: Dict[str, TypeInfo]
    
    def get_node_by_id(self, node_id: str) -> Optional[Node]:
        """Get a node by its ID."""
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None
    
    def get_edges_from(self, source_id: str) -> List[Edge]:
        """Get all edges originating from a node."""
        return [edge for edge in self.edges if edge.source == source_id]
    
    def get_edges_to(self, target_id: str) -> List[Edge]:
        """Get all edges pointing to a node."""
        return [edge for edge in self.edges if edge.target == target_id]


class LayoutPosition(TypedDict):
    """Position information for layout algorithms."""
    x: float
    y: float
    width: float
    height: float


LayoutPositions = Dict[str, LayoutPosition]