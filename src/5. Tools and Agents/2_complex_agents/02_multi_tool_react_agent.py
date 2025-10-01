"""
Multi-Tool ReAct Agent Implementation
====================================

This script demonstrates building sophisticated ReAct agents with external API integration.
It shows the progression from simple tool composition to production-ready agents that
can access real-world data sources.

Learning Progression:
1. Basic multi-tool agent with mathematical operations
2. External API integration (weather, search, knowledge bases)
3. Error handling and API reliability patterns
4. Advanced ReAct reasoning with complex tool combinations

Key concepts:
- External API integration with proper error handling
- Tool composition across different domains
- Production-ready agent patterns
- Async/await patterns for API calls
- Real-world data integration
"""

from dotenv import load_dotenv
import json
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool

# Load environment variables
load_dotenv(override=True)

# ================================
# BASIC MATHEMATICAL TOOLS
# ================================

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers together.

    Args:
        a: First number to multiply
        b: Second number to multiply

    Returns:
        int: The product of a and b
    """
    print(f"🔢 Computing: {a} × {b}")
    return a * b

@tool
def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number to add
        b: Second number to add

    Returns:
        int: The sum of a and b
    """
    print(f"➕ Computing: {a} + {b}")
    return a + b

@tool
def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second number.

    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)

    Returns:
        float: The result of a divided by b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    print(f"➗ Computing: {a} ÷ {b}")
    return a / b

@tool
def calculate_percentage(part: float, whole: float) -> float:
    """
    Calculate what percentage 'part' is of 'whole'.

    Args:
        part: The part value
        whole: The whole value

    Returns:
        float: The percentage (0-100)
    """
    if whole == 0:
        raise ValueError("Cannot calculate percentage with whole = 0")

    percentage = (part / whole) * 100
    print(f"📊 Computing: {part} is {percentage:.2f}% of {whole}")
    return percentage

# ================================
# EXTERNAL API TOOLS
# ================================

@tool
def get_current_weather(location: str, unit: str = "celsius") -> str:
    """
    Get the current weather information for a given location.

    Args:
        location: The city and state/country, e.g. "San Francisco, CA" or "London, UK"
        unit: Temperature unit, either "celsius" or "fahrenheit"

    Returns:
        str: JSON string with weather information
    """
    print(f"🌤️  Fetching weather for: {location}")

    # Simulated weather data for educational purposes
    # In production, this would call a real weather API
    weather_data = {
        "location": location,
        "temperature": 22 if unit == "celsius" else 72,
        "unit": unit,
        "condition": "partly cloudy",
        "humidity": 65,
        "wind_speed": 8,
        "description": f"Pleasant weather in {location} with partly cloudy skies"
    }

    return json.dumps(weather_data, indent=2)

@tool
def search_web(query: str, max_results: int = 3) -> str:
    """
    Search the web for information about a given query.

    Args:
        query: The search query
        max_results: Maximum number of results to return (default: 3)

    Returns:
        str: JSON string with search results
    """
    print(f"🔍 Searching web for: '{query}'")

    # Simulated search results for educational purposes
    # In production, this would call a real search API like Tavily
    search_results = {
        "query": query,
        "results": [
            {
                "title": f"Understanding {query}: A Comprehensive Guide",
                "url": f"https://example.com/{query.replace(' ', '-').lower()}",
                "snippet": f"Learn everything about {query} with this detailed guide covering key concepts and practical applications.",
                "relevance_score": 0.95
            },
            {
                "title": f"Latest News on {query}",
                "url": f"https://news.example.com/{query.replace(' ', '-').lower()}",
                "snippet": f"Recent developments and updates related to {query} from trusted news sources.",
                "relevance_score": 0.87
            },
            {
                "title": f"{query} - Best Practices and Tips",
                "url": f"https://tips.example.com/{query.replace(' ', '-').lower()}",
                "snippet": f"Expert advice and best practices for working with {query} effectively.",
                "relevance_score": 0.82
            }
        ][:max_results]
    }

    return json.dumps(search_results, indent=2)

@tool
def get_wikipedia_summary(topic: str, sentences: int = 3) -> str:
    """
    Get a summary of a topic from Wikipedia.

    Args:
        topic: The topic to search for on Wikipedia
        sentences: Number of sentences to include in summary (default: 3)

    Returns:
        str: Summary text from Wikipedia
    """
    print(f"📚 Fetching Wikipedia summary for: '{topic}'")

    # Simulated Wikipedia summary for educational purposes
    # In production, this would call the Wikipedia API
    summaries = {
        "artificial intelligence": "Artificial intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and act like humans. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving. AI research has been highly successful in developing effective techniques for solving a wide range of problems, from game playing to medical diagnosis.",
        "python programming": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming.",
        "machine learning": "Machine learning (ML) is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data, without being explicitly programmed. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so."
    }

    # Default summary if topic not found in our simulated data
    summary = summaries.get(topic.lower(),
        f"{topic} is a complex topic with multiple aspects and applications. "
        f"It involves various concepts and methodologies that are studied and applied across different fields. "
        f"For detailed information, please refer to comprehensive academic sources and recent research.")

    # Limit to requested number of sentences
    sentences_list = summary.split('. ')
    limited_summary = '. '.join(sentences_list[:sentences])
    if not limited_summary.endswith('.'):
        limited_summary += '.'

    return limited_summary

# ================================
# TEXT ANALYSIS TOOLS
# ================================

@tool
def analyze_text(text: str) -> str:
    """
    Analyze text and provide various statistics and insights.

    Args:
        text: The text to analyze

    Returns:
        str: JSON string with text analysis results
    """
    print(f"📝 Analyzing text: '{text[:50]}{'...' if len(text) > 50 else ''}'")

    # Perform text analysis
    word_count = len(text.split())
    char_count = len(text)
    char_count_no_spaces = len(text.replace(' ', ''))
    sentence_count = len([s for s in text.split('.') if s.strip()])

    # Calculate averages
    avg_word_length = char_count_no_spaces / word_count if word_count > 0 else 0
    avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0

    analysis = {
        "text_preview": text[:100] + ("..." if len(text) > 100 else ""),
        "statistics": {
            "word_count": word_count,
            "character_count": char_count,
            "character_count_no_spaces": char_count_no_spaces,
            "sentence_count": sentence_count,
            "average_word_length": round(avg_word_length, 2),
            "average_sentence_length": round(avg_sentence_length, 2)
        },
        "readability": {
            "complexity_level": "Simple" if avg_word_length < 5 else "Moderate" if avg_word_length < 7 else "Complex",
            "sentence_structure": "Short" if avg_sentence_length < 10 else "Medium" if avg_sentence_length < 20 else "Long"
        }
    }

    return json.dumps(analysis, indent=2)

# ================================
# AGENT CREATION AND CONFIGURATION
# ================================

def create_multi_tool_agent():
    """Create a sophisticated multi-tool ReAct agent with external API access."""

    # Initialize the language model
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Define all available tools
    tools = [
        # Mathematical tools
        multiply, add, divide, calculate_percentage,

        # External API tools
        get_current_weather, search_web, get_wikipedia_summary,

        # Text analysis tools
        analyze_text
    ]

    # Create comprehensive system prompt
    system_prompt = """You are a sophisticated AI assistant with access to multiple tools for:

**Mathematical Operations:**
- Basic arithmetic (multiply, add, divide)
- Percentage calculations

**Information Retrieval:**
- Current weather information
- Web search capabilities
- Wikipedia knowledge access

**Text Analysis:**
- Comprehensive text statistics and readability analysis

**Working Principles:**
1. **Break down complex queries** into manageable steps
2. **Use appropriate tools** for each type of information or calculation
3. **Show your reasoning** clearly before and after tool usage
4. **Combine results** from multiple tools when needed
5. **Provide context** and explain the significance of results

**Response Style:**
- Be thorough but concise
- Explain your tool selection rationale
- Present results in a clear, structured format
- Offer follow-up suggestions when appropriate"""

    # Create the ReAct agent with checkpointing for conversation persistence
    agent = create_react_agent(
        llm,
        tools=tools,
        prompt=system_prompt,
        checkpointer=MemorySaver()
    )

    return agent

# ================================
# DEMONSTRATION EXAMPLES
# ================================

def run_basic_multi_tool_example():
    """Demonstrate basic multi-tool usage with mathematical operations."""
    print("=== EXAMPLE 1: Basic Multi-Tool Operations ===")

    agent = create_multi_tool_agent()
    session_config = {'configurable': {'thread_id': 'multi_tool_session_1'}}

    query = "Calculate 25% of 240, then divide that result by 3"
    print(f"Query: {query}")

    response = agent.invoke({'messages': [('user', query)]}, session_config)
    print(f"Response: {response['messages'][-1].content}")
    print("-" * 50)

def run_external_api_example():
    """Demonstrate external API tool integration."""
    print("=== EXAMPLE 2: External API Integration ===")

    agent = create_multi_tool_agent()
    session_config = {'configurable': {'thread_id': 'multi_tool_session_2'}}

    query = "What's the weather in Tokyo, and can you search for recent news about Japanese technology?"
    print(f"Query: {query}")

    response = agent.invoke({'messages': [('user', query)]}, session_config)
    print(f"Response: {response['messages'][-1].content}")
    print("-" * 50)

def run_complex_reasoning_example():
    """Demonstrate complex multi-step reasoning across different tool types."""
    print("=== EXAMPLE 3: Complex Multi-Tool Reasoning ===")

    agent = create_multi_tool_agent()
    session_config = {'configurable': {'thread_id': 'multi_tool_session_3'}}

    query = """I have a research project about artificial intelligence. Can you:
1. Get me a Wikipedia summary about AI
2. Analyze the text you retrieved (word count, readability, etc.)
3. Calculate what percentage of the summary consists of technical terms (assume 15 technical terms)
4. Search for recent developments in AI to complement the summary"""

    print(f"Complex Query: {query}")

    response = agent.invoke({'messages': [('user', query)]}, session_config)
    print(f"Response: {response['messages'][-1].content}")
    print("-" * 50)

def run_mixed_domain_example():
    """Demonstrate mixing different tool domains in a single query."""
    print("=== EXAMPLE 4: Mixed Domain Analysis ===")

    agent = create_multi_tool_agent()
    session_config = {'configurable': {'thread_id': 'multi_tool_session_4'}}

    query = """Help me plan a presentation. The text is: 'Machine learning transforms industries through data-driven insights and automated decision-making processes.'

Please:
1. Analyze this text for presentation planning
2. If the character count is over 100, calculate what percentage it exceeds 100 by
3. Get weather info for San Francisco (where I'm presenting)
4. Find additional information about machine learning applications"""

    print(f"Mixed Domain Query: {query}")

    response = agent.invoke({'messages': [('user', query)]}, session_config)
    print(f"Response: {response['messages'][-1].content}")
    print("-" * 50)

def run_conversation_context_example():
    """Demonstrate conversation context and follow-up interactions."""
    print("=== EXAMPLE 5: Conversation Context ===")

    agent = create_multi_tool_agent()
    session_config = {'configurable': {'thread_id': 'multi_tool_session_5'}}

    # First interaction
    query1 = "Calculate 15% of 300 and tell me about Python programming"
    print(f"First Query: {query1}")

    response1 = agent.invoke({'messages': [('user', query1)]}, session_config)
    print(f"First Response: {response1['messages'][-1].content}")

    # Follow-up interaction using context
    query2 = "Can you analyze the Python description you just provided and compare its word count to the percentage result from the calculation?"
    print(f"\nFollow-up Query: {query2}")

    response2 = agent.invoke({'messages': [('user', query2)]}, session_config)
    print(f"Follow-up Response: {response2['messages'][-1].content}")
    print("-" * 50)

def analyze_agent_capabilities():
    """Analyze the capabilities and patterns of the multi-tool agent."""
    print("=== AGENT CAPABILITIES ANALYSIS ===")

    print("🔧 Available Tool Categories:")
    print("1. Mathematical Operations: multiply, add, divide, calculate_percentage")
    print("2. External APIs: weather, web search, Wikipedia")
    print("3. Text Analysis: comprehensive text statistics and readability")

    print("\n🧠 Agent Intelligence Patterns:")
    print("• Multi-step reasoning across tool domains")
    print("• Contextual tool selection based on query analysis")
    print("• Result combination and cross-referencing")
    print("• Conversation memory and context retention")

    print("\n📊 Production Considerations:")
    print("• Error handling for API failures and edge cases")
    print("• Rate limiting for external API calls")
    print("• Caching strategies for repeated information requests")
    print("• Security considerations for user input validation")

    print("\n🎯 Educational Value:")
    print("• Demonstrates real-world agent capabilities")
    print("• Shows progression from simple to complex tool usage")
    print("• Illustrates ReAct reasoning patterns")
    print("• Provides foundation for custom agent development")

if __name__ == "__main__":
    print("Multi-Tool ReAct Agent Demonstration")
    print("===================================")

    # Run all demonstration examples
    run_basic_multi_tool_example()
    run_external_api_example()
    run_complex_reasoning_example()
    run_mixed_domain_example()
    run_conversation_context_example()
    analyze_agent_capabilities()

    print("\n✅ All multi-tool examples completed!")
    print("💡 Key Takeaway: ReAct agents can seamlessly combine tools from")
    print("   different domains to solve complex, multi-faceted problems.")