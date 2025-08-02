#!/usr/bin/env python3
"""
Demo script for Categorical Flow Visualization.

This script demonstrates the key features of the categorical visualization
system with various agent configurations.
"""

import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import Agent, function_tool
from categorical_viz import (
    draw_categorical_flow,
    draw_categorical_flow_comparison,
    validate_agent_composition,
    get_flow_statistics
)


def create_demo_agents():
    """Create various demo agents for visualization."""
    
    # Basic agent with single tool
    @function_tool
    def calculator(expression: str) -> str:
        """Calculate mathematical expressions."""
        try:
            result = eval(expression)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    basic_agent = Agent(
        name="Math Tutor",
        instructions="You are a helpful math tutor. Use the calculator tool to solve mathematical expressions.",
        tools=[calculator]
    )
    
    # Agent with multiple tools
    @function_tool
    def text_processor(text: str) -> str:
        """Process and clean text."""
        return text.strip().lower()
    
    @function_tool
    def word_counter(text: str) -> int:
        """Count words in text."""
        return len(text.split())
    
    @function_tool
    def sentiment_analyzer(text: str) -> str:
        """Analyze sentiment of text."""
        positive_words = ["good", "great", "excellent", "amazing"]
        negative_words = ["bad", "terrible", "awful", "horrible"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "POSITIVE"
        elif negative_count > positive_count:
            return "NEGATIVE"
        else:
            return "NEUTRAL"
    
    multi_tool_agent = Agent(
        name="Text Analyzer",
        instructions="You are a text analysis agent that processes and analyzes text content.",
        tools=[text_processor, word_counter, sentiment_analyzer]
    )
    
    # Agent with handoffs
    specialist1 = Agent(
        name="Data Specialist",
        instructions="You are a data processing specialist.",
        tools=[text_processor, word_counter]
    )
    
    specialist2 = Agent(
        name="Analysis Specialist", 
        instructions="You are an analysis specialist.",
        tools=[sentiment_analyzer]
    )
    
    handoff_agent = Agent(
        name="Coordinator",
        instructions="You are a coordinator that routes tasks to specialists.",
        tools=[text_processor],
        handoffs=[specialist1, specialist2]
    )
    
    # Agent with guardrails
    @function_tool
    def safety_check(text: str) -> str:
        """Check if text is safe."""
        unsafe_words = ["dangerous", "harmful", "unsafe"]
        for word in unsafe_words:
            if word.lower() in text.lower():
                return "UNSAFE"
        return "SAFE"
    
    @function_tool
    def quality_check(output: str) -> str:
        """Check output quality."""
        if len(output) < 10:
            return "LOW_QUALITY"
        return "HIGH_QUALITY"
    
    guardrail_agent = Agent(
        name="Protected Processor",
        instructions="You are a protected text processor with safety and quality checks.",
        tools=[text_processor, sentiment_analyzer],
        input_guardrails=[safety_check],
        output_guardrails=[quality_check]
    )
    
    return {
        "basic": basic_agent,
        "multi_tool": multi_tool_agent,
        "handoff": handoff_agent,
        "guardrail": guardrail_agent
    }


def run_demo():
    """Run the categorical visualization demo."""
    print("🎯 Categorical Flow Visualization Demo")
    print("=" * 50)
    
    # Create demo agents
    agents = create_demo_agents()
    
    for agent_name, agent in agents.items():
        print(f"\n📊 Demo: {agent_name.upper()} AGENT")
        print("-" * 30)
        
        # Get statistics
        stats = get_flow_statistics(agent)
        print(f"Nodes: {stats['total_nodes']}, Edges: {stats['total_edges']}")
        print(f"Node types: {stats['node_type_counts']}")
        print(f"Flow types: {stats['flow_type_counts']}")
        
        # Validate composition
        comp = validate_agent_composition(agent)
        print(f"Tools: {comp['tool_count']}, Valid compositions: {comp['valid_compositions']}/{comp['total_pairs']}")
        
        # Generate diagrams for different layouts
        layouts = ["linear", "hierarchical", "temporal"]
        
        for layout in layouts:
            print(f"  Generating {layout} layout...")
            
            try:
                fig = draw_categorical_flow(
                    agent=agent,
                    layout=layout,
                    show_types=True,
                    figsize=(10, 6)
                )
                
                # Save diagram
                filename = f"demo_{agent_name}_{layout}.png"
                fig.savefig(filename, dpi=300, bbox_inches='tight')
                print(f"    ✅ Saved: {filename}")
                
                # Close figure to free memory
                plt.close(fig)
                
            except Exception as e:
                print(f"    ❌ Error generating {layout} layout: {e}")
    
    # Generate comparison diagram
    print(f"\n📊 COMPARISON DIAGRAM")
    print("-" * 30)
    
    try:
        # Use the multi-tool agent for comparison
        fig = draw_categorical_flow_comparison(
            agent=agents["multi_tool"],
            layouts=layouts,
            show_types=True,
            figsize=(18, 6)
        )
        
        filename = "demo_comparison.png"
        fig.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✅ Saved comparison diagram: {filename}")
        
        plt.close(fig)
        
    except Exception as e:
        print(f"❌ Error generating comparison diagram: {e}")
    
    print(f"\n🎉 Demo completed! Check the generated PNG files.")
    print("Files generated:")
    for agent_name in agents.keys():
        for layout in layouts:
            print(f"  - demo_{agent_name}_{layout}.png")
    print("  - demo_comparison.png")


if __name__ == "__main__":
    run_demo()