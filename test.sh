#!/bin/bash

# Set the Python module search path
export PYTHONPATH=$(realpath src)

# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1

# Run all tests inside src/tests/
python3 -m unittest discover -s src/tests