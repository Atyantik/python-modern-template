# Project Context & Architecture

> **Shared documentation for all AI coding assistants**
>
> This file is referenced by multiple AI tool configurations. Changes here automatically apply to all tools that support file references.

## 📋 Project Overview

**Name**: Leadership Blog Generator
**Version**: 0.1.0
**License**: MIT
**Description**: A Python tool for generating leadership-focused blog content

**Purpose**: Generate leadership-focused blog content with best practices and modern tooling, while serving as a reference implementation for AI-assisted TDD development.

## 🛠️ Technology Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ (3.13 recommended) | Primary language |
| **uv** | Latest | Fast package manager |
| **setuptools** | ≥61.0 | Build system |

### Development Tools

| Tool | Version | Purpose |
|------|---------|---------|
| **Black** | ≥25.9.0 | Code formatter |
| **isort** | ≥7.0.0 | Import sorter |
| **Ruff** | ≥0.14.3 | Fast linter |
| **mypy** | ≥1.18.2 | Type checker (strict mode) |
| **Pylint** | ≥4.0.2 | Comprehensive linter |
| **pytest** | ≥8.4.2 | Testing framework |
| **pytest-cov** | ≥7.0.0 | Coverage reporting |
| **pytest-mock** | ≥3.15.1 | Mocking utilities |
| **pre-commit** | ≥4.3.0 | Git hooks manager |

## 📁 Project Structure

```
leadership-blog-generator/
├── AI_DOCS/                    # Shared AI documentation (2025 standard)
│   ├── README.md               # Documentation overview
│   ├── tdd-workflow.md         # TDD process and testing
│   ├── ai-tools.md             # AI session management tools
│   ├── code-conventions.md     # Code style and standards
│   └── project-context.md      # This file - tech stack & architecture
│
├── src/
│   └── leadership_blog_generator/
│       ├── __init__.py         # Package exports & version
│       ├── main.py             # CLI and main functionality
│       └── [modules].py        # Additional feature modules
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Shared pytest fixtures
│   ├── test_main.py            # Tests for main.py
│   └── test_[module].py        # Tests mirror src structure
│
├── scripts/
│   └── ai_tools/               # AI context management CLI tools
│       ├── __init__.py
│       ├── start_task.py       # ai-start-task
│       ├── log_execution.py    # ai-log
│       ├── update_plan.py      # ai-update-plan
│       ├── finish_task.py      # ai-finish-task
│       ├── context_summary.py  # ai-context-summary
│       ├── check_conflicts.py  # ai-check-conflicts
│       ├── add_decision.py     # ai-add-decision
│       └── add_convention.py   # ai-add-convention
│
├── .ai-context/                # AI session tracking (git-tracked)
│   ├── REQUIRED_READING.md     # Master checklist for AI agents
│   ├── LAST_SESSION_SUMMARY.md # Most recent session summary
│   ├── ACTIVE_TASKS.md         # Tasks currently in progress
│   ├── RECENT_DECISIONS.md     # Architectural decisions
│   ├── CONVENTIONS.md          # Code patterns and standards
│   └── sessions/               # Session files (local only)
│       ├── YYYYMMDDHHMMSS-PLAN-*.md
│       ├── YYYYMMDDHHMMSS-SUMMARY-*.md
│       └── YYYYMMDDHHMMSS-EXECUTION-*.md
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml              # GitHub Actions CI/CD
│   └── copilot-instructions.md # GitHub Copilot config (2025 standard)
│
├── .gemini/
│   └── styleguide.md           # Gemini Code Assist config (2025 standard)
│
├── docs/                       # User documentation
│
├── AGENTS.md                   # Universal AI instructions (all tools)
├── CLAUDE.md                   # Claude Code config (2025 standard)
├── .cursorrules                # Cursor IDE config
├── .aider.conf.yml             # Aider AI config
├── AI_CONFIG_MIGRATION_2025.md # Migration documentation
│
├── .gitignore                  # Git ignore patterns
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── pyproject.toml              # Project configuration and dependencies
├── Makefile                    # Development commands
├── README.md                   # Main documentation
└── uv.lock                     # Locked dependencies
```

## 🎯 Package Architecture

### Package Organization

```python
# src/leadership_blog_generator/__init__.py
"""Leadership blog generator package."""

from .main import generate_blog
from .validators import validate_email, validate_phone

__version__ = "0.1.0"

__all__ = [
    "generate_blog",
    "validate_email",
    "validate_phone",
]
```

### Import Pattern

```python
# ✅ Correct - import from package name
from leadership_blog_generator import function_name
from leadership_blog_generator.module import ClassName

# ❌ Wrong - never use src prefix
from src.leadership_blog_generator import function_name
```

### Module Breakdown

- **`main.py`**: CLI entry point and main application logic
- **`validators.py`** (example): Data validation functions
- **`processors.py`** (example): Data processing functions
- **`utils.py`** (example): Utility functions

## 🔧 Configuration

All tool configurations are centralized in `pyproject.toml`.

### Black Configuration

```toml
[tool.black]
line-length = 88
target-version = ['py313']
```

### isort Configuration

```toml
[tool.isort]
profile = "black"
line_length = 88
```

### Ruff Configuration

```toml
[tool.ruff]
target-version = "py313"
line-length = 88

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "UP",   # pyupgrade
    "ARG",  # flake8-unused-arguments
    "SIM",  # flake8-simplify
]
```

### mypy Configuration (Strict Mode)

```toml
[tool.mypy]
python_version = "3.13"
strict = true
warn_return_any = true
disallow_untyped_defs = true
disallow_any_generics = true
```

### pytest Configuration

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = [
    "--verbose",
    "--cov=src",
    "--cov-fail-under=80",  # 80% minimum coverage
]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
```

## 🚀 CLI Tools

### Main Application

```bash
# Entry point: leadership_blog_generator.main:main
uv run leadership-blog-generator --help
```

### AI Context Management Tools (8 tools)

```bash
# Session management
uv run ai-start-task "Task description"      # Start session
uv run ai-log "Progress message"             # Log progress
uv run ai-update-plan "Item completed"       # Update plan
uv run ai-finish-task --summary="..."        # End session

# Context utilities
uv run ai-context-summary                    # Show context
uv run ai-check-conflicts "Task name"        # Check conflicts
uv run ai-add-decision                       # Add decision
uv run ai-add-convention                     # Add convention
```

See `@AI_DOCS/ai-tools.md` for comprehensive documentation.

## 🔄 Development Workflow

### Setup

```bash
# Clone repository
git clone <repo-url>
cd leadership-blog-generator

# Install dependencies
uv sync --all-extras --dev

# Install package in editable mode
uv pip install -e .

# Install pre-commit hooks
uv run pre-commit install
```

### Daily Workflow

```bash
# 1. Start AI session
uv run ai-start-task "Feature description"

# 2. Write tests first (TDD)
# Create tests/test_feature.py

# 3. Implement code
# Create src/leadership_blog_generator/feature.py

# 4. Run quality checks
make check  # Runs format, lint, and tests

# 5. Finish session
uv run ai-finish-task --summary="Implementation complete"

# 6. Commit
git add .
git commit -m "Add feature X with tests"
```

### Makefile Commands

```bash
# Essential Commands
make help        # Show all available commands
make check       # Run format, lint, and tests (most important!)
make test        # Run tests only
make coverage    # Generate test coverage report
make format      # Format code with Black and isort
make lint        # Run all linters (Ruff + mypy + Pylint)

# Setup
make install     # Install dependencies + pre-commit hooks

# Maintenance
make clean       # Remove generated files
make build       # Build distribution package
make pre-commit  # Run pre-commit hooks manually
make update      # Update dependencies
```

## 🧪 Testing Strategy

### Test Organization

- **Location**: `tests/` directory
- **Naming**: `test_*.py` files mirror `src/` structure
- **Framework**: pytest with plugins
- **Coverage**: Minimum 80%, target 90%+

### Test Types

```python
# Unit tests (default)
@pytest.mark.unit
def test_function():
    ...

# Integration tests
@pytest.mark.integration
def test_api_integration():
    ...

# Slow tests (can be excluded)
@pytest.mark.slow
def test_large_dataset():
    ...
```

### Fixtures

```python
# tests/conftest.py - Shared fixtures
@pytest.fixture
def temp_dir(tmp_path):
    """Provide temporary directory."""
    return tmp_path

# Minimize use of fixtures - prefer real code
```

## 📦 Dependencies

### Production Dependencies

Currently no production dependencies. The project is self-contained.

### Development Dependencies

See `pyproject.toml` `[dependency-groups.dev]` for complete list:
- Code quality: Black, isort, Ruff, mypy, Pylint
- Testing: pytest, pytest-cov, pytest-mock
- Git hooks: pre-commit

### Adding Dependencies

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Update all dependencies
uv sync --upgrade
```

## 🔒 Security

### Security Scanning

CI automatically runs:
- **Bandit**: Python security linter
- **Safety**: Dependency vulnerability scanner

### Best Practices

- Never commit secrets/credentials
- Use environment variables for sensitive config
- Validate all user input
- Use parameterized queries for database access
- Keep dependencies updated

## 🌐 CI/CD Pipeline

### GitHub Actions (`.github/workflows/ci.yml`)

**Triggers**: Push to any branch, Pull requests

**Jobs**:
1. **Linting**: Runs all code quality tools
2. **Testing**: Tests on Python 3.11, 3.12, 3.13
3. **Coverage**: Reports coverage to Codecov
4. **Security**: Scans for vulnerabilities
5. **Build**: Creates distribution packages

**Required to pass**:
- All linters (Black, isort, Ruff, mypy, Pylint)
- All tests across all Python versions
- Coverage ≥ 80%
- No security vulnerabilities

## 🤖 AI Configuration (2025 Standards)

### File Locations

| Tool | Config File | Format |
|------|------------|---------|
| **Universal** | `AGENTS.md` | Markdown |
| **Cursor** | `.cursorrules` | Markdown |
| **Claude Code** | `CLAUDE.md` | Markdown |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Markdown |
| **Gemini** | `.gemini/styleguide.md` | Markdown |
| **Aider** | `.aider.conf.yml` | YAML |

### Shared Documentation

All configs reference these shared docs via `@AI_DOCS/` syntax:
- `@AI_DOCS/tdd-workflow.md` - TDD process
- `@AI_DOCS/ai-tools.md` - Session management
- `@AI_DOCS/code-conventions.md` - Code standards
- `@AI_DOCS/project-context.md` - This file

**Exception**: GitHub Copilot and Gemini styleguide.md require manual content duplication (no file reference support).

## 📊 Quality Metrics

### Current Status

- ✅ **Tests**: 35 passing (26 AI tools + 9 main package)
- ✅ **Coverage**: 100%
- ✅ **Linting**: All tools pass (Ruff, mypy, Pylint 10/10)
- ✅ **Security**: No vulnerabilities
- ✅ **CI**: All checks passing

### Target Metrics

- **Code Coverage**: ≥80% (enforced), 90%+ (target)
- **Pylint Score**: 10.0/10.0 (enforced)
- **Type Coverage**: 100% (mypy strict mode)
- **Test Success Rate**: 100%
- **Security Issues**: 0

## 🎓 Learning Resources

### For AI Agents

- **TDD Workflow**: `@AI_DOCS/tdd-workflow.md`
- **AI Tools**: `@AI_DOCS/ai-tools.md`
- **Code Standards**: `@AI_DOCS/code-conventions.md`
- **Universal Instructions**: `AGENTS.md`

### For Developers

- **Main README**: `README.md`
- **Migration Guide**: `AI_CONFIG_MIGRATION_2025.md`
- **Required Reading**: `.ai-context/REQUIRED_READING.md`

## 🔄 Version Control

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/description

# Make changes following TDD
# (tests first, implementation, quality checks)

# Commit with descriptive message
git commit -m "Add feature X with tests (closes #123)"

# Push and create PR
git push origin feature/description
```

### Commit Message Format

```
<type>: <description>

[optional body]
[optional footer]
```

**Types**: feat, fix, docs, test, refactor, style, chore

## 📝 Documentation Standards

### Code Documentation

- **Modules**: Module-level docstring at top
- **Classes**: Class docstring explaining purpose
- **Functions**: Google-style docstrings with Args, Returns, Raises
- **Type Hints**: Required on all public functions

### Project Documentation

- **README.md**: User-facing documentation
- **AI_DOCS/**: AI agent documentation
- **CHANGELOG.md**: Version history (if needed)
- **docs/**: Additional user guides (if needed)

## 🚦 Quality Gates

Before merging code:

1. ✅ All tests pass (`make test`)
2. ✅ Coverage ≥ 80% (`make coverage`)
3. ✅ All linters pass (`make lint`)
4. ✅ Code formatted (`make format`)
5. ✅ Pre-commit hooks pass (`make pre-commit`)
6. ✅ CI pipeline passes
7. ✅ No merge conflicts
8. ✅ AI session properly closed (`ai-finish-task`)

## 🎯 Future Enhancements

Potential areas for expansion:
- Add actual blog generation functionality
- Integrate with LLM APIs for content generation
- Add web interface
- Support multiple output formats
- Add content templates

## 📚 Additional Resources

- **Python 3.13 Docs**: https://docs.python.org/3.13/
- **uv Documentation**: https://github.com/astral-sh/uv
- **pytest Documentation**: https://docs.pytest.org/
- **Black Documentation**: https://black.readthedocs.io/
- **mypy Documentation**: https://mypy.readthedocs.io/

---

**Remember**: This project emphasizes quality over speed. Follow TDD, maintain high coverage, and use AI tools for session tracking.
