"""Tests for ai-finish-task tool."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.ai_tools.finish_task import finish_task


def test_finish_task_with_yes_flag_bypasses_incomplete_plan_prompt(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test --yes flag bypasses prompt when plan is incomplete."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    # Create incomplete plan (0 items checked)
    plan_content = """# Task Plan: Test Task

## Phase 1: Setup
- [ ] Item 1
- [ ] Item 2
"""
    plan_file.write_text(plan_content)

    # Add minimal execution content
    execution_file.write_text("[2025-11-03 16:00:00] Started task\n")

    # Act & Assert - should NOT prompt and should complete successfully
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch(
            "builtins.input", side_effect=AssertionError("input() should not be called")
        ),
    ):
        # This should not raise AssertionError because input() shouldn't be called
        finish_task(summary="Test summary", session_id=None, yes=True)


def test_finish_task_with_yes_flag_bypasses_make_check_prompt(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test --yes flag bypasses prompt when make check not run."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    # Create complete plan
    plan_content = """# Task Plan: Test Task

## Phase 1: Setup
- [x] Item 1
- [x] Item 2
"""
    plan_file.write_text(plan_content)

    # Execution without 'make check'
    execution_file.write_text("[2025-11-03 16:00:00] Started task\n")

    # Act & Assert - should NOT prompt
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch(
            "builtins.input", side_effect=AssertionError("input() should not be called")
        ),
    ):
        finish_task(summary="Test summary", session_id=None, yes=True)


def test_finish_task_without_yes_flag_prompts_on_incomplete_plan(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test without --yes flag prompts user when plan incomplete."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    plan_content = """# Task Plan: Test Task

## Phase 1: Setup
- [ ] Item 1
"""
    plan_file.write_text(plan_content)
    execution_file.write_text("[2025-11-03 16:00:00] Started\n")

    # Act & Assert - should call input() and exit when user says 'n'
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("builtins.input", return_value="n"),
        pytest.raises(SystemExit) as exc_info,
    ):
        finish_task(summary="Test", session_id=None, yes=False)

    assert exc_info.value.code == 0


def test_finish_task_without_yes_flag_prompts_on_missing_make_check(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test without --yes flag prompts when make check missing."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    # Complete plan but no make check
    plan_content = """# Task Plan: Test Task

## Phase 1: Setup
- [x] Item 1
"""
    plan_file.write_text(plan_content)
    execution_file.write_text("[2025-11-03 16:00:00] Started\n")

    # Act & Assert
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("builtins.input", return_value="n"),
        pytest.raises(SystemExit) as exc_info,
    ):
        finish_task(summary="Test", session_id=None, yes=False)

    assert exc_info.value.code == 0


def test_finish_task_yes_defaults_to_false(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test yes parameter defaults to False for backward compatibility."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    plan_content = """# Task Plan: Test Task

## Phase 1: Setup
- [x] Item 1
"""
    plan_file.write_text(plan_content)

    # Add make check to execution
    execution_content = """[2025-11-03 16:00:00] Started task
[2025-11-03 16:01:00] Running make check
"""
    execution_file.write_text(execution_content)

    # Act - call without yes parameter (should default to False, but pass checks)
    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        # Should complete successfully without prompts since all checks pass
        finish_task(summary="Test summary", session_id=None)


def test_finish_task_extracts_task_name_correctly(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test task name is correctly extracted from PLAN file."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    plan_content = """# Task Plan: Add Email Validation Feature

**Session ID**: 20251102150000
**Created**: 2025-11-02 15:00:00

## Phase 1: Setup
- [x] Item 1
"""
    plan_file.write_text(plan_content)

    # Add make check to execution
    execution_content = """[2025-11-03 16:00:00] Started task
[2025-11-03 16:01:00] Running make check
"""
    execution_file.write_text(execution_content)

    # Act
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch(
            "scripts.ai_tools.utils.get_context_dir",
            return_value=temp_context_dir,
        ),
    ):
        finish_task(summary="Test summary", session_id=None, yes=True)

    # Assert - check LAST_SESSION_SUMMARY.md contains correct task name
    last_summary = (temp_context_dir / "LAST_SESSION_SUMMARY.md").read_text()
    assert "Add Email Validation Feature" in last_summary
    assert "Unknown Task" not in last_summary


def test_finish_task_handles_missing_task_name_with_filename_fallback(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test fallback to filename when task name cannot be extracted from PLAN."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    # Create PLAN with malformed header (no "# Task Plan:" line)
    plan_content = """Task Plan Add Email Validation

**Session ID**: 20251102150000

## Phase 1: Setup
- [x] Item 1
"""
    plan_file.write_text(plan_content)

    # Add make check to execution
    execution_content = """[2025-11-03 16:00:00] Started task
[2025-11-03 16:01:00] Running make check
"""
    execution_file.write_text(execution_content)

    # Act
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch(
            "scripts.ai_tools.utils.get_context_dir",
            return_value=temp_context_dir,
        ),
    ):
        finish_task(summary="Test summary", session_id=None, yes=True)

    # Assert - should use filename slug as fallback, not "Unknown Task"
    last_summary = (temp_context_dir / "LAST_SESSION_SUMMARY.md").read_text()
    # Should extract from filename: "20251102150000-PLAN-test-task.md"
    assert "test-task" in last_summary.lower() or "test task" in last_summary.lower()
    assert "Unknown Task" not in last_summary


def test_finish_task_handles_malformed_plan_header(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test handling of PLAN with completely malformed header."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    # Create PLAN with no recognizable header at all
    plan_content = """Random content here
No proper header

- [x] Item 1
"""
    plan_file.write_text(plan_content)

    # Add make check to execution
    execution_content = """[2025-11-03 16:00:00] Started task
[2025-11-03 16:01:00] Running make check
"""
    execution_file.write_text(execution_content)

    # Act
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch(
            "scripts.ai_tools.utils.get_context_dir",
            return_value=temp_context_dir,
        ),
    ):
        finish_task(summary="Test summary", session_id=None, yes=True)

    # Assert - should use filename fallback
    last_summary = (temp_context_dir / "LAST_SESSION_SUMMARY.md").read_text()
    # Should not say "Unknown Task" but rather extract from filename
    assert "Unknown Task" not in last_summary


def test_finish_task_reports_uncompleted_plan_items(
    temp_context_dir: Path,
    sample_session_files: dict[str, Path],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Test finish_task reports when plan items are checked but not mentioned in execution."""
    # Arrange
    plan_file = sample_session_files["plan"]
    execution_file = sample_session_files["execution"]

    # Create plan with checked items
    plan_content = """# Task Plan: Test Task

## Phase 1: Implementation
- [x] Write comprehensive tests in test_feature.py
- [x] Implement feature in src/feature.py
- [x] Run make check
"""
    plan_file.write_text(plan_content)

    # Execution log mentions only one item specifically
    execution_content = """[2025-11-03 16:00:00] Started task
[2025-11-03 16:01:00] Wrote tests in test_feature.py
[2025-11-03 16:02:00] make check passed
"""
    execution_file.write_text(execution_content)

    # Act
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch(
            "scripts.ai_tools.utils.get_context_dir",
            return_value=temp_context_dir,
        ),
    ):
        finish_task(summary="Test summary", session_id=None, yes=True)

    # Assert - should warn about unmentioned items
    captured = capsys.readouterr()
    # Check output contains warning about execution verification
    assert (
        "⚠" in captured.out
        or "warning" in captured.out.lower()
        or "not mentioned" in captured.out.lower()
    )
