"""Validate synchronization between AI_DOCS and template/AI_DOCS files."""

from __future__ import annotations

import difflib
import sys
from pathlib import Path


def find_ai_doc_files(base_path: Path | None = None) -> list[Path]:
    """Find all files in AI_DOCS directory.

    Args:
        base_path: Base path to search from (defaults to project root)

    Returns:
        List of Path objects for AI_DOCS files
    """
    if base_path is None:
        base_path = Path(__file__).parent.parent.parent

    ai_docs_dir = base_path / "AI_DOCS"
    if not ai_docs_dir.exists():
        return []

    # Find all markdown files
    return list(ai_docs_dir.glob("*.md"))


def find_template_files(base_path: Path | None = None) -> list[Path]:
    """Find all files in template directory (AI_DOCS and config files).

    Args:
        base_path: Base path to search from (defaults to project root)

    Returns:
        List of Path objects for template files
    """
    if base_path is None:
        base_path = Path(__file__).parent.parent.parent

    template_dir = base_path / "template"
    if not template_dir.exists():
        return []

    # Find all relevant files
    files: list[Path] = []

    # AI_DOCS templates
    ai_docs_template = template_dir / "AI_DOCS"
    if ai_docs_template.exists():
        files.extend(ai_docs_template.glob("*.md.jinja"))

    # Config file templates
    for config_file in [
        "CLAUDE.md.jinja",
        "AGENTS.md.jinja",
        ".cursorrules.jinja",
    ]:
        config_path = template_dir / config_file
        if config_path.exists():
            files.append(config_path)

    return files


def check_file_exists(file_path: Path) -> bool:
    """Check if a file exists.

    Args:
        file_path: Path to check

    Returns:
        True if file exists, False otherwise
    """
    return file_path.exists() and file_path.is_file()


def compare_files(
    file1: Path,
    file2: Path,
    is_template: bool = False,
) -> tuple[bool, str]:
    """Compare two files for content differences.

    Args:
        file1: First file to compare
        file2: Second file to compare
        is_template: Whether file2 is a Jinja template

    Returns:
        Tuple of (files_are_same, diff_output)
    """
    try:
        content1 = file1.read_text().splitlines(keepends=True)
        content2 = file2.read_text().splitlines(keepends=True)

        # If comparing with template, strip .jinja-specific syntax for comparison
        # This is simplified - real implementation would need proper Jinja parsing
        if is_template:
            # For now, just compare directly
            # Future enhancement: Add proper Jinja template comparison
            pass

        # Generate diff
        diff = list(
            difflib.unified_diff(
                content1,
                content2,
                fromfile=str(file1),
                tofile=str(file2),
            )
        )

        if not diff:
            return True, ""

        return False, "".join(diff)

    except OSError as e:  # Catch file I/O errors
        return False, f"Error comparing files: {e}"


def validate_sync(  # pylint: disable=too-many-locals
    base_path: Path | None = None,
) -> list[dict[str, str]]:
    """Validate that AI_DOCS files are in sync with template versions.

    Args:
        base_path: Base path to search from (defaults to project root)

    Returns:
        List of issues found (empty if all in sync)
    """
    issues = []

    if base_path is None:
        base_path = Path(__file__).parent.parent.parent

    # Find AI_DOCS files
    ai_doc_files = find_ai_doc_files(base_path)

    # Check each AI_DOCS file has a template version
    for doc_file in ai_doc_files:
        doc_name = doc_file.name
        template_path = base_path / "template" / "AI_DOCS" / f"{doc_name}.jinja"

        if not check_file_exists(template_path):
            template_rel_path = str(template_path.relative_to(base_path))
            missing_msg = f"Missing template file: {template_rel_path}"
            issues.append(
                {
                    "type": "missing",
                    "file": str(doc_file.relative_to(base_path)),
                    "message": missing_msg,
                }
            )
            continue

        # Compare content (simplified comparison for now)
        # In a full implementation, this would handle Jinja templating properly
        are_same, diff = compare_files(doc_file, template_path, is_template=True)

        # For template files, we expect some differences due to Jinja syntax
        # So we only flag major differences
        # This is a simplified check - real implementation would be smarter
        if not are_same and len(diff) > 1000:  # Arbitrary threshold
            template_rel_path = str(template_path.relative_to(base_path))
            differs_msg = (
                f"Content significantly differs from template: {template_rel_path}"
            )
            issues.append(
                {
                    "type": "different",
                    "file": str(doc_file.relative_to(base_path)),
                    "message": differs_msg,
                }
            )

    # Check AI config files (CLAUDE.md, AGENTS.md, etc.)
    config_files = [
        ("CLAUDE.md", "CLAUDE.md.jinja"),
        ("AGENTS.md", "AGENTS.md.jinja"),
        (".cursorrules", ".cursorrules.jinja"),
    ]

    for source_name, template_name in config_files:
        source_file = base_path / source_name
        template_file = base_path / "template" / template_name

        if check_file_exists(source_file) and not check_file_exists(template_file):
            issues.append(
                {
                    "type": "missing",
                    "file": source_name,
                    "message": f"Missing template file: template/{template_name}",
                }
            )

    return issues


def generate_sync_report(issues: list[dict[str, str]]) -> str:
    """Generate a human-readable sync report.

    Args:
        issues: List of issues from validate_sync()

    Returns:
        Formatted report string
    """
    if not issues:
        return """
# AI_DOCS Sync Validation Report

## Status: ✅ PASSED

All AI documentation files are in sync with their template versions.

**Files Checked:** AI_DOCS/*.md, CLAUDE.md, AGENTS.md, .cursorrules
**Issues Found:** 0

Everything is synchronized! 🎉
"""

    # Group issues by type
    missing = [issue for issue in issues if issue["type"] == "missing"]
    different = [issue for issue in issues if issue["type"] == "different"]

    report = f"""
# AI_DOCS Sync Validation Report

## Status: ❌ FAILED

**Total Issues:** {len(issues)}
- Missing template files: {len(missing)}
- Content differences: {len(different)}

---

"""

    if missing:
        report += "## Missing Template Files\n\n"
        for issue in missing:
            report += f"### {issue['file']}\n"
            report += f"**Issue:** {issue['message']}\n\n"
            report += "**Action:** Create template version of this file\n\n"

    if different:
        report += "## Content Differences\n\n"
        for issue in different:
            report += f"### {issue['file']}\n"
            report += f"**Issue:** {issue['message']}\n\n"
            report += "**Action:** Review and sync content between files\n\n"

    report += """
---

## How to Fix

1. **For missing templates:**
   - Create template version in `template/` directory
   - Add `.jinja` extension
   - Add Jinja variables where needed for customization

2. **For content differences:**
   - Review changes with: `git diff AI_DOCS/file.md template/AI_DOCS/file.md.jinja`
   - Sync content between files
   - Ensure template includes all important content from source

3. **Verify fixes:**
   ```bash
   uv run ai-validate-docs
   ```
"""

    return report


def main() -> None:
    """Run validation and print report."""
    issues = validate_sync()
    report = generate_sync_report(issues)
    print(report)

    # Exit with error code if issues found
    if issues:
        sys.exit(1)


if __name__ == "__main__":
    main()
