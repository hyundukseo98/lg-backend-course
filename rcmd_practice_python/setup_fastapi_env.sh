#!/bin/bash
echo "Setting up FastAPI development environment..."

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

echo ""
echo "FastAPI environment setup complete!"
echo "To activate: source .venv/bin/activate"
echo "To run FastAPI: uvicorn app.main:app --reload --port 8080"