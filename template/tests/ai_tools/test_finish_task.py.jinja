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
