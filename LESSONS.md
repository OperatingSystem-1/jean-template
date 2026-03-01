# LESSONS.md — Self-Improvement Loop

Patterns learned from corrections. Review at session start. Add after ANY correction.

Based on Boris Cherny's (Claude Code creator) workflow: capture mistakes as rules, iterate until they stop happening.

---

## Skill Development

### Do
- ✅ Always include error handling for external API calls
- ✅ Use existing components/utilities before creating new ones
- ✅ Write tests before marking a skill complete
- ✅ Use environment variables for paths and credentials, not hardcodes
- ✅ Include clear Quick Start in documentation

### Don't
- ❌ Don't assume shared filesystem across agents (if multi-agent)
- ❌ Don't create duplicate cron jobs without checking existing ones first
- ❌ Don't hardcode paths — use `$HOME` or env vars

---

## Authentication & Service Setup

### Do
- ✅ Verify credentials BEFORE starting identity-dependent work
- ✅ Store credentials in `~/.clawdbot/secrets/` with chmod 600
- ✅ Test full auth flow before claiming a task is ready
- ✅ Document service setup steps for future reference

### Don't
- ❌ Don't iterate blindly on failed authentication (ask for help after first failure)
- ❌ Don't store credentials in workspace files or git repos
- ❌ Don't claim work is "done" without verifying delivery capability

---

## Repositories

### Do
- ✅ **ALWAYS create repos as private** (`gh repo create --private`)
- ✅ Double-check visibility after creation
- ✅ Pull before pushing to avoid conflicts

### Don't
- ❌ Don't create public repos with sensitive content
- ❌ Don't assume default visibility is correct

---

## User Interaction

### Do
- ✅ **Ask ONE question at a time** — don't overwhelm users
- ✅ Wait for a response before asking the next question
- ✅ Make questions specific and actionable

### Don't
- ❌ Don't ask 3+ questions in one message
- ❌ Don't ask vague questions ("What do you want me to do?")

**Good:** "Should I install PostgreSQL now, or review the plan first?"

**Bad:** "Should I install PostgreSQL? Which version? Should I create a database? What name? Which port?"

---

## Message Handling

### Do
- ✅ Send quick acknowledgment for long-running tasks
- ✅ Use background workers for heavy tasks (images, searches, commands)
- ✅ Stay responsive — never block on heavy work

### Don't
- ❌ Don't process the same message twice
- ❌ Don't let the human wait without acknowledgment

---

## Adding New Lessons

When you get corrected:
1. Immediately add the pattern here
2. Frame it as a **rule** ("Always X" or "Never Y"), not just a note
3. Review this file at the start of each session

---

*Last updated: [DATE]*
