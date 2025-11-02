"""AI Update Plan tool - updates checkboxes in PLAN file."""

from __future__ import annotations

import argparse
import re
import sys

from scripts.ai_tools.log_execution import log_execution
from scripts.ai_tools.utils import (
    get_current_session,
    get_session_files,
    print_error,
    print_success,
)


def find_checkbox_line(content: str, item_text: str) -> tuple[int, str] | None:
    """Find the line number and content of a checkbox matching the item text.

    Args:
        content: File content
        item_text: Text to search for

    Returns:
        Tuple of (line_number, line_content) or None if not found
    """
    lines = content.split("\n")
    item_lower = item_text.lower()

    for i, line in enumerate(lines):
        # Check if line contains a checkbox
        if re.match(r"^\s*-\s*\[([ x])\]", line):
            # Check if item text is in line (case-insensitive, fuzzy)
            line_lower = line.lower()
            if item_lower in line_lower:
                return (i, line)

    return None


def toggle_checkbox(line: str, check: bool) -> str:
    """Toggle checkbox state in a line.

    Args:
        line: Line containing checkbox
        check: True to check, False to uncheck

    Returns:
        Updated line
    """
    checkbox = "[x]" if check else "[ ]"
    return re.sub(r"\[([ x])\]", checkbox, line, count=1)


def count_checkboxes(content: str) -> tuple[int, int]:
    """Count checked and total checkboxes.

    Args:
        content: File content

    Returns:
        Tuple of (checked_count, total_count)
    """
    lines = content.split("\n")
    total = 0
    checked = 0

    for line in lines:
        match = re.match(r"^\s*-\s*\[([ x])\]", line)
        if match:
            total += 1
            if match.group(1) == "x":
                checked += 1

    return (checked, total)


def extract_phase_section(content: str, line_num: int) -> str:
    """Extract the phase section containing the given line.

    Args:
        content: File content
        line_num: Line number to find section for

    Returns:
        Section content
    """
    lines = content.split("\n")

    # Find the phase header before this line
    phase_start = 0
    for i in range(line_num, -1, -1):
        if lines[i].startswith("### Phase"):
            phase_start = i
            break

    # Find the next phase header or end
    phase_end = len(lines)
    for i in range(line_num + 1, len(lines)):
        if lines[i].startswith("###"):
            phase_end = i
            break

    return "\n".join(lines[phase_start:phase_end])


def update_plan(
    item: str | None = None,
    check: bool = True,
    uncheck: bool = False,
    show: bool = False,
    session_id: str | None = None,
) -> None:
    """Update checkboxes in PLAN file.

    Args:
        item: Text of the checkbox item to update
        check: Check the box (default)
        uncheck: Uncheck the box
        show: Show current plan with progress
        session_id: Session ID (default: most recent)
    """
    # Get current session if not specified
    if session_id is None:
        session_id = get_current_session()

    if session_id is None:
        print_error("No active session found")
        print("Run 'ai-start-task' first to create a session")
        sys.exit(1)

    # Get session files
    session_files = get_session_files(session_id)
    plan_file = session_files["plan"]

    if plan_file is None:
        print_error(f"Plan file not found for session {session_id}")
        sys.exit(1)

    # Read current content
    content = plan_file.read_text()

    # If show flag, display plan with progress
    if show:
        checked, total = count_checkboxes(content)
        percentage = int((checked / total) * 100) if total > 0 else 0

        print(f"\n📋 Plan for session {session_id}:\n")
        print(content)
        print(f"\nProgress: {checked}/{total} items complete ({percentage}%)\n")
        return

    # Item must be provided if not showing
    if item is None:
        print_error("Item text must be provided (or use --show)")
        sys.exit(1)

    # Find checkbox
    result = find_checkbox_line(content, item)

    if result is None:
        print_error(f"Checkbox item not found: {item}")
        print("Use 'ai-update-plan --show' to see all items")
        sys.exit(1)

    line_num, old_line = result

    # Update checkbox
    should_check = check and not uncheck
    new_line = toggle_checkbox(old_line, should_check)

    # Replace in content
    lines = content.split("\n")
    lines[line_num] = new_line
    new_content = "\n".join(lines)

    # Write back
    plan_file.write_text(new_content)

    # Log the update
    action = "Checked" if should_check else "Unchecked"
    try:
        log_execution(f"{action} plan item: {item}", level="success")
    except SystemExit:
        # If logging fails, continue anyway
        pass

    # Display updated section
    checked, total = count_checkboxes(new_content)
    percentage = int((checked / total) * 100) if total > 0 else 0

    print_success(f"Updated plan for session {session_id}:")
    print()
    section = extract_phase_section(new_content, line_num)
    print(section)
    print()
    print(f"Progress: {checked}/{total} items complete ({percentage}%)")


def main() -> None:
    """Main entry point for ai-update-plan command."""
    parser = argparse.ArgumentParser(
        description="Update checkboxes in session PLAN file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-update-plan "Write test file(s)"
  ai-update-plan "Run make check" --check
  ai-update-plan "Implement functionality" --uncheck
  ai-update-plan --show  # Show current plan
        """,
    )
    parser.add_argument(
        "item",
        nargs="?",
        help="Text of the checkbox item to update",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        default=True,
        help="Check the box (default)",
    )
    parser.add_argument(
        "--uncheck",
        action="store_true",
        help="Uncheck the box",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Show current plan with progress",
    )
    parser.add_argument(
        "--session-id",
        help="Specific session ID (default: most recent session)",
    )

    args = parser.parse_args()

    update_plan(
        item=args.item,
        check=args.check,
        uncheck=args.uncheck,
        show=args.show,
        session_id=args.session_id,
    )


if __name__ == "__main__":
    main()
