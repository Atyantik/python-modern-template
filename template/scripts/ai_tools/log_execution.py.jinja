"""AI Log tool - logs execution progress to session EXECUTION file."""

from __future__ import annotations

import argparse
import sys

from scripts.ai_tools.utils import (
    append_to_file,
    format_timestamp,
    get_current_session,
    get_session_files,
    print_error,
    print_success,
)


def get_emoji_for_level(level: str) -> str:
    """Get emoji for log level.

    Args:
        level: Log level (info, warning, error, success)

    Returns:
        Emoji character
    """
    emoji_map = {
        "info": "📝",
        "warning": "⚠️ ",
        "error": "❌",
        "success": "✅",
    }
    return emoji_map.get(level, "📝")


def check_log_specificity(message: str) -> list[str]:
    """Check if log message includes specific details.

    Args:
        message: Log message to check

    Returns:
        List of suggestions for improving specificity
    """
    suggestions = []

    # Check for vague phrases
    vague_phrases = [
        (
            "write test",
            "Which test file? Example: 'Wrote tests in tests/test_feature.py'",
        ),
        (
            "update file",
            "Which file? Example: 'Updated src/module.py with new function'",
        ),
        (
            "add feature",
            "Which feature file? Example: 'Added validation to src/auth.py'",
        ),
        (
            "fix bug",
            "Which file/function? Example: 'Fixed validation bug in src/auth.py:validate_email()'",
        ),
        (
            "implement",
            "Which file/module? Be specific about location and what was implemented",
        ),
    ]

    message_lower = message.lower()
    for vague_phrase, suggestion in vague_phrases:
        if vague_phrase in message_lower and not any(
            ext in message_lower for ext in [".py", ".md", ".txt", ".yml", ".toml"]
        ):
            suggestions.append(suggestion)
            break  # Only show one suggestion

    return suggestions


def log_execution(
    message: str,
    level: str = "info",
    session_id: str | None = None,
) -> None:
    """Log execution progress to EXECUTION file with specific details.

    IMPORTANT: Include specific file names, test names, or function names in your log messages.
    This helps with execution verification and provides clear audit trail.

    Good examples:
    - "Wrote tests in tests/ai_tools/test_feature.py (3 test cases)"
    - "Implemented validate_email() in src/auth.py"
    - "Updated User model in src/models/user.py to add email field"
    - "Fixed bug in calculate_total() at src/billing.py:45"

    Bad examples (too vague):
    - "Wrote some tests"
    - "Updated a file"
    - "Fixed a bug"

    Args:
        message: Log message with specific details (file names, function names, etc.)
        level: Log level (info, warning, error, success)
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
    execution_file = session_files["execution"]

    if execution_file is None:
        print_error(f"Execution file not found for session {session_id}")
        sys.exit(1)

    # Check log specificity
    suggestions = check_log_specificity(message)

    # Format log entry
    timestamp = format_timestamp()
    emoji = get_emoji_for_level(level)
    log_entry = f"[{timestamp}] {emoji} {message}\n"

    # Append to file
    append_to_file(execution_file, log_entry)

    # Display confirmation
    print_success(f"Logged to session {session_id}:")
    print(f"   {log_entry.strip()}")

    # Show suggestions if log is vague
    if suggestions:
        print("\n💡 Tip: Consider being more specific in your log messages:")
        for suggestion in suggestions:
            print(f"   {suggestion}")
        print()


def main() -> None:
    """Main entry point for ai-log command."""
    parser = argparse.ArgumentParser(
        description="Log execution progress to current session",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-log "Created test file"
  ai-log "All tests passing" --level success
  ai-log "Found an issue" --level warning
  ai-log "Test failed" --level error
        """,
    )
    parser.add_argument(
        "message",
        help="Log message to record",
    )
    parser.add_argument(
        "--level",
        choices=["info", "warning", "error", "success"],
        default="info",
        help="Log level (default: info)",
    )
    parser.add_argument(
        "--session-id",
        help="Specific session ID (default: most recent session)",
    )

    args = parser.parse_args()

    log_execution(
        message=args.message,
        level=args.level,
        session_id=args.session_id,
    )


if __name__ == "__main__":
    main()
