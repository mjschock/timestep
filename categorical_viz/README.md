# Categorical Flow Visualization for OpenAI Agents SDK

This module provides enhanced visualization capabilities that complement the existing OpenAI Agents SDK `draw_graph()` function by adding information flow arrows, type annotations, compositional structure, and temporal flow visualization.

## 🎯 Features

- **Information Flow Arrows**: Show data movement through agents/tools
- **Type Annotations**: Display type information on connections for interface validation
- **Compositional Structure**: Use category theory principles to show tool composition
- **Temporal Flow**: Visualize session evolution and time-based layouts
- **Multiple Layouts**: Linear, hierarchical, and temporal layout options
- **Performance Optimized**: Generate diagrams in <2 seconds for typical agents

## 🚀 Quick Start

```python
from agents import Agent, function_tool
from categorical_viz import draw_categorical_flow

@function_tool
def calculator(expression: str) -> str:
    return f"Result: {eval(expression)}"

agent = Agent(
    name="Math Tutor",
    instructions="Help with math problems",
    tools=[calculator]
)

# Generate categorical flow diagram
fig = draw_categorical_flow(agent, layout="hierarchical", show_types=True)
fig.show()
fig.savefig("math_tutor_flow.png")
```

## 📋 API Reference

### Main Function

#### `draw_categorical_flow(agent, layout="hierarchical", show_types=True, show_flow_direction=True, figsize=(12, 8), save_path=None)`

Create a categorical flow diagram for an OpenAI SDK Agent.

**Parameters:**
- `agent`: OpenAI SDK Agent object
- `layout`: Layout type ("linear", "hierarchical", "temporal")
- `show_types`: Whether to show type annotations on connections
- `show_flow_direction`: Whether to show flow direction arrows
- `figsize`: Figure size as (width, height)
- `save_path`: Optional path to save the diagram

**Returns:**
- `matplotlib.Figure`: The generated diagram

### Layout Types

#### Linear Layout
Left-to-right flow showing data progression: `input → agent → tools → output`

#### Hierarchical Layout
Tree structure showing agent-tool-handoff relationships using networkx spring layout

#### Temporal Layout
Time-based layout for session evolution showing temporal progression

### Convenience Functions

```python
# Layout-specific functions
draw_linear_flow(agent, **kwargs)
draw_hierarchical_flow(agent, **kwargs)
draw_temporal_flow(agent, **kwargs)

# Comparison diagrams
draw_categorical_flow_comparison(agent, layouts=["linear", "hierarchical", "temporal"])

# Analysis functions
validate_agent_composition(agent)  # Check tool composition
get_flow_statistics(agent)         # Get flow statistics
```

## 🎨 Visual Elements

### Node Types (Objects in Category)
- **Agents**: Yellow rectangles (matching current `draw_graph()`)
- **Tools**: Green ellipses (matching current `draw_graph()`)
- **Guardrails**: Red diamonds with sharp corners
- **Sessions**: Purple rectangles for input/output

### Edge Types (Morphisms in Category)
- **Input/Output**: Blue/red solid arrows showing data flow
- **Tool Calls**: Green solid arrows for tool invocation
- **Tool Results**: Green dashed arrows for tool responses
- **Handoffs**: Orange dashed arrows for agent handoffs
- **Guardrails**: Red dotted arrows for safety checks
- **Sessions**: Purple dotted arrows for session management

### Type Annotations
- Display input/output types on connections
- Show composition validation
- Highlight type mismatches

## 📊 Examples

### Basic Agent
```python
from categorical_viz.examples.basic_agent import main
main()
```

### Handoff Flow
```python
from categorical_viz.examples.handoff_flow import main
main()
```

### Guardrail Demo
```python
from categorical_viz.examples.guardrail_demo import main
main()
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python -m pytest categorical_viz/test_categorical_viz.py -v
```

### Test Categories
- **Basic Functionality**: Simple agent visualization
- **Handoff Testing**: Multi-agent workflows
- **Guardrail Testing**: Safety and validation flows
- **Type Annotations**: Type extraction and display
- **Performance**: <2 second generation target
- **Error Handling**: Invalid inputs and edge cases

## 🏗️ Architecture

### Core Modules

#### `types.py`
- Data structures for nodes, edges, and type information
- Color schemes and flow styles
- Layout position definitions

#### `extractor.py`
- Agent structure extraction from SDK objects
- Type information parsing from function signatures
- Composition validation utilities

#### `layouts.py`
- Layout algorithms (linear, hierarchical, temporal)
- Position calculation and optimization
- Networkx integration for complex layouts

#### `visualizer.py`
- Matplotlib rendering engine
- Node and edge drawing functions
- Legend and annotation utilities

#### `core.py`
- Main `draw_categorical_flow()` function
- Workflow orchestration
- Performance monitoring

### Data Flow

1. **Extraction**: Parse Agent object to extract structure
2. **Layout**: Calculate node positions based on layout type
3. **Visualization**: Render diagram with matplotlib
4. **Output**: Return figure or save to file

## 🔧 Dependencies

### Required
- `matplotlib`: Visualization engine
- `networkx`: Graph layout algorithms
- `typing_extensions`: Type hints support

### Optional
- `pytest`: Testing framework
- `numpy`: Numerical operations (for matplotlib)

## 📈 Performance

### Targets
- **Generation Time**: <2 seconds for agents with <20 tools
- **Memory Usage**: <100MB for typical agents
- **Output Quality**: High-resolution figures suitable for documentation

### Optimization
- Efficient structure extraction
- Cached layout calculations
- Optimized matplotlib rendering

## 🎯 Success Criteria

### Must Have ✅
- [x] Function works with any existing SDK Agent without modification
- [x] Generates clear, readable flow diagrams
- [x] Shows information flow direction with arrows
- [x] Displays type annotations on connections
- [x] Supports all three layout modes
- [x] Performance: <2 seconds for agents with <20 tools

### Should Have ✅
- [x] Visual compatibility with existing `draw_graph()` color scheme
- [x] High-quality output suitable for documentation
- [x] Error handling for complex agent structures
- [x] Composition validation highlighting

### Could Have 🔮
- [ ] Interactive features (zoom, pan, hover tooltips)
- [ ] Export to multiple formats (SVG, PDF, PNG)
- [ ] Animation showing flow over time
- [ ] Integration with performance metrics

## 🚀 Future Enhancements

### Planned Features
- **Interactive Exploration**: Click to expand tool details
- **Temporal Visualization**: Animate conversation flows
- **Export Integrations**: Direct export to documentation systems
- **Composition Analysis**: Automatic detection of optimization opportunities

### Performance Metrics
- **Execution Times**: Show tool execution durations
- **Success Rates**: Display tool success/failure rates
- **Resource Usage**: Monitor memory and CPU usage

## 📝 License

This module is part of the OpenAI Agents SDK and follows the same licensing terms.

## 🤝 Contributing

1. Follow the existing code style and patterns
2. Add comprehensive tests for new features
3. Update documentation for API changes
4. Ensure performance targets are met

## 📞 Support

For issues and questions:
- Check the test suite for usage examples
- Review the API documentation
- Run performance tests to validate targets