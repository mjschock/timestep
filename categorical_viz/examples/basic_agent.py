"""
Basic Agent Example for Categorical Flow Visualization.

This example demonstrates the basic usage of draw_categorical_flow()
with a simple agent that has a single tool.
"""

from agents import Agent, function_tool
from categorical_viz import draw_categorical_flow


@function_tool
def calculator(expression: str) -> str:
    """Calculate the result of a mathematical expression."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


def create_basic_agent():
    """Create a basic agent with a calculator tool."""
    return Agent(
        name="Math Tutor",
        instructions="You are a helpful math tutor. Use the calculator tool to solve mathematical expressions.",
        tools=[calculator]
    )


def main():
    """Run the basic agent example."""
    print("Creating basic agent...")
    agent = create_basic_agent()
    
    print("Generating categorical flow diagram...")
    
    # Generate diagram with hierarchical layout
    fig = draw_categorical_flow(
        agent=agent,
        layout="hierarchical",
        show_types=True,
        figsize=(10, 6)
    )
    
    # Save the diagram
    fig.savefig("basic_agent_flow.png", dpi=300, bbox_inches='tight')
    print("Diagram saved as 'basic_agent_flow.png'")
    
    # Show the diagram
    fig.show()
    
    print("Example completed successfully!")


if __name__ == "__main__":
    main()