"""
Handoff Flow Example for Categorical Flow Visualization.

This example demonstrates the visualization of agents with handoffs,
showing how information flows between different agents.
"""

from agents import Agent, function_tool
from categorical_viz import draw_categorical_flow, draw_categorical_flow_comparison


@function_tool
def get_user_info(user_id: str) -> dict:
    """Get user information from database."""
    return {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john@example.com",
        "preferences": ["math", "science"]
    }


@function_tool
def analyze_preferences(preferences: list) -> str:
    """Analyze user preferences and provide recommendations."""
    if "math" in preferences:
        return "Recommended: Advanced Calculus, Linear Algebra"
    elif "science" in preferences:
        return "Recommended: Physics, Chemistry"
    else:
        return "Recommended: General Education courses"


@function_tool
def generate_schedule(recommendations: str) -> str:
    """Generate a class schedule based on recommendations."""
    return f"Schedule generated: {recommendations}"


def create_triage_agent():
    """Create the main triage agent."""
    return Agent(
        name="Triage Agent",
        instructions="You are a triage agent that handles initial user requests and routes them to appropriate specialists.",
        tools=[get_user_info]
    )


def create_analysis_agent():
    """Create the analysis specialist agent."""
    return Agent(
        name="Analysis Specialist",
        instructions="You are an analysis specialist that processes user preferences and provides recommendations.",
        tools=[analyze_preferences]
    )


def create_scheduling_agent():
    """Create the scheduling specialist agent."""
    return Agent(
        name="Scheduling Specialist", 
        instructions="You are a scheduling specialist that creates class schedules based on recommendations.",
        tools=[generate_schedule]
    )


def create_handoff_agent():
    """Create an agent with handoffs to specialists."""
    triage_agent = create_triage_agent()
    analysis_agent = create_analysis_agent()
    scheduling_agent = create_scheduling_agent()
    
    # Create main agent with handoffs
    main_agent = Agent(
        name="Student Advisor",
        instructions="You are a student advisor that coordinates with specialists to help students.",
        tools=[get_user_info],
        handoffs=[analysis_agent, scheduling_agent]
    )
    
    return main_agent


def main():
    """Run the handoff flow example."""
    print("Creating handoff agent...")
    agent = create_handoff_agent()
    
    print("Generating categorical flow diagrams...")
    
    # Generate comparison diagram with different layouts
    fig = draw_categorical_flow_comparison(
        agent=agent,
        layouts=["linear", "hierarchical", "temporal"],
        show_types=True,
        figsize=(18, 6)
    )
    
    # Save the comparison diagram
    fig.savefig("handoff_flow_comparison.png", dpi=300, bbox_inches='tight')
    print("Comparison diagram saved as 'handoff_flow_comparison.png'")
    
    # Generate individual diagrams
    for layout in ["linear", "hierarchical", "temporal"]:
        fig = draw_categorical_flow(
            agent=agent,
            layout=layout,
            show_types=True,
            figsize=(12, 8)
        )
        
        # Save individual diagram
        fig.savefig(f"handoff_flow_{layout}.png", dpi=300, bbox_inches='tight')
        print(f"Diagram saved as 'handoff_flow_{layout}.png'")
    
    print("Example completed successfully!")


if __name__ == "__main__":
    main()