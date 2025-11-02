"""Test runner with pytest - single source of truth."""

from __future__ import annotations

import subprocess
import sys

from scripts.quality.config import get_min_coverage, get_test_paths


def run_tests(coverage: bool = False, verbose: bool = False) -> int:
    """Run tests with pytest.

    Args:
        coverage: If True, run with coverage reporting
        verbose: If True, run with verbose output

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    test_paths = get_test_paths()
    paths_str = " ".join(test_paths)

    print("Running tests with pytest...")
    print(f"Test paths: {paths_str}")
    if coverage:
        min_cov = get_min_coverage()
        print(f"Coverage reporting: enabled (minimum {min_cov}%)")
    if verbose:
        print("Verbose mode: enabled")
    print()

    # Build pytest command
    pytest_args = ["pytest"]

    if verbose:
        pytest_args.append("-v")

    if coverage:
        min_cov = get_min_coverage()
        pytest_args.extend(
            [
                "--cov=src",
                "--cov-report=term-missing",
                "--cov-report=html",
                f"--cov-fail-under={min_cov}",
            ]
        )

    pytest_args.extend(test_paths)

    print(f"Running: {' '.join(pytest_args)}")
    result = subprocess.run(pytest_args, check=False)

    if result.returncode != 0:
        print("\n❌ Tests failed")
        return result.returncode

    print("\n✅ All tests passed!")
    return 0


def main() -> int:
    """Main entry point for test command.

    Returns:
        Exit code
    """
    coverage_mode = "--coverage" in sys.argv
    verbose_mode = "-v" in sys.argv or "--verbose" in sys.argv

    print("=" * 60)
    print("Running Tests")
    print("=" * 60)

    return run_tests(coverage=coverage_mode, verbose=verbose_mode)


if __name__ == "__main__":
    sys.exit(main())
