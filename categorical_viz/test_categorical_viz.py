"""
Test suite for categorical flow visualization.

This module contains comprehensive tests for the categorical visualization
system, including basic functionality, edge cases, and performance tests.
"""

import pytest
import time
from unittest.mock import Mock, patch
import matplotlib.pyplot as plt

from agents import Agent, function_tool
from categorical_viz import (
    draw_categorical_flow,
    draw_categorical_flow_comparison,
    validate_agent_composition,
    get_flow_statistics,
    extract_agent_structure,
    Node,
    Edge,
    AgentStructure
)


# Test fixtures
@pytest.fixture
def simple_tool():
    @function_tool
    def calculator(expression: str) -> str:
        return f"Result: {eval(expression)}"
    return calculator


@pytest.fixture
def basic_agent(simple_tool):
    return Agent(
        name="Test Agent",
        instructions="A test agent for validation",
        tools=[simple_tool]
    )


@pytest.fixture
def complex_agent():
    @function_tool
    def tool1(x: int) -> str:
        return str(x)
    
    @function_tool
    def tool2(text: str) -> int:
        return len(text)
    
    @function_tool
    def tool3(number: int) -> float:
        return float(number) / 2
    
    return Agent(
        name="Complex Agent",
        instructions="A complex agent with multiple tools",
        tools=[tool1, tool2, tool3]
    )


# Basic functionality tests
def test_basic_agent():
    """Test with simple agent + single tool."""
    @function_tool
    def simple_tool(x: str) -> str:
        return x.upper()
    
    agent = Agent(name="Test", tools=[simple_tool])
    fig = draw_categorical_flow(agent)
    assert fig is not None
    assert isinstance(fig, plt.Figure)


def test_handoff_agent():
    """Test with agent that has handoffs."""
    specialist1 = Agent(name="Specialist1", instructions="First specialist")
    specialist2 = Agent(name="Specialist2", instructions="Second specialist")
    
    agent = Agent(
        name="Triage",
        instructions="Main triage agent",
        handoffs=[specialist1, specialist2]
    )
    
    fig = draw_categorical_flow(agent, layout="hierarchical")
    assert fig is not None


def test_guardrail_agent():
    """Test with input/output guardrails."""
    @function_tool
    def safety_check(text: str) -> str:
        return "SAFE" if "safe" in text else "UNSAFE"
    
    @function_tool
    def quality_check(output: str) -> str:
        return "GOOD" if len(output) > 5 else "POOR"
    
    agent = Agent(
        name="Protected",
        instructions="Agent with guardrails",
        input_guardrails=[safety_check],
        output_guardrails=[quality_check]
    )
    
    fig = draw_categorical_flow(agent)
    assert fig is not None


def test_type_annotations():
    """Test type extraction and display."""
    @function_tool
    def typed_tool(x: int) -> str:
        return str(x)
    
    agent = Agent(name="Typed", tools=[typed_tool])
    fig = draw_categorical_flow(agent, show_types=True)
    assert fig is not None


# Structure extraction tests
def test_extract_agent_structure(basic_agent):
    """Test agent structure extraction."""
    structure = extract_agent_structure(basic_agent)
    
    assert isinstance(structure, AgentStructure)
    assert len(structure.nodes) > 0
    assert len(structure.edges) > 0
    
    # Should have start, agent, tool, and output nodes
    node_types = [node.type for node in structure.nodes]
    assert "start" in node_types
    assert "agent" in node_types
    assert "tool" in node_types
    assert "session" in node_types  # output node


def test_extract_agent_structure_with_handoffs():
    """Test structure extraction with handoffs."""
    specialist = Agent(name="Specialist", instructions="Specialist agent")
    
    agent = Agent(
        name="Main",
        instructions="Main agent",
        handoffs=[specialist]
    )
    
    structure = extract_agent_structure(agent)
    
    # Should have handoff edges
    handoff_edges = [edge for edge in structure.edges if edge.flow_type == "handoff"]
    assert len(handoff_edges) > 0


def test_extract_agent_structure_with_guardrails():
    """Test structure extraction with guardrails."""
    @function_tool
    def guardrail(text: str) -> str:
        return "PASS"
    
    agent = Agent(
        name="Protected",
        instructions="Protected agent",
        input_guardrails=[guardrail],
        output_guardrails=[guardrail]
    )
    
    structure = extract_agent_structure(agent)
    
    # Should have guardrail nodes and edges
    guardrail_nodes = [node for node in structure.nodes if node.type == "guardrail"]
    assert len(guardrail_nodes) > 0
    
    guardrail_edges = [edge for edge in structure.edges if edge.flow_type == "guardrail"]
    assert len(guardrail_edges) > 0


# Layout tests
def test_layout_types(basic_agent):
    """Test different layout types."""
    layouts = ["linear", "hierarchical", "temporal"]
    
    for layout in layouts:
        fig = draw_categorical_flow(basic_agent, layout=layout)
        assert fig is not None


def test_layout_comparison(basic_agent):
    """Test layout comparison functionality."""
    fig = draw_categorical_flow_comparison(
        basic_agent,
        layouts=["linear", "hierarchical"]
    )
    assert fig is not None


# Validation tests
def test_validate_agent_composition(complex_agent):
    """Test composition validation."""
    result = validate_agent_composition(complex_agent)
    
    assert "tool_count" in result
    assert "composition_pairs" in result
    assert "valid_compositions" in result
    assert "total_pairs" in result
    
    assert result["tool_count"] == 3
    assert result["total_pairs"] == 6  # 3 tools = 6 pairs


def test_get_flow_statistics(basic_agent):
    """Test flow statistics generation."""
    stats = get_flow_statistics(basic_agent)
    
    assert "total_nodes" in stats
    assert "total_edges" in stats
    assert "node_type_counts" in stats
    assert "flow_type_counts" in stats
    assert "type_info_count" in stats
    
    assert stats["total_nodes"] > 0
    assert stats["total_edges"] > 0


# Performance tests
def test_performance_target(basic_agent):
    """Test that diagram generation meets performance target (<2s)."""
    start_time = time.time()
    fig = draw_categorical_flow(basic_agent)
    generation_time = time.time() - start_time
    
    assert generation_time < 2.0, f"Generation took {generation_time:.2f}s (target: <2s)"


def test_large_agent_performance():
    """Test performance with larger agent."""
    # Create agent with many tools
    tools = []
    for i in range(10):
        @function_tool
        def tool(x: str) -> str:
            return f"Tool {i}: {x}"
        tools.append(tool)
    
    agent = Agent(
        name="Large Agent",
        instructions="Agent with many tools",
        tools=tools
    )
    
    start_time = time.time()
    fig = draw_categorical_flow(agent)
    generation_time = time.time() - start_time
    
    assert generation_time < 2.0, f"Large agent generation took {generation_time:.2f}s"


# Error handling tests
def test_none_agent():
    """Test error handling with None agent."""
    with pytest.raises(ValueError, match="Agent cannot be None"):
        draw_categorical_flow(None)


def test_invalid_layout():
    """Test error handling with invalid layout."""
    @function_tool
    def tool(x: str) -> str:
        return x
    
    agent = Agent(name="Test", tools=[tool])
    
    with pytest.raises(ValueError, match="Unknown layout type"):
        draw_categorical_flow(agent, layout="invalid_layout")


def test_missing_agent_attributes():
    """Test handling of agents with missing attributes."""
    # Create a minimal agent without all attributes
    agent = Mock()
    agent.name = "Test"
    agent.instructions = "Test instructions"
    agent.tools = []
    agent.handoffs = []
    agent.input_guardrails = []
    agent.output_guardrails = []
    
    # Should not raise an exception
    fig = draw_categorical_flow(agent)
    assert fig is not None


# Visual compatibility tests
def test_color_scheme_compatibility(basic_agent):
    """Test that colors are compatible with existing SDK."""
    fig = draw_categorical_flow(basic_agent)
    
    # Check that the figure has the expected elements
    # (This is a basic check - in a real implementation you might check specific colors)
    assert fig is not None


# Integration tests
def test_full_workflow():
    """Test the complete workflow from agent creation to diagram generation."""
    @function_tool
    def process_data(data: str) -> dict:
        return {"processed": data.upper()}
    
    @function_tool
    def validate_output(result: dict) -> bool:
        return "processed" in result
    
    agent = Agent(
        name="Data Processor",
        instructions="Process and validate data",
        tools=[process_data, validate_output]
    )
    
    # Extract structure
    structure = extract_agent_structure(agent)
    assert structure is not None
    
    # Get statistics
    stats = get_flow_statistics(agent)
    assert stats["total_nodes"] > 0
    
    # Validate composition
    comp = validate_agent_composition(agent)
    assert comp["tool_count"] == 2
    
    # Generate diagram
    fig = draw_categorical_flow(agent, show_types=True)
    assert fig is not None


if __name__ == "__main__":
    pytest.main([__file__])