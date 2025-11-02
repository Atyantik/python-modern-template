"""Code formatting with black and isort - single source of truth."""

from __future__ import annotations

import subprocess
import sys

from scripts.quality.config import get_code_paths


def format_code(check: bool = False) -> int:
    """Format code with black and isort.

    Args:
        check: If True, only check formatting without making changes

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    paths = get_code_paths()
    paths_str = " ".join(paths)

    print(f"{'Checking' if check else 'Formatting'} code with black and isort...")
    print(f"Paths: {paths_str}")
    print()

    # Run black
    black_args = ["black"]
    if check:
        black_args.append("--check")
    black_args.extend(paths)

    print(f"Running: {' '.join(black_args)}")
    result = subprocess.run(black_args, check=False)

    if result.returncode != 0:
        print(f"\n❌ Black {'check' if check else 'formatting'} failed")
        return result.returncode

    # Run isort
    isort_args = ["isort"]
    if check:
        isort_args.append("--check-only")
    isort_args.extend(paths)

    print(f"\nRunning: {' '.join(isort_args)}")
    result = subprocess.run(isort_args, check=False)

    if result.returncode != 0:
        print(f"\n❌ isort {'check' if check else 'formatting'} failed")
        return result.returncode

    print(f"\n✅ Code formatting {'check' if check else 'complete'} - all good!")
    return 0


def main() -> int:
    """Main entry point for format command.

    Returns:
        Exit code
    """
    check_mode = "--check" in sys.argv

    if check_mode:
        print("=" * 60)
        print("Code Formatting Check")
        print("=" * 60)
    else:
        print("=" * 60)
        print("Code Formatting")
        print("=" * 60)

    return format_code(check=check_mode)


if __name__ == "__main__":
    sys.exit(main())
