# GitHub Copilot Instructions

> Instructions for GitHub Copilot when assisting with this Python project

## 🎯 Primary Directive

**Test-Driven Development (TDD) is mandatory. Always write tests before implementation code.**

## Quick Reference

| What | Requirement |
|------|-------------|
| **Testing** | Write tests FIRST, TDD always |
| **Mocking** | Minimize - use real code when possible |
| **Coverage** | Minimum 80%, aim for 90%+ |
| **Quality** | Run `make check` before pushing |
| **Types** | Type hints required (mypy strict) |
| **Style** | Black (88 chars) + isort + Ruff + Pylint 10/10 |

## 🧪 TDD Workflow with Copilot

### When Copilot Suggests Code

Copilot will naturally suggest implementation code, but you should:

1. **Ignore implementation suggestions initially**
2. **Ask Copilot to suggest tests first**
3. **Write tests**
4. **Then accept implementation suggestions**

### Example Flow

**❌ Don't Do This:**
```python
# You start typing in src/leadership_blog_generator/math_utils.py
def factorial(n):  # Copilot suggests implementation immediately
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**✅ Do This Instead:**
```python
# Start in tests/test_math_utils.py FIRST
def test_factorial_base_case():  # Write test first
    """Test factorial of 0."""
    result = factorial(0)
    assert result == 1

def test_factorial_positive():
    """Test factorial of positive number."""
    result = factorial(5)
    assert result == 120

# NOW go to src/leadership_blog_generator/math_utils.py
def factorial(n: int) -> int:  # Now accept Copilot's implementation
    """Calculate factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## 📝 Using Copilot Comments for TDD

Guide Copilot with comments to generate tests first:

```python
# Test: function should reverse a string
# Input: "hello"
# Expected: "olleh"
def test_reverse_string_basic() -> None:
    # Copilot will suggest the test body
    result = reverse_string("hello")
    assert result == "olleh"

# Test: function should handle empty strings
def test_reverse_string_empty() -> None:
    # Copilot suggests
    result = reverse_string("")
    assert result == ""
```

## 🚫 Rejecting Implementation-First Suggestions

When Copilot suggests implementation before tests:

```python
# In src/leadership_blog_generator/feature.py
def new_feature():  # Copilot suggests implementation
    # ⏸️ STOP - reject this suggestion
    # Go to tests/test_feature.py first
```

Press `Esc` to reject, then:
1. Open `tests/test_feature.py`
2. Write tests with Copilot's help
3. Return to implementation file
4. Accept Copilot's implementation suggestions

## 🎯 Type Hints with Copilot

Train Copilot to include type hints:

```python
# ✅ Good prompt for Copilot
def calculate_average(numbers: list[float]) -> float:
    # Copilot will suggest typed implementation
    """Calculate the average of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0.0

# ❌ Bad - no type hints
def calculate_average(numbers):
    # Copilot might suggest untyped code
```

## 🧩 Copilot Chat for TDD

Use Copilot Chat to explicitly request TDD:

```
@workspace Write tests for a function that validates email addresses.
The function should:
- Accept valid emails (user@example.com)
- Reject invalid emails (no @, no domain, etc.)
- Follow TDD: write tests first
- Use pytest
- Include type hints
- Minimize mocks
```

Copilot Chat Response:
```python
# tests/test_validators.py
import pytest
from leadership_blog_generator.validators import validate_email

def test_valid_email() -> None:
    """Test that valid email is accepted."""
    assert validate_email("user@example.com") is True

def test_invalid_email_no_at() -> None:
    """Test that email without @ is rejected."""
    assert validate_email("userexample.com") is False
```

## 💡 Copilot Inline Suggestions

### For Test Files (tests/test_*.py)

Start typing and guide Copilot:

```python
class TestDataProcessor:
    """Test data processing functionality."""

    def test_process_empty_data(self) -> None:
        """Test processing with empty data."""
        # Copilot suggests:
        result = process_data([])
        assert result == []

    def test_process_single_item(self) -> None:
        # Copilot continues pattern
```

### For Implementation Files

Only use after tests exist:

```python
# tests already written and failing
def process_data(items: list[str]) -> list[str]:
    """Process list of items."""
    # Copilot suggests implementation based on test expectations
```

## 🔍 Minimizing Mocks with Copilot

Guide Copilot to use real code:

```python
# ✅ Prompt Copilot for real code usage
from leadership_blog_generator.utils import validate_input, transform_data

def test_full_pipeline() -> None:
    """Test complete pipeline with real functions."""
    raw_data = "test input"
    # Copilot suggests using real functions
    validated = validate_input(raw_data)
    result = transform_data(validated)
    assert result is not None

# ❌ Copilot might suggest over-mocking
@patch('leadership_blog_generator.utils.validate_input')
def test_full_pipeline(mock_validate):
    # Unnecessary mocking of internal function
```

## 📊 Coverage-Driven Suggestions

Use comments to guide Copilot for coverage:

```python
# Test edge case: negative numbers
def test_factorial_negative() -> None:
    """Test that factorial raises error for negative numbers."""
    # Copilot suggests
    with pytest.raises(ValueError):
        factorial(-1)

# Test edge case: large numbers
def test_factorial_large() -> None:
    # Copilot continues
```

## 🎨 Code Quality with Copilot

### Docstrings

Copilot learns from existing patterns:

```python
def example_function(param: str) -> int:
    """Brief description.

    Args:
        param: Description of parameter

    Returns:
        Description of return value
    """
    # Copilot matches this style in new functions
```

### Formatting

Copilot respects your formatting config:

```python
# .editorconfig or pyproject.toml settings guide Copilot
# Copilot will suggest code matching Black (88 chars, double quotes)
```

## 🔄 Workflow Integration

### Before Accepting Copilot Suggestions

1. ✅ Are we in a test file? (Good - accept test suggestions)
2. ✅ Do tests exist for this function? (Good - accept implementation)
3. ❌ Are we writing implementation without tests? (Bad - write tests first)
4. ✅ Do suggestions include type hints? (Good)
5. ✅ Do suggestions follow project patterns? (Good)

### After Writing Code

Always run:
```bash
make check
```

If Copilot suggested code that fails checks:
1. Review the errors
2. Let Copilot suggest fixes
3. Run `make check` again
4. Repeat until clean

## 🎓 Training Copilot for This Project

### Establish Patterns Early

Write a few high-quality examples:

```python
# tests/test_example.py - Copilot learns from this
from typing import Any
import pytest
from leadership_blog_generator.example import example_function

class TestExampleFunction:
    """Test example functionality."""

    def test_basic_case(self) -> None:
        """Test basic functionality."""
        result = example_function("input")
        assert result == "expected"

    @pytest.mark.parametrize(
        "input,expected",
        [
            ("hello", "HELLO"),
            ("world", "WORLD"),
        ],
    )
    def test_various_inputs(self, input: str, expected: str) -> None:
        """Test with various inputs."""
        assert example_function(input) == expected
```

Copilot will suggest similar patterns for new tests.

### Use Descriptive Function Names

```python
# ✅ Copilot understands intent
def validate_email_format(email: str) -> bool:
    # Copilot suggests email validation logic

# ✅ Copilot suggests appropriate test
def test_validate_email_format_accepts_valid_emails() -> None:
    # Copilot knows what to test
```

## 🚦 Quality Checklist with Copilot

When Copilot suggests code, verify:

- [ ] Tests written first (TDD)
- [ ] Type hints included
- [ ] Docstrings present
- [ ] No unnecessary mocks
- [ ] Follows existing patterns
- [ ] Edge cases covered
- [ ] `make check` passes

## 🛠️ Commands Reference

```bash
# After Copilot suggestions
make check          # Run all quality checks

# Individual checks
make test           # Run tests
make coverage       # Check coverage
make format         # Auto-format code
make lint           # Run linters

# If checks fail
make format         # Fix formatting issues
# Review lint errors, let Copilot suggest fixes
make check          # Verify fixes
```

## 📚 Learning Resources for Copilot

Copilot learns from:
1. **AGENTS.md** - Universal TDD guidelines
2. **Existing tests** in `tests/` directory
3. **Project patterns** in `src/`
4. **pyproject.toml** - Quality tool configs
5. **This file** - Copilot-specific instructions

## 🔒 Security with Copilot

Copilot might suggest code with security issues:

```python
# ❌ Copilot might suggest
password = "hardcoded_password"  # Security issue!

# ✅ Guide Copilot with comments
# Use environment variable for password
import os
password = os.getenv("PASSWORD")
if not password:
    raise ValueError("PASSWORD environment variable not set")
```

Always review Copilot suggestions for:
- Hardcoded secrets
- SQL injection vulnerabilities
- XSS vulnerabilities
- Unsafe eval/exec usage

## 🎯 Advanced: Multi-File Copilot

When working across files, open:
1. Test file (`tests/test_feature.py`)
2. Implementation file (`src/leadership_blog_generator/feature.py`)
3. Related files for context

Copilot uses all open files for better suggestions.

### Example Multi-File Session

```python
# 1. Open tests/test_feature.py - write tests
def test_new_feature() -> None:
    """Test new feature."""
    result = new_feature("input")
    assert result == "expected"

# 2. Open src/leadership_blog_generator/feature.py
# Copilot sees the test and suggests matching implementation
def new_feature(input: str) -> str:
    """Implement new feature."""
    # Copilot suggests code that makes test pass
    return "expected" if input == "input" else ""

# 3. Return to test file
# Copilot suggests more test cases based on implementation
def test_new_feature_edge_case() -> None:
    """Test edge case."""
    result = new_feature("")
    assert result == ""
```

## ⚡ Quick Tips

1. **Comment your intent** - Copilot responds to clear comments
2. **Follow test patterns** - Copilot learns from existing tests
3. **Use type hints** - Copilot generates better typed code
4. **Run `make check` often** - Catch issues early
5. **Review suggestions** - Don't blindly accept
6. **Guide with examples** - Show Copilot what you want
7. **Stay in TDD flow** - Tests → Implementation → Refactor

## 📖 See Also

- **AGENTS.md** - Complete universal guidelines
- **.cursorrules** - Cursor-specific TDD instructions
- **.claude/INSTRUCTIONS.md** - Claude-specific examples
- **GEMINI.md** - Gemini-specific instructions
- **.aider.conf.yml** - Aider configuration

---

**Remember:** Copilot is a powerful tool, but YOU control the workflow. Always prioritize tests first, use real code over mocks, and run `make check` before pushing!
