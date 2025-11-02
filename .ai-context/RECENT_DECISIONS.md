# Recent Decisions

## Git Commits: No AI Co-Authoring (2025-11-02)

**Decision**: Never add AI co-author attribution to git commits
**Rationale**:
- Commits should represent human intent and responsibility
- Professional git history without AI attribution
- Clear accountability for code changes
- Industry standard practice
**Implementation**:
- Added CRITICAL rule to AI_DOCS/code-conventions.md
- Duplicated in .gemini/styleguide.md
- Duplicated in .github/copilot-instructions.md
- Applied to both root and template directories
- Rule: No "Co-Authored-By: Claude" or "Generated with [AI Tool]" in commits
**Status**: Implemented

## AI-Generated Summaries Location (2025-11-02)

**Decision**: All AI-generated summaries must go in `.ai-summary/` directory
**Rationale**:
- Prevents accidental commits of AI tool output
- Keeps git history clean and professional
- Separates code from AI artifacts
- Consistent across all AI assistants
**Implementation**:
- Added `.ai-summary/` to .gitignore (root and template)
- Added CRITICAL rule to AI_DOCS/code-conventions.md
- Duplicated in .gemini/styleguide.md
- Duplicated in .github/copilot-instructions.md
- Applied to both root and template directories
**Status**: Implemented

## AI Instructions: No Decorative Emojis (2025-11-02)

**Decision**: Add CRITICAL emoji prohibition rule to all AI agent configurations
**Rationale**: Professional appearance, universal compatibility, accessibility, Atyantik branding
**Implementation**:
- Added to AI_DOCS/code-conventions.md (shared by Claude, Cursor, Aider, Agents)
- Duplicated in .gemini/styleguide.md (Gemini doesn't support file references)
- Duplicated in .github/copilot-instructions.md (Copilot doesn't support file references)
- Applied to both root and template directories
- Rule: No decorative emojis (🚀🎯🐳 etc), only functional checkboxes (✅❌)
**Pattern**: Use AI_DOCS/ for shared rules, duplicate only for Gemini/Copilot
**Status**: Implemented

## Documentation Style (2025-11-02)

**Decision**: Remove all decorative emojis from documentation
**Rationale**: Professional appearance, universal compatibility, accessibility
**Impact**: All .md files updated, code output cleaned
**Status**: Implemented

## Examples Strategy (2025-11-02)

**Decision**: Don't track generated examples in git
**Rationale**:
- Keeps repository lightweight (~200 files saved)
- Examples always fresh from latest template
- Standard practice for template repos

**Implementation**:
- Track only: README.md, generate-all.sh, .gitkeep
- Ignore: 7 generated project directories
**Status**: Implemented

## Project Naming (2025-11-02)

**Decision**: Rename to `python-modern-template`
**From**: `leadership-blog-generator`
**Rationale**: Accurately reflects purpose as a template
**Author**: Atyantik Technologies Private Limited
**Status**: Complete (pending root directory rename)

## AI Tools Integration (2025-11-02)

**Decision**: Support multiple AI assistants
**Tools Included**: Claude Code, Cursor, Copilot, Gemini, Aider
**Config Files**: Each AI has dedicated config file
**Session Management**: Optional, configurable via `include_ai_tools`
**Status**: Implemented

## Template Architecture (2025-11-02)

**Decision**: Use Copier over Cookiecutter
**Rationale**:
- Template update capabilities
- Modern YAML configuration
- Better uv integration
**Status**: Implemented

## Quality Standards (2025-11-02)

**Decision**: Single source of truth in pyproject.toml
**Coverage**: Minimum 80%, target 100%
**Tools**: Black, Ruff, mypy, Pylint, pytest, Bandit
**TDD**: Required - tests before implementation
**Status**: Implemented and enforced
