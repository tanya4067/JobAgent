# Variables
VENV = venv
PYTHON = python3
PIP = $(VENV)/bin/pip
UVICORN = $(VENV)/bin/uvicorn
STREAMLIT = $(VENV)/bin/streamlit

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)

# Install dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Pull LLM model (Ollama)
ollama:
	@echo "Checking Ollama..."
	@if ! command -v ollama >/dev/null 2>&1; then \
		echo "❌ Ollama not installed. Install from https://ollama.com"; \
	else \
		echo "✅ Ollama found. Pulling model..."; \
		ollama pull llama3; \
	fi

# Run FastAPI app
run:
	$(UVICORN) main:app --reload

# Run Streamlit UI
ui:
	$(STREAMLIT) run app.py

# Clean temp files
clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -f temp_*

# Full setup (one command)
setup: install ollama
	@echo "🚀 Setup complete!"

# Default command
all: setup run