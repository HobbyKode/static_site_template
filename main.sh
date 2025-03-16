#!/bin/bash

# Ensure we're in the correct project root
cd "$(dirname "$0")"

# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1

# Run the main script for local testing
echo "🚀 Running site generator locally..."
python3 src/main.py

# Start the local web server in the docs directory
echo "🌐 Starting local server at http://localhost:8888"
cd docs && python3 -m http.server 8888

