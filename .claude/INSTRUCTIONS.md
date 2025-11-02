# Claude Code Instructions

> Instructions specific to Claude Code (Anthropic's CLI coding assistant)

## Overview

You are Claude Code, working on a Python project with **strict Test-Driven Development (TDD)** and code quality standards. These instructions complement the universal guidelines in `AGENTS.md`.

## 🎯 Your Primary Directive

**ALWAYS write tests BEFORE implementation code. No exceptions.**

## Claude-Specific Workflow

### Before Writing Any Code

1. **Read the relevant files** to understand current implementation
2. **Check existing tests** in `tests/` directory for patterns
3. **Plan the test cases** needed for the new functionality
4. **Write failing tests FIRST**
5. **Run tests** to confirm they fail appropriately
6. **Implement** the minimal code to make tests pass
7. **Refactor** while keeping tests green
8. **Run `make check`** to ensure all quality gates pass

### Using Claude Code Tools

```bash
# Read files to understand context
Read: src/leadership_blog_generator/module.py
Read: tests/test_module.py

# Write tests FIRST
Edit: tests/test_module.py  # Add new test cases

# Run tests to see them fail
Bash: make test

# Write implementation
Edit: src/leadership_blog_generator/module.py

# Run tests to see them pass
Bash: make test

# Run all quality checks
Bash: make check

# If all pass, you can commit
```

## 🧪 Test-Driven Development with Claude

### Example TDD Session

**User Request:** "Add a function to calculate word count in a string"

**Your Response:**

1. **First, write the test:**
```python
# Edit tests/test_utils.py

def test_count_words_in_simple_sentence() -> None:
    """Test word counting in a simple sentence."""
    text = "Hello world from Python"
    result = count_words(text)
    assert result == 4

def test_count_words_with_multiple_spaces() -> None:
    """Test word counting handles multiple spaces."""
    text = "Hello    world"
    result = count_words(text)
    assert result == 2

def test_count_words_empty_string() -> None:
    """Test word counting on empty string."""
    result = count_words("")
    assert result == 0
```

2. **Run tests (they will fail - this is expected):**
```bash
Bash: make test
# Output shows: ModuleNotFoundError or NameError for count_words
```

3. **Implement the function:**
```python
# Edit src/leadership_blog_generator/utils.py

def count_words(text: str) -> int:
    """Count the number of words in text.

    Args:
        text: The input string

    Returns:
        Number of words in the text
    """
    if not text:
        return 0
    return len(text.split())
```

4. **Run tests again (they should pass):**
```bash
Bash: make test
# All tests pass
```

5. **Run quality checks:**
```bash
Bash: make check
# Formatting, linting, type checking, and tests all pass
```

6. **Communicate to user:**
"I've implemented the `count_words` function following TDD:
1. ✅ Wrote 3 test cases first
2. ✅ Tests initially failed (as expected)
3. ✅ Implemented the function
4. ✅ All tests now pass
5. ✅ `make check` passes (100% quality)

The function handles simple sentences, multiple spaces, and empty strings."

## 🚫 Anti-Patterns to Avoid

### DON'T Do This:
```python
# ❌ Writing implementation first
# Edit src/leadership_blog_generator/feature.py
def new_feature():
    # implementation here
    pass

# Then writing tests after
# Edit tests/test_feature.py
def test_new_feature():
    ...
```

### DO This Instead:
```python
# ✅ Write tests FIRST
# Edit tests/test_feature.py
def test_new_feature_basic_case() -> None:
    """Test basic functionality."""
    result = new_feature()
    assert result == expected

# Then implementation
# Edit src/leadership_blog_generator/feature.py
def new_feature() -> ExpectedType:
    """Implementation."""
    ...
```

## 🔍 Real Code Over Mocks

### When to Use Real Code (Preferred)

```python
# ✅ Test internal functions directly
from leadership_blog_generator.processor import process_data, validate_input

def test_process_with_validation() -> None:
    """Test processing with real validation function."""
    raw_data = "test input"

    # Use real validation function
    if validate_input(raw_data):
        result = process_data(raw_data)
        assert result is not None
```

### When to Mock (Only When Necessary)

```python
# ✅ Mock external dependencies
from unittest.mock import patch, Mock

@patch('requests.get')
def test_fetch_data_from_api(mock_get: Mock) -> None:
    """Test API fetching with mocked HTTP call."""
    mock_response = Mock()
    mock_response.json.return_value = {'key': 'value'}
    mock_get.return_value = mock_response

    result = fetch_data_from_api('https://example.com')
    assert result == {'key': 'value'}
```

**Mock only:**
- HTTP requests (requests.get, requests.post)
- Database calls (if not using test DB)
- File I/O that would be destructive
- Time-dependent code (datetime.now)
- Random values (random.randint)

## 📊 Coverage Requirements

### Check Coverage Before Finishing
```bash
Bash: make coverage
```

**Requirements:**
- **Minimum**: 80% (enforced)
- **Target**: 90%+
- **Ideal**: 100% for new code

### If Coverage is Low:
```python
# Identify uncovered lines from coverage report
# Add tests for those specific cases

def test_edge_case_not_covered() -> None:
    """Test the edge case that wasn't covered."""
    # Test the specific branch/condition
```

## 🔧 Using Make Commands

Claude Code has access to these commands via Bash tool:

```bash
# Before starting work
Bash: make help                    # See all commands

# Development cycle
Bash: make test                    # Run tests only
Bash: make coverage                # Tests with coverage report
Bash: make format                  # Auto-format code
Bash: make lint                    # Run all linters
Bash: make check                   # Complete quality check

# Use check before considering work done
Bash: make check
```

**Always run `make check` before telling the user the task is complete!**

## 🎯 Type Hints with Claude

### Every Function Needs Types

```python
# ✅ Claude should write
def process_items(
    items: list[str],
    filter_func: Callable[[str], bool] | None = None,
) -> dict[str, int]:
    """Process items and return counts.

    Args:
        items: List of items to process
        filter_func: Optional filter function

    Returns:
        Dictionary mapping items to their counts
    """
    ...
```

### Import Annotations
```python
from __future__ import annotations  # At top of file
from typing import Any, Callable
from collections.abc import Iterable
```

## 📝 Docstring Standards

### Functions (Public API)
```python
def public_function(param: str, count: int = 10) -> bool:
    """Brief one-line summary.

    Longer description if needed. Explain what the function does,
    not how it does it.

    Args:
        param: Description of parameter
        count: Number of iterations (default: 10)

    Returns:
        True if successful, False otherwise

    Raises:
        ValueError: If param is empty
    """
```

### Classes
```python
class DataProcessor:
    """Process data with configurable options.

    This class handles data processing with various transformation
    options and validation.

    Attributes:
        config: Configuration dictionary
        strict_mode: Whether to enforce strict validation
    """
```

## 🔄 Synchronizing AI Instructions

### When You Update Critical Functionality

If implementing major changes, update **ALL** these files:
1. `.cursorrules`
2. `AGENTS.md`
3. `.claude/INSTRUCTIONS.md` (this file)
4. `GEMINI.md`
5. `.aider.conf.yml`
6. `COPILOT_INSTRUCTIONS.md`

**How to update:**
```bash
# 1. Edit all instruction files
Edit: .cursorrules
Edit: AGENTS.md
Edit: .claude/INSTRUCTIONS.md
Edit: GEMINI.md
Edit: .aider.conf.yml
Edit: COPILOT_INSTRUCTIONS.md

# 2. Validate they're in sync
Bash: make validate-ai-docs
```

**Critical changes that need syncing:**
- New testing patterns
- Changed build/deploy process
- Security updates
- Architectural decisions
- New quality requirements

## 🚨 Quality Gates Checklist

Before completing any task, verify:

- [ ] Tests written BEFORE implementation
- [ ] Tests initially failed (confirmed TDD)
- [ ] Implementation makes tests pass
- [ ] Used real code instead of mocks (where possible)
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] `make test` passes
- [ ] Coverage ≥ 80% (`make coverage`)
- [ ] `make format` passes (Black + isort)
- [ ] `make lint` passes (Ruff + mypy + Pylint 10/10)
- [ ] `make check` passes (complete validation)
- [ ] No duplicate code (DRY principle)
- [ ] README updated (if user-facing changes)
- [ ] AI instructions synced (if critical changes)

## 💬 Communicating with Users

### When Starting a Task
"I'll implement [feature] using TDD. First, I'll write comprehensive tests, then implement the functionality to make them pass."

### While Working
"Writing tests first for [feature]... ✓
Running tests (they fail as expected)... ✓
Implementing [feature]... ✓
Tests now pass... ✓
Running make check... ✓"

### When Complete
"Implementation complete with TDD:
- ✅ 5 test cases written first
- ✅ All tests pass
- ✅ Coverage: 95%
- ✅ make check passes (all quality gates)
- ✅ Type hints and docstrings added"

### If Issues Found
"Found issues during `make check`:
- Pylint: Unused import on line 23
- Coverage: 78% (below 80% minimum)

Fixing issues... [explain what you're doing]
Re-running make check... ✓"

## 🔍 Example: Complete TDD Flow

**User:** "Add a function to validate email addresses"

**Claude's Response:**

"I'll implement email validation using TDD. Let me start by writing tests first."

```python
# Step 1: Write tests (Edit tests/test_validators.py)
import pytest
from leadership_blog_generator.validators import validate_email

class TestEmailValidation:
    """Test email validation functionality."""

    def test_valid_email(self) -> None:
        """Test that valid emails are accepted."""
        assert validate_email("user@example.com") is True

    def test_invalid_email_no_at(self) -> None:
        """Test that emails without @ are rejected."""
        assert validate_email("userexample.com") is False

    def test_invalid_email_no_domain(self) -> None:
        """Test that emails without domain are rejected."""
        assert validate_email("user@") is False

    @pytest.mark.parametrize(
        "email",
        [
            "test@domain.com",
            "user.name@example.co.uk",
            "user+tag@example.com",
        ],
    )
    def test_various_valid_formats(self, email: str) -> None:
        """Test various valid email formats."""
        assert validate_email(email) is True
```

```bash
# Step 2: Run tests - they fail
Bash: make test
# Output: ModuleNotFoundError: No module named 'leadership_blog_generator.validators'
```

"Tests are failing as expected (function doesn't exist yet). Now implementing..."

```python
# Step 3: Implement (Edit src/leadership_blog_generator/validators.py)
import re

def validate_email(email: str) -> bool:
    """Validate an email address.

    Args:
        email: Email address to validate

    Returns:
        True if email is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

```bash
# Step 4: Run tests - they pass
Bash: make test
# All tests pass!

# Step 5: Run complete quality check
Bash: make check
# Format ✓, Lint ✓, Tests ✓
```

"Email validation implemented successfully using TDD:
- ✅ 6 test cases written first
- ✅ Tests initially failed (confirmed TDD approach)
- ✅ Implementation makes all tests pass
- ✅ `make check` passes (100% quality)
- ✅ Handles various email formats and edge cases"

## 📚 Reference

For universal guidelines applicable to all AI agents, see:
- **AGENTS.md** - Complete universal instructions
- **.cursorrules** - Cursor IDE specific
- **GEMINI.md** - Google Gemini specific
- **.aider.conf.yml** - Aider specific
- **COPILOT_INSTRUCTIONS.md** - GitHub Copilot specific

---

**Remember:** As Claude Code, you excel at following systematic processes. Use TDD rigorously, run `make check` always, and maintain the highest code quality standards.
