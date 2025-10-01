# MCP Servers Collection

A collection of Model Context Protocol (MCP) servers providing various tools for AI assistants and applications.

## Quick Start for Students

We provide three different demo approaches - start with the simplest:

### 1. **Start Simple: Direct Function Calls**
```bash
uv run 1_direct_demo.py
```
This calls the server functions directly (no MCP protocol). Perfect to understand **what** each tool does.

### 2. **Learn MCP Protocol: Fixed Demo**
```bash
uv run 2_simple_demo.py
```
This uses proper MCP client with initialization. Shows **how** to use MCP protocol correctly.

### 3. **Advanced MCP Usage**
```bash
uv run 3_mcp_client_demo.py
```
This demonstrates more detailed MCP client patterns with better error handling and explanations.

### 4. **Run Individual Servers**
```bash
python3 run_server.py math     # Math operations
python3 run_server.py weather  # US weather data
```

**Learning Path**: `direct_demo.py` → `simple_demo.py` → `mcp_client_demo.py` → Build your own!

## Demo Scripts Explained

### `direct_demo.py` - Functions Without MCP 🎯
- **Purpose**: Understand what each tool does
- **Approach**: Imports server modules directly, calls functions
- **Pros**: Simple, fast, no protocol complexity
- **Cons**: Not how MCP is actually used
- **Best for**: First-time learners, debugging tool logic

### `simple_demo.py` - MCP Protocol Made Simple 🔧
- **Purpose**: Learn proper MCP client usage
- **Approach**: Uses MCP ClientSession with initialization
- **Pros**: Shows correct MCP pattern, educational comments
- **Cons**: Creates new connection per tool call (inefficient)
- **Best for**: Understanding MCP protocol basics

### `mcp_client_demo.py` - Production-Ready MCP 🚀
- **Purpose**: Advanced MCP client patterns
- **Approach**: Efficient connections, better error handling
- **Pros**: Closer to real-world usage, demonstrates best practices
- **Cons**: More complex code structure
- **Best for**: Building actual MCP applications

## Overview

This repository contains five MCP servers, each providing specialized functionality:

- **math_server**: Mathematical operations and calculations
- **weather_server**: Weather data from US National Weather Service
- **tavily_server**: Web search capabilities via Tavily API
- **arxiv_server**: Academic paper search from ArXiv
- **wikipedia_server**: Wikipedia article search and retrieval

## Requirements

- Python 3.10 or higher
- `httpx` for HTTP requests
- `mcp[cli]` for MCP server functionality

## Quick Start

1. **Clone or download this repository**

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Set up environment variables** (optional, for specific servers):
   ```bash
   export TAVILY_API_KEY="your_tavily_api_key_here"
   ```

4. **Run servers with uv**:
   ```bash
   # Using the helper script (recommended)
   python3 run_server.py math
   python3 run_server.py weather
   
   # Or run directly with dependencies
   uv run --with mcp --with httpx math_server/math.py
   uv run --with mcp --with httpx weather_server/weather.py
   
   # Run example scripts
   uv run --with mcp --with httpx run_example.py
   uv run --with mcp --with httpx run_natural_language.py
   ```

## Server Details

### 🔢 Math Server

**Location**: `math_server/`

**Tools**:
- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract b from a
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide a by b (with zero-division protection)
- `power(a, b)`: Raise a to the power of b
- `sqrt(a)`: Calculate square root (with negative number protection)
- `factorial(n)`: Calculate factorial of non-negative integer

**Usage**:
```bash
uv run math_server/math.py
```

**Example**:
```python
# Via MCP call
{"tool": "add", "args": {"a": 5, "b": 3}}  # Returns: 8
{"tool": "power", "args": {"a": 2, "b": 10}}  # Returns: 1024
```

### 🌤️ Weather Server

**Location**: `weather_server/`

**Tools**:
- `get_alerts(state)`: Get weather alerts for US state (e.g., "CA", "NY")
- `get_forecast(latitude, longitude)`: Get 5-day forecast for coordinates
- `get_current_conditions(latitude, longitude)`: Get current weather conditions

**Data Source**: US National Weather Service API

**Usage**:
```bash
uv run weather_server/weather.py
```

**Example**:
```python
# Get forecast for San Francisco
{"tool": "get_forecast", "args": {"latitude": 37.7749, "longitude": -122.4194}}
```

### 🔍 Tavily Server

**Location**: `tavily_server/`

**Requirements**: `TAVILY_API_KEY` environment variable

**Tools**:
- `search(query, max_results=5)`: General web search
- `search_news(query, max_results=5)`: Search recent news articles

**Usage**:
```bash
export TAVILY_API_KEY="your_api_key"
uv run tavily_server/tavily.py
```

**Example**:
```python
{"tool": "search", "args": {"query": "latest AI developments", "max_results": 3}}
```

### 📚 ArXiv Server

**Location**: `arxiv_server/`

**Tools**:
- `search_papers(query, max_results=5)`: Search papers by keywords
- `search_by_author(author, max_results=5)`: Search papers by author name
- `search_by_category(category, max_results=5)`: Search papers by ArXiv category

**Common Categories**: `cs.AI`, `cs.LG`, `cs.CL`, `math.ST`, `physics.gen-ph`

**Usage**:
```bash
uv run arxiv_server/arxiv.py
```

**Example**:
```python
{"tool": "search_papers", "args": {"query": "transformer neural networks", "max_results": 3}}
{"tool": "search_by_category", "args": {"category": "cs.AI", "max_results": 5}}
```

### 📖 Wikipedia Server

**Location**: `wikipedia_server/`

**Tools**:
- `search_wikipedia(query, limit=5)`: Search Wikipedia articles
- `get_wikipedia_summary(title)`: Get article summary
- `get_wikipedia_content(title, section=None)`: Get full article or specific section
- `get_random_wikipedia()`: Get random article

**Usage**:
```bash
uv run wikipedia_server/wikipedia.py
```

**Example**:
```python
{"tool": "search_wikipedia", "args": {"query": "machine learning", "limit": 3}}
{"tool": "get_wikipedia_summary", "args": {"title": "Artificial intelligence"}}
```

## Running Individual Servers

Each server can be run independently using Python:

```bash
# Math operations
uv run math_server/math.py

# Weather data
uv run weather_server/weather.py

# Web search (requires API key)
TAVILY_API_KEY="your_key" uv run tavily_server/tavily.py

# Academic papers
uv run arxiv_server/arxiv.py

# Wikipedia
uv run wikipedia_server/wikipedia.py
```

## Integration with MCP Clients

These servers are designed to work with MCP-compatible clients like Claude Desktop, LangChain, or custom applications.

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "math": {
      "command": "uv",
      "args": ["run", "/path/to/math_server/math.py"],
      "env": {}
    },
    "weather": {
      "command": "uv", 
      "args": ["run", "/path/to/weather_server/weather.py"],
      "env": {}
    },
    "tavily": {
      "command": "uv",
      "args": ["run", "/path/to/tavily_server/tavily.py"],
      "env": {
        "TAVILY_API_KEY": "your_api_key_here"
      }
    },
    "arxiv": {
      "command": "uv",
      "args": ["run", "/path/to/arxiv_server/arxiv.py"],
      "env": {}
    },
    "wikipedia": {
      "command": "uv",
      "args": ["run", "/path/to/wikipedia_server/wikipedia.py"],
      "env": {}
    }
  }
}
```

## Example Workflows

### Research Workflow
1. Search Wikipedia for background information
2. Find recent papers on ArXiv
3. Search for latest news/developments via Tavily
4. Perform calculations related to findings

### Weather Planning
1. Get current conditions for multiple locations
2. Check weather alerts for travel areas
3. Get detailed forecasts for event planning

### Academic Research
1. Search ArXiv by category or author
2. Get Wikipedia summaries for unfamiliar concepts
3. Use math server for calculations in papers
4. Search web for recent developments

## Project Structure

```
MCP/
├── math_server/
│   ├── math.py
│   └── pyproject.toml
├── weather_server/
│   ├── weather.py
│   └── pyproject.toml
├── tavily_server/
│   ├── tavily.py
│   └── pyproject.toml
├── arxiv_server/
│   ├── arxiv.py
│   └── pyproject.toml
├── wikipedia_server/
│   ├── wikipedia.py
│   └── pyproject.toml
├── ref_agents/          # Original LangChain examples
├── ref_weather_server/  # Original reference implementation
├── run_example.py       # Demonstration script
└── README.md           # This file
```

## Error Handling

All servers include comprehensive error handling:

- **Network timeouts**: 30-second timeout for all HTTP requests
- **API errors**: Graceful handling of API failures
- **Input validation**: Type checking and bounds validation
- **Missing dependencies**: Clear error messages for missing requirements

## Development

### Adding New Tools

To add a new tool to any server:

1. Define the function with `@mcp.tool()` decorator
2. Add proper type hints and docstring
3. Include error handling
4. Test with the example script

### Creating New Servers

Follow the pattern established in existing servers:

1. Import `FastMCP` from `mcp.server.fastmcp`
2. Initialize with `mcp = FastMCP("server_name")`
3. Define tools with `@mcp.tool()` decorator
4. Run with `mcp.run(transport='stdio')`
5. Create corresponding `pyproject.toml`

## API Keys and Environment Variables

- **TAVILY_API_KEY**: Required for Tavily search functionality
  - Get from: https://tavily.com/
  - Used by: `tavily_server`

## Troubleshooting

### Common Issues

1. **"Module not found" errors**: Install dependencies with `pip install -e .` in each server directory

2. **Tavily authentication errors**: Ensure `TAVILY_API_KEY` is set correctly

3. **Weather server location errors**: Verify coordinates are for US locations (NWS API limitation)

4. **ArXiv search returns no results**: Try broader search terms or different categories

5. **Wikipedia disambiguation pages**: Use more specific article titles

### Debug Mode

Run servers with debug output:
```bash
uv run --verbose server_name/server.py
```

## References

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Quickstart Guide](https://modelcontextprotocol.io/quickstart)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)