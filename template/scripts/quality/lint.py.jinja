"""Code linting with ruff, mypy, and pylint - single source of truth."""

from __future__ import annotations

import subprocess
import sys

from scripts.quality.config import get_code_paths


def lint_code(fix: bool = False) -> int:
    """Lint code with ruff, mypy, and pylint.

    Args:
        fix: If True, auto-fix issues where possible (ruff only)

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    paths = get_code_paths()
    paths_str = " ".join(paths)

    print("Linting code with ruff, mypy, and pylint...")
    print(f"Paths: {paths_str}")
    if fix:
        print("Auto-fix mode: enabled (ruff only)")
    print()

    # Run ruff
    ruff_args = ["ruff", "check"]
    if fix:
        ruff_args.append("--fix")
    ruff_args.extend(paths)

    print(f"Running: {' '.join(ruff_args)}")
    result = subprocess.run(ruff_args, check=False)

    if result.returncode != 0:
        print("\n❌ Ruff linting failed")
        return result.returncode

    # Run mypy
    mypy_args = ["mypy"]
    mypy_args.extend(paths)

    print(f"\nRunning: {' '.join(mypy_args)}")
    result = subprocess.run(mypy_args, check=False)

    if result.returncode != 0:
        print("\n❌ MyPy type checking failed")
        return result.returncode

    # Run pylint
    pylint_args = ["pylint"]
    pylint_args.extend(paths)

    print(f"\nRunning: {' '.join(pylint_args)}")
    result = subprocess.run(pylint_args, check=False)

    if result.returncode != 0:
        print("\n❌ Pylint checking failed")
        return result.returncode

    print("\n✅ All linting checks passed!")
    return 0


def main() -> int:
    """Main entry point for lint command.

    Returns:
        Exit code
    """
    fix_mode = "--fix" in sys.argv

    print("=" * 60)
    print("Code Linting")
    if fix_mode:
        print("(with auto-fix enabled)")
    print("=" * 60)

    return lint_code(fix=fix_mode)


if __name__ == "__main__":
    sys.exit(main())
