"""Security scanning with bandit and safety - single source of truth."""

from __future__ import annotations

import subprocess
import sys

from scripts.quality.config import get_code_paths


def run_security_checks() -> int:
    """Run security checks with bandit and safety.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    paths = get_code_paths()
    # Only scan src for security issues (not tests)
    src_paths = [p for p in paths if "src" in p]
    paths_str = " ".join(src_paths)

    print("Running security checks with bandit and safety...")
    print(f"Scanning paths: {paths_str}")
    print()

    # Run bandit for code security issues
    bandit_args = ["bandit", "-r"]
    bandit_args.extend(src_paths)
    bandit_args.extend(["-ll"])  # Low-low severity

    print(f"Running: {' '.join(bandit_args)}")
    result = subprocess.run(bandit_args, check=False)

    if result.returncode != 0:
        print("\n❌ Bandit security scan found issues")
        return result.returncode

    # Run safety for known vulnerabilities in dependencies
    print("\nRunning: safety check")
    result = subprocess.run(["safety", "check"], check=False)

    if result.returncode != 0:
        print("\n❌ Safety found known vulnerabilities")
        return result.returncode

    print("\n✅ All security checks passed!")
    return 0


def main() -> int:
    """Main entry point for security command.

    Returns:
        Exit code
    """
    print("=" * 60)
    print("Security Scanning")
    print("=" * 60)

    return run_security_checks()


if __name__ == "__main__":
    sys.exit(main())
