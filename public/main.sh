#!/bin/bash

# Get the absolute directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Calculate the absolute path to the src directory (adjusted to public/src/)
src_dir=$(realpath "$script_dir/src")

# Run the Python script within public/src/
python3 "$src_dir/main.py"

# Debugging output
echo "SCRIPT DIR: $script_dir"
echo "SRC DIR: $src_dir"


