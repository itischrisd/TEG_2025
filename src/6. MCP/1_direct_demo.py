#!/usr/bin/env python3
"""
Direct Function Demo - The simplest way to understand MCP server tools.

This script imports and calls server functions directly, bypassing MCP protocol.
Perfect for students to understand WHAT each tool does before learning HOW MCP works.

Usage: python3 direct_demo.py
"""

import asyncio
import sys
import os

# Import server modules using importlib
import importlib.util

def load_server_module(server_name, file_name):
    """Dynamically load a server module."""
    module_path = os.path.join(os.path.dirname(__file__), server_name, file_name)
    spec = importlib.util.spec_from_file_location(f"{server_name}_module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load server modules
math_module = load_server_module('math_server', 'math_server.py')
weather_module = load_server_module('weather_server', 'weather.py')
wikipedia_module = load_server_module('wikipedia_server', 'wikipedia.py')
arxiv_module = load_server_module('arxiv_server', 'arxiv.py')

# Extract functions from modules
add = math_module.add
subtract = math_module.subtract
multiply = math_module.multiply
divide = math_module.divide
power = math_module.power
sqrt = math_module.sqrt
factorial = math_module.factorial

get_forecast = weather_module.get_forecast
get_wikipedia_summary = wikipedia_module.get_wikipedia_summary
search_papers = arxiv_module.search_papers


def demo_math_functions():
    """Demonstrate math functions by calling them directly."""
    print("\n🔢 MATH FUNCTIONS - DIRECT CALL DEMO")
    print("=" * 45)
    print("These are the actual functions inside math_server.py")

    # Simple addition
    result = add(5, 3)
    print(f"  ➕ add(5, 3) = {result}")

    # Multiplication
    result = multiply(7, 6)
    print(f"  ✖️  multiply(7, 6) = {result}")

    # Power calculation
    result = power(2, 8)
    print(f"  🔺 power(2, 8) = {result}")

    # Square root
    result = sqrt(16)
    print(f"  √ sqrt(16) = {result}")

    # Division
    result = divide(15, 3)
    print(f"  ➗ divide(15, 3) = {result}")

    # Factorial
    result = factorial(5)
    print(f"  ! factorial(5) = {result}")

    print("  💡 These are just regular Python functions!")


async def demo_weather_functions():
    """Demonstrate weather functions by calling them directly."""
    print("\n🌤️  WEATHER FUNCTIONS - DIRECT CALL DEMO")
    print("=" * 45)
    print("These are the actual async functions inside weather_server.py")

    try:
        # Get forecast for San Francisco
        print("  🏙️  Calling get_forecast(37.7749, -122.4194)...")
        result = await get_forecast(37.7749, -122.4194)

        # Show first 300 characters
        print(f"  📊 Result: {result[:300]}...")

        print("  💡 This is an async function that calls the National Weather Service API!")

    except Exception as e:
        print(f"  ❌ Weather function failed: {e}")


async def demo_wikipedia_functions():
    """Demonstrate Wikipedia functions by calling them directly."""
    print("\n📖 WIKIPEDIA FUNCTIONS - DIRECT CALL DEMO")
    print("=" * 45)
    print("These are the actual async functions inside wikipedia_server.py")

    try:
        print("  🔍 Calling get_wikipedia_summary('Machine learning')...")
        result = await get_wikipedia_summary("Machine learning")

        # Show first 400 characters
        print(f"  📄 Result: {result[:400]}...")

        print("  💡 This function calls the Wikipedia API directly!")

    except Exception as e:
        print(f"  ❌ Wikipedia function failed: {e}")


async def demo_arxiv_functions():
    """Demonstrate ArXiv functions by calling them directly."""
    print("\n📚 ARXIV FUNCTIONS - DIRECT CALL DEMO")
    print("=" * 45)
    print("These are the actual async functions inside arxiv_server.py")

    try:
        print("  🔬 Calling search_papers('machine learning', max_results=2)...")
        result = await search_papers("machine learning", max_results=2)

        # Show first 500 characters
        print(f"  📑 Result: {result[:500]}...")

        print("  💡 This function searches the ArXiv API for research papers!")

    except Exception as e:
        print(f"  ❌ ArXiv function failed: {e}")


async def main():
    """Main function demonstrating direct function calls."""
    print("🚀 DIRECT FUNCTION CALL DEMO")
    print("=" * 50)
    print("This is the SIMPLEST way to understand what MCP servers do.")
    print("We're calling the functions directly - no MCP protocol needed!")

    try:
        # Demo synchronous functions
        demo_math_functions()

        # Demo asynchronous functions
        await demo_weather_functions()
        await demo_wikipedia_functions()
        await demo_arxiv_functions()

        print("\n✅ DIRECT DEMO COMPLETE!")
        print("=" * 50)
        print("🎓 What you learned:")
        print("  • MCP servers are just collections of Python functions")
        print("  • Some functions are sync (math), others are async (API calls)")
        print("  • Functions do the actual work - MCP just exposes them")
        print("  • This is what happens 'under the hood' in MCP")
        print("\n🔄 Next steps:")
        print("  • Run mcp_client_demo.py to see proper MCP protocol")
        print("  • Compare this direct approach vs. MCP approach")
        print("  • Understand: Direct = Simple, MCP = Standardized")

    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")


if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 10):
        print("❌ Error: Python 3.10 or higher is required")
        sys.exit(1)

    # Run the direct function demo
    asyncio.run(main())