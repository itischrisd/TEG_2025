#!/usr/bin/env python3
"""
Simple script to run MCP servers with dependencies.
Usage: python run_server.py <server_name>
"""

import sys
import subprocess
import os

def run_server(server_name: str):
    """Run a specific MCP server with required dependencies."""
    
    server_map = {
        "math": "math_server/math_server.py",
        "weather": "weather_server/weather.py",
        "tavily": "tavily_server/tavily.py",
        "arxiv": "arxiv_server/arxiv.py",
        "wikipedia": "wikipedia_server/wikipedia.py",
        "context7": "context7_server/context7.py"
    }
    
    if server_name not in server_map:
        print(f"Unknown server: {server_name}")
        print(f"Available servers: {', '.join(server_map.keys())}")
        return 1
    
    server_path = server_map[server_name]
    
    # Check if server file exists
    if not os.path.exists(server_path):
        print(f"Server file not found: {server_path}")
        return 1
    
    print(f"Starting {server_name} server...")
    
    # Run with uv and required dependencies
    cmd = [
        "uv", "run",
        "--with", "mcp>=1.2.0",
        "--with", "httpx>=0.28.1",
        server_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        return 0
    
    return 0

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_server.py <server_name>")
        print("Available servers: math, weather, tavily, arxiv, wikipedia, context7")
        return 1
    
    server_name = sys.argv[1]
    return run_server(server_name)

if __name__ == "__main__":
    sys.exit(main())