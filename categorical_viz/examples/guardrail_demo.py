"""
Guardrail Demo Example for Categorical Flow Visualization.

This example demonstrates the visualization of agents with input and output
guardrails, showing how safety checks and validation flows work.
"""

from agents import Agent, function_tool
from categorical_viz import draw_categorical_flow, validate_agent_composition, get_flow_statistics


@function_tool
def safety_check(input_text: str) -> str:
    """Check if input contains safe content."""
    unsafe_words = ["dangerous", "harmful", "unsafe"]
    for word in unsafe_words:
        if word.lower() in input_text.lower():
            return "UNSAFE: Input contains potentially harmful content"
    return "SAFE: Input passed safety check"


@function_tool
def quality_check(output_text: str) -> str:
    """Check if output meets quality standards."""
    if len(output_text) < 10:
        return "LOW_QUALITY: Output too short"
    elif len(output_text) > 1000:
        return "LOW_QUALITY: Output too long"
    else:
        return "HIGH_QUALITY: Output meets standards"


@function_tool
def process_text(text: str) -> str:
    """Process the input text and generate a response."""
    return f"Processed: {text} - This is a sample response that demonstrates text processing capabilities."


@function_tool
def format_response(response: str) -> str:
    """Format the response for better presentation."""
    return f"📝 {response} ✨"


def create_guardrail_agent():
    """Create an agent with input and output guardrails."""
    return Agent(
        name="Protected Text Processor",
        instructions="You are a text processing agent that safely processes user input and ensures high-quality output.",
        tools=[process_text, format_response],
        input_guardrails=[safety_check],
        output_guardrails=[quality_check]
    )


def create_complex_guardrail_agent():
    """Create a more complex agent with multiple guardrails."""
    
    @function_tool
    def content_filter(text: str) -> str:
        """Filter inappropriate content."""
        inappropriate_words = ["spam", "inappropriate", "blocked"]
        for word in inappropriate_words:
            if word.lower() in text.lower():
                return "BLOCKED: Content contains inappropriate material"
        return "APPROVED: Content is appropriate"
    
    @function_tool
    def length_validator(text: str) -> str:
        """Validate text length."""
        if len(text) < 5:
            return "TOO_SHORT: Text must be at least 5 characters"
        elif len(text) > 500:
            return "TOO_LONG: Text must be under 500 characters"
        return "VALID_LENGTH: Text length is appropriate"
    
    @function_tool
    def sentiment_analyzer(text: str) -> str:
        """Analyze sentiment of the text."""
        positive_words = ["good", "great", "excellent", "amazing"]
        negative_words = ["bad", "terrible", "awful", "horrible"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "POSITIVE: Text has positive sentiment"
        elif negative_count > positive_count:
            return "NEGATIVE: Text has negative sentiment"
        else:
            return "NEUTRAL: Text has neutral sentiment"
    
    return Agent(
        name="Advanced Text Processor",
        instructions="You are an advanced text processing agent with comprehensive safety and quality checks.",
        tools=[process_text, format_response],
        input_guardrails=[safety_check, content_filter, length_validator],
        output_guardrails=[quality_check, sentiment_analyzer]
    )


def main():
    """Run the guardrail demo example."""
    print("Creating guardrail agents...")
    
    # Create simple guardrail agent
    simple_agent = create_guardrail_agent()
    
    # Create complex guardrail agent
    complex_agent = create_complex_guardrail_agent()
    
    print("Generating categorical flow diagrams...")
    
    # Generate diagrams for simple agent
    print("\n--- Simple Guardrail Agent ---")
    fig = draw_categorical_flow(
        agent=simple_agent,
        layout="hierarchical",
        show_types=True,
        figsize=(12, 8)
    )
    fig.savefig("simple_guardrail_flow.png", dpi=300, bbox_inches='tight')
    print("Simple guardrail diagram saved as 'simple_guardrail_flow.png'")
    
    # Generate diagrams for complex agent
    print("\n--- Complex Guardrail Agent ---")
    fig = draw_categorical_flow(
        agent=complex_agent,
        layout="temporal",
        show_types=True,
        figsize=(14, 10)
    )
    fig.savefig("complex_guardrail_flow.png", dpi=300, bbox_inches='tight')
    print("Complex guardrail diagram saved as 'complex_guardrail_flow.png'")
    
    # Show statistics
    print("\n--- Flow Statistics ---")
    simple_stats = get_flow_statistics(simple_agent)
    complex_stats = get_flow_statistics(complex_agent)
    
    print(f"Simple Agent:")
    print(f"  Total nodes: {simple_stats['total_nodes']}")
    print(f"  Total edges: {simple_stats['total_edges']}")
    print(f"  Node types: {simple_stats['node_type_counts']}")
    print(f"  Flow types: {simple_stats['flow_type_counts']}")
    
    print(f"\nComplex Agent:")
    print(f"  Total nodes: {complex_stats['total_nodes']}")
    print(f"  Total edges: {complex_stats['total_edges']}")
    print(f"  Node types: {complex_stats['node_type_counts']}")
    print(f"  Flow types: {complex_stats['flow_type_counts']}")
    
    # Show composition validation
    print("\n--- Composition Validation ---")
    simple_comp = validate_agent_composition(simple_agent)
    complex_comp = validate_agent_composition(complex_agent)
    
    print(f"Simple Agent:")
    print(f"  Tool count: {simple_comp['tool_count']}")
    print(f"  Valid compositions: {simple_comp['valid_compositions']}/{simple_comp['total_pairs']}")
    
    print(f"\nComplex Agent:")
    print(f"  Tool count: {complex_comp['tool_count']}")
    print(f"  Valid compositions: {complex_comp['valid_compositions']}/{complex_comp['total_pairs']}")
    
    print("\nExample completed successfully!")


if __name__ == "__main__":
    main()