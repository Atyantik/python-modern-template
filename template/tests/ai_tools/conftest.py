"""Shared fixtures for AI tools tests."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def temp_context_dir(tmp_path: Path) -> Path:
    """Create temporary .ai-context directory.

    Args:
        tmp_path: Pytest temporary path fixture

    Returns:
        Path to temporary .ai-context directory
    """
    context_dir = tmp_path / ".ai-context"
    context_dir.mkdir()
    (context_dir / "sessions").mkdir()
    (context_dir / "sessions" / "archive").mkdir()

    # Create basic context files
    (context_dir / "LAST_SESSION_SUMMARY.md").write_text(
        "# Last Session Summary\n\nNo sessions yet.\n"
    )
    (context_dir / "ACTIVE_TASKS.md").write_text(
        "# Active Tasks\n\n## In Progress\n\n## Blocked\n\n## Completed\n\n"
    )
    (context_dir / "RECENT_DECISIONS.md").write_text("# Recent Decisions\n\n")
    (context_dir / "CONVENTIONS.md").write_text("# Conventions\n\n")

    return context_dir


@pytest.fixture
def sample_session_files(temp_context_dir: Path) -> dict[str, Path]:
    """Create sample session files for testing.

    Args:
        temp_context_dir: Temporary context directory

    Returns:
        Dictionary with keys 'plan', 'summary', 'execution' and Path values
    """
    session_id = "20251102150000"
    slug = "test-task"

    plan_file = temp_context_dir / "sessions" / f"{session_id}-PLAN-{slug}.md"
    summary_file = temp_context_dir / "sessions" / f"{session_id}-SUMMARY-{slug}.md"
    execution_file = temp_context_dir / "sessions" / f"{session_id}-EXECUTION-{slug}.md"

    # Write sample content
    plan_file.write_text(
        """# Task Plan: Test Task

**Session ID**: 20251102150000
**Created**: 2025-11-02 15:00:00
**Task Type**: feature
**Status**: 🚧 In Progress

---

## Implementation Steps

### Phase 1: Write Tests (TDD)
- [ ] Identify test cases
- [ ] Write test file(s)
- [ ] Run tests to confirm they fail

### Phase 2: Implementation
- [ ] Implement functionality
- [ ] Run tests to confirm they pass
"""
    )

    summary_file.write_text(
        """# Task Summary: Test Task

**Session ID**: 20251102150000
**Created**: 2025-11-02 15:00:00
**Status**: 🚧 In Progress

---

## What Was Done

[To be filled at end of session]
"""
    )

    execution_file.write_text(
        """# Execution Log: Test Task

**Session ID**: 20251102150000
**Started**: 2025-11-02 15:00:00

---

## Log

[2025-11-02 15:00:00] 🎯 Task started: Test Task
[2025-11-02 15:00:00] 📚 Context loaded successfully
[2025-11-02 15:00:00] ✅ Session files created
"""
    )

    return {
        "plan": plan_file,
        "summary": summary_file,
        "execution": execution_file,
    }
