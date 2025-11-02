.PHONY: help install format lint test coverage clean run pre-commit validate-ai-docs

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies with uv
	uv sync --all-extras --dev
	uv run pre-commit install

format: ## Format code with black and isort
	uv run black src tests
	uv run isort src tests

lint: ## Run all linters (ruff, mypy, pylint)
	uv run ruff check src tests --fix
	uv run mypy src tests
	uv run pylint src tests

test: ## Run tests with pytest
	uv run pytest -v

coverage: ## Run tests with coverage report
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build dist htmlcov .coverage coverage.xml
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

run: ## Run the main application
	uv run leadership-blog-generator

pre-commit: ## Run pre-commit on all files
	uv run pre-commit run --all-files

update: ## Update all dependencies to latest versions
	uv update
	uv run pre-commit autoupdate

check: format lint test ## Run format, lint, and test

build: ## Build the package
	uv build

install-editable: ## Install package in editable mode for development
	uv pip install -e .

validate-ai-docs: ## Validate AI instruction files are present and consistent
	uv run python scripts/validate_ai_instructions.py
