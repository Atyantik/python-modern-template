"""Tests for ai-log tool."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.ai_tools.log_execution import (
    check_log_specificity,
    log_execution,
    main,
)


def test_log_execution_basic(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test basic log execution."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("Created test file", level="info")

    # Read the execution file
    content = execution_file.read_text()

    # Verify log was appended
    assert "📝 Created test file" in content


def test_log_execution_warning(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test log execution with warning level."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("Found an issue", level="warning")

    content = execution_file.read_text()
    assert "⚠️  Found an issue" in content


def test_log_execution_error(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test log execution with error level."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("Test failed", level="error")

    content = execution_file.read_text()
    assert "❌ Test failed" in content


def test_log_execution_success(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test log execution with success level."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("All tests passing", level="success")

    content = execution_file.read_text()
    assert "✅ All tests passing" in content


def test_log_execution_specific_session(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test log execution with specific session ID."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("Test message", session_id="20251102150000")

    content = execution_file.read_text()
    assert "📝 Test message" in content


def test_log_execution_no_session(temp_context_dir: Path) -> None:
    """Test log execution when no session exists."""
    sessions_dir = temp_context_dir / "sessions"

    with (
        patch("scripts.ai_tools.utils.get_sessions_dir", return_value=sessions_dir),
        pytest.raises(SystemExit),
    ):
        log_execution("Test message")


def test_log_execution_preserves_existing(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test that logging preserves existing content."""
    execution_file = sample_session_files["execution"]
    original_content = execution_file.read_text()

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("New log entry")

    new_content = execution_file.read_text()

    # Original content should be preserved
    assert original_content in new_content
    # New entry should be added
    assert "New log entry" in new_content


def test_log_execution_timestamp_format(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test that log entries include timestamp."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("Test with timestamp")

    content = execution_file.read_text()

    # Should have timestamp format [YYYY-MM-DD HH:MM:SS]
    import re

    pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"
    assert re.search(pattern, content)


def test_main_basic(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test main function with basic message."""
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("sys.argv", ["ai-log", "Test message"]),
    ):
        main()

    execution_file = sample_session_files["execution"]
    content = execution_file.read_text()
    assert "Test message" in content


def test_main_with_level(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test main function with log level."""
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("sys.argv", ["ai-log", "Warning message", "--level", "warning"]),
    ):
        main()

    execution_file = sample_session_files["execution"]
    content = execution_file.read_text()
    assert "⚠️  Warning message" in content


def test_main_with_session_id(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test main function with specific session ID."""
    with (
        patch(
            "scripts.ai_tools.utils.get_sessions_dir",
            return_value=temp_context_dir / "sessions",
        ),
        patch("sys.argv", ["ai-log", "Test", "--session-id", "20251102150000"]),
    ):
        main()

    execution_file = sample_session_files["execution"]
    content = execution_file.read_text()
    assert "Test" in content


def test_multiple_logs_chronological(
    temp_context_dir: Path, sample_session_files: dict[str, Path]
) -> None:
    """Test multiple logs appear in chronological order."""
    execution_file = sample_session_files["execution"]

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=temp_context_dir / "sessions",
    ):
        log_execution("First log")
        log_execution("Second log")
        log_execution("Third log")

    content = execution_file.read_text()

    # All logs should be present
    assert "First log" in content
    assert "Second log" in content
    assert "Third log" in content

    # They should appear in order
    first_pos = content.find("First log")
    second_pos = content.find("Second log")
    third_pos = content.find("Third log")

    assert first_pos < second_pos < third_pos


def test_check_log_specificity_vague_write_test() -> None:
    """Test specificity checker detects vague 'write test' messages."""
    suggestions = check_log_specificity("write test for feature")
    assert len(suggestions) > 0
    assert "test file" in suggestions[0].lower()


def test_check_log_specificity_specific_write_test() -> None:
    """Test specificity checker accepts specific test file mentions."""
    suggestions = check_log_specificity("Wrote tests in tests/test_feature.py")
    assert len(suggestions) == 0


def test_check_log_specificity_vague_update_file() -> None:
    """Test specificity checker detects vague 'update file' messages."""
    suggestions = check_log_specificity("update file with new code")
    assert len(suggestions) > 0
    assert "which file" in suggestions[0].lower()


def test_check_log_specificity_specific_update_file() -> None:
    """Test specificity checker accepts specific file mentions."""
    suggestions = check_log_specificity("Updated src/module.py with validation")
    assert len(suggestions) == 0


def test_check_log_specificity_vague_fix_bug() -> None:
    """Test specificity checker detects vague 'fix bug' messages."""
    suggestions = check_log_specificity("fix bug in code")
    assert len(suggestions) > 0


def test_check_log_specificity_specific_fix_bug() -> None:
    """Test specificity checker accepts specific bug fixes."""
    suggestions = check_log_specificity(
        "Fixed validation bug in src/auth.py:validate_email()"
    )
    assert len(suggestions) == 0


def test_log_execution_shows_specificity_tip_for_vague_message(
    temp_context_dir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test that vague log messages trigger specificity tips."""
    # Create a sample session first
    session_id = "20251102150000"
    sessions_dir = temp_context_dir / "sessions"
    execution_file = sessions_dir / f"{session_id}-EXECUTION-test.md"
    execution_file.write_text("# Execution Log\n")

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=sessions_dir,
    ):
        log_execution("write test for feature", session_id=session_id)

    captured = capsys.readouterr()
    assert "💡" in captured.out or "Tip" in captured.out


def test_log_execution_no_tip_for_specific_message(
    temp_context_dir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test that specific log messages don't trigger tips."""
    # Create a sample session first
    session_id = "20251102150000"
    sessions_dir = temp_context_dir / "sessions"
    execution_file = sessions_dir / f"{session_id}-EXECUTION-test.md"
    execution_file.write_text("# Execution Log\n")

    with patch(
        "scripts.ai_tools.utils.get_sessions_dir",
        return_value=sessions_dir,
    ):
        log_execution(
            "Wrote comprehensive tests in tests/ai_tools/test_feature.py",
            session_id=session_id,
        )

    captured = capsys.readouterr()
    # Should not contain specificity tip
    assert "💡" not in captured.out or "test file" not in captured.out.lower()
