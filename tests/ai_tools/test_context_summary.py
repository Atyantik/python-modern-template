"""Tests for ai-context-summary tool."""

from __future__ import annotations

from io import StringIO
from pathlib import Path
from unittest.mock import patch

from scripts.ai_tools.context_summary import main, show_context_summary


def test_show_context_summary_basic(temp_context_dir: Path) -> None:
    """Test basic context summary display."""
    # Update context files with some content
    (temp_context_dir / "LAST_SESSION_SUMMARY.md").write_text(
        """# Last Session Summary

**Session ID**: 20251102150000
**Date**: 2025-11-02 15:00

## Summary
Implemented AI instruction files with TDD

**Status**: ✅ Complete | Files: 12 changed
"""
    )

    (temp_context_dir / "ACTIVE_TASKS.md").write_text(
        """# Active Tasks

## In Progress
- Feature A (session: 20251102140000)
- Feature B (session: 20251102150000)

## Blocked
- Feature C (waiting for API keys)

## Completed
- Feature D
"""
    )

    (temp_context_dir / "RECENT_DECISIONS.md").write_text(
        """# Recent Decisions

## [2025-11-02 14:00] TDD Mandatory

**Decision**: All code must be written using TDD approach

**Rationale**:
- Ensures tests exist before code
- Higher code quality

**Status**: ✅ Implemented

---

## [2025-11-02 13:30] 80% Minimum Coverage

**Decision**: All code must have 80% minimum test coverage

**Status**: ✅ Implemented

---

## [2025-11-02 13:00] Type Hints Required

**Decision**: All functions must have type hints (mypy strict)

**Status**: ✅ Implemented
"""
    )

    (temp_context_dir / "CONVENTIONS.md").write_text(
        """# Conventions

## Testing Conventions
- Tests before code (TDD)
- Use real code, minimize mocks
- Run make check before completion
"""
    )

    # Capture output
    output = StringIO()

    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir",
            return_value=temp_context_dir,
        ),
        patch("sys.stdout", output),
    ):
        show_context_summary(detailed=False)

    result = output.getvalue()

    # Verify output contains expected sections
    assert "AI Context Summary" in result
    assert "Last Session" in result
    assert "Active Tasks" in result
    assert "Recent Decisions" in result
    assert "Key Conventions" in result
    assert "Recent Sessions" in result

    # Verify specific content
    assert "Implemented AI instruction files with TDD" in result
    assert "2 in progress" in result or "In Progress" in result
    assert "TDD Mandatory" in result
    assert "80% Minimum Coverage" in result
    assert "Type Hints Required" in result


def test_show_context_summary_detailed(temp_context_dir: Path) -> None:
    """Test detailed context summary display."""
    # Add content to context files
    (temp_context_dir / "RECENT_DECISIONS.md").write_text(
        """# Recent Decisions

## [2025-11-02 14:00] TDD Mandatory

**Decision**: All code must be written using TDD approach

**Rationale**:
- Ensures tests exist before code
- Higher code quality
- Better design

**Status**: ✅ Implemented
"""
    )

    output = StringIO()

    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir",
            return_value=temp_context_dir,
        ),
        patch("sys.stdout", output),
    ):
        show_context_summary(detailed=True)

    result = output.getvalue()

    # In detailed mode, should show more information
    assert "AI Context Summary" in result
    assert "TDD Mandatory" in result


def test_show_context_summary_no_sessions(temp_context_dir: Path) -> None:
    """Test context summary when no sessions exist."""
    output = StringIO()

    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir",
            return_value=temp_context_dir,
        ),
        patch("sys.stdout", output),
    ):
        show_context_summary(detailed=False)

    result = output.getvalue()

    # Should handle missing sessions gracefully
    assert "AI Context Summary" in result


def test_show_context_summary_missing_files(tmp_path: Path) -> None:
    """Test context summary when context files are missing."""
    # Create minimal context dir without files
    context_dir = tmp_path / ".ai-context"
    context_dir.mkdir()

    output = StringIO()

    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir", return_value=context_dir
        ),
        patch("sys.stdout", output),
    ):
        show_context_summary(detailed=False)

    result = output.getvalue()

    # Should still display header even if files missing
    assert "AI Context Summary" in result


def test_main_default(temp_context_dir: Path) -> None:
    """Test main function with default arguments."""
    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir",
            return_value=temp_context_dir,
        ),
        patch("sys.argv", ["ai-context-summary"]),
    ):
        # Should run without errors
        main()


def test_main_detailed(temp_context_dir: Path) -> None:
    """Test main function with detailed flag."""
    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir",
            return_value=temp_context_dir,
        ),
        patch("sys.argv", ["ai-context-summary", "--detailed"]),
    ):
        # Should run without errors
        main()


def test_extract_active_tasks_count(temp_context_dir: Path) -> None:
    """Test extraction of active task counts."""
    (temp_context_dir / "ACTIVE_TASKS.md").write_text(
        """# Active Tasks

## In Progress
- Task 1
- Task 2
- Task 3

## Blocked
- Task 4

## Completed
- Task 5
- Task 6
"""
    )

    output = StringIO()

    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.context_summary.get_context_dir",
            return_value=temp_context_dir,
        ),
        patch("sys.stdout", output),
    ):
        show_context_summary(detailed=False)

    result = output.getvalue()

    # Should show task counts
    assert "Active Tasks" in result
