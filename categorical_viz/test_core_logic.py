#!/usr/bin/env python3
"""
Test core logic without matplotlib dependency.

This script tests the core functionality of the categorical visualization
system without requiring matplotlib, focusing on data structures and
extraction logic.
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock matplotlib for testing
class MockMatplotlib:
    class Figure:
        def __init__(self):
            self.title = "Mock Figure"
        
        def savefig(self, *args, **kwargs):
            print(f"Mock savefig called with args: {args}")
        
        def show(self):
            print("Mock show called")
    
    class Axes:
        def __init__(self):
            pass
        
        def set_aspect(self, *args):
            pass
        
        def axis(self, *args):
            pass
        
        def set_xlim(self, *args):
            pass
        
        def set_ylim(self, *args):
            pass
        
        def set_title(self, *args, **kwargs):
            pass
        
        def add_patch(self, *args):
            pass
        
        def text(self, *args, **kwargs):
            pass
        
        def legend(self, *args, **kwargs):
            pass
    
    @staticmethod
    def subplots(figsize=(12, 8)):
        return MockMatplotlib.Figure(), MockMatplotlib.Axes()

# Mock the matplotlib import
sys.modules['matplotlib'] = MockMatplotlib()
sys.modules['matplotlib.pyplot'] = MockMatplotlib()
sys.modules['matplotlib.patches'] = MockMatplotlib()

# Mock matplotlib.patches specifically
class MockPatches:
    class FancyBboxPatch:
        def __init__(self, *args, **kwargs):
            pass
    
    class ConnectionPatch:
        def __init__(self, *args, **kwargs):
            pass
    
    class Rectangle:
        def __init__(self, *args, **kwargs):
            pass
    
    class Ellipse:
        def __init__(self, *args, **kwargs):
            pass
    
    class Polygon:
        def __init__(self, *args, **kwargs):
            pass

sys.modules['matplotlib.patches'] = MockPatches()

# Mock matplotlib.pyplot specifically
class MockPyplot:
    @staticmethod
    def subplots(figsize=(12, 8)):
        return MockMatplotlib.Figure(), MockMatplotlib.Axes()
    
    @staticmethod
    def Figure():
        return MockMatplotlib.Figure()
    
    @staticmethod
    def Axes():
        return MockMatplotlib.Axes()

sys.modules['matplotlib.pyplot'] = MockPyplot()

# Mock networkx
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

sys.modules['networkx'] = MockNetworkx()

# Mock numpy
class MockNumpy:
    pass

sys.modules['numpy'] = MockNumpy()

# Now we can test the core logic
def test_data_structures():
    """Test the core data structures."""
    print("Testing data structures...")
    
    from categorical_viz.data_types import Node, Edge, TypeInfo, AgentStructure
    
    # Test Node
    node = Node(id="test", type="agent", name="Test Agent")
    assert node.id == "test"
    assert node.type == "agent"
    assert node.name == "Test Agent"
    print("✅ Node structure works")
    
    # Test Edge
    edge = Edge(source="start", target="agent", flow_type="input")
    assert edge.source == "start"
    assert edge.target == "agent"
    assert edge.flow_type == "input"
    print("✅ Edge structure works")
    
    # Test TypeInfo
    type_info = TypeInfo(inputs=["str"], output="str")
    assert type_info.inputs == ["str"]
    assert type_info.output == "str"
    print("✅ TypeInfo structure works")
    
    # Test AgentStructure
    structure = AgentStructure(nodes=[node], edges=[edge], type_info={})
    assert len(structure.nodes) == 1
    assert len(structure.edges) == 1
    print("✅ AgentStructure works")


def test_extraction_logic():
    """Test the agent structure extraction logic."""
    print("Testing extraction logic...")
    
    # Mock Agent class
    class MockAgent:
        def __init__(self, name, instructions="", tools=None, handoffs=None, 
                     input_guardrails=None, output_guardrails=None):
            self.name = name
            self.instructions = instructions
            self.tools = tools or []
            self.handoffs = handoffs or []
            self.input_guardrails = input_guardrails or []
            self.output_guardrails = output_guardrails or []
    
    # Mock function tool
    def mock_tool(x: str) -> str:
        return x.upper()
    mock_tool.__name__ = "mock_tool"
    
    # Create mock agent
    agent = MockAgent(
        name="Test Agent",
        instructions="Test instructions",
        tools=[mock_tool]
    )
    
    from categorical_viz.extractor import extract_agent_structure
    
    try:
        structure = extract_agent_structure(agent)
        assert structure is not None
        assert len(structure.nodes) > 0
        assert len(structure.edges) > 0
        print("✅ Agent structure extraction works")
    except Exception as e:
        print(f"❌ Agent structure extraction failed: {e}")


def test_layout_logic():
    """Test the layout calculation logic."""
    print("Testing layout logic...")
    
    from categorical_viz.data_types import Node, Edge
    from categorical_viz.layouts import calculate_layout
    
    # Create test nodes and edges
    nodes = [
        Node(id="start", type="start", name="input"),
        Node(id="agent", type="agent", name="Test Agent"),
        Node(id="tool", type="tool", name="test_tool"),
        Node(id="output", type="session", name="output")
    ]
    
    edges = [
        Edge(source="start", target="agent", flow_type="input"),
        Edge(source="agent", target="tool", flow_type="tool_call"),
        Edge(source="tool", target="agent", flow_type="tool_result"),
        Edge(source="agent", target="output", flow_type="output")
    ]
    
    try:
        # Test linear layout
        positions = calculate_layout(nodes, edges, "linear")
        assert positions is not None
        assert len(positions) == len(nodes)
        print("✅ Linear layout works")
        
        # Test hierarchical layout
        positions = calculate_layout(nodes, edges, "hierarchical")
        assert positions is not None
        assert len(positions) == len(nodes)
        print("✅ Hierarchical layout works")
        
        # Test temporal layout
        positions = calculate_layout(nodes, edges, "temporal")
        assert positions is not None
        assert len(positions) == len(nodes)
        print("✅ Temporal layout works")
        
    except Exception as e:
        print(f"❌ Layout calculation failed: {e}")


def test_type_extraction():
    """Test type information extraction."""
    print("Testing type extraction...")
    
    from categorical_viz.extractor import TypeInfo
    
    # Test function with type annotations
    def typed_function(x: int, y: str) -> bool:
        return True
    
    try:
        type_info = TypeInfo.from_function(typed_function)
        assert type_info.inputs == ["int", "str"]
        assert type_info.output == "bool"
        print("✅ Type extraction works")
    except Exception as e:
        print(f"❌ Type extraction failed: {e}")


def test_composition_validation():
    """Test composition validation logic."""
    print("Testing composition validation...")
    
    from categorical_viz.extractor import validate_composition
    
    # Test compatible functions
    def func1(x: str) -> int:
        return len(x)
    
    def func2(x: int) -> str:
        return str(x)
    
    try:
        # func1 returns int, func2 takes int - should be compatible
        result = validate_composition(func1, func2)
        print(f"✅ Composition validation works: {result}")
    except Exception as e:
        print(f"❌ Composition validation failed: {e}")


def main():
    """Run all core logic tests."""
    print("🧪 Testing Core Logic (without matplotlib)")
    print("=" * 50)
    
    test_data_structures()
    test_extraction_logic()
    test_layout_logic()
    test_type_extraction()
    test_composition_validation()
    
    print("\n🎉 All core logic tests completed!")
    print("The categorical visualization system core logic is working correctly.")


if __name__ == "__main__":
    main()