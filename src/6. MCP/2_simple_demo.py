#!/usr/bin/env python3
"""
Simple MCP Demo Script - A beginner-friendly demonstration of MCP servers.

This script shows how to programmatically call MCP tools using proper MCP protocol.
Updated to use correct MCP client initialization.

Usage: python3 simple_demo.py
"""

import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def call_mcp_tool(server_path: str, tool_name: str, args: dict) -> str:
    """
    Call an MCP server tool using proper MCP protocol with initialization.

    This is the core function that shows the CORRECT way to communicate with MCP servers.
    """
    print(f"  📞 Calling {server_path} -> {tool_name}({args})")

    # Step 1: Create server parameters for the MCP connection
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "--with", "mcp>=1.2.0", "--with", "httpx>=0.28.1", server_path]
    )

    try:
        # Step 2: Create connection to server
        async with stdio_client(server_params) as (read_stream, write_stream):
            # Step 3: Create client session and initialize (CRITICAL!)
            async with ClientSession(read_stream, write_stream) as session:
                # Step 4: Initialize the MCP connection - this is what was missing!
                await session.initialize()

                # Step 5: Now we can safely call the tool
                result = await session.call_tool(tool_name, args)
                return result.content[0].text

    except Exception as e:
        return f"❌ Error: {e}"


async def demo_math_server():
    """Demonstrate the math server with simple calculations."""
    print("\n🔢 MATH SERVER DEMO")
    print("=" * 40)
    print("The math server provides basic mathematical operations.")

    # Simple addition
    result = await call_mcp_tool("math_server/math_server.py", "add", {"a": 5, "b": 3})
    print(f"  ➕ 5 + 3 = {result}")

    # Multiplication
    result = await call_mcp_tool("math_server/math_server.py", "multiply", {"a": 7, "b": 6})
    print(f"  ✖️  7 × 6 = {result}")

    # Power calculation
    result = await call_mcp_tool("math_server/math_server.py", "power", {"a": 2, "b": 8})
    print(f"  🔺 2^8 = {result}")

    # Square root
    result = await call_mcp_tool("math_server/math_server.py", "sqrt", {"a": 16})
    print(f"  √ √16 = {result}")


async def demo_weather_server():
    """Demonstrate the weather server with a US location."""
    print("\n🌤️  WEATHER SERVER DEMO")
    print("=" * 40)
    print("The weather server provides US weather data (no API key needed).")

    # Get forecast for San Francisco
    print("  🏙️  Getting forecast for San Francisco...")
    result = await call_mcp_tool("weather_server/weather.py", "get_forecast",
                           {"latitude": 37.7749, "longitude": -122.4194})

    # Show first 300 characters to keep output manageable
    if len(result) > 300:
        print(f"  📊 {result[:300]}...")
    else:
        print(f"  📊 {result}")


async def demo_wikipedia_server():
    """Demonstrate the Wikipedia server with a simple search."""
    print("\n📖 WIKIPEDIA SERVER DEMO")
    print("=" * 40)
    print("The Wikipedia server searches and retrieves Wikipedia articles.")

    # Get summary of a famous topic
    print("  🔍 Getting summary of 'Artificial Intelligence'...")
    result = await call_mcp_tool("wikipedia_server/wikipedia.py", "get_wikipedia_summary",
                           {"title": "Artificial intelligence"})

    # Show first 400 characters
    if len(result) > 400:
        print(f"  📄 {result[:400]}...")
    else:
        print(f"  📄 {result}")


async def demo_arxiv_server():
    """Demonstrate the ArXiv server with a simple paper search."""
    print("\n📚 ARXIV SERVER DEMO")
    print("=" * 40)
    print("The ArXiv server searches academic papers (no API key needed).")

    # Search for machine learning papers
    print("  🔬 Searching for 'machine learning' papers...")
    result = await call_mcp_tool("arxiv_server/arxiv.py", "search_papers",
                           {"query": "machine learning", "max_results": 2})

    # Show first 500 characters
    if len(result) > 500:
        print(f"  📑 {result[:500]}...")
    else:
        print(f"  📑 {result}")


async def demo_tavily_server():
    """Demonstrate the Tavily server (requires API key)."""
    print("\n🔍 TAVILY SERVER DEMO")
    print("=" * 40)
    print("The Tavily server provides web search (requires TAVILY_API_KEY).")

    # Check if we can use Tavily (this will show how to handle API keys)
    result = await call_mcp_tool("tavily_server/tavily.py", "search",
                           {"query": "latest AI news", "max_results": 2})

    if "API key not found" in result:
        print("  ⚠️  Skipped: TAVILY_API_KEY environment variable not set")
        print("  💡 To enable: Set TAVILY_API_KEY in your environment or .env file")
    else:
        if len(result) > 300:
            print(f"  🌐 {result[:300]}...")
        else:
            print(f"  🌐 {result}")


async def main():
    """Main function that runs all demos."""
    print("🚀 SIMPLE MCP SERVERS DEMO (Fixed Version)")
    print("=" * 50)
    print("This script demonstrates the CORRECT way to call MCP servers.")
    print("Key fix: Added proper MCP initialization before calling tools!\n")

    try:
        # Run demos in order of complexity (simplest first)
        await demo_math_server()
        await demo_weather_server()
        await demo_wikipedia_server()
        await demo_arxiv_server()
        await demo_tavily_server()

        print("\n✅ DEMO COMPLETE!")
        print("=" * 50)
        print("🎓 What you learned:")
        print("  • MCP servers need proper initialization BEFORE calling tools")
        print("  • ClientSession manages the MCP protocol connection")
        print("  • session.initialize() is the critical missing step")
        print("  • MCP provides standardized tool calling")
        print("\n💡 Compare with other demos:")
        print("  • direct_demo.py: Calls functions directly (simplest)")
        print("  • simple_demo.py: Uses MCP protocol (this file)")
        print("  • mcp_client_demo.py: More detailed MCP examples")

    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")


if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 10):
        print("❌ Error: Python 3.10 or higher is required")
        sys.exit(1)

    # Run the async demo
    asyncio.run(main())