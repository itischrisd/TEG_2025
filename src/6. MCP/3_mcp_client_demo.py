#!/usr/bin/env python3
"""
Proper MCP Client Demo - Shows correct way to use MCP protocol.

This script demonstrates the proper MCP (Model Context Protocol) client implementation
with correct initialization handshake. Perfect for understanding MCP protocol flow.

Usage: python3 mcp_client_demo.py
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def demo_math_server():
    """Demonstrate the math server using proper MCP client."""
    print("\n🔢 MATH SERVER - MCP CLIENT DEMO")
    print("=" * 45)
    print("This shows the correct way to use MCP servers.")

    # Step 1: Define server parameters
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "--with", "mcp>=1.2.0", "math_server/math_server.py"]
    )

    try:
        # Step 2: Create connection to server
        async with stdio_client(server_params) as (read_stream, write_stream):
            # Step 3: Create client session
            async with ClientSession(read_stream, write_stream) as session:
                # Step 4: Initialize the MCP connection (CRITICAL!)
                print("  🤝 Initializing MCP connection...")
                await session.initialize()
                print("  ✅ MCP initialization complete!")

                # Step 5: List available tools
                tools_result = await session.list_tools()
                print(f"  🛠️  Available tools: {[tool.name for tool in tools_result.tools]}")

                # Step 6: Now we can safely call tools
                print("\n  📞 Making tool calls...")

                # Addition
                result = await session.call_tool("add", {"a": 5, "b": 3})
                print(f"  ➕ 5 + 3 = {result.content[0].text}")

                # Multiplication
                result = await session.call_tool("multiply", {"a": 7, "b": 6})
                print(f"  ✖️  7 × 6 = {result.content[0].text}")

                # Power
                result = await session.call_tool("power", {"a": 2, "b": 8})
                print(f"  🔺 2^8 = {result.content[0].text}")

                # Square root
                result = await session.call_tool("sqrt", {"a": 16})
                print(f"  √ √16 = {result.content[0].text}")

    except Exception as e:
        print(f"  ❌ Math server demo failed: {e}")


async def demo_weather_server():
    """Demonstrate the weather server using proper MCP client."""
    print("\n🌤️  WEATHER SERVER - MCP CLIENT DEMO")
    print("=" * 45)

    server_params = StdioServerParameters(
        command="uv",
        args=["run", "--with", "mcp>=1.2.0", "--with", "httpx>=0.28.1", "weather_server/weather.py"]
    )

    try:
        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                # Get forecast for San Francisco
                print("  🏙️  Getting forecast for San Francisco...")
                result = await session.call_tool("get_forecast", {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                })

                forecast = result.content[0].text
                # Show just the first part to keep output manageable
                print(f"  📊 {forecast[:300]}...")

    except Exception as e:
        print(f"  ❌ Weather server demo failed: {e}")


async def demo_wikipedia_server():
    """Demonstrate the Wikipedia server using proper MCP client."""
    print("\n📖 WIKIPEDIA SERVER - MCP CLIENT DEMO")
    print("=" * 45)

    server_params = StdioServerParameters(
        command="uv",
        args=["run", "--with", "mcp>=1.2.0", "--with", "httpx>=0.28.1", "wikipedia_server/wikipedia.py"]
    )

    try:
        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                print("  🔍 Getting summary of 'Machine Learning'...")
                result = await session.call_tool("get_wikipedia_summary", {
                    "title": "Machine learning"
                })

                summary = result.content[0].text
                print(f"  📄 {summary[:400]}...")

    except Exception as e:
        print(f"  ❌ Wikipedia server demo failed: {e}")


async def main():
    """Main function demonstrating proper MCP usage."""
    print("🚀 PROPER MCP CLIENT DEMO")
    print("=" * 50)
    print("This script shows the CORRECT way to use MCP servers.")
    print("Key steps: Initialize → List Tools → Call Tools")

    try:
        # Demo each server with proper MCP protocol
        await demo_math_server()
        await demo_weather_server()
        await demo_wikipedia_server()

        print("\n✅ MCP CLIENT DEMO COMPLETE!")
        print("=" * 50)
        print("🎓 What you learned:")
        print("  • Proper MCP initialization is required")
        print("  • ClientSession manages the MCP connection")
        print("  • Initialize before calling any tools")
        print("  • MCP protocol ensures reliable communication")
        print("\n💡 Key difference from simple_demo.py:")
        print("  • This uses MCP ClientSession (proper protocol)")
        print("  • simple_demo.py tried direct subprocess calls (broken)")
        print("  • Always use session.initialize() first!")

    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")


if __name__ == "__main__":
    # Check Python version
    import sys
    if sys.version_info < (3, 10):
        print("❌ Error: Python 3.10 or higher is required")
        sys.exit(1)

    # Run the proper MCP client demo
    asyncio.run(main())