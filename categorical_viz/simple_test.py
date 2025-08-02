#!/usr/bin/env python3
"""
Simple test for core data structures.

This script tests the basic data structures without importing the full
categorical_viz module to avoid matplotlib dependencies.
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_data_types():
    """Test the data types module directly."""
    print("Testing data_types module...")
    
    # Import the data_types module directly
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from data_types import Node, Edge, TypeInfo, AgentStructure, COLORS, FLOW_STYLES
    
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
    
    # Test constants
    assert "agent" in COLORS
    assert "tool" in COLORS
    assert "input" in FLOW_STYLES
    assert "tool_call" in FLOW_STYLES
    print("✅ Constants defined correctly")


def test_extractor_logic():
    """Test the extractor logic directly."""
    print("Testing extractor logic...")
    
    # Import the extractor module directly
    from extractor import TypeInfo, validate_composition, extract_type_information
    
    # Test TypeInfo.from_function
    def test_function(x: int, y: str) -> bool:
        return True
    
    type_info = TypeInfo.from_function(test_function)
    assert type_info.inputs == ["int", "str"]
    assert type_info.output == "bool"
    print("✅ TypeInfo.from_function works")
    
    # Test extract_type_information
    type_dict = extract_type_information(test_function)
    assert type_dict["inputs"] == ["int", "str"]
    assert type_dict["output"] == "bool"
    print("✅ extract_type_information works")
    
    # Test validate_composition
    def func1(x: str) -> int:
        return len(x)
    
    def func2(x: int) -> str:
        return str(x)
    
    result = validate_composition(func1, func2)
    print(f"✅ validate_composition works: {result}")


def test_layout_logic():
    """Test the layout logic directly."""
    print("Testing layout logic...")
    
    # Import the layouts module directly
    from layouts import layout_linear, layout_hierarchical, layout_temporal
    
    # Create test data
    from data_types import Node, Edge
    
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
    
    # Test linear layout
    positions = layout_linear(nodes, edges)
    assert positions is not None
    assert len(positions) == len(nodes)
    print("✅ Linear layout works")
    
    # Test hierarchical layout
    positions = layout_hierarchical(nodes, edges)
    assert positions is not None
    assert len(positions) == len(nodes)
    print("✅ Hierarchical layout works")
    
    # Test temporal layout
    positions = layout_temporal(nodes, edges)
    assert positions is not None
    assert len(positions) == len(nodes)
    print("✅ Temporal layout works")


def main():
    """Run all tests."""
    print("🧪 Testing Core Data Structures and Logic")
    print("=" * 50)
    
    try:
        test_data_types()
        test_extractor_logic()
        test_layout_logic()
        
        print("\n🎉 All tests passed!")
        print("The categorical visualization system core logic is working correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()