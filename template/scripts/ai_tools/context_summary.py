"""AI Context Summary tool - displays current AI context."""

from __future__ import annotations

import argparse
import re

from scripts.ai_tools.utils import (
    get_recent_sessions,
    print_header,
    read_context_file,
)


def count_tasks_in_section(content: str, section: str) -> int:
    """Count tasks in a specific section of ACTIVE_TASKS.md.

    Args:
        content: Content of ACTIVE_TASKS.md
        section: Section name (e.g., "In Progress", "Blocked")

    Returns:
        Number of tasks in section
    """
    # Find the section
    pattern = rf"## {re.escape(section)}\s*(.*?)(?=##|$)"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return 0

    section_content = match.group(1)

    # Count bullet points (tasks)
    tasks = re.findall(r"^\s*[-*]\s+", section_content, re.MULTILINE)
    return len(tasks)


def extract_recent_decisions(content: str, count: int = 3) -> list[str]:
    """Extract recent decisions from RECENT_DECISIONS.md.

    Args:
        content: Content of RECENT_DECISIONS.md
        count: Number of recent decisions to extract

    Returns:
        List of decision summaries
    """
    # Find all decision headers
    pattern = r"##\s+\[([\d\-: ]+)\]\s+([^\n]+)"
    matches = re.findall(pattern, content)

    decisions = []
    for timestamp, title in matches[:count]:
        decisions.append(f"[{timestamp}] {title}")

    return decisions


def extract_key_conventions(content: str) -> list[str]:
    """Extract key conventions from CONVENTIONS.md.

    Args:
        content: Content of CONVENTIONS.md

    Returns:
        List of convention summaries
    """
    conventions = []

    # Find all level-3 headers (###) which are individual conventions
    pattern = r"###\s+([^\n]+)"
    matches = re.findall(pattern, content)

    # Take first 5 conventions
    for title in matches[:5]:
        conventions.append(title.strip())

    return conventions


def get_last_session_summary(content: str) -> dict[str, str]:
    """Extract last session summary information.

    Args:
        content: Content of LAST_SESSION_SUMMARY.md

    Returns:
        Dictionary with session info
    """
    info = {
        "session_id": "",
        "date": "",
        "summary": "",
        "status": "",
        "files": "",
    }

    # Extract session ID
    match = re.search(r"\*\*Session ID\*\*:\s*(\d+)", content)
    if match:
        info["session_id"] = match.group(1)

    # Extract date
    match = re.search(r"\*\*Date\*\*:\s*([^\n]+)", content)
    if match:
        info["date"] = match.group(1)

    # Extract summary (look for ## Summary section)
    match = re.search(r"##\s+Summary\s*\n([^\n]+)", content)
    if match:
        info["summary"] = match.group(1).strip()

    # Extract status line
    match = re.search(r"\*\*Status\*\*:\s*([^\n]+)", content)
    if match:
        info["status"] = match.group(1)

    return info


def show_context_summary(detailed: bool = False) -> None:
    """Show quick context summary.

    Args:
        detailed: Show detailed view with more information
    """
    print_header("📚 AI Context Summary")

    # Read context files
    last_session = read_context_file("LAST_SESSION_SUMMARY.md")
    active_tasks = read_context_file("ACTIVE_TASKS.md")
    recent_decisions = read_context_file("RECENT_DECISIONS.md")
    conventions = read_context_file("CONVENTIONS.md")

    # Display last session
    print("📝 Last Session:")
    if last_session and "No sessions yet" not in last_session:
        session_info = get_last_session_summary(last_session)
        if session_info["date"]:
            print(f"  [{session_info['date']}] {session_info['summary']}")
            if session_info["status"]:
                print(f"  {session_info['status']}")
        else:
            # Fallback to first line
            lines = last_session.split("\n")
            if len(lines) > 2:
                print(f"  {lines[2].strip()}")
    else:
        print("  No sessions yet")
    print()

    # Display active tasks
    print("🚧 Active Tasks:")
    if active_tasks:
        in_progress = count_tasks_in_section(active_tasks, "In Progress")
        blocked = count_tasks_in_section(active_tasks, "Blocked")
        completed = count_tasks_in_section(active_tasks, "Completed")

        print(f"  • {in_progress} in progress")
        print(f"  • {blocked} blocked")
        print(f"  • {completed} completed")

        if detailed:
            # Show actual task names
            print()
            sections = ["In Progress", "Blocked"]
            for section in sections:
                pattern = rf"## {re.escape(section)}\s*(.*?)(?=##|$)"
                match = re.search(pattern, active_tasks, re.DOTALL)
                if match:
                    section_content = match.group(1).strip()
                    if section_content:
                        print(f"\n  {section}:")
                        for line in section_content.split("\n"):
                            if line.strip().startswith(("-", "*")):
                                print(f"    {line.strip()}")
    else:
        print("  No active tasks")
    print()

    # Display recent decisions
    print("🎯 Recent Decisions (Last 3):")
    if recent_decisions:
        decisions = extract_recent_decisions(recent_decisions, count=3)
        if decisions:
            for i, decision in enumerate(decisions, 1):
                print(f"  {i}. {decision}")
        else:
            print("  No decisions recorded")

        if detailed and decisions:
            # Show full decision content
            print()
            pattern = r"(##\s+\[[\d\-: ]+\].*?)(?=##|$)"
            matches = re.findall(pattern, recent_decisions, re.DOTALL)
            for match in matches[:3]:
                print(f"\n{match.strip()}\n")
    else:
        print("  No decisions recorded")
    print()

    # Display key conventions
    print("📋 Key Conventions:")
    if conventions:
        conv_list = extract_key_conventions(conventions)
        if conv_list:
            for conv in conv_list:
                print(f"  • {conv}")
        else:
            # Fallback: show section headers
            sections = re.findall(r"##\s+([^\n]+)", conventions)
            for section in sections[:5]:
                print(f"  • {section}")
    else:
        print("  No conventions defined")
    print()

    # Display recent sessions
    print("📂 Recent Sessions:")
    sessions = get_recent_sessions(5)
    if sessions:
        for i, session in enumerate(sessions, 1):
            session_id = session["session_id"]
            task_slug = session["task_slug"].replace("-", " ").title()
            print(f"  {i}. [{session_id}] {task_slug}")
    else:
        print("  No sessions found")
    print()

    print("=" * 60)
    print("💡 Tip: Run 'ai-start-task \"task name\"' to begin work")
    print()


def main() -> None:
    """Main entry point for ai-context-summary command."""
    parser = argparse.ArgumentParser(
        description="Show AI context summary",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed view with more information",
    )

    args = parser.parse_args()

    show_context_summary(detailed=args.detailed)


if __name__ == "__main__":
    main()
