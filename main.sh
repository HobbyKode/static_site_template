#!/bin/bash

# Ensure we're in the correct project root
cd "$(dirname "$0")"

# Define the correct path to `main.py` inside `public/src/`
main_script="./public/src/main.py"

# Run the main script
python3 "$main_script"

