@echo off
echo Setting up FastAPI development environment...

python -m venv .venv
call .venv\Scripts\activate.bat

pip install -r requirements.txt

echo.
echo FastAPI environment setup complete!
echo To activate: .venv\Scripts\activate.bat
echo To run FastAPI: uvicorn app.main:app --reload --port 8080