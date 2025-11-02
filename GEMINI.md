# Gemini AI Instructions

> Instructions for Google Gemini when working on this Python project

## Quick Start

**Primary Rule:** Write tests BEFORE code. Use TDD (Test-Driven Development) always.

## 🎯 Your Core Responsibilities

1. **Test-Driven Development** - Write failing tests first
2. **Quality First** - Run `make check` before completing tasks
3. **Real Code Over Mocks** - Minimize test fixtures and mocks
4. **Type Safety** - Add type hints to all functions (mypy strict mode)
5. **Documentation Sync** - Update all AI instruction files for critical changes

## 📖 Complete Guidelines

See `AGENTS.md` for comprehensive universal instructions that apply to all AI agents.

## 🧪 Gemini-Specific TDD Workflow

### Step-by-Step Process

**User Request Example:** "Add a function to reverse a string"

### Your Implementation:

#### 1. First, Write the Test
```python
# File: tests/test_string_utils.py

from leadership_blog_generator.string_utils import reverse_string

def test_reverse_string_basic() -> None:
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty() -> None:
    """Test reversing empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_char() -> None:
    """Test reversing single character."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces() -> None:
    """Test reversing string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"
```

#### 2. Run Tests (They Will Fail)
```bash
make test
# Expected: ImportError or ModuleNotFoundError
```

#### 3. Implement the Function
```python
# File: src/leadership_blog_generator/string_utils.py

def reverse_string(text: str) -> str:
    """Reverse the given string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string
    """
    return text[::-1]
```

#### 4. Export from __init__.py
```python
# File: src/leadership_blog_generator/__init__.py

from .string_utils import reverse_string

__all__ = [..., "reverse_string"]
```

#### 5. Run Tests (Should Pass Now)
```bash
make test
# All tests should pass
```

#### 6. Run Quality Checks
```bash
make check
# This runs: format → lint → test
# All must pass!
```

#### 7. Report to User
"Implemented `reverse_string` using TDD:
- ✅ Wrote 4 test cases first
- ✅ Tests failed initially (function didn't exist)
- ✅ Implemented function
- ✅ All tests now pass
- ✅ `make check` passes with 100% quality
- ✅ Handles edge cases: empty strings, single chars, spaces"

## 🚫 Don't Mock Internal Code

### ❌ Bad Approach (Over-Mocking)
```python
from unittest.mock import patch

@patch('leadership_blog_generator.utils.helper_function')
def test_main_function(mock_helper):
    """Testing with unnecessary mock."""
    mock_helper.return_value = "mocked"
    result = main_function()
    assert result == "mocked"
```

### ✅ Good Approach (Use Real Code)
```python
from leadership_blog_generator.utils import helper_function
from leadership_blog_generator.main import main_function

def test_main_function() -> None:
    """Testing with real helper function."""
    # Use actual implementation
    result = main_function()
    # Test against real behavior
    assert isinstance(result, str)
    assert len(result) > 0
```

### When to Mock
Only mock:
- ✅ External APIs (HTTP requests)
- ✅ Database connections
- ✅ File system operations
- ✅ Current time/dates
- ✅ Random number generation
- ✅ Environment variables

## 🎨 Code Quality Standards

### Type Hints Required
```python
# ✅ Correct - all types specified
def process_data(
    input_str: str,
    options: dict[str, Any] | None = None,
    max_length: int = 100,
) -> list[str]:
    """Process input data with options."""
    ...

# ❌ Wrong - no type hints
def process_data(input_str, options=None, max_length=100):
    ...
```

### Formatting Standards
- **Line length**: 88 characters (Black)
- **Imports**: Sorted with isort
- **Quotes**: Double quotes preferred
- **Docstrings**: Google style

### Quality Checks
```bash
# Run before finishing ANY task
make check

# Individual checks
make format    # Black + isort
make lint      # Ruff + mypy + Pylint
make test      # Pytest with coverage
make coverage  # Detailed coverage report
```

## 📊 Coverage Requirements

- **Minimum**: 80% (enforced by pytest)
- **Target**: 90%+
- **Ideal**: 100% for new code

### Check Coverage
```bash
make coverage
# Review terminal output and htmlcov/index.html
```

### If Coverage Low
Add tests for uncovered lines:
```python
def test_edge_case_branch() -> None:
    """Test the specific branch that wasn't covered."""
    # Test the specific condition
    result = function_under_test(edge_case_input)
    assert result == expected_for_edge_case
```

## 🏗️ Project Structure

```
src/leadership_blog_generator/
  ├── __init__.py          # Package exports
  ├── main.py              # CLI implementation
  └── [modules].py         # Feature modules

tests/
  ├── conftest.py          # Shared fixtures (minimal use)
  ├── test_main.py         # Tests for main.py
  └── test_[module].py     # Tests for each module
```

### Import Pattern
```python
# ✅ Correct
from leadership_blog_generator import function_name

# ❌ Wrong
from src.leadership_blog_generator import function_name
```

## 🔄 Keeping Documentation in Sync

### When to Update All AI Instruction Files

Update these files together for critical changes:
- `.cursorrules`
- `AGENTS.md`
- `.claude/INSTRUCTIONS.md`
- `GEMINI.md` (this file)
- `.aider.conf.yml`
- `COPILOT_INSTRUCTIONS.md`

**Critical changes:**
- New testing patterns
- Build/deploy process changes
- Security requirements
- Architecture decisions
- Code quality rules

### Validation
```bash
make validate-ai-docs
```

## 🛠️ Available Commands

```bash
# Setup
make install           # Install deps + pre-commit hooks
uv pip install -e .    # Install package in editable mode

# Development
make test              # Run tests
make coverage          # Tests with coverage report
make format            # Auto-format (Black + isort)
make lint              # Lint (Ruff + mypy + Pylint)
make check             # Complete quality check ⭐

# Maintenance
make clean             # Remove generated files
make build             # Build distribution package

# Help
make help              # Show all commands
```

## ✅ Pre-Commit Checklist

Before saying "task complete", verify:

- [ ] Wrote tests FIRST (TDD)
- [ ] Tests initially failed
- [ ] Implementation makes tests pass
- [ ] Used real code (not mocks) where possible
- [ ] Type hints on all functions
- [ ] Docstrings on public functions
- [ ] `make test` passes
- [ ] Coverage ≥ 80%
- [ ] `make check` passes
- [ ] No duplicate code (DRY)
- [ ] README updated (if needed)
- [ ] AI docs synced (if critical change)

## 🔒 Security

- Never commit secrets/credentials
- Use environment variables for config
- CI runs Bandit + Safety automatically
- Fix security warnings immediately

## 💡 Best Practices for Gemini

### Small, Focused Commits
Each feature should:
1. Have tests written first
2. Implement minimal code to pass tests
3. Pass all quality checks
4. Be a logical unit of work

### Communicate Clearly
```markdown
**Implementing [Feature] with TDD:**

1. ✅ Writing tests first...
   - test_basic_case
   - test_edge_case_1
   - test_edge_case_2

2. ✅ Tests fail (as expected - function doesn't exist)

3. ✅ Implementing function...

4. ✅ Tests now pass

5. ✅ Running make check...
   - Format: PASS
   - Lint: PASS
   - Tests: PASS (95% coverage)

**Task complete!** All quality gates passed.
```

### Handle Errors Gracefully
If `make check` fails:
```markdown
**Issue found during quality check:**
- Pylint: Unused variable on line 45
- Coverage: 78% (below 80% minimum)

**Fixing:**
1. Removed unused variable
2. Added tests for uncovered branch

**Re-running make check:** ✅ All pass
```

## 🎓 Example Complete Flow

**User:** "Add validation for phone numbers"

**Gemini Response:**

"I'll implement phone number validation using TDD. Writing tests first..."

```python
# Step 1: tests/test_validators.py
import pytest
from leadership_blog_generator.validators import validate_phone

class TestPhoneValidation:
    """Test phone number validation."""

    @pytest.mark.parametrize(
        "phone,expected",
        [
            ("123-456-7890", True),
            ("(123) 456-7890", True),
            ("1234567890", True),
            ("123-456-789", False),  # Too short
            ("abc-def-ghij", False),  # Non-numeric
            ("", False),  # Empty
        ],
    )
    def test_phone_formats(self, phone: str, expected: bool) -> None:
        """Test various phone number formats."""
        assert validate_phone(phone) == expected
```

"Running tests - they fail as expected..."
```bash
make test
# ImportError: cannot import name 'validate_phone'
```

"Implementing function..."
```python
# src/leadership_blog_generator/validators.py
import re

def validate_phone(phone: str) -> bool:
    """Validate a US phone number.

    Args:
        phone: Phone number to validate

    Returns:
        True if valid, False otherwise
    """
    # Remove formatting characters
    digits = re.sub(r'[^0-9]', '', phone)

    # Check if exactly 10 digits
    return len(digits) == 10
```

"Running tests..."
```bash
make test
# ✅ All 6 tests pass
```

"Running complete quality check..."
```bash
make check
# ✅ Format: PASS
# ✅ Lint: PASS (Pylint 10/10)
# ✅ Tests: PASS (coverage 92%)
```

"**Phone validation implemented successfully:**
- ✅ Wrote 6 parametrized tests first (TDD)
- ✅ Tests failed initially
- ✅ Implemented validation function
- ✅ All tests pass
- ✅ `make check` passes
- ✅ Handles multiple formats and edge cases
- ✅ Coverage: 92%"

## 📚 Additional Resources

- **Universal guidelines**: `AGENTS.md`
- **Cursor-specific**: `.cursorrules`
- **Claude-specific**: `.claude/INSTRUCTIONS.md`
- **Aider-specific**: `.aider.conf.yml`
- **Copilot-specific**: `COPILOT_INSTRUCTIONS.md`

---

**Remember, Gemini:** Tests first, quality always, real code over mocks. Run `make check` before completing any task!
