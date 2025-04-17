"""FastAPI application for LangGraph backend with smolagents integration."""

from fastapi import FastAPI, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn
import json
from typing import Dict, Any, List
from fastapi.websockets import WebSocket
from agent.graph import graph, State
from agent.state import Message
import time

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/chat")
async def chat(message: Dict[str, Any]):
    """Process chat messages through LangGraph with smolagents."""
    try:
        # Extract the user message
        messages = message.get("messages", [])
        last_message = messages[-1] if messages else {}
        user_message = ""
        
        # Handle different message formats
        if isinstance(last_message.get("content"), str):
            user_message = last_message.get("content", "")
        elif isinstance(last_message.get("content"), list):
            # Handle array format with text objects
            content_parts = last_message.get("content", [])
            text_parts = []
            for part in content_parts:
                if isinstance(part, dict) and part.get("type") == "text":
                    text_parts.append(part.get("text", ""))
            user_message = " ".join(text_parts)
        
        print(f"Received message: {user_message}")
        
        # Convert messages to the format expected by the state
        history: List[Message] = []
        for msg in messages:
            if isinstance(msg.get("content"), str):
                history.append(Message(
                    role=msg.get("role", "user"),
                    content=msg.get("content", "")
                ))
        
        # Create initial state
        initial_state = State(changeme=user_message, messages=history)
        
        # Format the response as a stream
        async def generate():
            try:
                # Send initial processing message
                yield f'data: {json.dumps({"type": 1, "content": "Processing your request..."})}\n\n'
                
                # Process the message through the agent
                async for event in graph.astream(initial_state):
                    if event.get("agent_history"):
                        # Send step messages
                        for step in event.get("agent_history", []):
                            step_message = f"Step {step.get('step_number', '?')}"
                            if step.get("action"):
                                step_message = f"{step_message}: {step.get('action')}"
                            if step.get("output"):
                                step_message = f"{step_message} → {step.get('output')}"
                            if step.get("error"):
                                step_message = f"{step_message} (Error: {step.get('error')})"
                            yield f'data: {json.dumps({"type": 2, "content": step_message})}\n\n'
                    
                    # Send the final response
                    if event.get("changeme"):
                        yield f'data: {json.dumps({"type": 0, "content": event["changeme"]})}\n\n'
                        
            except Exception as e:
                # Send error message
                yield f'data: {json.dumps({"type": 3, "content": f"Error: {str(e)}"})}\n\n'
        
        return StreamingResponse(
            generate(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            }
        )
        
    except Exception as e:
        print(f"Error processing chat message: {str(e)}")
        return StreamingResponse(
            iter([f'data: {json.dumps({"type": 3, "content": f"Error: {str(e)}"})}\n\n']),
            media_type="text/event-stream"
        )

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for streaming chat responses."""
    await websocket.accept()
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Process with LangGraph
            user_message = message_data.get("message", "")
            history = message_data.get("history", [])
            
            print(f"WebSocket received: {user_message}")
            
            # Convert history to the format expected by the state
            message_history = []
            for msg in history:
                message_history.append(Message(
                    role=msg.get("role", "user"),
                    content=msg.get("content", "")
                ))
            
            initial_state = State(changeme=user_message, messages=message_history)
            
            # Send initial thinking status
            await websocket.send_text(json.dumps({
                "type": "status", 
                "status": "thinking",
                "message": "Starting to process your request..."
            }))
            
            # Keep track of steps for progress reporting
            step_counter = 0
            last_progress_time = 0
            
            try:
                # Stream the response
                async for event in graph.astream(initial_state):
                    current_time = time.time()
                    
                    # Send agent progress updates
                    if event.get("agent_history") and event.get("agent_history") != []:
                        agent_history = event.get("agent_history", [])
                        
                        # Find new steps (ones we haven't reported yet)
                        while step_counter < len(agent_history):
                            step = agent_history[step_counter]
                            step_counter += 1
                            
                            # Create a descriptive step message
                            step_message = f"Step {step_counter}"
                            if "action" in step:
                                step_message = f"{step_message}: {step['action']}"
                            
                            # Add input/output/error information if available
                            if "output" in step and step["output"]:
                                step_message = f"{step_message} → {step['output']}"
                            elif "error" in step and step["error"]:
                                step_message = f"{step_message} (Error: {step['error']})"
                            
                            # Send step info as progress update
                            await websocket.send_text(json.dumps({
                                "type": "progress", 
                                "step": step_counter,
                                "total_steps": len(agent_history),
                                "details": step,
                                "message": step_message
                            }))
                    
                    # Send intermediate status update if no new steps in a while 
                    # but we're still processing
                    elif current_time - last_progress_time > 3 and not event.get("changeme"):
                        last_progress_time = current_time
                        await websocket.send_text(json.dumps({
                            "type": "status",
                            "status": "processing",
                            "message": "Still working on your request..."
                        }))
                    
                    # Send response fragments
                    response = event.get("changeme", "")
                    if response:
                        await websocket.send_text(json.dumps({
                            "type": "message",
                            "response": response
                        }))
                
                # Signal completion
                await websocket.send_text(json.dumps({
                    "type": "done"
                }))
                
            except Exception as e:
                error_msg = f"Error processing request: {str(e)}"
                print(error_msg)
                await websocket.send_text(json.dumps({
                    "type": "error",
                    "error": error_msg
                }))
                
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error in websocket: {str(e)}")
        try:
            await websocket.send_text(json.dumps({
                "type": "error",
                "error": f"Websocket error: {str(e)}"
            }))
        except:
            print("Could not send error message to client")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 