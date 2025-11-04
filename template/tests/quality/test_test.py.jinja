"""Tests for quality.test module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from scripts.quality.test import main, run_tests


@patch("scripts.quality.test.subprocess.run")
@patch("scripts.quality.test.get_test_paths")
@patch("scripts.quality.test.get_min_coverage")
def test_run_tests_basic(
    mock_coverage: MagicMock, mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that run_tests runs pytest with correct paths."""
    mock_paths.return_value = ["tests"]
    mock_coverage.return_value = 80
    mock_run.return_value = MagicMock(returncode=0)

    result = run_tests(coverage=False, verbose=False)

    assert result == 0
    mock_run.assert_called_once()

    call_args = mock_run.call_args[0][0]
    assert "pytest" in call_args
    assert "tests" in call_args


@patch("scripts.quality.test.subprocess.run")
@patch("scripts.quality.test.get_test_paths")
@patch("scripts.quality.test.get_min_coverage")
def test_run_tests_with_coverage(
    mock_coverage: MagicMock, mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that run_tests includes coverage when requested."""
    mock_paths.return_value = ["tests"]
    mock_coverage.return_value = 80
    mock_run.return_value = MagicMock(returncode=0)

    result = run_tests(coverage=True, verbose=False)

    assert result == 0

    call_args = mock_run.call_args[0][0]
    assert "--cov=src" in call_args
    assert "--cov-report=term-missing" in call_args
    assert "--cov-report=html" in call_args
    assert "--cov-fail-under=80" in call_args


@patch("scripts.quality.test.subprocess.run")
@patch("scripts.quality.test.get_test_paths")
@patch("scripts.quality.test.get_min_coverage")
def test_run_tests_with_verbose(
    mock_coverage: MagicMock, mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that run_tests includes verbose flag when requested."""
    mock_paths.return_value = ["tests"]
    mock_coverage.return_value = 80
    mock_run.return_value = MagicMock(returncode=0)

    result = run_tests(coverage=False, verbose=True)

    assert result == 0

    call_args = mock_run.call_args[0][0]
    assert "-v" in call_args


@patch("scripts.quality.test.subprocess.run")
@patch("scripts.quality.test.get_test_paths")
@patch("scripts.quality.test.get_min_coverage")
def test_run_tests_returns_failure(
    mock_coverage: MagicMock, mock_paths: MagicMock, mock_run: MagicMock
) -> None:
    """Test that run_tests returns non-zero on test failure."""
    mock_paths.return_value = ["tests"]
    mock_coverage.return_value = 80
    mock_run.return_value = MagicMock(returncode=1)

    result = run_tests(coverage=False, verbose=False)

    assert result == 1


@patch("scripts.quality.test.run_tests")
@patch("sys.argv", ["test.py"])
def test_main_default_flags(mock_tests: MagicMock) -> None:
    """Test main with default flags."""
    mock_tests.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_tests.assert_called_once_with(coverage=False, verbose=False)


@patch("scripts.quality.test.run_tests")
@patch("sys.argv", ["test.py", "--coverage"])
def test_main_with_coverage_flag(mock_tests: MagicMock) -> None:
    """Test main with coverage flag."""
    mock_tests.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_tests.assert_called_once_with(coverage=True, verbose=False)


@patch("scripts.quality.test.run_tests")
@patch("sys.argv", ["test.py", "-v"])
def test_main_with_verbose_flag(mock_tests: MagicMock) -> None:
    """Test main with verbose flag."""
    mock_tests.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_tests.assert_called_once_with(coverage=False, verbose=True)


@patch("scripts.quality.test.run_tests")
@patch("sys.argv", ["test.py", "--coverage", "-v"])
def test_main_with_multiple_flags(mock_tests: MagicMock) -> None:
    """Test main with multiple flags."""
    mock_tests.return_value = 0

    exit_code = main()

    assert exit_code == 0
    mock_tests.assert_called_once_with(coverage=True, verbose=True)
