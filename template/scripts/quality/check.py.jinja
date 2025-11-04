"""Quality check orchestrator - runs all quality checks in sequence."""

from __future__ import annotations

import sys

from scripts.quality.format import format_code
from scripts.quality.lint import lint_code
from scripts.quality.test import run_tests


def run_all_checks() -> int:
    """Run all quality checks in sequence.

    Runs: format, lint, test (with coverage)

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    print("\n" + "=" * 60)
    print("STEP 1/3: Code Formatting")
    print("=" * 60)

    result = format_code(check=False)
    if result != 0:
        print("\n❌ Quality check failed at: formatting")
        return result

    print("\n" + "=" * 60)
    print("STEP 2/3: Code Linting")
    print("=" * 60)

    result = lint_code(fix=False)
    if result != 0:
        print("\n❌ Quality check failed at: linting")
        return result

    print("\n" + "=" * 60)
    print("STEP 3/3: Tests with Coverage")
    print("=" * 60)

    result = run_tests(coverage=True, verbose=False)
    if result != 0:
        print("\n❌ Quality check failed at: tests")
        return result

    print("\n" + "=" * 60)
    print("✅ ALL QUALITY CHECKS PASSED!")
    print("=" * 60)
    print("\nSummary:")
    print("  ✅ Code formatting")
    print("  ✅ Code linting (ruff, mypy, pylint)")
    print("  ✅ Tests with coverage")
    print("\nYour code meets all quality standards!")
    print()

    return 0


def main() -> int:
    """Main entry point for check command.

    Returns:
        Exit code
    """
    print("=" * 60)
    print("Running Complete Quality Check")
    print("=" * 60)
    print("\nThis will run:")
    print("  1. Code formatting (black, isort)")
    print("  2. Code linting (ruff, mypy, pylint)")
    print("  3. Tests with coverage")
    print()

    return run_all_checks()


if __name__ == "__main__":
    sys.exit(main())
