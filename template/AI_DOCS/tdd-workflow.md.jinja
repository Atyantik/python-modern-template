# Test-Driven Development (TDD) Workflow

> **Shared documentation for all AI coding assistants**
>
> This file is referenced by multiple AI tool configurations. Changes here automatically apply to all tools that support file references.

## 🎯 Core Principle

**Tests MUST be written BEFORE implementation code. This is non-negotiable.**

## 📋 The TDD Cycle

```
1. Write failing test
2. Run test (confirm it fails)
3. Write minimal code to pass test
4. Run test (confirm it passes)
5. Refactor if needed
6. Run make check (all quality gates)
7. Commit
```

## 🔄 Step-by-Step TDD Process

### Step 1: Write the Test First

```python
# File: tests/test_calculator.py

def test_add_two_numbers() -> None:
    """Test that add function correctly sums two numbers."""
    result = add(2, 3)
    assert result == 5

def test_add_negative_numbers() -> None:
    """Test adding negative numbers."""
    result = add(-5, 3)
    assert result == -2

def test_add_zero() -> None:
    """Test adding zero."""
    result = add(10, 0)
    assert result == 10
```

### Step 2: Run Tests (They Should Fail)

```bash
make test
# Expected: ImportError or ModuleNotFoundError
# This confirms the test is actually testing something!
```

### Step 3: Implement Minimal Code

```python
# File: src/{{ package_name }}/calculator.py

def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b
```

### Step 4: Run Tests (Should Pass)

```bash
make test
# All tests should now pass
```

### Step 5: Refactor if Needed

```python
# If implementation can be improved, refactor now
# Then run tests again to ensure nothing broke
make test
```

### Step 6: Run All Quality Checks

```bash
make check
# This runs:
# - Format (Black + isort)
# - Lint (Ruff + mypy + Pylint)
# - Tests with coverage
```

### Step 7: Commit

```bash
git add .
git commit -m "Add calculator add function with tests"
```

## 🧪 Testing Best Practices

### Test Organization

```
tests/
├── __init__.py
├── conftest.py           # Shared fixtures (use sparingly)
├── test_main.py          # Tests for main.py
├── test_calculator.py    # Tests for calculator.py
└── integration/          # Integration tests (if needed)
    └── test_workflow.py
```

### Test Structure (Arrange-Act-Assert)

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

### Parametrized Tests

```python
import pytest

@pytest.mark.parametrize(
    "input,expected",
    [
        ("hello", 5),
        ("world", 5),
        ("", 0),
        ("a", 1),
    ],
)
def test_string_length(input: str, expected: int) -> None:
    """Test length calculation with various inputs."""
    assert len(input) == expected
```

### Test Markers

```python
@pytest.mark.slow  # For slow tests
@pytest.mark.integration  # For integration tests
@pytest.mark.unit  # For unit tests (default)
```

## 🚫 Minimize Mocks - Use Real Code

### ✅ Preferred Approach (Real Code)

```python
# Use real function from codebase
from {{ package_name }}.processor import process_data

def test_process_data() -> None:
    """Test with real data."""
    real_input = "test string"
    result = process_data(real_input)
    assert result == expected_value
```

### ❌ Avoid Unless Necessary (Over-Mocking)

```python
from unittest.mock import patch

# Only mock external dependencies
@patch('requests.get')  # OK - external API
def test_api_call(mock_get):
    ...

# Don't mock internal functions
@patch('{{ package_name }}.utils.helper')  # Bad - use real helper
def test_with_mock(mock_helper):
    ...
```

### When to Mock

**Only mock:**
- ✅ External API calls (HTTP requests)
- ✅ Database connections
- ✅ File system writes
- ✅ Time/date operations (`datetime.now()`)
- ✅ Random number generation
- ✅ Environment variables for testing different configs

**Do NOT mock:**
- ❌ Internal project functions
- ❌ Pure functions (deterministic output)
- ❌ Simple data transformations
- ❌ Business logic

## 📊 Coverage Requirements

- **Minimum**: 80% (enforced by pytest)
- **Target**: 90%+
- **Ideal**: 100% for new code

### Check Coverage

```bash
make coverage
# Review terminal output and htmlcov/index.html
```

### If Coverage is Low

Add tests for uncovered lines:

```python
def test_edge_case_branch() -> None:
    """Test the specific branch that wasn't covered."""
    # Test the specific condition
    result = function_under_test(edge_case_input)
    assert result == expected_for_edge_case
```

## ✅ Quality Gates (All Must Pass)

Before committing code, ensure:

1. ✅ **Tests written FIRST** (TDD)
2. ✅ **All tests pass**: `make test`
3. ✅ **Coverage ≥ 80%**: `make coverage`
4. ✅ **Formatted**: Black + isort via `make format`
5. ✅ **Linted**: Ruff, mypy, Pylint via `make lint`
6. ✅ **Pre-commit hooks pass**: `make pre-commit`
7. ✅ **Type hints everywhere**: mypy strict mode
8. ✅ **No security issues**: CI runs Bandit + Safety

## 🛠️ Development Commands

```bash
# Essential Commands
make test                 # Run tests
make coverage             # Run tests with coverage report
make format               # Format code (Black + isort)
make lint                 # Run linters (Ruff + mypy + Pylint)
make check                # ALL quality checks (format + lint + test)

# Running Specific Tests
uv run pytest tests/test_main.py -v
uv run pytest tests/test_main.py::test_specific_function -v
uv run pytest --cov=src --cov-report=term-missing
uv run pytest -m "not slow"  # Exclude slow tests
```

## 🎓 Complete TDD Example

**User Request:** "Add email validation feature"

### AI Implementation:

#### 1. Write Tests First
```python
# File: tests/test_validators.py

import pytest
from {{ package_name }}.validators import validate_email

class TestEmailValidation:
    """Test email validation."""

    @pytest.mark.parametrize(
        "email,expected",
        [
            ("test@example.com", True),
            ("user.name@domain.co.uk", True),
            ("invalid.email", False),
            ("@example.com", False),
            ("user@", False),
            ("", False),
        ],
    )
    def test_email_formats(self, email: str, expected: bool) -> None:
        """Test various email formats."""
        assert validate_email(email) == expected
```

#### 2. Run Tests (Fail)
```bash
make test
# ImportError: cannot import name 'validate_email'
# ✅ Good - test is actually testing something!
```

#### 3. Implement Function
```python
# File: src/{{ package_name }}/validators.py

import re

def validate_email(email: str) -> bool:
    """Validate an email address.

    Args:
        email: Email address to validate

    Returns:
        True if valid, False otherwise
    """
    if not email:
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

#### 4. Export from __init__.py
```python
# File: src/{{ package_name }}/__init__.py

from .validators import validate_email

__all__ = [..., "validate_email"]
```

#### 5. Run Tests (Pass)
```bash
make test
# ✅ All 6 parametrized tests pass
```

#### 6. Run Quality Checks
```bash
make check
# ✅ Format: PASS
# ✅ Lint: PASS (Pylint 10/10)
# ✅ Tests: PASS (coverage 100%)
```

#### 7. Report to User
"**Email validation implemented successfully:**
- ✅ Wrote 6 parametrized tests first (TDD)
- ✅ Tests failed initially (function didn't exist)
- ✅ Implemented validation function
- ✅ All tests now pass
- ✅ `make check` passes
- ✅ Handles multiple formats and edge cases
- ✅ Coverage: 100%"

## 🔒 Security in Testing

- Never commit test files with real secrets or credentials
- Use environment variables or fixtures for test credentials
- Mock external services that require authentication
- CI automatically runs security scans (Bandit + Safety)

## 📝 Test Documentation

```python
def test_function_behavior() -> None:
    """Test that function does X when given Y.

    This test ensures that edge case Z is handled correctly
    by verifying that the output matches expected format.
    """
    # Clear test implementation
```

## 🆘 Troubleshooting TDD

### Tests Failing After Implementation

```bash
# Run with verbose output
uv run pytest tests/test_file.py::test_name -vv

# Check for import errors
uv pip install -e .

# Verify test is testing the right thing
# Add print statements temporarily if needed
```

### Coverage Not Increasing

```bash
# See which lines aren't covered
make coverage
# Open htmlcov/index.html in browser
# Add tests specifically for uncovered branches
```

### Linting Errors After Tests Pass

```bash
# Auto-fix formatting
make format

# Fix Ruff issues automatically
uv run ruff check --fix src tests

# Check mypy errors
uv run mypy src tests
```

---

**Remember**: Tests first, always. This prevents bugs, documents intent, and saves time in the long run.
