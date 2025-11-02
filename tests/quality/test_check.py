"""Tests for quality.check module (orchestrator)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scripts.quality.check import main, run_all_checks


@patch("scripts.quality.check.format_code")
@patch("scripts.quality.check.lint_code")
@patch("scripts.quality.check.run_tests")
def test_run_all_checks_success(
    mock_tests: MagicMock, mock_lint: MagicMock, mock_format: MagicMock
) -> None:
    """Test that run_all_checks runs all steps when all succeed."""
    mock_format.return_value = 0
    mock_lint.return_value = 0
    mock_tests.return_value = 0

    result = run_all_checks()

    assert result == 0
    mock_format.assert_called_once_with(check=False)
    mock_lint.assert_called_once_with(fix=False)
    mock_tests.assert_called_once_with(coverage=True, verbose=False)


@patch("scripts.quality.check.format_code")
def test_run_all_checks_stops_on_format_failure(
    mock_format: MagicMock,
) -> None:
    """Test that run_all_checks stops if formatting fails."""
    mock_format.return_value = 1

    result = run_all_checks()

    assert result == 1
    # Only format should be called
    mock_format.assert_called_once()


@patch("scripts.quality.check.format_code")
@patch("scripts.quality.check.lint_code")
def test_run_all_checks_stops_on_lint_failure(
    mock_lint: MagicMock, mock_format: MagicMock
) -> None:
    """Test that run_all_checks stops if linting fails."""
    mock_format.return_value = 0
    mock_lint.return_value = 1

    result = run_all_checks()

    assert result == 1
    mock_format.assert_called_once()
    mock_lint.assert_called_once()


@patch("scripts.quality.check.format_code")
@patch("scripts.quality.check.lint_code")
@patch("scripts.quality.check.run_tests")
def test_run_all_checks_stops_on_test_failure(
    mock_tests: MagicMock, mock_lint: MagicMock, mock_format: MagicMock
) -> None:
    """Test that run_all_checks stops if tests fail."""
    mock_format.return_value = 0
    mock_lint.return_value = 0
    mock_tests.return_value = 1

    result = run_all_checks()

    assert result == 1
    mock_format.assert_called_once()
    mock_lint.assert_called_once()
    mock_tests.assert_called_once()


@patch("scripts.quality.check.format_code")
@patch("scripts.quality.check.lint_code")
@patch("scripts.quality.check.run_tests")
def test_run_all_checks_prints_summary_on_success(
    mock_tests: MagicMock,
    mock_lint: MagicMock,
    mock_format: MagicMock,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Test that run_all_checks prints success summary."""
    mock_format.return_value = 0
    mock_lint.return_value = 0
    mock_tests.return_value = 0

    result = run_all_checks()

    assert result == 0
    captured = capsys.readouterr()
    assert "✅" in captured.out or "All quality checks passed" in captured.out


@patch("scripts.quality.check.run_all_checks")
def test_main_calls_run_all_checks(mock_checks: MagicMock) -> None:
    """Test that main calls run_all_checks."""
    mock_checks.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_checks.assert_called_once()


@patch("scripts.quality.check.run_all_checks")
def test_main_returns_check_exit_code(mock_checks: MagicMock) -> None:
    """Test that main returns run_all_checks exit code."""
    mock_checks.return_value = 42

    exit_code = main()

    assert exit_code == 42
