.PHONY: help install format lint test coverage clean run pre-commit validate-ai-docs

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies with uv
	uv sync --all-extras --dev
	uv run pre-commit install

format: ## Format code with black and isort
	uv run quality-format

lint: ## Run all linters (ruff, mypy, pylint)
	uv run quality-lint

test: ## Run tests with pytest
	uv run quality-test -v

coverage: ## Run tests with coverage report
	uv run quality-test --coverage

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

check: ## Run complete quality check (format, lint, test with coverage)
	uv run quality-check

build: ## Build the package
	uv build

install-editable: ## Install package in editable mode for development
	uv pip install -e .

validate-ai-docs: ## Validate AI instruction files are present and consistent
	uv run python scripts/validate_ai_instructions.py

## AI Tools
.PHONY: ai-help ai-context ai-start ai-finish

ai-help: ## Show AI tools help
	@echo "AI Context Management Tools:"
	@echo "  make ai-context         - Show current AI context"
	@echo "  make ai-start TASK=\"...\" - Start new AI task"
	@echo "  make ai-finish          - Finish current AI task"
	@echo ""
	@echo "Individual commands:"
	@echo "  uv run ai-start-task \"task description\""
	@echo "  uv run ai-log \"message\" [--level=success|warning|error]"
	@echo "  uv run ai-update-plan \"task item\""
	@echo "  uv run ai-update-plan --show"
	@echo "  uv run ai-finish-task --summary=\"what was done\""
	@echo "  uv run ai-context-summary [--detailed]"
	@echo "  uv run ai-check-conflicts [\"task name\"]"
	@echo "  uv run ai-add-decision"
	@echo "  uv run ai-add-convention"

ai-context: ## Show current AI context summary
	uv run ai-context-summary

ai-start: ## Start new AI task (usage: make ai-start TASK="task description")
ifndef TASK
	@echo "Error: TASK not specified. Usage: make ai-start TASK=\"task description\""
	@exit 1
endif
	uv run ai-start-task "$(TASK)"

ai-finish: ## Finish current AI task (prompts for summary)
	uv run ai-finish-task
