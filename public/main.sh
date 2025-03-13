#!/bin/bash

# Get the absolute directory of the script (which is inside public/)
script_dir=$(dirname "$(realpath "$0")")

# Set the correct path to the src directory inside public/
src_dir="$script_dir/src"

# Run the Python script inside public/src/
python3 -B "$src_dir/main.py"

# Debugging output
echo "SCRIPT DIR: $script_dir"
echo "SRC DIR: $src_dir"



