# Documentation-First Approach

> **Shared documentation for all AI coding assistants**
>
> This file is referenced by multiple AI tool configurations. Changes here automatically apply to all tools that support file references.

## 🚨 CRITICAL: Research Before Implementation

**Before implementing ANY task, you MUST research and discover existing solutions, tools, and documentation.**

This is NOT optional. Every AI agent must follow this workflow to avoid over-engineering and reinventing the wheel.

## ❌ Common Anti-Pattern (DO NOT DO THIS)

**Bad Example:** User asks to "create an Agno app to fetch latest 2 stories of HackerNews"

**What NOT to do:**
1. ❌ View source of docs.agno.com to reverse-engineer the API
2. ❌ Go to news.ycombinator.com to see which API is called
3. ❌ Manually call HackerNews API with custom code
4. ❌ Reinvent functionality that already exists in the framework

**Why this is wrong:**
- Wastes time reverse-engineering when docs are available
- Misses existing tools/utilities provided by the framework
- Creates unnecessary custom code instead of using built-in features
- Over-engineers simple tasks

## ✅ Correct Pattern: Documentation-First Workflow

### Phase 1: Discover MCP Tools (ALWAYS FIRST)

**MCP (Model Context Protocol) tools provide access to documentation, APIs, and utilities.**

```bash
# Check if MCP tools are available
# Look for tools starting with "mcp__"
```

**What to look for:**
- Documentation fetch tools (mcp__docs__, mcp__context7__)
- API integration tools
- Framework-specific utilities
- Code search and exploration tools

**Example:**
```bash
# ✅ Good: Use MCP to fetch Agno documentation
mcp__docs__fetch "agno hackernews tools"
# OR
mcp__context7__search "agno hackernews integration"
```

### Phase 2: Fetch Latest Documentation

**ALWAYS get the latest official documentation before implementing.**

**Priority order:**
1. **Official MCP documentation tools** (if available)
2. **WebFetch from official docs** (docs.framework.com)
3. **WebSearch for official tutorials** (framework.com/tutorials)
4. **WebSearch for recent examples** (2024-2025 only)

**What to fetch:**
- Official API reference
- Getting started guides
- Framework-specific tools/utilities
- Best practices and patterns
- Example code and tutorials

**Example:**
```bash
# ✅ Good: Fetch official Agno documentation
WebFetch: url="https://docs.agno.com/tools/hackernews" prompt="What HackerNews tools are available in Agno?"

# ✅ Good: Search for recent tutorials
WebSearch: query="Agno HackerNews integration tutorial 2025"
```

### Phase 3: Search for Built-In Tools/Features

**Before writing custom code, check if the framework already provides the functionality.**

**What to check:**
- Built-in tools and utilities
- Official integrations
- Standard library functions
- Framework plugins/extensions

**Example:**
```bash
# ✅ Good: Check Agno docs for built-in HackerNews tools
WebFetch: url="https://docs.agno.com/api-reference/tools" prompt="Does Agno provide built-in HackerNews tools?"
```

### Phase 4: Implement with Discovered Resources

**Only after completing research, implement using the best available approach.**

**Decision tree:**
1. **Built-in tool exists?** → Use it directly
2. **Official integration exists?** → Use official integration
3. **Standard pattern exists?** → Follow the pattern
4. **No existing solution?** → Implement custom (but verify first!)

## 🎯 Complete Example: The Right Way

**Task:** "Create an Agno app to fetch latest 2 stories of HackerNews"

### Step 1: Check for MCP Tools

```bash
# Check available MCP tools
# Look for documentation fetch capabilities
```

### Step 2: Fetch Agno Documentation

```bash
# Use MCP if available
mcp__docs__fetch "agno hackernews"

# OR use WebFetch from official docs
WebFetch: url="https://docs.agno.com/tools" prompt="What tools are available in Agno for fetching data from external APIs? Specifically, are there HackerNews-related tools?"

# Search for tutorials
WebSearch: query="Agno framework HackerNews integration example 2025"
```

### Step 3: Analyze Documentation

**From Agno docs, you discover:**
- Agno has built-in `hackernews_tools` module
- Provides `get_top_stories()` function
- Handles API calls automatically
- Includes error handling and rate limiting

### Step 4: Implement Using Built-In Tools

```python
# ✅ Good: Use built-in Agno HackerNews tools
from agno.tools import hackernews_tools

app = Agno(
    name="hn-fetcher",
    tools=[hackernews_tools.get_top_stories]
)

# Fetch 2 stories using built-in functionality
stories = app.run("Get the top 2 stories from HackerNews")
```

**NOT:**
```python
# ❌ Bad: Custom implementation ignoring built-in tools
import requests

def fetch_hackernews():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    # ... custom parsing and error handling ...
```

## 📋 Mandatory Pre-Implementation Checklist

Before writing ANY implementation code:

- [ ] **MCP Tools Checked**: Looked for relevant MCP documentation tools
- [ ] **Official Docs Fetched**: Retrieved latest documentation from official sources
- [ ] **Built-In Features Verified**: Confirmed no existing functionality covers this use case
- [ ] **Recent Tutorials Reviewed**: Checked for 2024-2025 examples and best practices
- [ ] **Framework Tools Discovered**: Identified all relevant framework-provided utilities
- [ ] **API Documentation Read**: Reviewed official API reference (if applicable)
- [ ] **Implementation Plan**: Documented approach based on discovered resources

## 🛠️ Tools for Documentation Discovery

### 1. MCP Tools (Highest Priority)

**Available MCP tools typically start with `mcp__`:**
- `mcp__docs__*` - Documentation fetchers
- `mcp__context7__*` - Codebase context and documentation
- Framework-specific MCP tools

**Usage:**
```bash
# Check available MCP tools
# Use them to fetch documentation before implementation
```

### 2. WebFetch (Official Documentation)

**Use for:**
- Official framework documentation
- API references
- Getting started guides
- Best practices

**Example:**
```bash
WebFetch: url="https://docs.framework.com/api-reference" prompt="What are the available tools and utilities for [specific task]?"
```

**Best practices:**
- Always use official documentation URLs (docs.framework.com)
- Ask specific questions in prompts
- Focus on discovering existing functionality
- Check multiple relevant documentation pages

### 3. WebSearch (Tutorials and Examples)

**Use for:**
- Recent tutorials and examples
- Community best practices
- Framework-specific patterns
- Problem-solving approaches

**Example:**
```bash
WebSearch: query="framework-name specific-task tutorial 2025"
WebSearch: query="framework-name best practices integration 2024"
```

**Best practices:**
- Include year (2024-2025) for recent results
- Search for official tutorials first
- Look for framework-specific examples
- Prefer official sources over blog posts

### 4. Codebase Search (Existing Patterns)

**Use Grep/Glob to find:**
- Similar implementations in current codebase
- Existing patterns and conventions
- Import statements (what's already being used)

**Example:**
```bash
Grep: pattern="import.*framework" output_mode="files_with_matches"
Grep: pattern="def.*similar_function" output_mode="content"
```

## 🎓 Learning from Mistakes

### Real-World Example: Agno HackerNews Task

**What Happened:**
An AI agent was asked to create an Agno app to fetch HackerNews stories.

**Mistakes Made:**
1. Viewed page source of docs.agno.com (unnecessary reverse-engineering)
2. Went to news.ycombinator.com to inspect API calls
3. Manually implemented HackerNews API integration
4. Ignored Agno's built-in HackerNews tools

**What Should Have Happened:**
1. Use MCP tools to fetch Agno documentation
2. Discover Agno has built-in HackerNews tools
3. Read official Agno docs for `hackernews_tools`
4. Implement using Agno's built-in functionality

**Result:**
- Over-engineered solution
- Reinvented the wheel
- Missed simpler built-in approach
- Wasted development time

### Lessons Learned

**Always ask yourself:**
1. "Does this framework provide this functionality?"
2. "Have I checked the official documentation?"
3. "Are there MCP tools that can help me find answers?"
4. "Am I reinventing something that already exists?"

**If you're not sure:**
- Search the documentation first
- Use MCP tools to fetch latest info
- Check for official integrations
- Look for recent tutorials

## 🚀 Framework-Specific Examples

### For Python Frameworks

**Before implementing:**
```bash
# Check official docs
WebFetch: url="https://docs.python-framework.org/api" prompt="What utilities does this framework provide for [task]?"

# Search for examples
WebSearch: query="python-framework [specific-feature] example 2025"

# Check PyPI for related packages
WebSearch: query="python-framework official integrations"
```

### For JavaScript/Node.js Frameworks

**Before implementing:**
```bash
# Check official docs
WebFetch: url="https://framework.dev/docs" prompt="What built-in tools are available for [task]?"

# Search npm documentation
WebSearch: query="framework-name official packages npm"

# Look for recent examples
WebSearch: query="framework-name integration tutorial 2024"
```

### For AI/ML Frameworks (Agno, LangChain, etc.)

**Before implementing:**
```bash
# Check for built-in tools
WebFetch: url="https://docs.framework.ai/tools" prompt="What pre-built tools are available for [specific integration]?"

# Look for official integrations
WebFetch: url="https://docs.framework.ai/integrations" prompt="Does this framework have official integration with [service]?"

# Search for recent examples
WebSearch: query="framework-name [service] integration example 2025"
```

## 📊 Decision Matrix

| Scenario | MCP Tools | WebFetch Docs | WebSearch | Custom Code |
|----------|-----------|---------------|-----------|-------------|
| Framework task | ✅ Check first | ✅ Yes | ✅ For examples | ❌ Last resort |
| API integration | ✅ Check first | ✅ Yes | ✅ For tutorials | ⚠️  Only if no built-in |
| Data processing | ✅ Check first | ✅ Check stdlib | ✅ For patterns | ⚠️  Prefer libraries |
| External service | ✅ Check first | ✅ Check integrations | ✅ For SDKs | ⚠️  Use official SDK |

**Legend:**
- ✅ Yes - Always do this
- ⚠️  Conditional - Only if necessary
- ❌ No - Avoid if possible

## 🎯 Success Criteria

**You've followed documentation-first approach when:**
- ✅ Checked for MCP documentation tools before coding
- ✅ Fetched official documentation from authoritative sources
- ✅ Verified no built-in functionality exists
- ✅ Searched for recent tutorials and examples
- ✅ Used framework-provided tools when available
- ✅ Implemented the simplest solution based on research
- ✅ Can explain why custom code was necessary (if used)

**Warning signs you're NOT following the approach:**
- ❌ Started coding immediately without research
- ❌ Reverse-engineered instead of reading docs
- ❌ Implemented custom solution without checking for built-ins
- ❌ Ignored MCP tools and documentation fetch capabilities
- ❌ Used outdated tutorials or examples
- ❌ Over-engineered when simple solution existed

## 🔄 Integration with TDD Workflow

**Documentation-first fits into TDD:**

1. **Discover** (NEW STEP - BEFORE TDD)
   - Check MCP tools for documentation
   - Fetch official docs and tutorials
   - Identify built-in functionality
   - Plan implementation approach

2. **Write Tests** (TDD Phase 1)
   - Based on discovered API/tools
   - Following framework patterns
   - Using official examples as reference

3. **Implement** (TDD Phase 2)
   - Using discovered built-in tools
   - Following framework conventions
   - Leveraging official integrations

4. **Refactor** (TDD Phase 3)
   - Align with framework best practices
   - Use framework utilities
   - Follow discovered patterns

## 📚 Reference Documentation

**Also see:**
- `@AI_DOCS/ai-tools.md` - Session management workflow
- `@AI_DOCS/tdd-workflow.md` - Test-Driven Development process
- `@AI_DOCS/code-conventions.md` - Code style and standards

---

**Remember:** Research first, implement second. Use MCP tools, fetch documentation, discover built-in functionality, then code. NEVER reinvent the wheel when official tools exist.
