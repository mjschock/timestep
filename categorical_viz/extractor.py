"""
Agent structure extraction for categorical visualization.

This module extracts the categorical structure from OpenAI SDK Agent objects,
including tools, handoffs, guardrails, and type information.
"""

import inspect
from typing import List, Dict, Optional, Any
try:
    from .data_types import Node, Edge, AgentStructure, TypeInfo, FlowType, NodeType
except ImportError:
    from data_types import Node, Edge, AgentStructure, TypeInfo, FlowType, NodeType


def extract_agent_structure(agent) -> AgentStructure:
    """
    Extract categorical structure from SDK Agent object.
    
    Args:
        agent: OpenAI SDK Agent object
        
    Returns:
        AgentStructure containing nodes, edges, and type information
    """
    nodes = []
    edges = []
    type_info = {}
    
    # 1. Create start node
    nodes.append(Node(id="start", type="start", name="input"))
    
    # 2. Create main agent node
    agent_id = f"agent_{agent.name}"
    nodes.append(Node(
        id=agent_id, 
        type="agent", 
        name=agent.name,
        metadata={"instructions": getattr(agent, 'instructions', '')}
    ))
    
    # 3. Extract tools
    tools = getattr(agent, 'tools', [])
    for tool in tools:
        tool_id = f"tool_{tool.__name__}"
        nodes.append(Node(id=tool_id, type="tool", name=tool.__name__))
        
        # Extract type information
        type_info[tool_id] = TypeInfo.from_function(tool)
        
        # Add bidirectional edges for tool calls
        edges.append(Edge(
            source=agent_id, 
            target=tool_id, 
            flow_type="tool_call",
            type_annotation=f"→ {type_info[tool_id].inputs[0] if type_info[tool_id].inputs else 'Any'}"
        ))
        edges.append(Edge(
            source=tool_id, 
            target=agent_id, 
            flow_type="tool_result",
            type_annotation=f"→ {type_info[tool_id].output}"
        ))
    
    # 4. Extract handoffs
    handoffs = getattr(agent, 'handoffs', [])
    for handoff in handoffs:
        handoff_id = f"handoff_{handoff.name}"
        nodes.append(Node(id=handoff_id, type="agent", name=handoff.name))
        edges.append(Edge(
            source=agent_id, 
            target=handoff_id, 
            flow_type="handoff"
        ))
    
    # 5. Extract input guardrails
    input_guardrails = getattr(agent, 'input_guardrails', [])
    for i, guardrail in enumerate(input_guardrails):
        guard_id = f"input_guard_{i}"
        nodes.append(Node(id=guard_id, type="guardrail", name=f"input_guard_{i}"))
        edges.append(Edge(source="start", target=guard_id, flow_type="guardrail"))
        edges.append(Edge(source=guard_id, target=agent_id, flow_type="guardrail"))
    
    # 6. Extract output guardrails
    output_guardrails = getattr(agent, 'output_guardrails', [])
    for i, guardrail in enumerate(output_guardrails):
        guard_id = f"output_guard_{i}"
        nodes.append(Node(id=guard_id, type="guardrail", name=f"output_guard_{i}"))
        edges.append(Edge(source=agent_id, target=guard_id, flow_type="guardrail"))
        # Add edge to output (we'll create an output node)
        if not any(node.id == "output" for node in nodes):
            nodes.append(Node(id="output", type="session", name="output"))
        edges.append(Edge(source=guard_id, target="output", flow_type="guardrail"))
    
    # 7. Add input/output edges if not already present
    if not any(edge.source == "start" and edge.target == agent_id for edge in edges):
        edges.append(Edge(source="start", target=agent_id, flow_type="input"))
    
    if not any(edge.source == agent_id and edge.target == "output" for edge in edges):
        if not any(node.id == "output" for node in nodes):
            nodes.append(Node(id="output", type="session", name="output"))
        edges.append(Edge(source=agent_id, target="output", flow_type="output"))
    
    return AgentStructure(nodes=nodes, edges=edges, type_info=type_info)


def get_tool_signature(tool) -> tuple[str, List[str], str]:
    """
    Extract function signature information from a tool.
    
    Args:
        tool: Function tool object
        
    Returns:
        Tuple of (function_name, input_types, output_type)
    """
    sig = inspect.signature(tool)
    input_types = []
    for param in sig.parameters.values():
        if param.annotation == inspect.Parameter.empty:
            input_types.append("Any")
        else:
            input_types.append(param.annotation.__name__)
    
    if sig.return_annotation == inspect.Signature.empty:
        output_type = "Any"
    else:
        output_type = sig.return_annotation.__name__
    
    return tool.__name__, input_types, output_type


def validate_composition(source_tool, target_tool) -> bool:
    """
    Check if tools can compose (output type matches input type).
    
    Args:
        source_tool: Source function tool
        target_tool: Target function tool
        
    Returns:
        True if tools can compose, False otherwise
    """
    source_info = TypeInfo.from_function(source_tool)
    target_info = TypeInfo.from_function(target_tool)
    
    # Check if source output type matches any target input type
    return source_info.output in target_info.inputs or "Any" in target_info.inputs


def extract_type_information(tool) -> Dict[str, str]:
    """
    Extract type annotations from function tools.
    
    Args:
        tool: Function tool object
        
    Returns:
        Dictionary with 'inputs' and 'output' type information
    """
    sig = inspect.signature(tool)
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
    
    return {
        "inputs": inputs,
        "output": output
    }


def get_agent_metadata(agent) -> Dict[str, Any]:
    """
    Extract metadata from an agent object.
    
    Args:
        agent: OpenAI SDK Agent object
        
    Returns:
        Dictionary of agent metadata
    """
    metadata = {}
    
    # Extract basic properties
    for attr in ['name', 'instructions', 'model']:
        if hasattr(agent, attr):
            metadata[attr] = getattr(agent, attr)
    
    # Extract tool information
    if hasattr(agent, 'tools'):
        metadata['tool_count'] = len(agent.tools)
        metadata['tool_names'] = [tool.__name__ for tool in agent.tools]
    
    # Extract handoff information
    if hasattr(agent, 'handoffs'):
        metadata['handoff_count'] = len(agent.handoffs)
        metadata['handoff_names'] = [h.name for h in agent.handoffs]
    
    # Extract guardrail information
    if hasattr(agent, 'input_guardrails'):
        metadata['input_guardrail_count'] = len(agent.input_guardrails)
    if hasattr(agent, 'output_guardrails'):
        metadata['output_guardrail_count'] = len(agent.output_guardrails)
    
    return metadata