#!/usr/bin/env python3
"""Validate that all AI instruction files exist and contain required rules.

This script ensures that AI coding assistants have consistent instructions
across all platforms and that critical TDD/quality rules are present.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import NamedTuple


class ValidationResult(NamedTuple):
    """Result of validation check."""

    passed: bool
    message: str


# Required AI instruction files
REQUIRED_FILES = [
    ".cursorrules",
    "AGENTS.md",
    ".claude/INSTRUCTIONS.md",
    "GEMINI.md",
    ".aider.conf.yml",
    "COPILOT_INSTRUCTIONS.md",
]

# Critical keywords that MUST appear in instruction files
REQUIRED_KEYWORDS = [
    "TDD",  # Test-Driven Development
    "test",  # Testing
    "make check",  # Quality gate
    "coverage",  # Code coverage
    "type hint",  # Type safety
    "mock",  # Mocking guidance
]

# Critical phrases for TDD
CRITICAL_TDD_PHRASES = [
    "test",  # Must mention tests
    "before",  # Tests before implementation
    "coverage",  # Coverage requirements
]


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path to project root
    """
    # Script is in scripts/, project root is parent
    return Path(__file__).parent.parent


def check_file_exists(file_path: Path) -> ValidationResult:
    """Check if a file exists.

    Args:
        file_path: Path to check

    Returns:
        ValidationResult indicating if file exists
    """
    if file_path.exists():
        return ValidationResult(True, f"✅ {file_path.name} exists")
    return ValidationResult(False, f"❌ {file_path.name} is missing")


def check_file_content(file_path: Path, keywords: list[str]) -> ValidationResult:
    """Check if file contains required keywords.

    Args:
        file_path: Path to file
        keywords: List of required keywords

    Returns:
        ValidationResult indicating if keywords are present
    """
    try:
        content = file_path.read_text().lower()
        missing = [kw for kw in keywords if kw.lower() not in content]

        if missing:
            return ValidationResult(
                False,
                f"❌ {file_path.name} missing keywords: {', '.join(missing)}",
            )
        return ValidationResult(
            True, f"✅ {file_path.name} contains all required keywords"
        )
    except OSError as e:
        return ValidationResult(False, f"❌ Error reading {file_path.name}: {e}")


def check_tdd_emphasis(file_path: Path) -> ValidationResult:
    """Check if file emphasizes TDD principles.

    Args:
        file_path: Path to file

    Returns:
        ValidationResult indicating TDD emphasis
    """
    try:
        content = file_path.read_text().lower()

        # Count occurrences of critical TDD phrases
        test_count = content.count("test")
        first_count = content.count("first") + content.count("before")

        if test_count < 5:
            return ValidationResult(
                False,
                f"⚠️  {file_path.name} mentions 'test' only "
                f"{test_count} times (expected 5+)",
            )

        if first_count < 2:
            return ValidationResult(
                False,
                f"⚠️  {file_path.name} doesn't emphasize 'tests first' enough",
            )

        return ValidationResult(
            True, f"✅ {file_path.name} emphasizes TDD appropriately"
        )
    except OSError as e:
        return ValidationResult(
            False, f"❌ Error checking TDD in {file_path.name}: {e}"
        )


def check_consistency_across_files(root: Path, files: list[str]) -> ValidationResult:
    """Check if core concepts are consistent across all files.

    Args:
        root: Project root directory
        files: List of file paths to check

    Returns:
        ValidationResult indicating consistency
    """
    coverage_requirements = []

    for file_rel_path in files:
        file_path = root / file_rel_path
        if not file_path.exists():
            continue

        try:
            content = file_path.read_text().lower()

            # Check for coverage percentage
            if "80%" in content or "80 percent" in content:
                coverage_requirements.append((file_rel_path, "80%"))
        except OSError:
            continue

    # All files should mention 80% coverage
    expected_count = len([f for f in files if (root / f).exists()])
    actual_count = len(coverage_requirements)

    if actual_count < expected_count - 1:  # Allow 1 file to not mention it
        return ValidationResult(
            False,
            f"⚠️  Only {actual_count}/{expected_count} files mention "
            f"80% coverage requirement",
        )

    return ValidationResult(True, "✅ Coverage requirements consistent across files")


def validate_all() -> bool:
    """Validate all AI instruction files.

    Returns:
        True if all validations pass, False otherwise
    """
    root = get_project_root()
    results: list[ValidationResult] = []
    all_passed = True

    print("🔍 Validating AI Instruction Files\n")
    print("=" * 60)

    # Check file existence
    print("\n📁 File Existence Check:")
    for file_path in REQUIRED_FILES:
        full_path = root / file_path
        result = check_file_exists(full_path)
        results.append(result)
        print(f"  {result.message}")
        if not result.passed:
            all_passed = False

    # Check required keywords in existing files
    print("\n🔑 Required Keywords Check:")
    for file_path in REQUIRED_FILES:
        full_path = root / file_path
        if full_path.exists():
            result = check_file_content(full_path, REQUIRED_KEYWORDS)
            results.append(result)
            print(f"  {result.message}")
            if not result.passed:
                all_passed = False

    # Check TDD emphasis
    print("\n🧪 TDD Emphasis Check:")
    for file_path in REQUIRED_FILES:
        full_path = root / file_path
        if full_path.exists():
            result = check_tdd_emphasis(full_path)
            results.append(result)
            print(f"  {result.message}")
            if not result.passed:
                all_passed = False

    # Check consistency
    print("\n🔄 Consistency Check:")
    result = check_consistency_across_files(root, REQUIRED_FILES)
    results.append(result)
    print(f"  {result.message}")
    if not result.passed:
        all_passed = False

    # Summary
    print("\n" + "=" * 60)
    passed_count = sum(1 for r in results if r.passed)
    total_count = len(results)
    print(f"\n📊 Summary: {passed_count}/{total_count} checks passed")

    if all_passed:
        print("\n✨ All AI instruction files are valid and consistent!")
        return True

    print("\n❌ Some validation checks failed. Please review above.")
    print("\n💡 Tips:")
    print("  - Ensure all required files exist")
    print("  - Include TDD keywords (test, coverage, make check, etc.)")
    print("  - Emphasize 'tests first' approach")
    print("  - Keep 80% coverage requirement consistent")
    return False


def main() -> int:
    """Main entry point.

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        passed = validate_all()
        return 0 if passed else 1
    except OSError as e:
        print(f"\n❌ Validation failed with error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
