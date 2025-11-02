"""AI Add Convention tool - adds code conventions."""

from __future__ import annotations

import argparse
import re
import sys

from scripts.ai_tools.log_execution import log_execution
from scripts.ai_tools.utils import (
    print_success,
    read_context_file,
    write_context_file,
)


def extract_sections(content: str) -> list[str]:
    """Extract section names from conventions file.

    Args:
        content: Content of CONVENTIONS.md

    Returns:
        List of section names
    """
    sections = []
    pattern = r"##\s+([^\n]+)"
    matches = re.findall(pattern, content)

    for match in matches:
        sections.append(match.strip())

    return sections


def format_convention_entry(
    title: str,
    description: str,
    correct_example: str,
    wrong_example: str,
) -> str:
    """Format a convention entry.

    Args:
        title: Convention title
        description: Convention description
        correct_example: Correct example code
        wrong_example: Wrong example code

    Returns:
        Formatted convention entry
    """
    entry = f"""### {title}

{description}

```python
# ✅ Correct
{correct_example}

# ❌ Wrong
{wrong_example}
```

"""
    return entry


def add_convention(
    section: str | None = None,
    title: str | None = None,
    description: str | None = None,
    examples: dict[str, str] | None = None,
) -> None:
    """Add convention to CONVENTIONS.md.

    Args:
        section: Section name (default: prompt)
        title: Convention title (default: prompt)
        description: Convention description (default: prompt)
        examples: Dict of {"correct": "...", "wrong": "..."} (default: prompt)
    """
    print("\n📋 Add Code Convention\n")

    # Read current conventions file
    conventions_content = read_context_file("CONVENTIONS.md")

    # If file is empty or doesn't exist, create with header
    if not conventions_content or conventions_content.strip() == "":
        conventions_content = "# Conventions\n\n"

    # Extract existing sections
    sections = extract_sections(conventions_content)

    # Prompt for section
    if section is None:
        if sections:
            print("Existing sections:")
            for i, s in enumerate(sections, 1):
                print(f"  {i}. {s}")
            print(f"  {len(sections) + 1}. [Create new section]")
            print()

            try:
                choice = input(f"Select section [1-{len(sections) + 1}]: ").strip()
                choice_num = int(choice)

                if 1 <= choice_num <= len(sections):
                    section = sections[choice_num - 1]
                else:
                    section = input("New section name: ").strip()
            except (ValueError, IndexError):
                section = input("Section name: ").strip()
        else:
            section = input("Section name: ").strip()

    if not section:
        print("Error: Section is required")
        sys.exit(1)

    # Prompt for other fields
    if title is None:
        title = input("\nTitle: ").strip()
        if not title:
            print("Error: Title is required")
            sys.exit(1)

    if description is None:
        description = input("\nDescription: ").strip()
        if not description:
            description = "No description provided"

    if examples is None:
        print()
        correct = input("Correct example:\n> ").strip()
        print()
        wrong = input("Wrong example:\n> ").strip()
        examples = {"correct": correct, "wrong": wrong}

    # Format new convention
    new_entry = format_convention_entry(
        title=title,
        description=description,
        correct_example=examples.get("correct", ""),
        wrong_example=examples.get("wrong", ""),
    )

    # Find section in content
    section_pattern = rf"(##\s+{re.escape(section)}.*?)(?=##|$)"
    section_match = re.search(section_pattern, conventions_content, re.DOTALL)

    if section_match:
        # Section exists - append to it
        section_content = section_match.group(1)
        new_section = section_content + new_entry

        conventions_content = conventions_content.replace(section_content, new_section)
    else:
        # Section doesn't exist - create it
        new_section = f"## {section}\n\n{new_entry}"
        conventions_content += "\n" + new_section

    # Write back
    write_context_file("CONVENTIONS.md", conventions_content)

    # Log to execution file
    try:
        log_execution(f"Added convention: {title} ({section})", level="success")
    except SystemExit:
        # If logging fails, continue anyway
        pass

    print_success(f"Convention added to CONVENTIONS.md ({section} section)")
    print()


def main() -> None:
    """Main entry point for ai-add-convention command."""
    parser = argparse.ArgumentParser(
        description="Add code convention",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-add-convention  # Interactive mode
  ai-add-convention --section="Error Handling" --title="Use specific exceptions"
        """,
    )
    parser.add_argument(
        "--section",
        help="Section name",
    )
    parser.add_argument(
        "--title",
        help="Convention title",
    )

    args = parser.parse_args()

    add_convention(
        section=args.section,
        title=args.title,
    )


if __name__ == "__main__":
    main()
