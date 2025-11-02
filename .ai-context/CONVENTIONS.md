# Project Conventions

> **Purpose**: Document project-specific patterns, naming conventions, and standards

**Follow these conventions for consistency across the codebase**

---

## File Naming Conventions

### Python Files
- **Modules**: `snake_case.py` (e.g., `email_validator.py`)
- **Tests**: `test_*.py` mirroring `src/` structure (e.g., `test_email_validator.py`)
- **Packages**: `snake_case/` directories with `__init__.py`

### Session Files
- **Format**: `YYYYMMDDHHMMSS-TYPE-slug.md`
- **Types**: PLAN, SUMMARY, EXECUTION
- **Slug**: lowercase, hyphens, max 50 chars
- **Example**: `20251102150000-PLAN-add-email-validation.md`

### Documentation
- **Markdown**: `SCREAMING_CASE.md` for important docs (e.g., `README.md`, `CONTRIBUTING.md`)
- **lowercase**: For less critical docs (e.g., `changelog.md`)

---

## Code Naming Conventions

### Functions & Variables
```python
# snake_case for functions and variables
def calculate_total_price(items: list[Item]) -> Decimal:
    total_amount = sum(item.price for item in items)
    return total_amount
```

### Classes
```python
# PascalCase for classes
class EmailValidator:
    pass

class UserAuthentication:
    pass
```

### Constants
```python
# SCREAMING_SNAKE_CASE for constants
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"
```

### Private Members
```python
# Leading underscore for private
class MyClass:
    def __init__(self):
        self._private_var = "internal"

    def _private_method(self):
        pass
```

---

## Import Conventions

### Import Order (enforced by isort)
```python
# 1. Standard library
import os
import sys
from datetime import datetime

# 2. Third-party packages
import pytest
import requests

# 3. Local package imports
from leadership_blog_generator import generate_blog
from leadership_blog_generator.validators import validate_email
```

### Import Style
```python
# ✅ Correct - import from package name
from leadership_blog_generator import function_name
from leadership_blog_generator.module import ClassName

# ❌ Wrong - don't use src prefix
from src.leadership_blog_generator import function_name
```

### Avoid Wildcard Imports
```python
# ❌ Wrong
from module import *

# ✅ Correct
from module import specific_function, SpecificClass
```

---

## Type Hint Conventions

### Always Use Type Hints
```python
from __future__ import annotations  # At top of file

def process_data(
    input_data: str,
    options: dict[str, Any] | None = None,
    max_length: int = 100,
) -> list[str]:
    """Process input data with options."""
    ...
```

### Common Patterns
```python
# Optional values
def get_user(user_id: int) -> User | None:
    ...

# Multiple return types
def parse_value(val: str) -> int | float | str:
    ...

# Collections
def get_items() -> list[str]:
    ...

def get_mapping() -> dict[str, int]:
    ...

# Callables
from collections.abc import Callable

def apply_func(func: Callable[[int], str]) -> str:
    ...
```

---

## Docstring Conventions

### Google Style Docstrings
```python
def calculate_price(
    quantity: int,
    unit_price: Decimal,
    discount: Decimal | None = None,
) -> Decimal:
    """Calculate total price with optional discount.

    Longer description if needed. Explain what the function does,
    not how it does it.

    Args:
        quantity: Number of items
        unit_price: Price per unit
        discount: Optional discount as decimal (e.g., 0.1 for 10%)

    Returns:
        Total price after applying discount

    Raises:
        ValueError: If quantity is negative or unit_price is zero
    """
    ...
```

### Module Docstrings
```python
"""Email validation utilities.

This module provides functions for validating email addresses
using industry-standard patterns.
"""
```

### Class Docstrings
```python
class DataProcessor:
    """Process and transform data with configurable options.

    This class handles data processing with various transformation
    options and validation.

    Attributes:
        config: Configuration dictionary
        strict_mode: Whether to enforce strict validation
    """
```

---

## Test Conventions

### Test Structure (Arrange-Act-Assert)
```python
def test_calculate_price_with_discount() -> None:
    """Test price calculation with discount applied."""
    # Arrange
    quantity = 5
    unit_price = Decimal("10.00")
    discount = Decimal("0.1")  # 10%

    # Act
    result = calculate_price(quantity, unit_price, discount)

    # Assert
    assert result == Decimal("45.00")
```

### Test Organization
```python
class TestEmailValidation:
    """Group related tests in a class."""

    def test_valid_email(self) -> None:
        """Test that valid emails are accepted."""
        ...

    def test_invalid_email_no_at(self) -> None:
        """Test that emails without @ are rejected."""
        ...
```

### Parametrized Tests
```python
@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@example.com", True),
        ("invalid.email", False),
        ("@example.com", False),
    ],
)
def test_email_validation(email: str, expected: bool) -> None:
    """Test email validation with various inputs."""
    assert validate_email(email) == expected
```

### Test Markers
```python
@pytest.mark.slow  # For slow tests
@pytest.mark.integration  # For integration tests
@pytest.mark.unit  # For unit tests (default)
def test_something():
    ...
```

---

## File Organization

### Project Structure
```
src/leadership_blog_generator/
├── __init__.py              # Package exports & version
├── main.py                  # CLI and main functionality
├── validators.py            # Validation functions
└── utils.py                 # Utility functions

tests/
├── __init__.py
├── conftest.py              # Shared fixtures
├── test_main.py             # Tests for main.py
├── test_validators.py       # Tests for validators.py
└── test_utils.py            # Tests for utils.py
```

### Test Files Mirror Source
```
src/leadership_blog_generator/validators.py
→ tests/test_validators.py

src/leadership_blog_generator/utils/helpers.py
→ tests/utils/test_helpers.py
```

---

## Code Style

### Line Length
- **Maximum**: 88 characters (Black default)
- **Comments**: Try to keep under 72 characters

### Indentation
- **Use**: 4 spaces (not tabs)
- **Continuation**: Align with opening delimiter

```python
# ✅ Correct
result = some_function(
    first_argument,
    second_argument,
    third_argument,
)

# ✅ Also correct
result = some_function(
    first_arg, second_arg,
    third_arg, fourth_arg,
)
```

### String Quotes
- **Preferred**: Double quotes `"`
- **Docstrings**: Triple double quotes `"""`
- **Exceptions**: Single quotes `'` when string contains double quotes

---

## Error Handling

### Raise Specific Exceptions
```python
# ✅ Correct
if quantity < 0:
    raise ValueError("Quantity must be non-negative")

# ❌ Wrong
if quantity < 0:
    raise Exception("Bad quantity")
```

### Use Custom Exceptions When Appropriate
```python
class ValidationError(Exception):
    """Raised when validation fails."""

def validate_email(email: str) -> None:
    if "@" not in email:
        raise ValidationError(f"Invalid email: {email}")
```

---

## Configuration

### Use pyproject.toml
- All tool configurations in `pyproject.toml`
- No separate config files (`.pylintrc`, etc.)

### Environment Variables
```python
import os

# ✅ Correct - with default
API_KEY = os.getenv("API_KEY", "default-dev-key")

# ✅ Correct - required
API_KEY = os.environ["API_KEY"]  # Raises if not set

# ❌ Wrong - hardcoded
API_KEY = "my-secret-key"
```

---

## Git Conventions

### Commit Messages
```
Add email validation with tests

- Implement validate_email function
- Add parametrized tests for various formats
- Update documentation

Fixes #123
```

### Branch Names
- **Feature**: `feature/short-description`
- **Bug Fix**: `fix/issue-description`
- **Hotfix**: `hotfix/critical-issue`

---

## AI Session Conventions

### Before Starting Task
1. Read `.ai-context/REQUIRED_READING.md`
2. Read context files (LAST_SESSION_SUMMARY, etc.)
3. Create session files: `make new-session --name="task"`
4. Fill out PLAN file

### During Task
1. Follow TDD (tests first)
2. Log to EXECUTION file
3. Update PLAN checkboxes
4. Run `make check` frequently

### After Completing Task
1. Finalize SUMMARY file
2. Update LAST_SESSION_SUMMARY.md
3. Update ACTIVE_TASKS.md
4. Add to RECENT_DECISIONS.md (if applicable)
5. Add to CONVENTIONS.md (if new pattern)
6. Archive old sessions: `make archive-sessions`

---

## Decision-Making Conventions

### When to Update Context Files

**Update RECENT_DECISIONS.md when**:
- Choosing architecture or design pattern
- Selecting technology or library
- Establishing new standard or rule
- Making breaking changes

**Update CONVENTIONS.md when**:
- Establishing naming pattern
- Defining code structure
- Creating reusable pattern
- Setting formatting rule

**Update LAST_SESSION_SUMMARY.md always**:
- At end of every AI session
- Include what was done
- Include decisions made
- Include next steps

---

## Quality Standards

### All Code Must
- ✅ Have tests written first (TDD)
- ✅ Have type hints (mypy strict)
- ✅ Pass `make check` (format + lint + test)
- ✅ Maintain 80%+ coverage
- ✅ Follow conventions in this file
- ✅ Have docstrings for public API

### All Tests Must
- ✅ Use real code (minimize mocks)
- ✅ Follow Arrange-Act-Assert pattern
- ✅ Have descriptive names
- ✅ Test one thing clearly
- ✅ Be fast (mark slow tests with @pytest.mark.slow)

---

**Last Updated**: 2025-11-02 15:00:00
**Updated By**: Claude Code

**How to Use**:
1. Read before starting any task
2. Follow these patterns consistently
3. Add new conventions when establishing patterns
4. Update when conventions change
5. Reference in code reviews

**Note**: This file is committed to git so everyone follows the same patterns.
