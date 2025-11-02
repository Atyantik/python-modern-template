# AI Agent Instructions

> **Universal instructions for all AI coding assistants working on this project**

## Quick Reference

| Aspect | Requirement |
|--------|-------------|
| **Development Approach** | Test-Driven Development (TDD) - Tests First! |
| **Minimum Coverage** | 80% (enforced by pytest) |
| **Mocks/Fixtures** | Minimize - use real code when possible |
| **Quality Check** | `make check` must pass before committing |
| **Type Hints** | Required on all functions (mypy strict mode) |
| **Code Style** | Black (88 chars) + isort + Ruff + Pylint (10/10) |

## 🎯 Core Principles

### 1. Test-Driven Development (TDD) is Non-Negotiable

**The Workflow:**
```
1. Write failing test
2. Run test (confirm it fails)
3. Write minimal code to pass test
4. Run test (confirm it passes)
5. Refactor if needed
6. Run make check (all quality gates)
7. Commit
```

**Example:**
```python
# Step 1: Write test FIRST in tests/test_calculator.py
def test_add_two_numbers() -> None:
    """Test that add function correctly sums two numbers."""
    result = add(2, 3)
    assert result == 5

# Step 2: Run test - it will fail (function doesn't exist yet)
# Step 3: Implement in src/leadership_blog_generator/calculator.py
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Step 4: Run test - it passes
# Step 5: Refactor if needed
# Step 6: Run make check
# Step 7: Commit
```

### 2. Minimize Mocks - Use Real Code

**✅ Preferred Approach:**
```python
# Use real function from codebase
from leadership_blog_generator.processor import process_data

def test_process_data() -> None:
    """Test with real data."""
    real_input = "test string"
    result = process_data(real_input)
    assert result == expected_value
```

**❌ Avoid Unless Necessary:**
```python
# Only mock external dependencies
@patch('requests.get')  # OK - external API
def test_api_call(mock_get):
    ...

# Don't mock internal functions
@patch('leadership_blog_generator.utils.helper')  # Bad - use real helper
```

**When to Mock:**
- External API calls (HTTP requests)
- Database connections
- File system writes
- Time/date operations (`datetime.now()`)
- Random number generation
- Environment variables for testing different configs

**When NOT to Mock:**
- Internal project functions
- Pure functions (deterministic output)
- Simple data transformations
- Business logic

### 3. Run Quality Checks Every Time

**After writing ANY code:**
```bash
make check
```

This single command runs:
- Format code (Black + isort)
- Lint code (Ruff + mypy + Pylint)
- Run all tests with coverage

**Never commit if `make check` fails!**

## 📋 Detailed Requirements

### Testing Standards

#### Test Organization
```
tests/
├── __init__.py
├── conftest.py           # Shared fixtures (use sparingly)
├── test_main.py          # Tests for main.py
├── test_calculator.py    # Tests for calculator.py
└── integration/          # Integration tests (if needed)
    └── test_workflow.py
```

#### Test Structure
```python
class TestFeatureName:
    """Group related tests in a class."""

    def test_specific_behavior(self) -> None:
        """Descriptive test name explaining what is tested."""
        # Arrange - Set up test data
        input_data = "example"

        # Act - Call the function being tested
        result = function_under_test(input_data)

        # Assert - Verify the result
        assert result == expected_output
```

#### Parametrized Tests
```python
@pytest.mark.parametrize(
    "input,expected",
    [
        ("hello", 5),
        ("world", 5),
        ("", 0),
    ],
)
def test_string_length(input: str, expected: int) -> None:
    """Test length calculation with various inputs."""
    assert len(input) == expected
```

#### Test Markers
```python
@pytest.mark.slow  # For slow tests
@pytest.mark.integration  # For integration tests
@pytest.mark.unit  # For unit tests (default)
```

### Code Quality Standards

#### Type Hints (Mandatory)
```python
from __future__ import annotations  # For forward references

def process(
    data: str,
    options: dict[str, Any] | None = None,
    count: int = 10,
) -> tuple[str, int]:
    """Process data with options.

    Args:
        data: Input data to process
        options: Optional processing options
        count: Number of iterations

    Returns:
        Tuple of processed data and iteration count
    """
    ...
```

#### Formatting
- **Line length**: 88 characters (Black default)
- **Import sorting**: isort with Black profile
- **Quote style**: Double quotes
- **Trailing commas**: Enforced in multi-line structures

#### Linting Rules
- **Ruff**: Pycodestyle, pyflakes, bugbear, comprehensions, pyupgrade
- **Pylint**: Must score 10.0/10.0
- **mypy**: Strict mode enabled

### Project Structure

```
leadership-blog-generator/
├── src/
│   └── leadership_blog_generator/
│       ├── __init__.py        # Package exports & version
│       ├── main.py            # CLI and main functionality
│       └── [other modules]    # Additional modules
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # Shared fixtures
│   └── test_*.py              # Test files mirror src structure
├── .cursorrules               # Cursor AI instructions
├── AGENTS.md                  # This file - universal instructions
├── .claude/                   # Claude-specific config
│   └── INSTRUCTIONS.md
├── GEMINI.md                  # Gemini AI instructions
├── .aider.conf.yml            # Aider config
├── COPILOT_INSTRUCTIONS.md    # GitHub Copilot instructions
├── pyproject.toml             # Project config & dependencies
├── Makefile                   # Development commands
└── README.md                  # User documentation
```

### Import Conventions
```python
# ✅ Correct - import from package name
from leadership_blog_generator import function_name
from leadership_blog_generator.module import ClassName

# ❌ Wrong - don't use src prefix
from src.leadership_blog_generator import function_name
```

## 🔄 Keeping AI Instructions Synchronized

### When to Update AI Instruction Files

Update **ALL** of these files when making critical changes:
- `.cursorrules`
- `AGENTS.md` (this file)
- `.claude/INSTRUCTIONS.md`
- `GEMINI.md`
- `.aider.conf.yml`
- `COPILOT_INSTRUCTIONS.md`

**Critical changes include:**
- New testing patterns or requirements
- Changes to build/test/lint process
- New code quality rules
- Security-related updates
- Major architectural decisions
- New development workflows

### Validation

Run this to check AI instruction files are in sync:
```bash
make validate-ai-docs
```

## 🛠️ Development Commands

### Essential Commands
```bash
# Setup
make install              # Install dependencies + pre-commit hooks
uv pip install -e .       # Install package in editable mode

# Development Cycle
make test                 # Run tests
make coverage             # Run tests with coverage report
make format               # Format code (Black + isort)
make lint                 # Run linters (Ruff + mypy + Pylint)
make check                # ALL quality checks (format + lint + test)

# Maintenance
make clean                # Remove generated files
make update               # Update dependencies
make pre-commit           # Run pre-commit hooks manually

# Building
make build                # Build distribution package

# Help
make help                 # Show all commands
```

### Running Specific Tests
```bash
# Single test file
uv run pytest tests/test_main.py -v

# Single test function
uv run pytest tests/test_main.py::test_specific_function -v

# With coverage
uv run pytest --cov=src --cov-report=term-missing

# Exclude slow tests
uv run pytest -m "not slow"
```

## 🚦 Quality Gates (All Must Pass)

Before committing code, ensure:

1. ✅ **Tests written FIRST** (TDD)
2. ✅ **All tests pass**: `make test`
3. ✅ **Coverage ≥ 80%**: `make coverage`
4. ✅ **Formatted**: Black + isort via `make format`
5. ✅ **Linted**: Ruff, mypy, Pylint via `make lint`
6. ✅ **Pre-commit hooks pass**: `make pre-commit`
7. ✅ **Type hints everywhere**: mypy strict mode
8. ✅ **No security issues**: CI runs Bandit + Safety

## 🔒 Security Guidelines

- Never commit secrets, API keys, or credentials
- Use environment variables for sensitive configuration
- Check `.gitignore` before committing
- CI automatically runs security scans (Bandit + Safety)
- Fix all security warnings immediately

## 📚 Documentation Requirements

### Code Documentation
```python
def public_function(param: str) -> int:
    """Brief one-line description.

    More detailed explanation if needed. Describe what the
    function does, not how it does it.

    Args:
        param: Description of parameter

    Returns:
        Description of return value

    Raises:
        ValueError: When param is invalid
    """
```

### When to Update README.md
- Adding user-facing features
- Changing installation steps
- New CLI commands or options
- Modifying project structure
- Adding development requirements

## 🎓 Best Practices

### DRY (Don't Repeat Yourself)
```python
# ❌ Bad - duplicate logic
def process_user(name: str) -> str:
    return name.strip().lower().replace(" ", "_")

def process_product(name: str) -> str:
    return name.strip().lower().replace(" ", "_")

# ✅ Good - shared logic
def normalize_name(name: str) -> str:
    """Normalize name to lowercase with underscores."""
    return name.strip().lower().replace(" ", "_")

def process_user(name: str) -> str:
    return normalize_name(name)

def process_product(name: str) -> str:
    return normalize_name(name)
```

### Small, Focused Functions
```python
# ✅ Good - single responsibility
def read_file(path: str) -> str:
    """Read file contents."""
    with open(path) as f:
        return f.read()

def parse_config(content: str) -> dict[str, Any]:
    """Parse config from string."""
    return json.loads(content)

def load_config(path: str) -> dict[str, Any]:
    """Load and parse config file."""
    content = read_file(path)
    return parse_config(content)
```

### Explicit over Implicit
```python
# ❌ Implicit behavior
def process(data, flag=True):
    if flag:
        return data.upper()
    return data

# ✅ Explicit, testable
def uppercase(data: str) -> str:
    return data.upper()

def process(data: str, transform: bool = True) -> str:
    if transform:
        return uppercase(data)
    return data
```

## 🆘 Troubleshooting

### Tests Failing
```bash
# Run tests with verbose output
make test

# Run specific failing test
uv run pytest tests/test_file.py::test_name -vv

# Check coverage
make coverage
```

### Linting Errors
```bash
# Auto-fix formatting
make format

# Check what linter is failing
make lint

# Fix Ruff issues automatically
uv run ruff check --fix src tests
```

### Import Errors
```bash
# Reinstall package in editable mode
uv pip install -e .

# Check imports are correct (no 'src.' prefix)
uv run mypy src tests
```

## 📞 Platform-Specific Instructions

For platform-specific details, see:
- **Cursor**: `.cursorrules`
- **Claude**: `.claude/INSTRUCTIONS.md`
- **Gemini**: `GEMINI.md`
- **Aider**: `.aider.conf.yml`
- **Copilot**: `COPILOT_INSTRUCTIONS.md`

---

**Remember**: Write tests first, use real code, run `make check`, maintain quality. This discipline prevents bugs and saves time.
