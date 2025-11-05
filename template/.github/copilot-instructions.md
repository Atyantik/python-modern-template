# GitHub Copilot Repository Instructions

<!-- ⚠️  SYNC WARNING: Minimal essential content for Copilot -->
<!-- Last synced: 2025-11-05 -->
<!-- GitHub Copilot does NOT support file references (@AI_DOCS syntax) -->
<!-- This file contains only Copilot-specific TDD workflow guidance -->
<!-- For complete documentation, manually read: AI_DOCS/documentation-first-approach.md, AI_DOCS/tdd-workflow.md, AI_DOCS/ai-tools.md, AI_DOCS/code-conventions.md, AI_DOCS/project-context.md -->

## STOP! READ THIS FIRST - MANDATORY SESSION MANAGEMENT

**User MUST run this command BEFORE starting ANY work:**

```bash
uv run ai-start-task "Task description"
```

**If user has NOT run this command yet, STOP and remind them to run it NOW!**

This is NOT optional. Every Copilot session MUST start with `ai-start-task`.

**During work:**
```bash
uv run ai-log "Progress message"
uv run ai-update-plan "Completed item"

# Customize your plan (add task-specific steps, remove irrelevant items)
uv run ai-update-plan --add "Specific task for this feature" --phase "Phase 2"
uv run ai-update-plan --remove "Generic irrelevant item"
uv run ai-update-plan --rename "Generic item" --to "Specific detailed item"
```

**When finishing:**
```bash
uv run ai-finish-task --summary="What was accomplished"
```

See `AI_DOCS/ai-tools.md` for complete workflow and all ai-update-plan features.

---

## CRITICAL! DOCUMENTATION-FIRST APPROACH

**BEFORE implementing ANY task, research existing solutions!**

1. Check for MCP tools (mcp__docs__, mcp__context7__)
2. Fetch official documentation with WebFetch
3. Search for recent tutorials with WebSearch
4. Verify no built-in solution exists

**Never reinvent the wheel. Always check documentation first.**

See `AI_DOCS/documentation-first-approach.md` for complete guidelines.

---

## CRITICAL Code Conventions

**See `AI_DOCS/code-conventions.md` for complete standards including:**
- No decorative emojis in any output
- AI summaries go in `.ai-summary/` directory
- No AI co-authoring in git commits
- Type hints required on all functions
- Formatter harmony (Black and Ruff must agree)

---

## Overview

> **Primary configuration file for GitHub Copilot**
>
> This file (`.github/copilot-instructions.md`) is read by GitHub Copilot on every chat or agent request.
> It provides repository-wide instructions in natural language using Markdown format.

**Primary Directive:** ALWAYS write tests BEFORE implementation code (Test-Driven Development).
**Secondary Directive:** ALWAYS research documentation BEFORE writing any code.

## Shared Documentation

For complete guidelines, see these shared documents in the project:

- `AI_DOCS/ai-tools.md` - Session management (MANDATORY workflow)
- `AI_DOCS/documentation-first-approach.md` - Research before implementation (MANDATORY)
- `AI_DOCS/ai-skills.md` - Specialized skills and agents (manual workflows)
- `AI_DOCS/tdd-workflow.md` - TDD process and testing standards
- `AI_DOCS/code-conventions.md` - Code style and best practices
- `AI_DOCS/project-context.md` - Tech stack and architecture

**Note**: This file contains essential excerpts. For comprehensive details, read the files above.

**Skills Available**: See `AI_DOCS/ai-skills.md` for test-generator, coverage-analyzer, quality-fixer, tdd-reviewer, and quality-enforcer workflows.

## Quick Reference

| What | Requirement |
|------|-------------|
| **Documentation Research** | MANDATORY - Check MCP tools, fetch docs, search tutorials BEFORE coding |
| **Testing** | Write tests FIRST, TDD always |
| **Mocking** | Minimize - use real code when possible |
| **Coverage** | Minimum 80%, aim for 90%+ |
| **Quality** | Run `make check` before pushing |
| **Types** | Type hints required (mypy strict) |
| **Style** | Black (88 chars) + isort + Ruff + Pylint 10/10 |
| **Formatter Harmony** | Let Black shape layout; refactor patterns so Ruff agrees |

## TDD Workflow with Copilot

### When Copilot Suggests Code

Copilot will naturally suggest implementation code, but you should:

1. **Ignore implementation suggestions initially**
2. **Ask Copilot to suggest tests first**
3. **Write tests**
4. **Then accept implementation suggestions**

### Example Flow

**❌ Don't Do This:**
```python
# You start typing in src/python_modern_template/math_utils.py
def factorial(n):  # Copilot suggests implementation immediately
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**✅ Do This Instead:**
```python
# Start in tests/test_math_utils.py FIRST
def test_factorial_base_case() -> None:
    """Test factorial of 0."""
    result = factorial(0)
    assert result == 1

def test_factorial_positive() -> None:
    """Test factorial of positive number."""
    result = factorial(5)
    assert result == 120

# NOW go to src/python_modern_template/math_utils.py
def factorial(n: int) -> int:  # Now accept Copilot's implementation
    """Calculate factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## Using Copilot Comments for TDD

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
    result = reverse_string("")
    assert result == ""
```

## Keep Black and Ruff in Sync

- Prefer explicit code constructs that both formatters accept. For long
  assertion or log messages, assign the string to a local variable instead of
  relying on multi-line wrapping.
- After Copilot-generated changes, run `pre-commit run --files …` (or
  `make format`) before staging to verify formatter agreement.
- If the same lines keep getting reformatted, adjust the code rather than
  fighting the tools—clarify the intent so both Black and Ruff produce identical
  output.

## Minimize Mocks - Use Real Code

### ✅ Preferred (Real Code)
```python
from python_modern_template.processor import process_data

def test_process_data() -> None:
    """Test with real data."""
    real_input = "test string"
    result = process_data(real_input)
    assert result == expected_value
```

### ❌ Avoid Unless Necessary (Mocks)
```python
# Only mock external dependencies
from unittest.mock import patch

@patch('requests.get')  # OK - external API
def test_api_call(mock_get):
    ...

# Don't mock internal functions
@patch('python_modern_template.utils.helper')  # Bad - use real helper
```

**When to Mock:**
- HTTP requests (external APIs)
- Database connections
- File system writes
- Time/date operations (`datetime.now()`)
- Random number generation

**When NOT to Mock:**
- Internal project functions
- Pure functions
- Simple data transformations
- Business logic

See `AI_DOCS/tdd-workflow.md` for complete mocking guidelines.

## Quality Checks

### Before Any Commit

```bash
make check  # Run ALL quality checks
```

This runs:
1. `make format` - Black + isort formatting
2. `make lint` - Ruff + mypy + Pylint
3. `make test` - Full test suite with coverage

**Never commit if `make check` fails!**

### Coverage Requirements

- **Minimum**: 80% (enforced)
- **Target**: 90%+
- **Ideal**: 100% for new code

```bash
make coverage  # Check coverage
```

## Code Standards

### Type Hints (Required)

```python
# ✅ Correct
def process_data(input: str, count: int = 5) -> dict[str, int]:
    """Process the input data."""
    return {"result": len(input) * count}

# ❌ Wrong - no type hints
def process_data(input, count=5):
    return {"result": len(input) * count}
```

### Imports

```python
# ✅ Correct - import from package name
from python_modern_template import function_name

# ❌ Wrong - don't use src prefix
from src.python_modern_template import function_name
```

### Docstrings (Google Style)

```python
def public_function(param: str) -> int:
    """Brief one-line description.

    More detailed explanation if needed.

    Args:
        param: Description of parameter

    Returns:
        Description of return value

    Raises:
        ValueError: When param is invalid
    """
```

See `AI_DOCS/code-conventions.md` for complete code conventions.

## Project Structure

```
src/python_modern_template/  # Implementation code
tests/                           # Test files mirror src structure
AI_DOCS/                         # Shared AI documentation
  ├── tdd-workflow.md            # TDD process
  ├── ai-tools.md                # Session management
  ├── code-conventions.md        # Code standards
  └── project-context.md         # Architecture
```

See `AI_DOCS/project-context.md` for complete project architecture.

## Development Workflow

### Complete TDD Cycle

1. **Write failing test** for new feature/fix
2. **Run tests** to confirm they fail: `make test`
3. **Implement** minimal code to make test pass
4. **Run tests** again to confirm they pass
5. **Refactor** if needed
6. **Run make check** to ensure quality
7. **Commit** if all checks pass

### Example with Copilot

```bash
# 1. User describes feature: "Add email validation"

# 2. You (with Copilot): Open tests/test_validators.py
# Write test comments to guide Copilot:
# Test: validate_email should accept valid emails
# Test: validate_email should reject invalid emails

# 3. Let Copilot suggest test implementations

# 4. Run tests (should fail)
make test

# 5. Open src/python_modern_template/validators.py
# Let Copilot suggest implementation

# 6. Run tests (should pass)
make test

# 7. Run quality check
make check

# 8. Commit if all pass
git commit -m "Add email validation with tests"
```

## Quality Gates

Before committing code, ensure:

1. ✅ Tests written FIRST (TDD)
2. ✅ All tests pass (`make test`)
3. ✅ Coverage ≥ 80% (`make coverage`)
4. ✅ Formatted (Black + isort via `make format`)
5. ✅ Linted (Ruff + mypy + Pylint via `make lint`)
6. ✅ `make check` passes
7. ✅ Type hints everywhere
8. ✅ No duplicate code (DRY)

## Required Development Workflow

Follow this workflow for every code change:

1. Write tests first (TDD approach)
2. Use real code/data instead of mocks when possible
3. Run `make check` after every change
4. Add type hints to all functions
5. Maintain coverage above 80%
6. Use AI session tools (`ai-start-task`, `ai-finish-task`)

## Complete Documentation

For comprehensive guidelines:

1. **AI_DOCS/ai-tools.md** - Session management (MANDATORY)
2. **AI_DOCS/ai-skills.md** - Specialized skills and agents
3. **AI_DOCS/tdd-workflow.md** - TDD process with examples
4. **AI_DOCS/code-conventions.md** - Code standards
5. **AI_DOCS/project-context.md** - Architecture and tech stack
6. **AGENTS.md** - Universal AI agent instructions

## Copilot Chat Commands

```
/explain - Explain code
/fix - Suggest fixes
/tests - Generate test cases (use this often!)
/doc - Add documentation
```

**Always use `/tests` to generate tests BEFORE implementing features!**

---

**Remember**: Tests first, quality always. Use Copilot to accelerate TDD, not bypass it.

**⚠️  This file requires manual synchronization when AI_DOCS/ changes**
