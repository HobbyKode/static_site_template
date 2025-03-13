#!/bin/bash

# Ensure the script runs from the correct location
cd "$(dirname "$0")"

# Define the correct path to `main.py` inside `public/src/`
main_script="./src/main.py"

# Run the main script
python3 "$main_script"
