"""AI Start Task tool - starts a new AI task with context loading."""

from __future__ import annotations

import argparse
import re

from scripts.ai_tools.check_conflicts import check_conflicts
from scripts.ai_tools.summarizer import (
    extract_objective_from_task_description,
    generate_context_summary,
)
from scripts.ai_tools.template_loader import load_template
from scripts.ai_tools.utils import (
    create_session_filename,
    create_session_id,
    format_timestamp,
    get_recent_sessions,
    get_sessions_dir,
    print_header,
    read_context_file,
    slugify,
    write_context_file,
)


def get_plan_template(session_id: str, task_name: str, task_type: str) -> str:
    """Get PLAN file template with auto-populated sections.

    Uses AI summarizer to intelligently populate Objective and Context
    sections based on task description and existing context.

    Args:
        session_id: Session ID
        task_name: Task name
        task_type: Task type (feature, bugfix, docs, refactor)

    Returns:
        Template content customized and auto-populated for task
    """
    # Load base template
    template = load_template(
        task_type=task_type,
        session_id=session_id,
        task_name=task_name,
    )

    # Auto-populate Objective section
    objective = extract_objective_from_task_description(task_name)
    template = template.replace(
        "[Describe what needs to be accomplished]",
        objective,
    )

    # Auto-populate Context section
    context = generate_context_summary(task_name, task_type)

    # Replace the Context section content
    # Find the Context section and replace its content
    context_pattern = r"(## Context\s*\n\s*\*\*Recent Decisions\*\*:.*?\*\*Dependencies\*\*:.*?)(\n\s*---)"
    context_replacement = f"## Context\n\n{context}\n\n---"

    if re.search(context_pattern, template, re.DOTALL):
        template = re.sub(
            context_pattern,
            context_replacement,
            template,
            flags=re.DOTALL,
        )

    return template


def get_summary_template(session_id: str, task_name: str) -> str:
    """Get SUMMARY file template.

    Args:
        session_id: Session ID
        task_name: Task name

    Returns:
        Template content
    """
    timestamp = format_timestamp()

    template = f"""# Task Summary: {task_name}

**Session ID**: {session_id}
**Created**: {timestamp}
**Status**: 🚧 In Progress

---

## What Was Done

[To be filled at end of session]

---

## Decisions Made

[To be filled at end of session]

---

## Files Changed

[To be filled at end of session]

---

## Next Steps

[To be filled at end of session]

---

## Notes

[Any important context for future sessions]
"""
    return template


def get_execution_template(session_id: str, task_name: str) -> str:
    """Get EXECUTION file template.

    Args:
        session_id: Session ID
        task_name: Task name

    Returns:
        Template content
    """
    timestamp = format_timestamp()

    template = f"""# Execution Log: {task_name}

**Session ID**: {session_id}
**Started**: {timestamp}

---

## Log

[{timestamp}] 🎯 Task started: {task_name}
[{timestamp}] 📚 Context loaded successfully
[{timestamp}] ✅ Session files created
"""
    return template


def add_task_to_active(task_name: str, session_id: str) -> None:
    """Add task to ACTIVE_TASKS.md.

    Args:
        task_name: Task name
        session_id: Session ID
    """
    active_tasks = read_context_file("ACTIVE_TASKS.md")

    if not active_tasks or active_tasks.strip() == "":
        active_tasks = (
            "# Active Tasks\n\n## In Progress\n\n## Blocked\n\n## Completed\n\n"
        )

    # Find "In Progress" section and add task
    lines = active_tasks.split("\n")
    in_progress_idx = -1

    for i, line in enumerate(lines):
        if line.strip() == "## In Progress":
            in_progress_idx = i
            break

    if in_progress_idx >= 0:
        # Insert after "## In Progress"
        insert_idx = in_progress_idx + 1
        # Skip any blank lines
        while insert_idx < len(lines) and not lines[insert_idx].strip():
            insert_idx += 1

        task_entry = f"- {task_name} (session: {session_id})"
        lines.insert(insert_idx, task_entry)

        active_tasks = "\n".join(lines)
        write_context_file("ACTIVE_TASKS.md", active_tasks)


def display_context_summary() -> None:
    """Display loaded context summary."""
    print("\n📚 Context Loaded:")

    # Check which files exist
    context_files = [
        "LAST_SESSION_SUMMARY.md",
        "ACTIVE_TASKS.md",
        "RECENT_DECISIONS.md",
        "CONVENTIONS.md",
    ]

    for filename in context_files:
        content = read_context_file(filename)
        if content:
            print(f"  ✅ {filename}")
        else:
            print(f"  ⚠️  {filename} (empty)")

    # Show recent sessions count
    sessions = get_recent_sessions(5)
    print(f"  ✅ Last {len(sessions)} sessions reviewed")


def display_important_decisions() -> None:
    """Display important decisions to follow."""
    decisions = read_context_file("RECENT_DECISIONS.md")

    if not decisions:
        return

    print("\n⚠️  IMPORTANT DECISIONS TO FOLLOW:")

    # Extract decision titles (just first 3)
    pattern = r"##\s+\[[\d\-: ]+\]\s+([^\n]+)"
    re.findall(pattern, decisions)

    key_decisions = [
        "TDD: Write tests BEFORE implementation",
        "Minimize mocks: Use real code",
        "Run make check before completion",
        "80% minimum coverage",
    ]

    for decision in key_decisions[:4]:
        print(f"  • {decision}")


def start_task(task_name: str, task_type: str = "feature") -> None:
    """Start a new AI task with full context loading.

    Args:
        task_name: Name of the task (used in session filename)
        task_type: Type of task (feature, bugfix, refactor, docs)
    """
    print_header(f"🎯 Starting Task: {task_name}")
    print(f"📝 Task Type: {task_type}")
    print()

    # Create session ID
    session_id = create_session_id()
    print(f"📝 Session ID: {session_id}")

    # Check for conflicts
    print("\n🔍 Checking for conflicts...")
    check_conflicts(task_name)

    # Display context
    display_context_summary()
    display_important_decisions()

    # Create session files
    sessions_dir = get_sessions_dir()
    sessions_dir.mkdir(parents=True, exist_ok=True)

    slugify(task_name)

    plan_file = sessions_dir / create_session_filename(session_id, "PLAN", task_name)
    summary_file = sessions_dir / create_session_filename(
        session_id, "SUMMARY", task_name
    )
    execution_file = sessions_dir / create_session_filename(
        session_id, "EXECUTION", task_name
    )

    # Write templates
    plan_file.write_text(get_plan_template(session_id, task_name, task_type))
    summary_file.write_text(get_summary_template(session_id, task_name))
    execution_file.write_text(get_execution_template(session_id, task_name))

    # Add to active tasks
    add_task_to_active(task_name, session_id)

    # Display session info
    print("\n📋 Session Files Created:")
    print(f"  • {plan_file.name}")
    print(f"  • {summary_file.name}")
    print(f"  • {execution_file.name}")

    print("\n✨ Ready to start! Follow TDD workflow:")
    print("  1. Write tests first")
    print("  2. Implement code")
    print("  3. Run make check")
    print("  4. Use ai-log to track progress")
    print("  5. Use ai-finish-task when complete")
    print()


def main() -> None:
    """Main entry point for ai-start-task command."""
    parser = argparse.ArgumentParser(
        description="Start a new AI task with context loading",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-start-task "Add email validation"
  ai-start-task "Fix user authentication bug" --type=bugfix
        """,
    )
    parser.add_argument(
        "task_name",
        help="Name of the task",
    )
    parser.add_argument(
        "--type",
        choices=["feature", "bugfix", "refactor", "docs"],
        default="feature",
        help="Type of task (default: feature)",
    )

    args = parser.parse_args()

    start_task(task_name=args.task_name, task_type=args.type)


if __name__ == "__main__":
    main()
