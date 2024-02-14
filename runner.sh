#!/bin/bash

# Run tests using pytest
echo "Running unit tests..."
python3 -m pip install -r requirements.txt
python3 -m pytest

# Check if tests passed
if [ $? -eq 0 ]; then
    # Tests passed, start Uvicorn server
    echo "Tests passed. Starting Uvicorn server..."
    python3 -m uvicorn app.main:app --host 0.0.0.0 --reload
else
    # Tests failed, exit with error
    echo "Tests failed. Exiting..."
    exit 1
fi