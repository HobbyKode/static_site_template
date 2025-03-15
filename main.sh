#!/bin/bash

# Ensure we're in the correct project root
cd "$(dirname "$0")"

# Define the correct path to `main.py` inside `public/src/`
main_script="./public/src/main.py"

# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1

# Run the main script
python3 "$main_script"

#Start the web server
cd public && python3 -m http.server 8888

