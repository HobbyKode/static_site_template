#!/bin/bash

# Get the absolute path of the script's directory
script_dir=$(dirname "$(realpath "$0")")

# Define the correct path to `main.py` inside `public/src/`
main_script="$script_dir/public/src/main.py"

# Run the main script
python3 "$main_script"
