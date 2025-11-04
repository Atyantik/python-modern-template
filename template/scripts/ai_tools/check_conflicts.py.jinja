"""AI Check Conflicts tool - checks for task conflicts."""

from __future__ import annotations

import argparse
import difflib
import re

from scripts.ai_tools.utils import get_context_dir, print_success, print_warning


def extract_tasks(content: str, section: str) -> list[dict[str, str]]:
    """Extract tasks from a section.

    Args:
        content: Content of ACTIVE_TASKS.md
        section: Section name

    Returns:
        List of task dictionaries with 'name' and 'details'
    """
    pattern = rf"## {re.escape(section)}\s*(.*?)(?=##|$)"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return []

    section_content = match.group(1)
    tasks = []

    for line in section_content.split("\n"):
        line = line.strip()
        if line.startswith(("-", "*")):
            # Remove bullet point
            task_text = re.sub(r"^[-*]\s+", "", line)
            tasks.append({"name": task_text, "details": task_text})

    return tasks


def find_similar_tasks(
    task_name: str, existing_tasks: list[dict[str, str]]
) -> list[tuple[str, float]]:
    """Find tasks similar to the given task name.

    Args:
        task_name: Task name to check
        existing_tasks: List of existing tasks

    Returns:
        List of (task_name, similarity_score) tuples
    """
    similar = []

    for task in existing_tasks:
        # Use difflib to calculate similarity
        ratio = difflib.SequenceMatcher(
            None, task_name.lower(), task["name"].lower()
        ).ratio()

        if ratio > 0.7:  # 70% similarity threshold
            similar.append((task["name"], ratio))

    # Sort by similarity (highest first)
    similar.sort(key=lambda x: x[1], reverse=True)

    return similar


def check_conflicts(task_name: str | None = None) -> None:
    """Check for task conflicts.

    Args:
        task_name: Task to check (default: check all active)
    """
    context_dir = get_context_dir()
    active_tasks_file = context_dir / "ACTIVE_TASKS.md"

    if not active_tasks_file.exists():
        print_success("No active tasks file found - no conflicts!")
        return

    content = active_tasks_file.read_text()

    # Extract tasks from different sections
    in_progress = extract_tasks(content, "In Progress")
    blocked = extract_tasks(content, "Blocked")

    if task_name:
        # Check specific task
        similar_in_progress = find_similar_tasks(task_name, in_progress)
        similar_blocked = find_similar_tasks(task_name, blocked)

        if similar_in_progress or similar_blocked:
            print_warning("Potential Conflict Detected!")
            print()
            print(f'Task: "{task_name}"')
            print()

            if similar_in_progress:
                print("🚧 Similar tasks in progress:")
                for task, similarity in similar_in_progress:
                    print(f"  • {task} (similarity: {similarity:.0%})")
                print()

            if similar_blocked:
                print("⏸️  Similar tasks blocked:")
                for task, similarity in similar_blocked:
                    print(f"  • {task} (similarity: {similarity:.0%})")
                print()

            print("📋 Recommendation:")
            print("  • Check if tasks overlap before proceeding")
            print("  • Consider combining into one task")
            print("  • Or coordinate which files each task modifies")
            print()
        else:
            print_success("No conflicts detected!")
            print(f'Task "{task_name}" appears unique.')
    else:
        # List all active tasks
        print("📋 Active Tasks Summary:\n")

        if in_progress:
            print("🚧 In Progress:")
            for task in in_progress:
                print(f"  • {task['name']}")
            print()

        if blocked:
            print("⏸️  Blocked:")
            for task in blocked:
                print(f"  • {task['name']}")
            print()

        if not in_progress and not blocked:
            print("  No active tasks found")
            print()

        print_success("Use 'ai-check-conflicts \"task name\"' to check a specific task")


def main() -> None:
    """Main entry point for ai-check-conflicts command."""
    parser = argparse.ArgumentParser(
        description="Check for task conflicts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-check-conflicts "Add email validation"
  ai-check-conflicts  # Show all active tasks
        """,
    )
    parser.add_argument(
        "task_name",
        nargs="?",
        help="Task name to check for conflicts (optional)",
    )

    args = parser.parse_args()

    check_conflicts(task_name=args.task_name)


if __name__ == "__main__":
    main()
