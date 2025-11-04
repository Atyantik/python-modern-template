"""Tests for quality.format module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from scripts.quality.format import format_code, main


@patch("scripts.quality.format.subprocess.run")
@patch("scripts.quality.format.get_code_paths")
def test_format_code_runs_black_and_isort(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that format_code runs both black and isort."""
    mock_get_paths.return_value = ["src", "tests"]
    mock_run.return_value = MagicMock(returncode=0)

    result = format_code(check=False)

    assert result == 0
    assert mock_run.call_count == 2

    # Verify black was called
    black_call = mock_run.call_args_list[0]
    assert "black" in black_call[0][0]
    assert "src" in black_call[0][0]
    assert "tests" in black_call[0][0]

    # Verify isort was called
    isort_call = mock_run.call_args_list[1]
    assert "isort" in isort_call[0][0]
    assert "src" in isort_call[0][0]
    assert "tests" in isort_call[0][0]


@patch("scripts.quality.format.subprocess.run")
@patch("scripts.quality.format.get_code_paths")
def test_format_code_with_check_mode(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that format_code uses check mode when requested."""
    mock_get_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=0)

    result = format_code(check=True)

    assert result == 0

    # Verify black was called with --check
    black_call = mock_run.call_args_list[0]
    assert "--check" in black_call[0][0]

    # Verify isort was called with --check-only
    isort_call = mock_run.call_args_list[1]
    assert "--check-only" in isort_call[0][0]


@patch("scripts.quality.format.subprocess.run")
@patch("scripts.quality.format.get_code_paths")
def test_format_code_returns_nonzero_on_failure(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that format_code returns non-zero exit code on failure."""
    mock_get_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=1)

    result = format_code(check=False)

    assert result == 1


@patch("scripts.quality.format.subprocess.run")
@patch("scripts.quality.format.get_code_paths")
def test_format_code_stops_on_black_failure(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that format_code stops if black fails."""
    mock_get_paths.return_value = ["src"]
    # Black fails
    mock_run.return_value = MagicMock(returncode=1)

    result = format_code(check=False)

    # Should only call black, not isort
    assert mock_run.call_count == 1
    assert result == 1


@patch("scripts.quality.format.format_code")
@patch("sys.argv", ["format.py"])
def test_main_without_arguments(mock_format: MagicMock) -> None:
    """Test main function without arguments runs in format mode."""
    mock_format.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_format.assert_called_once_with(check=False)


@patch("scripts.quality.format.format_code")
@patch("sys.argv", ["format.py", "--check"])
def test_main_with_check_flag(mock_format: MagicMock) -> None:
    """Test main function with --check flag."""
    mock_format.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_format.assert_called_once_with(check=True)


@patch("scripts.quality.format.format_code")
@patch("sys.argv", ["format.py", "--check"])
def test_main_returns_format_code_exit_code(mock_format: MagicMock) -> None:
    """Test that main returns format_code's exit code."""
    mock_format.return_value = 42

    exit_code = main()

    assert exit_code == 42
