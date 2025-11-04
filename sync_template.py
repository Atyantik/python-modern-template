#!/usr/bin/env python3
"""Sync source files to template with Jinja variable replacement."""

from __future__ import annotations

import re
from pathlib import Path


def convert_to_jinja(content: str) -> str:
    """Convert Python code to use Jinja template variables.

    Args:
        content: Source file content

    Returns:
        Content with template variables replaced
    """
    # Replace package name references
    content = re.sub(r"\bpython_modern_template\b", "{{ package_name }}", content)

    # Replace project name references (hyphenated)
    content = re.sub(r"\bpython-modern-template\b", "{{ project_name }}", content)

    return content


def sync_file(source: Path, dest: Path, add_jinja_ext: bool = True) -> None:
    """Sync a single file from source to template.

    Args:
        source: Source file path
        dest: Destination file path (in template directory)
        add_jinja_ext: Whether to add .jinja extension
    """
    # Read source content
    content = source.read_text(encoding="utf-8")

    # Files that contain literal {{...}} patterns that should NOT be processed by Jinja
    # These files will be copied as-is without .jinja extension
    no_jinja_files = {"template_loader.py", "test_template_loader.py"}

    if source.name in no_jinja_files:
        # Copy as-is without Jinja processing or extension
        add_jinja_ext = False
        jinja_content = content  # Don't process
    else:
        # Convert to Jinja
        jinja_content = convert_to_jinja(content)

    # Determine destination path
    if add_jinja_ext and not dest.name.endswith(".jinja"):
        dest = dest.with_suffix(dest.suffix + ".jinja")

    # Ensure destination directory exists
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Write to destination
    dest.write_text(jinja_content, encoding="utf-8")
    src_rel = source.relative_to(PROJECT_ROOT)
    dst_rel = dest.relative_to(PROJECT_ROOT)
    print(f"✅ Synced: {src_rel} → {dst_rel}")


def sync_directory(source_dir: Path, template_dir: Path, pattern: str = "*.py") -> int:
    """Sync all matching files from source directory to template.

    Args:
        source_dir: Source directory
        template_dir: Template destination directory
        pattern: Glob pattern for files to sync

    Returns:
        Number of files synced
    """
    count = 0
    for source_file in source_dir.glob(pattern):
        if source_file.is_file():
            dest_file = template_dir / source_file.name
            sync_file(source_file, dest_file, add_jinja_ext=True)
            count += 1
    return count


PROJECT_ROOT = Path(__file__).parent
TEMPLATE_ROOT = PROJECT_ROOT / "template"


def sync_file_list(files: list[str], src_dir: Path, dst_dir: Path, label: str) -> int:
    """Sync a list of files from source to destination.

    Args:
        files: List of filenames to sync
        src_dir: Source directory
        dst_dir: Destination directory
        label: Label for progress message

    Returns:
        Number of files synced
    """
    print(f"\n{label}")
    count = 0
    for filename in files:
        source = src_dir / filename
        if source.exists():
            sync_file(source, dst_dir / filename, add_jinja_ext=True)
            count += 1
    return count


def main() -> None:
    """Sync all source files to template."""
    print("=" * 70)
    print("SYNCING SOURCE FILES TO TEMPLATE")
    print("=" * 70)

    total = 0

    # Sync AI tools tests
    total += sync_file_list(
        [
            "test_finish_task.py",
            "test_template_loader.py",
            "test_update_plan_backward_compat.py",
            "test_update_plan_extended.py",
            "test_update_plan_fuzzy.py",
            "test_update_plan_validation.py",
        ],
        PROJECT_ROOT / "tests" / "ai_tools",
        TEMPLATE_ROOT / "tests" / "ai_tools",
        "📋 Syncing AI tools tests...",
    )

    # Sync quality tests
    total += sync_file_list(
        [
            "test_check.py",
            "test_format.py",
            "test_lint.py",
            "test_security.py",
            "test_test.py",
        ],
        PROJECT_ROOT / "tests" / "quality",
        TEMPLATE_ROOT / "tests" / "quality",
        "🔍 Syncing quality tests...",
    )

    # Sync project-level tests
    total += sync_file_list(
        [
            "test_dependencies.py",
            "test_docs.py",
            "test_makefile.py",
            "test_validate_ai_docs_sync.py",
        ],
        PROJECT_ROOT / "tests",
        TEMPLATE_ROOT / "tests",
        "📦 Syncing project-level tests...",
    )

    # Sync quality scripts
    total += sync_file_list(
        ["config.py", "check.py", "format.py", "lint.py", "security.py", "test.py"],
        PROJECT_ROOT / "scripts" / "quality",
        TEMPLATE_ROOT / "scripts" / "quality",
        "⚙️  Syncing quality scripts...",
    )

    # Sync AI tools scripts
    total += sync_file_list(
        [
            "__init__.py",
            "add_convention.py",
            "add_decision.py",
            "check_conflicts.py",
            "context_summary.py",
            "finish_task.py",
            "log_execution.py",
            "start_task.py",
            "template_loader.py",
            "update_plan.py",
            "utils.py",
        ],
        PROJECT_ROOT / "scripts" / "ai_tools",
        TEMPLATE_ROOT / "scripts" / "ai_tools",
        "🤖 Syncing AI tools scripts...",
    )

    # Sync AI tools task templates (used by template_loader.py)
    print("\n📋 Syncing AI tools task templates...")
    ai_templates_src = PROJECT_ROOT / "scripts" / "ai_tools" / "templates"
    ai_templates_dst = TEMPLATE_ROOT / "scripts" / "ai_tools" / "templates"

    template_files = [
        "__init__.py",
        "bugfix.md",
        "docs.md",
        "feature.md",
        "refactor.md",
    ]
    for template_file in template_files:
        source = ai_templates_src / template_file
        if source.exists():
            # Don't add .jinja extension to these files - they're used as-is
            sync_file(source, ai_templates_dst / template_file, add_jinja_ext=False)
            total += 1

    # Sync scripts/__init__.py
    print("\n📄 Syncing scripts/__init__.py...")
    scripts_init_src = PROJECT_ROOT / "scripts" / "__init__.py"
    scripts_init_dst = TEMPLATE_ROOT / "scripts" / "__init__.py"
    if scripts_init_src.exists():
        sync_file(scripts_init_src, scripts_init_dst, add_jinja_ext=False)
        total += 1

    # Sync src module files
    total += sync_file_list(
        ["validate_ai_docs_sync.py"],
        PROJECT_ROOT / "src" / "python_modern_template",
        TEMPLATE_ROOT / "src" / "{{ package_name }}",
        "📦 Syncing src module files...",
    )

    print("\n" + "=" * 70)
    print(f"✅ SYNC COMPLETE: {total} files synced")
    print("=" * 70)


if __name__ == "__main__":
    main()
