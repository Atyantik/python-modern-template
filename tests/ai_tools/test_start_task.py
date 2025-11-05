"""Tests for ai-start-task tool."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.ai_tools.start_task import (
    add_task_to_active,
    start_task,
)


def test_add_task_to_active_updates_file_immediately(temp_context_dir: Path) -> None:
    """Test ACTIVE_TASKS.md is updated immediately when task is added."""
    # Arrange
    active_tasks_file = temp_context_dir / "ACTIVE_TASKS.md"
    initial_content = """# Active Tasks

## In Progress

## Blocked

## Completed

"""
    active_tasks_file.write_text(initial_content)

    # Act
    with patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir):
        add_task_to_active("Test task name", "20251105120000")

    # Assert - file should be updated immediately
    updated_content = active_tasks_file.read_text()
    assert "Test task name" in updated_content
    assert "20251105120000" in updated_content
    assert "## In Progress" in updated_content


def test_add_task_to_active_creates_file_if_missing(temp_context_dir: Path) -> None:
    """Test ACTIVE_TASKS.md is created if it doesn't exist."""
    # Arrange
    active_tasks_file = temp_context_dir / "ACTIVE_TASKS.md"
    # Delete the file if it exists
    if active_tasks_file.exists():
        active_tasks_file.unlink()

    # Act
    with patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir):
        add_task_to_active("New task", "20251105120001")

    # Assert
    assert active_tasks_file.exists()
    content = active_tasks_file.read_text()
    assert "New task" in content
    assert "20251105120001" in content


def test_add_task_to_active_adds_to_correct_section(temp_context_dir: Path) -> None:
    """Test task is added to 'In Progress' section specifically."""
    # Arrange
    active_tasks_file = temp_context_dir / "ACTIVE_TASKS.md"
    initial_content = """# Active Tasks

## In Progress

## Blocked

- Some blocked task

## Completed

- Some completed task
"""
    active_tasks_file.write_text(initial_content)

    # Act
    with patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir):
        add_task_to_active("New active task", "20251105120002")

    # Assert - new task should be in "In Progress", not in other sections
    updated_content = active_tasks_file.read_text()
    lines = updated_content.split("\n")

    # Find the line with our new task
    task_line_idx = -1
    for i, line in enumerate(lines):
        if "New active task" in line and "20251105120002" in line:
            task_line_idx = i
            break

    assert task_line_idx > 0, "Task not found in ACTIVE_TASKS.md"

    # Find which section it's in
    section = None
    for i in range(task_line_idx, -1, -1):
        if lines[i].startswith("## "):
            section = lines[i]
            break

    assert (
        section == "## In Progress"
    ), f"Task not in 'In Progress' section, found in: {section}"


def test_start_task_updates_active_tasks_immediately(temp_context_dir: Path) -> None:
    """Test start_task function updates ACTIVE_TASKS.md immediately."""
    # Arrange
    active_tasks_file = temp_context_dir / "ACTIVE_TASKS.md"

    # Act
    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("scripts.ai_tools.start_task.check_conflicts"),
    ):
        start_task("Implement feature X", task_type="feature")

    # Assert - ACTIVE_TASKS.md should be updated immediately
    assert active_tasks_file.exists()
    content = active_tasks_file.read_text()
    assert "Implement feature X" in content
    # Check that session ID is included (format: YYYYMMDDHHMMSS)
    assert any(char.isdigit() for char in content)


def test_start_task_provides_confirmation_message(
    temp_context_dir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test start_task prints confirmation that files were created."""
    # Arrange & Act
    with (
        patch("scripts.ai_tools.utils.get_context_dir", return_value=temp_context_dir),
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("scripts.ai_tools.start_task.check_conflicts"),
    ):
        start_task("Test task", task_type="feature")

    # Assert - output should mention session files created
    captured = capsys.readouterr()
    assert "Session Files Created" in captured.out or "PLAN" in captured.out
