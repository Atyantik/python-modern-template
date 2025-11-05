# CLAUDE.md - Claude Code Configuration

## STOP! READ THIS FIRST - MANDATORY SESSION MANAGEMENT

**BEFORE doing ANYTHING in this session, you MUST run:**

```bash
Bash: uv run ai-start-task "Your task description"
```

**If you have NOT run this command yet, STOP NOW and run it!**

This is NOT optional. Every session MUST start with `ai-start-task`.

**During work:**
```bash
Bash: uv run ai-log "Progress message"
Bash: uv run ai-update-plan "Completed item"

# Customize your plan (add task-specific steps, remove irrelevant items)
Bash: uv run ai-update-plan --add "Specific task for this feature" --phase "Phase 2"
Bash: uv run ai-update-plan --remove "Generic irrelevant item"
Bash: uv run ai-update-plan --rename "Generic item" --to "Specific detailed item"
```

**When finishing:**
```bash
Bash: uv run ai-finish-task --summary="What you accomplished"
```

See `@AI_DOCS/ai-tools.md` for complete workflow and all ai-update-plan features.

---

## CRITICAL! DOCUMENTATION-FIRST APPROACH

**BEFORE implementing ANY task, you MUST research existing solutions and documentation!**

This is NOT optional. You MUST:

1. **Check for MCP Tools First**
   - Look for `mcp__docs__`, `mcp__context7__`, or framework-specific MCP tools
   - Use them to fetch latest documentation

2. **Fetch Official Documentation**
   - Use WebFetch from official docs (docs.framework.com)
   - Search for built-in tools and features
   - Read API references and getting started guides

3. **Search for Recent Tutorials**
   - Use WebSearch for 2024-2025 tutorials and examples
   - Look for official framework tutorials
   - Find existing integration patterns

4. **Verify No Built-In Solution Exists**
   - Check if framework provides the functionality
   - Look for official integrations
   - Confirm custom code is actually needed

**Why This Matters:**

❌ **DON'T** reinvent the wheel:
- Don't reverse-engineer documentation sites
- Don't manually implement APIs when SDK exists
- Don't create custom code when built-in tools are available
- Don't over-engineer simple tasks

✅ **DO** discover and use existing solutions:
- Use MCP tools to fetch documentation
- Read official framework docs
- Leverage built-in tools and integrations
- Follow framework best practices

**Example:** If asked to "create an Agno app to fetch HackerNews stories":
1. ✅ Use MCP to fetch Agno documentation
2. ✅ Discover Agno has built-in `hackernews_tools`
3. ✅ Use the built-in tools instead of custom API calls
4. ❌ Don't view page source or reverse-engineer APIs

See `@AI_DOCS/documentation-first-approach.md` for complete guidelines and examples.

---

## Overview

You are Claude Code, working on a Python project with strict Test-Driven Development (TDD) and code quality standards.

**Primary Directive:** ALWAYS write tests BEFORE implementation code.
**Secondary Directive:** ALWAYS research documentation BEFORE writing any code.

## Shared Documentation

Reference these for complete guidelines:

- `@AI_DOCS/ai-tools.md` - Session management workflow (MANDATORY)
- `@AI_DOCS/documentation-first-approach.md` - Research before implementation (MANDATORY)
- `@AI_DOCS/ai-skills.md` - Specialized skills and agents (use via Skill/Task tools)
- `@AI_DOCS/tdd-workflow.md` - TDD process and testing standards
- `@AI_DOCS/code-conventions.md` - Code style and best practices
- `@AI_DOCS/project-context.md` - Tech stack and architecture
- `@AI_DOCS/documentation-sync-rules.md` - AI doc synchronization (MANDATORY)

## Claude-Specific Workflow

### Before Writing Any Code

**Phase 0: Documentation Discovery (MANDATORY FIRST STEP)**
1. Check for MCP tools (`mcp__docs__`, `mcp__context7__`, etc.)
2. Use WebFetch to get official documentation from framework
3. Use WebSearch for recent tutorials and examples (2024-2025)
4. Verify no built-in tools/features exist for the task
5. Document research findings before proceeding

**Phase 1: TDD Preparation**
6. Read relevant files to understand current implementation
7. Check existing tests in `tests/` directory
8. Plan test cases needed (based on discovered patterns)

**Phase 2: TDD Implementation**
9. **Write failing tests FIRST**
10. Run tests to confirm they fail
11. Implement minimal code to make tests pass (using discovered tools/patterns)
12. Refactor while keeping tests green
13. Run `make check` to ensure all quality gates pass

### Using Claude Code Tools

```bash
# Read files
Read: src/python_modern_template/module.py
Read: tests/test_module.py

# Write tests FIRST
Edit: tests/test_module.py

# Run tests to see them fail
Bash: make test

# Write implementation
Edit: src/python_modern_template/module.py

# Run tests to see them pass
Bash: make test

# Run all quality checks
Bash: make check
```

## TDD Example

**User Request:** "Add a function to calculate word count"

**Your Response:**

1. Write test first:
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

2. Run tests (they will fail):
```bash
Bash: make test
# Output: ModuleNotFoundError or NameError for count_words
```

3. Implement the function:
```python
# Edit src/python_modern_template/utils.py
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

4. Run tests again (should pass):
```bash
Bash: make test
```

5. Run quality checks:
```bash
Bash: make check
```

6. Communicate to user:
"Implemented `count_words` function following TDD:
- Wrote 3 test cases first
- Tests initially failed (as expected)
- Implemented the function
- All tests now pass
- `make check` passes (100% quality)"

## Required Pattern: Tests First

Write tests before implementation:
```python
# Step 1: Write the test
def test_new_feature_basic_case() -> None:
    """Test basic functionality."""
    result = new_feature()
    assert result == expected

# Step 2: Write the implementation
def new_feature():
    # implementation here
    pass
```

## Real Code Over Mocks

**Prefer real code:**
```python
from python_modern_template.processor import process_data, validate_input

def test_process_with_validation() -> None:
    """Test with real validation function."""
    raw_data = "test input"
    if validate_input(raw_data):
        result = process_data(raw_data)
        assert result is not None
```

**Mock only when necessary:**
```python
from unittest.mock import patch, Mock

@patch('requests.get')
def test_fetch_data_from_api(mock_get: Mock) -> None:
    """Test API with mocked HTTP call."""
    mock_response = Mock()
    mock_response.json.return_value = {'key': 'value'}
    mock_get.return_value = mock_response
    result = fetch_data_from_api('https://example.com')
    assert result == {'key': 'value'}
```

**Mock only:** HTTP requests, database calls, file I/O, time operations, random values

See `@AI_DOCS/tdd-workflow.md` for complete mocking guidelines.

## Coverage Requirements

```bash
Bash: make coverage
```

**Requirements:**
- Minimum: 80% (enforced)
- Target: 90%+
- Ideal: 100% for new code

See `@AI_DOCS/tdd-workflow.md` for coverage guidelines.

## Make Commands

```bash
Bash: make help                    # See all commands
Bash: make test                    # Run tests only
Bash: make coverage                # Tests with coverage report
Bash: make format                  # Auto-format code
Bash: make lint                    # Run all linters
Bash: make check                   # Complete quality check
```

**Always run `make check` before telling user task is complete!**

See `@AI_DOCS/project-context.md` for complete development workflow.

## Type Hints

Every function needs types:

```python
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

Import annotations:
```python
from __future__ import annotations
from typing import Any, Callable
from collections.abc import Iterable
```

See `@AI_DOCS/code-conventions.md` for complete conventions.

## Docstring Standards

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

See `@AI_DOCS/code-conventions.md` for complete documentation standards.

## Quality Gates Checklist

Before completing any task:

- [ ] **Documentation research completed** (MANDATORY)
  - [ ] Checked for MCP tools and used them
  - [ ] Fetched official framework documentation
  - [ ] Searched for recent tutorials and examples
  - [ ] Verified no built-in solution exists
  - [ ] Documented research findings
- [ ] Tests written BEFORE implementation
- [ ] Tests initially failed (confirmed TDD)
- [ ] Implementation makes tests pass
- [ ] Used real code instead of mocks (where possible)
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] `make test` passes
- [ ] Coverage ≥ 80%
- [ ] `make format` passes
- [ ] `make lint` passes
- [ ] `make check` passes
- [ ] No duplicate code (DRY)
- [ ] README updated (if user-facing changes)
- [ ] Formatter harmony check (Black vs Ruff) — adjust code (e.g., use message variables)
      if tools disagree
- [ ] **AI documentation synchronized** (MANDATORY)
  - [ ] Run `uv run ai-validate-docs`
  - [ ] Update `.gemini/styleguide.md` if AI_DOCS changed (add sync date)
  - [ ] Update `.github/copilot-instructions.md` if AI_DOCS changed (add sync date)
  - [ ] Update `.claude/skills/` or `.claude/agents/` if relevant
  - [ ] Update `template/AI_DOCS/` if changes should apply to new projects
  - [ ] See `@AI_DOCS/documentation-sync-rules.md` for complete workflow

## Communication Style

**When starting:**
"I'll implement [feature] using TDD. First, I'll write comprehensive tests, then implement the functionality."

**While working:**
"Writing tests first for [feature]...
Running tests (they fail as expected)...
Implementing [feature]...
Tests now pass...
Running make check..."

**When complete:**
"Implementation complete with TDD:
- 5 test cases written first
- All tests pass
- Coverage: 95%
- make check passes
- Type hints and docstrings added"

**If issues found:**
"Found issues during `make check`:
- Pylint: Unused import on line 23
- Coverage: 78% (below 80% minimum)

Fixing issues...
Re-running make check..."

## Specialized Skills and Agents

**You have access to specialized skills and agents via the Skill and Task tools:**

See `@AI_DOCS/ai-skills.md` for complete documentation on:
- `Skill: test-generator` - Generate test boilerplate
- `Skill: coverage-analyzer` - Analyze coverage gaps
- `Skill: quality-fixer` - Apply automated fixes
- `Skill: session-template` - Load task templates
- `Task: tdd-reviewer` - Review TDD compliance
- `Task: quality-enforcer` - Enforce quality gates

**Use these proactively!** Don't wait for user to request them.

## Reference

**Shared documentation:**
- `@AI_DOCS/ai-tools.md` - Session management workflow
- `@AI_DOCS/documentation-first-approach.md` - Research before implementation (MANDATORY)
- `@AI_DOCS/ai-skills.md` - Specialized skills and agents
- `@AI_DOCS/tdd-workflow.md` - TDD process, testing standards, coverage
- `@AI_DOCS/code-conventions.md` - Code style, formatting, best practices
- `@AI_DOCS/project-context.md` - Tech stack, architecture, dependencies

**Tool-specific:**
- `AGENTS.md` - Universal instructions
- `.cursorrules` - Cursor IDE
- `.gemini/styleguide.md` - Gemini
- `.aider.conf.yml` - Aider
- `.github/copilot-instructions.md` - GitHub Copilot

---

**Remember:** Use TDD rigorously, run `make check` always, maintain highest code quality standards.
