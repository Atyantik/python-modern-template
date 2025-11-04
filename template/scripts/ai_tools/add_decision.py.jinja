"""AI Add Decision tool - adds architectural/design decisions."""

from __future__ import annotations

import argparse
import sys

from scripts.ai_tools.log_execution import log_execution
from scripts.ai_tools.utils import (
    format_timestamp,
    print_success,
    read_context_file,
    write_context_file,
)


def get_multiline_input(prompt: str) -> list[str]:
    """Get multiple lines of input from user.

    Args:
        prompt: Prompt to display

    Returns:
        List of input lines
    """
    print(prompt)
    lines = []
    while True:
        try:
            line = input("> ")
            if not line:  # Empty line to finish
                break
            lines.append(line)
        except EOFError:
            break
    return lines


def format_decision_entry(
    title: str,
    rationale: list[str],
    impact: list[str],
    implementation: str,
    files: list[str],
    status: str,
) -> str:
    """Format a decision entry.

    Args:
        title: Decision title
        rationale: List of rationale points
        impact: List of impact points
        implementation: Implementation details
        files: List of affected files
        status: Decision status

    Returns:
        Formatted decision entry
    """
    timestamp = format_timestamp()

    # Map status to emoji
    status_emoji_map = {
        "Implemented": "✅",
        "In Progress": "🚧",
        "Paused": "⏸️",
        "Rejected": "❌",
    }
    status_emoji = status_emoji_map.get(status, "📋")

    # Format rationale
    rationale_text = "\n".join(f"- {r}" for r in rationale)

    # Format impact
    impact_text = "\n".join(f"- {i}" for i in impact)

    # Format files
    files_text = "\n".join(f"- `{f}`" for f in files) if files else "- None"

    entry = f"""## [{timestamp}] {title}

**Decision**: {title}

**Rationale**:
{rationale_text}

**Impact**:
{impact_text}

**Implementation**:
{implementation}

**Files Affected**:
{files_text}

**Status**: {status_emoji} {status}

---

"""
    return entry


def add_decision(
    title: str | None = None,
    rationale: list[str] | None = None,
    impact: list[str] | None = None,
    implementation: str | None = None,
    files: list[str] | None = None,
    status: str = "Implemented",
) -> None:
    """Add decision to RECENT_DECISIONS.md.

    Args:
        title: Decision title (default: prompt)
        rationale: List of rationale points (default: prompt)
        impact: List of impact points (default: prompt)
        implementation: Implementation details (default: prompt)
        files: List of affected files (default: prompt)
        status: Decision status (default: Implemented)
    """
    print("\n📋 Add Architectural Decision\n")

    # Prompt for missing information
    if title is None:
        title = input("Title: ").strip()
        if not title:
            print("Error: Title is required")
            sys.exit(1)

    if rationale is None:
        rationale = get_multiline_input(
            "\nRationale (one point per line, empty line to finish):"
        )
        if not rationale:
            rationale = ["No rationale provided"]

    if impact is None:
        impact = get_multiline_input(
            "\nImpact (one point per line, empty line to finish):"
        )
        if not impact:
            impact = ["No impact specified"]

    if implementation is None:
        implementation = input("\nImplementation details: ").strip()
        if not implementation:
            implementation = "No implementation details provided"

    if files is None:
        files_input = get_multiline_input(
            "\nFiles affected (one per line, empty line to finish):"
        )
        files = files_input if files_input else []

    # Read current decisions file
    decisions_content = read_context_file("RECENT_DECISIONS.md")

    # If file is empty or doesn't exist, add header
    if not decisions_content or decisions_content.strip() == "":
        decisions_content = "# Recent Decisions\n\n"

    # Format new decision
    new_entry = format_decision_entry(
        title=title,
        rationale=rationale,
        impact=impact,
        implementation=implementation,
        files=files,
        status=status,
    )

    # Insert after header (most recent first)
    lines = decisions_content.split("\n")
    header_end = 0

    # Find end of header (after # Recent Decisions)
    for i, line in enumerate(lines):
        if line.startswith("# Recent Decisions"):
            # Skip to next non-empty line
            for j in range(i + 1, len(lines)):
                if lines[j].strip() and not lines[j].startswith("#"):
                    header_end = j
                    break
            if header_end == 0:
                header_end = i + 2  # After header + blank line
            break

    # Insert new entry
    lines.insert(header_end, new_entry)
    new_content = "\n".join(lines)

    # Write back
    write_context_file("RECENT_DECISIONS.md", new_content)

    # Log to execution file
    try:
        log_execution(f"Added decision: {title}", level="success")
    except SystemExit:
        # If logging fails, continue anyway
        pass

    print_success("Decision added to RECENT_DECISIONS.md")
    print()


def main() -> None:
    """Main entry point for ai-add-decision command."""
    parser = argparse.ArgumentParser(
        description="Add architectural/design decision",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-add-decision  # Interactive mode
  ai-add-decision --title="Use PostgreSQL for storage"
        """,
    )
    parser.add_argument(
        "--title",
        help="Decision title",
    )
    parser.add_argument(
        "--status",
        choices=["Implemented", "In Progress", "Paused", "Rejected"],
        default="Implemented",
        help="Decision status (default: Implemented)",
    )

    args = parser.parse_args()

    add_decision(
        title=args.title,
        status=args.status,
    )


if __name__ == "__main__":
    main()
