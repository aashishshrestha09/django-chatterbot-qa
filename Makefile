# Makefile for Django ChatterBot Terminal Client

.PHONY: help venv install migrate run test clean

# Python and virtual environment settings
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help:
	@echo "Django ChatterBot Terminal Client - Available Commands:"
	@echo ""
	@echo "  make venv       - Create virtual environment"
	@echo "  make install    - Install dependencies (creates venv if needed)"
	@echo "  make migrate    - Run database migrations"
	@echo "  make run        - Start the chat client"
	@echo "  make test       - Run test cases"
	@echo "  make clean      - Remove cache files and database"
	@echo "  make cleanall   - Remove everything including venv"
	@echo "  make setup      - Complete setup (venv + install + migrate)"
	@echo ""

venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "Virtual environment created! Activate with: source $(VENV)/bin/activate"

install: venv
	@echo "Installing dependencies (including Spacy model)..."
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencies installed!"

migrate:
	@echo "Running database migrations..."
	$(PYTHON) manage.py migrate

run:
	@echo "Starting ChatterBot Terminal Client..."
	$(PYTHON) manage.py runchat

test:
	@echo "Running test cases..."
	$(PYTHON) manage.py test chat_app

clean:
	@echo "Cleaning up cache files and database..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -f db.sqlite3
	rm -f chatbot_database.db*
	@echo "Clean complete!"

cleanall: clean
	@echo "Removing virtual environment..."
	rm -rf $(VENV)
	@echo "Complete cleanup done!"

setup: install migrate
	@echo ""
	@echo "✅ Setup complete! Run 'make run' to start chatting."
