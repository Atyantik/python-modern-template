"""Tests for ai-update-plan tool."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.ai_tools.update_plan import (
    count_checkboxes,
    find_checkbox_line,
    toggle_checkbox,
    update_plan,
)


def test_find_checkbox_line() -> None:
    """Test finding checkbox line by text."""
    content = """# Plan
- [ ] Task one
- [ ] Write test file
- [x] Already done
"""
    result = find_checkbox_line(content, "Write test")
    assert result is not None
    line_num, line = result
    assert "Write test file" in line


def test_toggle_checkbox_check() -> None:
    """Test checking a checkbox."""
    line = "- [ ] Task to do"
    result = toggle_checkbox(line, check=True)
    assert result == "- [x] Task to do"


def test_toggle_checkbox_uncheck() -> None:
    """Test unchecking a checkbox."""
    line = "- [x] Done task"
    result = toggle_checkbox(line, check=False)
    assert result == "- [ ] Done task"


def test_count_checkboxes() -> None:
    """Test counting checkboxes."""
    content = """# Plan
- [ ] Task one
- [x] Task two
- [x] Task three
- [ ] Task four
"""
    checked, total = count_checkboxes(content)
    assert total == 4
    assert checked == 2


def test_update_plan_check_item(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test checking a plan item."""
    plan_file = sample_session_files["plan"]

    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("scripts.ai_tools.update_plan.log_execution"),  # Mock to avoid errors
    ):
        update_plan("Identify test cases")

    content = plan_file.read_text()
    assert "- [x] Identify test cases" in content


def test_update_plan_show(
    temp_context_dir: Path,
    sample_session_files: dict[str, Path],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Test showing current plan."""
    _ = sample_session_files  # Use the fixture to create files
    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        update_plan(show=True)

    captured = capsys.readouterr()
    assert "Plan for session" in captured.out
    assert "Progress:" in captured.out


def test_update_plan_no_session(temp_context_dir: Path) -> None:
    """Test update plan when no session exists."""
    sessions_dir = temp_context_dir / "sessions"

    with (
        patch("scripts.ai_tools.utils.get_sessions_dir", return_value=sessions_dir),
        pytest.raises(SystemExit),
    ):
        update_plan("Some item")
