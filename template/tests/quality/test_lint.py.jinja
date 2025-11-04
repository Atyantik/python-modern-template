"""Tests for quality.lint module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from scripts.quality.lint import lint_code, main


@patch("scripts.quality.lint.subprocess.run")
@patch("scripts.quality.lint.get_code_paths")
def test_lint_code_runs_all_linters(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that lint_code runs ruff, mypy, and pylint."""
    mock_get_paths.return_value = ["src", "tests"]
    mock_run.return_value = MagicMock(returncode=0)

    result = lint_code(fix=False)

    assert result == 0
    assert mock_run.call_count == 3

    # Verify ruff was called
    ruff_call = mock_run.call_args_list[0]
    assert "ruff" in ruff_call[0][0]
    assert "check" in ruff_call[0][0]
    assert "src" in ruff_call[0][0]
    assert "tests" in ruff_call[0][0]

    # Verify mypy was called
    mypy_call = mock_run.call_args_list[1]
    assert "mypy" in mypy_call[0][0]
    assert "src" in mypy_call[0][0]
    assert "tests" in mypy_call[0][0]

    # Verify pylint was called
    pylint_call = mock_run.call_args_list[2]
    assert "pylint" in pylint_call[0][0]
    assert "src" in pylint_call[0][0]
    assert "tests" in pylint_call[0][0]


@patch("scripts.quality.lint.subprocess.run")
@patch("scripts.quality.lint.get_code_paths")
def test_lint_code_with_fix_mode(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that lint_code uses fix mode when requested."""
    mock_get_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=0)

    result = lint_code(fix=True)

    assert result == 0

    # Verify ruff was called with --fix
    ruff_call = mock_run.call_args_list[0]
    assert "--fix" in ruff_call[0][0]


@patch("scripts.quality.lint.subprocess.run")
@patch("scripts.quality.lint.get_code_paths")
def test_lint_code_without_fix_mode(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that lint_code doesn't auto-fix by default."""
    mock_get_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=0)

    result = lint_code(fix=False)

    assert result == 0

    # Verify ruff was NOT called with --fix
    ruff_call = mock_run.call_args_list[0]
    assert "--fix" not in ruff_call[0][0]


@patch("scripts.quality.lint.subprocess.run")
@patch("scripts.quality.lint.get_code_paths")
def test_lint_code_returns_nonzero_on_failure(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that lint_code returns non-zero exit code on failure."""
    mock_get_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=1)

    result = lint_code(fix=False)

    assert result == 1


@patch("scripts.quality.lint.subprocess.run")
@patch("scripts.quality.lint.get_code_paths")
def test_lint_code_stops_on_ruff_failure(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that lint_code stops if ruff fails."""
    mock_get_paths.return_value = ["src"]
    # Ruff fails
    mock_run.return_value = MagicMock(returncode=1)

    result = lint_code(fix=False)

    # Should only call ruff, not mypy or pylint
    assert mock_run.call_count == 1
    assert result == 1


@patch("scripts.quality.lint.subprocess.run")
@patch("scripts.quality.lint.get_code_paths")
def test_lint_code_continues_through_all_on_success(
    mock_get_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that all linters run when each succeeds."""
    mock_get_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=0)

    result = lint_code(fix=False)

    # Should call all three linters
    assert mock_run.call_count == 3
    assert result == 0


@patch("scripts.quality.lint.lint_code")
@patch("sys.argv", ["lint.py"])
def test_main_without_arguments(mock_lint: MagicMock) -> None:
    """Test main function without arguments runs without fix mode."""
    mock_lint.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_lint.assert_called_once_with(fix=False)


@patch("scripts.quality.lint.lint_code")
@patch("sys.argv", ["lint.py", "--fix"])
def test_main_with_fix_flag(mock_lint: MagicMock) -> None:
    """Test main function with --fix flag."""
    mock_lint.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_lint.assert_called_once_with(fix=True)
