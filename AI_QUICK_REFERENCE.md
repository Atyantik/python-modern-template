# AI Coding Assistant Quick Reference

> **TL;DR**: Write tests first, use real code, run `make check` before committing.

## 🚀 Quick Start

```bash
# Validate AI setup
make validate-ai-docs

# Run complete quality check
make check

# Your AI will automatically follow TDD!
```

## 📋 The Rule

**TESTS FIRST, ALWAYS**

1. Write failing test
2. Implement minimal code
3. Make test pass
4. Run `make check`
5. Commit

## 🎯 AI Platforms Configured

| Platform | Instruction File |
|----------|------------------|
| **Cursor** | `.cursorrules` |
| **Claude Code** | `.claude/INSTRUCTIONS.md` |
| **GitHub Copilot** | `COPILOT_INSTRUCTIONS.md` |
| **Gemini** | `GEMINI.md` |
| **Aider** | `.aider.conf.yml` |
| **All/Generic** | `AGENTS.md` |

## ✅ Quality Checklist

Before committing, ensure:
- [ ] Tests written FIRST (TDD)
- [ ] All tests pass
- [ ] Coverage ≥ 80%
- [ ] Type hints added
- [ ] `make check` passes
- [ ] No mocks (unless necessary)

## 🛠️ Essential Commands

```bash
# Validate AI instructions are synced
make validate-ai-docs

# Run all tests
make test

# Check coverage
make coverage

# Format code
make format

# Run linters
make lint

# Complete check (format + lint + test)
make check

# See all commands
make help
```

## 🧪 TDD Workflow

```python
# 1. Write test FIRST
def test_my_feature():
    result = my_feature("input")
    assert result == "expected"

# 2. Run tests (they fail)
# make test

# 3. Implement
def my_feature(input: str) -> str:
    return "expected"

# 4. Run tests (they pass)
# make test

# 5. Quality check
# make check
```

## 🚫 Don't Mock These

❌ Internal functions
❌ Pure functions
❌ Business logic

## ✅ Do Mock These

✅ HTTP requests
✅ Database calls
✅ File I/O
✅ datetime.now()
✅ random values

## 📊 Coverage Requirements

- **Minimum**: 80% (enforced)
- **Target**: 90%+
- **Ideal**: 100% for new code

## 🎨 Type Hints Required

```python
# ✅ Correct
def func(param: str, count: int = 10) -> bool:
    """Docstring here."""
    return True

# ❌ Wrong
def func(param, count=10):
    return True
```

## 📝 When to Update AI Docs

Update ALL instruction files when changing:
- Testing patterns
- Build process
- Security requirements
- Architecture
- Code quality rules

Files to update:
```
.cursorrules
AGENTS.md
.claude/INSTRUCTIONS.md
GEMINI.md
.aider.conf.yml
COPILOT_INSTRUCTIONS.md
```

Then run: `make validate-ai-docs`

## 🔥 Common Issues

### "Tests not written first"
**Solution**: AI should write tests before implementation. Check the AI instruction file for your platform.

### "Coverage below 80%"
**Solution**: Add more test cases
```bash
make coverage  # See what's not covered
```

### "Pylint score < 10"
**Solution**: Fix linting issues
```bash
make lint  # See specific issues
```

### "`make check` fails"
**Solution**: Run individual checks
```bash
make format  # Fix formatting
make lint    # See lint errors
make test    # Run tests
```

## 🎓 Examples

### Good TDD Flow
```
User: "Add email validation"
AI:
1. Writing tests/test_validators.py... ✓
2. Tests fail (no function yet)... ✓
3. Implementing validate_email... ✓
4. Tests pass... ✓
5. make check... ✓
Done!
```

### Bad Flow
```
User: "Add email validation"
AI:
1. Implementing validate_email... ❌ STOP!
   Should write tests FIRST!
```

## 📚 Full Documentation

- **Complete guide**: `AGENTS.md`
- **Summary**: `AI_INSTRUCTIONS_SUMMARY.md`
- **Platform-specific**: See individual instruction files

## 🆘 Help

```bash
# Validate setup
make validate-ai-docs

# See all commands
make help

# Check which AI instructions exist
ls -la | grep -E "\.cursorrules|AGENTS|GEMINI|COPILOT|\.aider"
```

## ⚡ Pro Tips

1. **Use real code** - Don't mock unless you have to
2. **Small tests** - Each test should check one thing
3. **Run `make check`** - Before every commit
4. **Type everything** - mypy strict mode is enforced
5. **Coverage matters** - 80% minimum, aim higher

## 🎯 Success Indicators

You're doing it right when:
- ✅ Tests are written before code
- ✅ Coverage stays above 80%
- ✅ `make check` always passes
- ✅ AI follows TDD automatically
- ✅ No merge conflicts on quality

---

**Remember**: Quality over speed. TDD saves debugging time!
