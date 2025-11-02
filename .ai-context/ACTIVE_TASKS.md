# Active Tasks

> **Purpose**: Track what's currently being worked on to avoid conflicts and duplication

## 🚧 In Progress

Currently, no tasks are in progress.

---

## 🚫 Blocked

Currently, no tasks are blocked.

---

## 📋 Queued

Currently, no tasks are queued.

---

## How to Use This File

### When Starting a Task
1. Add your task to "In Progress" section
2. Include: Task name, AI agent, started timestamp
3. Example:
```markdown
### Add User Authentication
- **AI Agent**: Claude Code
- **Started**: 2025-11-02 15:30:00
- **Session**: 20251102153000-PLAN-add-user-auth.md
- **Status**: Writing tests
```

### When Task is Blocked
1. Move from "In Progress" to "Blocked"
2. Document reason for blocker
3. Example:
```markdown
### Add Email Service Integration
- **AI Agent**: Cursor
- **Blocked Since**: 2025-11-02 14:00:00
- **Blocker**: Waiting for SMTP credentials
- **Session**: 20251102140000-PLAN-email-service.md
```

### When Task is Complete
1. Remove from this file
2. Task details move to LAST_SESSION_SUMMARY.md
3. Session files remain in `.ai-context/sessions/`

### When Queuing a Task
1. Add to "Queued" section
2. Include: Priority, dependencies, notes
3. Example:
```markdown
### Implement Password Reset
- **Priority**: Medium
- **Depends On**: User Authentication (in progress)
- **Notes**: Can start after auth is complete
- **Queued By**: User request
```

## Template for In-Progress Task

```markdown
### [Task Name]
- **AI Agent**: [Agent Name]
- **Started**: YYYY-MM-DD HH:MM:SS
- **Session**: YYYYMMDDHHMMSS-PLAN-task-name.md
- **Status**: [Current status]
- **Files**: [Main files being modified]
- **Notes**: [Any important notes]
```

## Template for Blocked Task

```markdown
### [Task Name]
- **AI Agent**: [Agent Name]
- **Blocked Since**: YYYY-MM-DD HH:MM:SS
- **Blocker**: [Description of what's blocking]
- **Session**: YYYYMMDDHHMMSS-PLAN-task-name.md
- **Unblock Condition**: [What needs to happen]
```

## Template for Queued Task

```markdown
### [Task Name]
- **Priority**: [High/Medium/Low]
- **Depends On**: [List of dependencies]
- **Notes**: [Additional information]
- **Queued By**: [Who/what queued this]
- **Estimated Effort**: [If known]
```

## Best Practices

### Before Starting Work
1. **Always check this file first!**
2. Make sure your task doesn't conflict with "In Progress"
3. Check if there are blockers you can help resolve
4. Consider queued tasks if looking for work

### While Working
1. Update your task status regularly
2. If blocked, move to "Blocked" section immediately
3. Document any new dependencies discovered

### After Completing
1. Remove your task from this file
2. Update LAST_SESSION_SUMMARY.md with your work
3. Update queued tasks if they can now proceed

## Examples

### Example: In Progress
```markdown
## 🚧 In Progress

### Add Database Migration System
- **AI Agent**: Claude Code
- **Started**: 2025-11-02 15:45:00
- **Session**: 20251102154500-PLAN-database-migrations.md
- **Status**: Implementing migration runner
- **Files**: src/database/migrations.py, tests/test_migrations.py
- **Notes**: Using Alembic for migrations
```

### Example: Blocked
```markdown
## 🚫 Blocked

### Deploy to Production
- **AI Agent**: Gemini
- **Blocked Since**: 2025-11-02 10:00:00
- **Blocker**: Waiting for AWS credentials and S3 bucket setup
- **Session**: 20251102100000-PLAN-production-deploy.md
- **Unblock Condition**: DevOps team provides credentials
```

### Example: Queued
```markdown
## 📋 Queued

### Add Rate Limiting to API
- **Priority**: High
- **Depends On**: API Authentication (completed)
- **Notes**: Use Redis for distributed rate limiting
- **Queued By**: Security review requirement
- **Estimated Effort**: 4-6 hours
```

---

**Last Updated**: 2025-11-02 15:00:00
**Updated By**: Claude Code
**Check This File**: Before starting any new task!

**Note**: This file is local only (not committed to git) to avoid merge conflicts during concurrent AI sessions.
