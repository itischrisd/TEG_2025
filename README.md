# TEG 2025: GenAI Course Materials

An educational repository for learning Generative AI concepts, from foundations to advanced implementations.

## 📚 Course Structure

### 1. Intro
Introduction to the course and fundamental concepts.

### 2. Models
Working with different LLM providers and understanding response structures:
- **OpenAI Integration**: API usage patterns and response analysis
- **Claude Integration**: Anthropic API and response object exploration
- **LangChain Models**: Multi-provider integration patterns

### 3. Retrieval Augmented Generation (RAG)
Complete RAG implementation guide from basics to advanced techniques:
- **Basic RAG**: Minimal implementations with chunking strategies
- **Vector Stores**: ChromaDB, FAISS, and in-memory storage comparison
- **Document Loading**: Multi-format processing (text, PDF, web)
- **Advanced Retrieval**: Hybrid search, reranking, query expansion
- **RAG Evaluation**: RAGAS framework for systematic assessment
- **GraphRAG**: Neo4j knowledge graph integration
- **TalentMatch Project**: Hands-on capstone implementation

### 4. Graphs
LangGraph-based workflow automation and parallel processing:
- **Simple Graphs**: Basic state management and node connections
- **Parallel Processing**: Concurrent execution with real-world APIs
- **Map-Reduce Patterns**: Dynamic parallelization with structured outputs

### 5. Tools and Agents
Multi-agent systems and advanced agent architectures:
- **Basic Agents**: Fundamental agent patterns and tool integration
- **Complex Agents**: Advanced reasoning and multi-step workflows
- **Multi-Agent Systems**: Collaborative agent communication

### 6. Model Context Protocol (MCP)
Collection of specialized MCP servers for tool integration:
- **Math Server**: Arithmetic operations and calculations
- **Weather Server**: US National Weather Service integration
- **Tavily Server**: Web search capabilities
- **ArXiv Server**: Academic paper search and retrieval
- **Wikipedia Server**: Knowledge base queries and content access

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher (3.11+ recommended)
- [uv](https://github.com/astral-sh/uv) for package management

### Installation

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone this repository:
```bash
git clone <repository-url>
cd TEG_2025
```

3. Install root dependencies:
```bash
uv sync
```

4. Set up API keys for each module you want to use:
```bash
# Create module-specific .env files as needed
cd "src/3. Retrieval Augmented Generation"
echo "OPENAI_API_KEY=your_openai_key_here" > .env

cd "../4. Graphs"
echo "OPENAI_API_KEY=your_openai_key_here" > .env
echo "TAVILY_API_KEY=your_tavily_key_here" >> .env
```

## 🔑 Required API Keys

Different modules require different API keys. Add these to module-specific `.env` files:

### Core API Keys
- `OPENAI_API_KEY`: Required for most modules (Models, RAG, Chains, Agents)
- `ANTHROPIC_API_KEY`: Required for Claude examples in Models module

### Optional API Keys
- `TAVILY_API_KEY`: Required for web search in Graphs and MCP modules
- `GOOGLE_API_KEY`: Optional for Gemini model examples

## 🏃 Running Examples

Follow the educational progression by starting with early modules:

### Models (Module 2)
```bash
cd "src/2. Models/2. LLMs"
uv run python "1. OpenAI - analyze the response object.py"
uv run python "2. Claude - analyze the response object.py"
```

### RAG Examples (Module 3)
```bash
cd "src/3. Retrieval Augmented Generation"
# Start with basics
uv run python "01_basic_rag/1. minimal_rag.py"
uv run python "02_vector_stores/2_chroma_basic.py"

# Advance to evaluation
uv run python "05_rag_evaluation/1. RAGAS_Naive_RAG.py"

# Try GraphRAG (requires Docker)
./06_GraphRAG/start_session.sh
uv run python "06_GraphRAG/1_generate_data.py"
./06_GraphRAG/end_session.sh
```

### Graphs Examples (Module 4)
```bash
cd "src/4. Graphs"
uv run python "1_Simple graph.py"
uv run python "2_parallel_processes.py"
uv run python "3_map_reduce.py"
```

### MCP Servers (Module 6)
```bash
cd "src/6. MCP"
# Try the progressive demos
uv run --with mcp>=1.2.0 --with httpx>=0.28.1 1_direct_demo.py
uv run --with mcp>=1.2.0 --with httpx>=0.28.1 2_simple_demo.py

# Run individual servers
python3 run_server.py math
python3 run_server.py weather
```

## 📖 Documentation

Each module contains detailed documentation and learning objectives:

### Module-Specific Documentation
- [RAG Complete Guide](src/3.%20Retrieval%20Augmented%20Generation/README.md) - Comprehensive RAG learning path
- [Graphs Workflows](src/4.%20Graphs/README.md) - LangGraph educational examples
- [MCP Servers Collection](src/6.%20MCP/README.md) - Model Context Protocol servers
- [Tools and Agents](src/5.%20Tools%20and%20Agents/) - Multi-agent system architectures

### Learning Path
1. **Start with Module 1**: Course orientation and AI fundamentals
2. **Module 2**: LLM API integration patterns
3. **Module 3**: RAG from basics to GraphRAG (most comprehensive)
4. **Module 4**: Workflow automation with LangGraph
5. **Module 5**: Advanced agent architectures
6. **Module 6**: Protocol-based tool integration

## 🛠️ Development

### Module Development
```bash
# Work within specific modules
cd "src/[module_name]"
uv sync                    # Install module dependencies
uv add package_name        # Add new dependencies
uv run python script.py    # Run module scripts
```

### Project Structure
- Each module is self-contained with its own `pyproject.toml`
- Progressive complexity within each module (numbered scripts)
- Comprehensive README files for each major module

## 📝 License

This project is for educational purposes.