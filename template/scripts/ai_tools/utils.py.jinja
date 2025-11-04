"""Shared utilities for AI tools."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Any


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path to project root
    """
    # Scripts are in scripts/ai_tools/, project root is two levels up
    return Path(__file__).parent.parent.parent


def get_context_dir() -> Path:
    """Get the .ai-context directory.

    Returns:
        Path to .ai-context directory
    """
    return get_project_root() / ".ai-context"


def get_sessions_dir() -> Path:
    """Get the sessions directory.

    Returns:
        Path to .ai-context/sessions directory
    """
    return get_context_dir() / "sessions"


def get_archive_dir() -> Path:
    """Get the archive directory.

    Returns:
        Path to .ai-context/sessions/archive directory
    """
    return get_sessions_dir() / "archive"


def create_session_id() -> str:
    """Create a timestamp-based session ID.

    Returns:
        Session ID in format YYYYMMDDHHMMSS
    """
    return datetime.now().strftime("%Y%m%d%H%M%S")


def slugify(text: str, max_length: int = 50) -> str:
    """Convert text to URL-friendly slug.

    Args:
        text: Text to slugify
        max_length: Maximum length of slug

    Returns:
        Slugified text
    """
    # Convert to lowercase
    slug = text.lower()

    # Replace spaces and underscores with hyphens
    slug = re.sub(r"[\s_]+", "-", slug)

    # Remove non-alphanumeric characters except hyphens
    slug = re.sub(r"[^a-z0-9-]", "", slug)

    # Remove consecutive hyphens
    slug = re.sub(r"-+", "-", slug)

    # Trim hyphens from start and end
    slug = slug.strip("-")

    # Limit length
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip("-")

    return slug or "task"


def create_session_filename(session_id: str, file_type: str, task_name: str) -> str:
    """Create a session filename.

    Args:
        session_id: Session ID (YYYYMMDDHHMMSS)
        file_type: Type of file (PLAN, SUMMARY, EXECUTION)
        task_name: Name of the task

    Returns:
        Filename in format YYYYMMDDHHMMSS-TYPE-slug.md
    """
    slug = slugify(task_name)
    return f"{session_id}-{file_type.upper()}-{slug}.md"


def get_current_session() -> str | None:
    """Get the most recent session ID.

    Returns:
        Session ID of most recent session, or None if no sessions exist
    """
    sessions_dir = get_sessions_dir()

    if not sessions_dir.exists():
        return None

    # Find all PLAN files (one per session)
    plan_files = list(sessions_dir.glob("*-PLAN-*.md"))

    if not plan_files:
        return None

    # Sort by filename (which starts with timestamp)
    plan_files.sort(reverse=True)

    # Extract session ID from filename (first 14 characters)
    latest_file = plan_files[0].name
    return latest_file[:14]


def get_session_files(session_id: str) -> dict[str, Path | None]:
    """Get all files for a session.

    Args:
        session_id: Session ID

    Returns:
        Dictionary with keys 'plan', 'summary', 'execution' and Path values
    """
    sessions_dir = get_sessions_dir()

    # Find files matching this session ID
    plan_file = list(sessions_dir.glob(f"{session_id}-PLAN-*.md"))
    summary_file = list(sessions_dir.glob(f"{session_id}-SUMMARY-*.md"))
    execution_file = list(sessions_dir.glob(f"{session_id}-EXECUTION-*.md"))

    return {
        "plan": plan_file[0] if plan_file else None,
        "summary": summary_file[0] if summary_file else None,
        "execution": execution_file[0] if execution_file else None,
    }


def read_context_file(filename: str) -> str:
    """Read a context file from .ai-context/.

    Args:
        filename: Name of the context file

    Returns:
        Contents of the file
    """
    context_dir = get_context_dir()
    file_path = context_dir / filename

    if not file_path.exists():
        return ""

    return file_path.read_text()


def write_context_file(filename: str, content: str) -> None:
    """Write to a context file in .ai-context/.

    Args:
        filename: Name of the context file
        content: Content to write
    """
    context_dir = get_context_dir()
    file_path = context_dir / filename

    # Ensure directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(content)


def append_to_file(file_path: Path, content: str) -> None:
    """Append content to a file.

    Args:
        file_path: Path to file
        content: Content to append
    """
    with file_path.open("a") as f:
        f.write(content)


def format_timestamp(dt: datetime | None = None) -> str:
    """Format a datetime as a readable timestamp.

    Args:
        dt: Datetime to format (default: now)

    Returns:
        Formatted timestamp
    """
    if dt is None:
        dt = datetime.now()

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_recent_sessions(count: int = 5) -> list[dict[str, Any]]:
    """Get information about recent sessions.

    Args:
        count: Number of recent sessions to get

    Returns:
        List of session info dictionaries
    """
    sessions_dir = get_sessions_dir()

    if not sessions_dir.exists():
        return []

    # Find all SUMMARY files
    summary_files = list(sessions_dir.glob("*-SUMMARY-*.md"))

    if not summary_files:
        return []

    # Sort by filename (timestamp)
    summary_files.sort(reverse=True)

    # Get the most recent N
    recent_files = summary_files[:count]

    sessions = []
    for summary_file in recent_files:
        # Extract session ID and task name
        filename = summary_file.name
        session_id = filename[:14]
        parts = filename[:-3].split("-", 2)  # Remove .md and split
        task_slug = parts[2] if len(parts) > 2 else "unknown"

        # Read summary for details
        content = summary_file.read_text()

        sessions.append(
            {
                "session_id": session_id,
                "task_slug": task_slug,
                "summary_file": summary_file,
                "content": content,
            }
        )

    return sessions


def print_success(message: str) -> None:
    """Print a success message.

    Args:
        message: Message to print
    """
    print(f"✅ {message}")


def print_error(message: str) -> None:
    """Print an error message.

    Args:
        message: Message to print
    """
    print(f"❌ {message}")


def print_info(message: str) -> None:
    """Print an info message.

    Args:
        message: Message to print
    """
    print(f"ℹ️  {message}")


def print_warning(message: str) -> None:
    """Print a warning message.

    Args:
        message: Message to print
    """
    print(f"⚠️  {message}")


def print_header(message: str) -> None:
    """Print a header message.

    Args:
        message: Message to print
    """
    print(f"\n{'=' * 60}")
    print(f"  {message}")
    print(f"{'=' * 60}\n")
