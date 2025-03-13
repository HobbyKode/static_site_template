#!/bin/bash

# Get the absolute path to the directory containing this script
script_dir=$(dirname "$(realpath "$0")")

# Navigate to the project root (adjust based on your structure)
project_root=$(realpath "$script_dir/..")

# Run the Python script from src/main.py
python3 "$project_root/src/main.py"


