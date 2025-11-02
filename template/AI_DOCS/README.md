# AI Documentation (Shared)

> **Single source of truth for all AI coding assistants**

This directory contains shared documentation referenced by all AI tool configurations. Changes made here automatically apply to all tools that support file references.

## 📚 Documentation Files

| File | Purpose | Who Uses It |
|------|---------|-------------|
| **tdd-workflow.md** | Test-Driven Development process, testing standards, coverage requirements | All AI tools |
| **ai-tools.md** | AI session management workflow (MANDATORY for all agents) | All AI tools |
| **code-conventions.md** | Code style, formatting, best practices, documentation standards | All AI tools |
| **project-context.md** | Tech stack, architecture, dependencies, CI/CD pipeline | All AI tools |

## 🔗 How Tools Reference These Docs

### ✅ Auto-Reference (Supports File Includes)

These tools automatically read the shared documentation:

1. **Cursor IDE** (`.cursorrules`)
   - Uses `@AI_DOCS/filename.md` syntax
   - Example: `@AI_DOCS/tdd-workflow.md`

2. **Claude Code** (`CLAUDE.md`)
   - Uses `@AI_DOCS/filename.md` syntax
   - Example: `@AI_DOCS/ai-tools.md`

3. **Gemini Code Assist** (`AGENTS.md`)
   - Uses `@AI_DOCS/filename.md` syntax
   - Example: `@AI_DOCS/code-conventions.md`

4. **Aider AI** (`.aider.conf.yml`)
   - Uses YAML `read:` parameter
   - Example:
     ```yaml
     read:
       - AI_DOCS/tdd-workflow.md
       - AI_DOCS/ai-tools.md
     ```

### ⚠️  Manual Sync Required (No File Reference Support)

These tools require manual content duplication:

1. **GitHub Copilot** (`.github/copilot-instructions.md`)
   - Does NOT support file references
   - Content must be manually copied
   - Has sync warning comment at top

2. **Gemini Code Assist** (`.gemini/styleguide.md`)
   - Does NOT support file references for styleguide.md
   - Content must be manually copied
   - Has sync warning comment at top

**When updating shared docs**, remember to manually sync content to these 2 files!

## 📝 How to Update Documentation

### For Changes That Apply to All Tools

1. **Edit the shared documentation file** in `AI_DOCS/`
   ```bash
   # Example: Update TDD workflow
   vim AI_DOCS/tdd-workflow.md
   ```

2. **Tools with auto-reference get updates automatically**:
   - Cursor IDE
   - Claude Code
   - Gemini (AGENTS.md)
   - Aider AI

3. **Manually sync to non-supporting tools**:
   ```bash
   # Copy relevant sections to:
   vim .github/copilot-instructions.md
   vim .gemini/styleguide.md
   ```

4. **Add sync warning comment** at the top of manually synced files:
   ```markdown
   <!-- ⚠️  SYNC WARNING: Content duplicated from AI_DOCS/ -->
   <!-- When AI_DOCS/ changes, manually update this file -->
   ```

### For Tool-Specific Changes

If the change only applies to one tool, edit that tool's config file directly:

- **Cursor**: `.cursorrules`
- **Claude**: `CLAUDE.md`
- **Gemini (universal)**: `AGENTS.md`
- **Gemini (style guide)**: `.gemini/styleguide.md`
- **GitHub Copilot**: `.github/copilot-instructions.md`
- **Aider**: `.aider.conf.yml`

## 🔍 What Goes Where?

### Shared Docs (AI_DOCS/)

Content that applies to **all AI tools**:
- TDD workflow and testing principles
- AI session management (ai-start-task, ai-log, etc.)
- Code conventions and style guides
- Project architecture and tech stack
- Quality gates and standards

### Tool-Specific Configs

Content that is **unique to each tool**:
- Tool-specific examples
- Tool-specific workflow instructions
- Integration with tool-specific features
- Communication style guidelines

## 📖 Quick Reference

### For AI Agents

**Always read these first**:
```
@AI_DOCS/ai-tools.md         # Session management (MANDATORY)
@AI_DOCS/tdd-workflow.md     # TDD process
@AI_DOCS/code-conventions.md # Code standards
@AI_DOCS/project-context.md  # Architecture
```

Then read your tool-specific config:
- Cursor → `.cursorrules`
- Claude → `CLAUDE.md`
- Gemini → `AGENTS.md` + `.gemini/styleguide.md`
- Copilot → `.github/copilot-instructions.md`
- Aider → `.aider.conf.yml`

### For Developers

**When adding a new workflow or pattern**:
1. Add to appropriate shared doc in `AI_DOCS/`
2. Test with `@AI_DOCS/filename.md` reference
3. Manually sync to Copilot and Gemini styleguide
4. Document the change in this README if needed

**When fixing a tool-specific issue**:
1. Edit that tool's config file directly
2. Don't add to shared docs unless it applies to all

## 🎯 Benefits of This Structure

### Single Source of Truth
- Update once, applies everywhere (for supporting tools)
- Reduces duplication and inconsistency
- Easier to maintain and keep in sync

### Clear Separation
- Shared standards in `AI_DOCS/`
- Tool-specific adaptations in tool configs
- Easy to see what's universal vs. tool-specific

### Better Organization
- Related documentation grouped together
- Easier to find information
- Clearer responsibilities

## 🔒 Important Rules

### DO ✅
- Update shared docs for universal changes
- Reference shared docs via `@AI_DOCS/` syntax
- Manually sync to Copilot and Gemini when shared docs change
- Add sync warning comments to manually synced content
- Keep shared docs focused on common patterns

### DON'T ❌
- Duplicate content unnecessarily
- Add tool-specific examples to shared docs
- Forget to sync manual-copy files
- Remove the `@AI_DOCS/` references from tool configs
- Mix universal and tool-specific content

## 📊 File Reference Support Matrix

| Tool | Config File | Supports References | Sync Method |
|------|-------------|---------------------|-------------|
| Cursor | `.cursorrules` | ✅ Yes (`@AI_DOCS/`) | Automatic |
| Claude Code | `CLAUDE.md` | ✅ Yes (`@AI_DOCS/`) | Automatic |
| Gemini (universal) | `AGENTS.md` | ✅ Yes (`@AI_DOCS/`) | Automatic |
| Aider | `.aider.conf.yml` | ✅ Yes (YAML `read:`) | Automatic |
| GitHub Copilot | `.github/copilot-instructions.md` | ❌ No | Manual copy |
| Gemini (style) | `.gemini/styleguide.md` | ❌ No | Manual copy |

## 🚀 Migration Notes

This structure was introduced on 2025-11-02 to consolidate AI documentation and reduce duplication.

### What Changed
- Created `AI_DOCS/` directory with 4 shared files
- Updated 4 tool configs to reference shared docs
- Identified 2 tools requiring manual sync
- Reduced total documentation size by ~60%

### Benefits Achieved
- Single source of truth for common patterns
- Easier maintenance and updates
- Consistent instructions across all tools
- Clear documentation hierarchy

---

**For complete project documentation, see the main `README.md` in the project root.**
