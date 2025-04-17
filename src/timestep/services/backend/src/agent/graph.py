"""Define a chatbot agent using smolagents.

This agent uses smolagents CodeAgent to handle chat messages.
"""

from typing import Any, Dict, List
import os
import json
import requests

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from smolagents import CodeAgent, HfApiModel, OpenAIServerModel, LiteLLMModel
from smolagents import DuckDuckGoSearchTool, tool

from agent.configuration import Configuration
from agent.state import State


@tool
def get_weather_forecast(location: str) -> str:
    """
    Get the current weather forecast for any location in the world.
    
    Args:
        location: The city or location name (e.g., "Tokyo", "New York", "Paris", "Oakland, California")
        
    Returns:
        A string with complete weather information including temperature and conditions
    """
    try:
        # Clean up the location string
        location = location.strip()
        
        # Using OpenMeteo API which is free and doesn't require API key
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
        geo_response = requests.get(geo_url)
        geo_response.raise_for_status()  # Raise an exception for bad status codes
        geo_data = geo_response.json()
        
        if not geo_data.get("results"):
            # Try searching with just the city name if the full location string fails
            city_name = location.split(",")[0].strip()
            if city_name != location:
                geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
                geo_response = requests.get(geo_url)
                geo_response.raise_for_status()
                geo_data = geo_response.json()
                
            if not geo_data.get("results"):
                return f"Could not find location: {location}"
            
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        found_location = geo_data["results"][0]["name"]
        
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m&temperature_unit=fahrenheit"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        if "current" not in weather_data:
            return f"Could not get weather data for {found_location}"
            
        current = weather_data["current"]
        temp = current["temperature_2m"]
        
        # Map WMO weather codes to descriptions
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog",
            51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
            56: "Light freezing drizzle", 57: "Dense freezing drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
            66: "Light freezing rain", 67: "Heavy freezing rain",
            71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
            77: "Snow grains",
            80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
            85: "Slight snow showers", 86: "Heavy snow showers",
            95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
        }
        
        weather_desc = weather_codes.get(current["weather_code"], "Unknown")
        wind = current["wind_speed_10m"]
        
        return f"The current weather in {found_location} is {weather_desc} with a temperature of {temp}°F and wind speed of {wind} mph."
    except requests.exceptions.RequestException as e:
        return f"Error getting weather data: {str(e)}"
    except Exception as e:
        return f"Unexpected error getting weather data: {str(e)}"


def get_tools(enabled_tools: List[str]):
    """Get the tools based on configuration."""
    # Always include the weather forecast tool at the start of the list
    tools = [get_weather_forecast]
    
    if "web_search" in enabled_tools:
        try:
            tools.append(DuckDuckGoSearchTool())
        except Exception as e:
            print(f"Error adding DuckDuckGoSearchTool: {str(e)}")
    
    # Add additional tools here as needed
    
    return tools


def get_model(model_provider: str, model_id: str, ollama_base_url: str = "http://host.docker.internal:11434"):
    """Get the model based on configuration."""
    try:
        if model_provider == "ollama":
            print(f"Using Ollama model: {model_id} via LiteLLM")
            # For Ollama via LiteLLM, the model_id format is 'ollama/modelname'
            ollama_model_id = f"ollama/{model_id}" if not model_id.startswith("ollama/") else model_id
            return LiteLLMModel(
                model_id=ollama_model_id,
                api_base=ollama_base_url
            )
        elif model_provider == "huggingface":
            token = os.environ.get("HUGGINGFACE_API_KEY")
            if not token:
                raise ValueError("HUGGINGFACE_API_KEY not found in environment variables")
            return HfApiModel(
                max_tokens=2096,
                temperature=0.5,
                model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
                custom_role_conversions=None,
                token=token
            )
        elif model_provider == "openai":
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            return OpenAIServerModel(model_id=model_id, api_key=api_key)
        elif model_provider == "litellm":
            api_key = os.environ.get("LITELLM_API_KEY", "")  # Empty string is fine for Ollama
            return LiteLLMModel(model_id=model_id, api_key=api_key)
        else:
            raise ValueError(f"Unsupported model provider: {model_provider}")
    except Exception as e:
        print(f"Error initializing model: {str(e)}")
        raise


async def process_message(state: State, config: RunnableConfig) -> Dict[str, Any]:
    """Process the user message and generate a response using smolagents."""
    configuration = Configuration.from_runnable_config(config)
    
    # Get the user message from state
    user_message = state.changeme
    
    try:
        # Initialize the smolagents model based on configuration
        model = get_model(
            configuration.model_provider, 
            configuration.model_id,
            configuration.ollama_base_url
        )
        
        # Get tools based on configuration
        tools = get_tools(configuration.enabled_tools)
        
        # Create the agent with additional_authorized_imports to allow logging, json, and requests
        agent = CodeAgent(
            additional_authorized_imports=["logging", "json", "requests"],
            add_base_tools=True,
            model=model, 
            tools=tools,
        )
        
        # Run the agent on the user message - use run instead of arun
        response = agent.run(user_message)
        
        # Save the agent execution logs (if any)
        agent_history = []
        
        # Try various ways to get step information from the agent
        if hasattr(agent, "memory") and agent.memory:
            print("Using agent.memory for step history")
            # Handle AgentMemory object - it's not directly iterable
            try:
                # Try to get steps from the memory as a list
                if hasattr(agent.memory, "to_list") and callable(agent.memory.to_list):
                    agent_history = agent.memory.to_list()
                elif hasattr(agent.memory, "steps") and agent.memory.steps:
                    agent_history = agent.memory.steps
                elif hasattr(agent.memory, "__dict__"):
                    # Convert memory dict to list if possible
                    agent_history = [agent.memory.__dict__]
                else:
                    # Last resort - try to convert to string and wrap in a dict
                    agent_history = [{"step_number": 1, "action": "Processing", "output": str(agent.memory)}]
            except Exception as e:
                print(f"Error extracting agent memory: {str(e)}")
                # Fallback to a simple history with the agent's response
                agent_history = [{"step_number": 1, "action": "Processing request", "output": "Step completed"}]
        elif hasattr(agent, "steps") and agent.steps:
            print("Using agent.steps for step history")
            agent_history = [
                {
                    "step_number": i + 1,
                    "action": f"Step {i + 1}",
                    "input": step.get("input", ""),
                    "output": step.get("output", "")
                }
                for i, step in enumerate(agent.steps)
            ]
        
        # Format the agent history to make it more readable
        formatted_history = []
        for i, step in enumerate(agent_history):
            step_num = i + 1
            
            # Create a default step info
            step_info = {
                "step_number": step_num,
                "action": f"Step {step_num}",
            }
            
            # Include useful info based on structure
            if isinstance(step, dict):
                # Extract action if available
                if "action" in step:
                    step_info["action"] = f"Step {step_num}: {step.get('action')}"
                
                # Extract most relevant info without including entire step content
                for key in ["input", "output", "error", "result"]:
                    if key in step and step[key]:
                        # Truncate to avoid overwhelming the frontend
                        value = str(step[key])
                        step_info[key] = value[:300] + "..." if len(value) > 300 else value
            elif isinstance(step, str):
                # Handle case where step might be a string
                step_info["output"] = step[:300] + "..." if len(step) > 300 else step
                        
            formatted_history.append(step_info)
        
        # Check for raw output logs from the LLM
        if hasattr(agent, "llm_stream_logs") and agent.llm_stream_logs:
            try:
                raw_log_step = {
                    "step_number": len(formatted_history) + 1,
                    "action": "Raw LLM output",
                    "output": str(agent.llm_stream_logs)[:1000]  # Limit to a reasonable size
                }
                formatted_history.append(raw_log_step)
            except Exception as e:
                print(f"Error adding LLM logs: {str(e)}")
                
        # If we have terminal output from the smolagents code execution
        if hasattr(agent, "terminal_output") and agent.terminal_output:
            try:
                terminal_step = {
                    "step_number": len(formatted_history) + 1,
                    "action": "Terminal output",
                    "output": str(agent.terminal_output)[:1000]  # Limit to a reasonable size
                }
                formatted_history.append(terminal_step)
            except Exception as e:
                print(f"Error adding terminal output: {str(e)}")
        
        # If we have a successful response but no formatted history, create a simple completed step
        if not formatted_history and response:
            formatted_history = [{
                "step_number": 1,
                "action": "Completed processing",
                "output": "Request completed successfully"
            }]
        
        return {
            "changeme": response,
            "agent_history": formatted_history
        }
    except Exception as e:
        error_message = f"Error processing message with smolagents: {str(e)}"
        print(error_message)
        
        # Create error step for the history to show in frontend
        error_steps = []
        
        # Try to capture any steps that were completed before the error
        if 'agent' in locals() and hasattr(agent, 'memory'):
            try:
                print("Trying to extract steps from agent memory after error")
                if hasattr(agent.memory, "steps") and agent.memory.steps:
                    error_steps = [
                        {
                            "step_number": i + 1,
                            "action": f"Step {i + 1}",
                            "output": str(step) if not isinstance(step, dict) else step.get("output", "No output")
                        }
                        for i, step in enumerate(agent.memory.steps)
                    ]
                elif hasattr(agent.memory, "__dict__"):
                    # Try to extract useful information from the memory dictionary
                    error_steps = []
                    for i, (key, value) in enumerate(agent.memory.__dict__.items()):
                        if key not in ["llm", "model", "tools", "toolbox"]:  # Skip non-step items
                            error_steps.append({
                                "step_number": i + 1,
                                "action": f"Step info: {key}",
                                "output": str(value)[:100]  # Limit length
                            })
            except Exception as mem_error:
                print(f"Error extracting memory after agent error: {str(mem_error)}")
        
        # Always include the error step
        final_error_step = {
            "step_number": len(error_steps) + 1,
            "action": "Error encountered",
            "error": str(e)
        }
        error_steps.append(final_error_step)
        
        # Add raw error logs if available
        if 'agent' in locals() and hasattr(agent, 'llm_stream_logs'):
            try:
                error_steps.append({
                    "step_number": len(error_steps) + 1,
                    "action": "LLM logs",
                    "output": str(agent.llm_stream_logs)[:200]  # Limit length
                })
            except:
                pass
        
        return {
            "changeme": f"I encountered an error: {error_message}. Please try again or contact support.",
            "agent_history": error_steps
        }


# Define a new graph
workflow = StateGraph(State, config_schema=Configuration)

# Add the node to the graph
workflow.add_node("process_message", process_message)

# Set the entrypoint
workflow.add_edge("__start__", "process_message")

# Compile the workflow into an executable graph
graph = workflow.compile()
graph.name = "SmolagentsChat"  # This defines the custom name in LangSmith
