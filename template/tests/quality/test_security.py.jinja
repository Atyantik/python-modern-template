"""Tests for quality.security module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from scripts.quality.security import main, run_security_checks


@patch("scripts.quality.security.subprocess.run")
@patch("scripts.quality.security.get_code_paths")
def test_run_security_checks_runs_bandit(
    mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that security checks run bandit."""
    mock_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=0)

    result = run_security_checks()

    assert result == 0
    # Should call bandit (safety check requires network, skipped in tests)
    assert mock_run.call_count >= 1

    # Verify bandit was called
    bandit_call = mock_run.call_args_list[0]
    assert "bandit" in bandit_call[0][0]
    assert "-r" in bandit_call[0][0]
    assert "src" in bandit_call[0][0]


@patch("scripts.quality.security.subprocess.run")
@patch("scripts.quality.security.get_code_paths")
def test_run_security_checks_bandit_with_severity(
    mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that bandit runs with low-low severity."""
    mock_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=0)

    result = run_security_checks()

    assert result == 0

    # Verify bandit includes severity flag
    bandit_call = mock_run.call_args_list[0]
    assert "-ll" in bandit_call[0][0]


@patch("scripts.quality.security.subprocess.run")
@patch("scripts.quality.security.get_code_paths")
def test_run_security_checks_returns_failure(
    mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that security checks return non-zero on failure."""
    mock_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=1)

    result = run_security_checks()

    assert result == 1


@patch("scripts.quality.security.subprocess.run")
@patch("scripts.quality.security.get_code_paths")
def test_run_security_checks_stops_on_bandit_failure(
    mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that security checks stop if bandit fails."""
    mock_paths.return_value = ["src"]
    mock_run.return_value = MagicMock(returncode=1)

    result = run_security_checks()

    # Should only call bandit, not safety
    assert mock_run.call_count == 1
    assert result == 1


@patch("scripts.quality.security.run_security_checks")
def test_main_calls_security_checks(mock_security: MagicMock) -> None:
    """Test that main calls run_security_checks."""
    mock_security.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_security.assert_called_once()


@patch("scripts.quality.security.run_security_checks")
def test_main_returns_security_check_exit_code(mock_security: MagicMock) -> None:
    """Test that main returns security check exit code."""
    mock_security.return_value = 42

    exit_code = main()

    assert exit_code == 42
