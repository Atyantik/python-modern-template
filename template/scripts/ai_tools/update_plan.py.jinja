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


def calculate_levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate Levenshtein distance between two strings.

    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one string
    into the other.

    Args:
        s1: First string
        s2: Second string

    Returns:
        Minimum edit distance between the strings
    """
    if len(s1) < len(s2):
        return calculate_levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    # Create distance matrix
    previous_row: list[int] = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Cost of substitution (0 if characters match, 1 if they don't)
            cost = 0 if c1 == c2 else 1
            # Minimum of: insert, delete, substitute
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + cost
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def find_similar_items(
    target: str,
    items: list[str],
    threshold: float = 0.6,
) -> list[tuple[str, float]]:
    """Find items similar to target using fuzzy matching.

    Uses both substring matching and Levenshtein distance to calculate
    similarity. Returns items above the similarity threshold, sorted by
    similarity (descending).

    Args:
        target: Target string to match against
        items: List of items to search
        threshold: Minimum similarity score (0.0 to 1.0) to include

    Returns:
        List of (item, similarity_score) tuples, sorted by similarity
    """
    if not items:
        return []

    target_lower = target.lower()
    results = []

    for item in items:
        item_lower = item.lower()

        # Check for substring match first (higher priority)
        if target_lower in item_lower:
            # Substring match - calculate score based on length ratio
            # Exact match = 1.0, substring = proportional to coverage
            if target_lower == item_lower:
                similarity = 1.0
            else:
                # Higher score if target covers more of the item
                similarity = 0.7 + (0.3 * len(target_lower) / len(item_lower))
        else:
            # Use Levenshtein distance for fuzzy matching
            distance = calculate_levenshtein_distance(target_lower, item_lower)

            # Convert distance to similarity score (0.0 to 1.0)
            max_len = max(len(target_lower), len(item_lower))
            similarity = 1.0 if max_len == 0 else 1.0 - (distance / max_len)

        # Include if above threshold
        if similarity >= threshold:
            results.append((item, similarity))

    # Sort by similarity (descending)
    results.sort(key=lambda x: x[1], reverse=True)

    return results


def validate_item_not_empty(item_text: str) -> str | None:
    """Validate that item text is not empty or whitespace-only.

    Args:
        item_text: Item text to validate

    Returns:
        Error message if invalid, None if valid
    """
    if not item_text or not item_text.strip():
        return (
            "Item text cannot be empty or whitespace-only. "
            "Please provide meaningful item text."
        )
    return None


def validate_phase_exists(plan_content: str, phase_name: str | None) -> str | None:
    """Validate that target phase exists in plan.

    Args:
        plan_content: Current plan content
        phase_name: Phase name to validate (None means "last phase", which is valid)

    Returns:
        Error message if phase not found, None if valid
    """
    if phase_name is None:
        # None means "add to last phase", which is always valid
        return None

    lines = plan_content.split("\n")
    phase_name_lower = phase_name.lower()

    # Find all phase headers
    available_phases = []
    for line in lines:
        if line.startswith("### Phase"):
            available_phases.append(line.strip())
            # Check if this line matches the target phase
            if phase_name_lower in line.lower():
                return None  # Phase found

    # Phase not found - build helpful error message
    if not available_phases:
        return (
            f"Phase '{phase_name}' does not exist. "
            f"No phases found in plan. Use --add-phase to create phases first."
        )

    phases_list = "\n  • ".join(available_phases)
    return (
        f"Phase '{phase_name}' does not exist in plan.\n\n"
        f"Available phases:\n  • {phases_list}\n\n"
        f"Use --add-phase to create it, or choose an existing phase."
    )


def validate_no_duplicates(plan_content: str, new_item: str) -> str | None:
    """Validate that item doesn't already exist in plan.

    Checks for duplicates using case-insensitive comparison with
    whitespace normalization.

    Args:
        plan_content: Current plan content
        new_item: New item text to validate

    Returns:
        Error message if duplicate found, None if valid
    """
    lines = plan_content.split("\n")

    # Normalize the new item for comparison
    new_item_normalized = " ".join(new_item.lower().split())

    for line in lines:
        # Check if line contains a checkbox
        match = re.match(r"^\s*-\s*\[([ x])\]\s*(.*)$", line)
        if match:
            existing_item = match.group(2)
            # Normalize existing item for comparison
            existing_normalized = " ".join(existing_item.lower().split())

            if new_item_normalized == existing_normalized:
                return (
                    f"Item '{new_item}' already exists in plan. "
                    f"Use --rename to modify it or --remove to delete it."
                )

    return None


def extract_all_checkbox_items(content: str) -> list[str]:
    """Extract all checkbox item texts from plan content.

    Args:
        content: Plan file content

    Returns:
        List of checkbox item texts (without checkbox markers)
    """
    lines = content.split("\n")
    items = []

    for line in lines:
        match = re.match(r"^\s*-\s*\[([ x])\]\s*(.*)$", line)
        if match:
            items.append(match.group(2))

    return items


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


def find_phase_section(content: str, phase_name: str) -> str:
    """Find and extract a phase section by name.

    Args:
        content: File content
        phase_name: Name or partial name of phase to find

    Returns:
        Phase section content, or empty string if not found
    """
    lines = content.split("\n")
    phase_name_lower = phase_name.lower()

    # Find phase header
    phase_start = -1
    for i, line in enumerate(lines):
        if line.startswith("### Phase") and phase_name_lower in line.lower():
            phase_start = i
            break

    if phase_start == -1:
        return ""

    # Find end of phase (next ### or end of file)
    phase_end = len(lines)
    for i in range(phase_start + 1, len(lines)):
        if lines[i].startswith("###"):
            phase_end = i
            break

    return "\n".join(lines[phase_start:phase_end])


def add_item_to_plan(
    plan_content: str,
    item_text: str,
    phase: str | None = None,
) -> str:
    """Add a new checklist item to plan.

    Args:
        plan_content: Current plan content
        item_text: Text of new item (without checkbox)
        phase: Phase name to add to (default: last phase)

    Returns:
        Updated plan content
    """
    lines = plan_content.split("\n")
    new_item = f"- [ ] {item_text}"

    # Find target phase
    if phase:
        phase_lower = phase.lower()
        target_phase_idx = -1

        for i, line in enumerate(lines):
            if line.startswith("### Phase") and phase_lower in line.lower():
                target_phase_idx = i
                break

        if target_phase_idx == -1:
            # Phase not found, add to end before ## sections
            insert_idx = len(lines)
            for i, line in enumerate(lines):
                if line.startswith("##") and not line.startswith("###"):
                    insert_idx = i
                    break
            lines.insert(insert_idx, new_item)
            lines.insert(insert_idx, "")  # Blank line before item
            return "\n".join(lines)

        # Find last checkbox in this phase
        insert_idx = target_phase_idx + 1
        for i in range(target_phase_idx + 1, len(lines)):
            if lines[i].startswith("###") and not lines[i].startswith("#### "):
                # Next phase found
                break
            if lines[i].startswith("##") and not lines[i].startswith("###"):
                # Non-phase section found
                break
            if re.match(r"^\s*-\s*\[([ x])\]", lines[i]):
                insert_idx = i + 1

        lines.insert(insert_idx, new_item)
    else:
        # No phase specified, add to last phase
        # Find last checkbox in entire plan
        last_checkbox_idx = -1
        for i, line in enumerate(lines):
            if re.match(r"^\s*-\s*\[([ x])\]", line):
                last_checkbox_idx = i

        if last_checkbox_idx == -1:
            # No checkboxes found, add to end
            lines.append(new_item)
        else:
            lines.insert(last_checkbox_idx + 1, new_item)

    return "\n".join(lines)


def remove_item_from_plan(
    plan_content: str,
    item_pattern: str,
) -> str:
    """Remove a checklist item from plan.

    Args:
        plan_content: Current plan content
        item_pattern: Pattern to match (case-insensitive, partial match)

    Returns:
        Updated plan content with item removed
    """
    lines = plan_content.split("\n")
    pattern_lower = item_pattern.lower()

    # Find and remove first matching checkbox item
    for i, line in enumerate(lines):
        if re.match(r"^\s*-\s*\[([ x])\]", line) and pattern_lower in line.lower():
            lines.pop(i)
            break

    return "\n".join(lines)


def rename_item_in_plan(
    plan_content: str,
    old_text: str,
    new_text: str,
) -> str:
    """Rename a checklist item in plan.

    Args:
        plan_content: Current plan content
        old_text: Current item text (partial match)
        new_text: New item text

    Returns:
        Updated plan content with item renamed
    """
    lines = plan_content.split("\n")
    old_lower = old_text.lower()

    # Find and rename first matching checkbox item
    for i, line in enumerate(lines):
        match = re.match(r"^(\s*-\s*\[([ x])\])\s*(.*)$", line)
        if match and old_lower in line.lower():
            # Preserve checkbox state and indentation
            checkbox_part = match.group(1)
            lines[i] = f"{checkbox_part} {new_text}"
            break

    return "\n".join(lines)


def add_phase_to_plan(
    plan_content: str,
    phase_name: str,
    items: list[str] | None = None,
) -> str:
    """Add a new phase section to plan.

    Args:
        plan_content: Current plan content
        phase_name: Name of new phase (e.g., "Phase 3: Deployment")
        items: Optional list of initial checklist items

    Returns:
        Updated plan content with new phase
    """
    lines = plan_content.split("\n")

    # Find where to insert (before ## sections that aren't ###)
    insert_idx = len(lines)
    for i, line in enumerate(lines):
        if line.startswith("##") and not line.startswith("###"):
            insert_idx = i
            break

    # Build phase section
    phase_lines = [f"### {phase_name}"]
    if items:
        for item in items:
            phase_lines.append(f"- [ ] {item}")
    phase_lines.append("")  # Blank line after phase

    # Insert phase
    for j, phase_line in enumerate(phase_lines):
        lines.insert(insert_idx + j, phase_line)

    return "\n".join(lines)


def update_plan(
    item: str | None = None,
    check: bool = True,
    uncheck: bool = False,
    show: bool = False,
    session_id: str | None = None,
    # New editing parameters
    add: str | None = None,
    remove: str | None = None,
    rename: str | None = None,
    to: str | None = None,
    add_phase: str | None = None,
    phase: str | None = None,
) -> None:
    """Update plan: check items OR edit plan structure.

    Backward compatible: defaults to checkbox mode.

    Modes of operation:
    1. Checkbox mode (default): Check/uncheck items
    2. Edit mode: Add/remove/rename items and phases

    Args:
        item: Text of the checkbox item to update (checkbox mode)
        check: Check the box (checkbox mode, default)
        uncheck: Uncheck the box (checkbox mode)
        show: Show current plan with progress (both modes)
        session_id: Session ID (default: most recent)

        add: Add new checklist item (edit mode)
        remove: Remove checklist item (edit mode)
        rename: Rename existing item (edit mode)
        to: New name for renamed item (edit mode, requires rename)
        add_phase: Add new phase section (edit mode)
        phase: Target phase for new item (edit mode, optional with add)
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

    # Determine mode based on which parameters are provided
    is_edit_mode = any([add, remove, rename, add_phase])

    if is_edit_mode:
        # EDIT MODE: Handle add/remove/rename operations
        new_content = content

        # Handle add operation
        if add:
            # Validate item is not empty
            empty_error = validate_item_not_empty(add)
            if empty_error:
                print_error(empty_error)
                sys.exit(1)

            # Validate phase exists (if specified)
            phase_error = validate_phase_exists(new_content, phase)
            if phase_error:
                print_error(phase_error)
                sys.exit(1)

            # Validate no duplicates
            duplicate_error = validate_no_duplicates(new_content, add)
            if duplicate_error:
                print_error(duplicate_error)
                sys.exit(1)

            new_content = add_item_to_plan(new_content, add, phase=phase)
            action = f"Added item: {add}"
            if phase:
                action += f" to {phase}"

        # Handle remove operation
        elif remove:
            new_content = remove_item_from_plan(new_content, remove)
            action = f"Removed item: {remove}"

        # Handle rename operation
        elif rename:
            if to is None:
                print_error("--to parameter required when using --rename")
                sys.exit(1)

            # Validate new item name is not empty
            empty_error = validate_item_not_empty(to)
            if empty_error:
                print_error(empty_error)
                sys.exit(1)

            new_content = rename_item_in_plan(new_content, rename, to)
            action = f"Renamed item: {rename} -> {to}"

        # Handle add-phase operation
        elif add_phase:
            new_content = add_phase_to_plan(new_content, add_phase)
            action = f"Added phase: {add_phase}"

        # Write back to file
        plan_file.write_text(new_content)

        # Log the update
        try:
            log_execution(action, level="success")
        except SystemExit:
            # If logging fails, continue anyway
            pass

        # Display success message
        checked, total = count_checkboxes(new_content)
        percentage = int((checked / total) * 100) if total > 0 else 0

        print_success(f"Updated plan for session {session_id}:")
        print()
        print(action)
        print()
        print(f"Progress: {checked}/{total} items complete ({percentage}%)")
        return

    # CHECKBOX MODE: Original behavior (backward compatible)
    # Item must be provided if not showing
    if item is None:
        print_error("Item text must be provided (or use --show)")
        sys.exit(1)

    # Find checkbox
    result = find_checkbox_line(content, item)

    if result is None:
        print_error(f"Checkbox item not found: {item}")

        # Show fuzzy suggestions
        all_items = extract_all_checkbox_items(content)
        suggestions = find_similar_items(item, all_items, threshold=0.5)

        if suggestions:
            print("\nDid you mean:")
            # Show top 3 suggestions
            for suggested_item, similarity in suggestions[:3]:
                print(f"  • {suggested_item} (similarity: {similarity:.0%})")

        print("\nUse 'ai-update-plan --show' to see all items")
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
        description="Update checkboxes in session PLAN file OR edit plan structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Checkbox Mode Examples:
  ai-update-plan "Write test file(s)"
  ai-update-plan "Run make check" --check
  ai-update-plan "Implement functionality" --uncheck
  ai-update-plan --show  # Show current plan

Edit Mode Examples:
  ai-update-plan --add "New checklist item"
  ai-update-plan --add "New item in phase 2" --phase="Phase 2"
  ai-update-plan --remove "Old item"
  ai-update-plan --rename "Old name" --to "New name"
  ai-update-plan --add-phase "Phase 3: Deployment"
        """,
    )
    parser.add_argument(
        "item",
        nargs="?",
        help="Text of the checkbox item to update (checkbox mode)",
    )

    # Checkbox mode arguments
    checkbox_group = parser.add_argument_group("checkbox mode")
    checkbox_group.add_argument(
        "--check",
        action="store_true",
        default=True,
        help="Check the box (default)",
    )
    checkbox_group.add_argument(
        "--uncheck",
        action="store_true",
        help="Uncheck the box",
    )

    # Edit mode arguments
    edit_group = parser.add_argument_group("edit mode")
    edit_group.add_argument(
        "--add",
        help="Add new checklist item to plan",
    )
    edit_group.add_argument(
        "--remove",
        help="Remove checklist item from plan",
    )
    edit_group.add_argument(
        "--rename",
        help="Rename existing checklist item",
    )
    edit_group.add_argument(
        "--to",
        help="New name for renamed item (requires --rename)",
    )
    edit_group.add_argument(
        "--add-phase",
        help="Add new phase section to plan",
    )
    edit_group.add_argument(
        "--phase",
        help="Target phase for new item (optional with --add)",
    )

    # Common arguments
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
        add=args.add,
        remove=args.remove,
        rename=args.rename,
        to=args.to,
        add_phase=args.add_phase,
        phase=args.phase,
    )


if __name__ == "__main__":
    main()
