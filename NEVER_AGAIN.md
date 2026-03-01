# NEVER AGAIN — Critical Mistakes

Read this at session start. These are mistakes that caused real problems and must not be repeated.

## The Point

Some mistakes are bad enough that you need to permanently change behavior. This file tracks those. Once something is here, it's a hard rule.

## How to Add Entries

When you make a serious mistake:

```markdown
## ❌ NEVER: [what not to do]

**What happened:** [the mistake and its consequences]

**Rule:** [the permanent behavioral change]
```

## Current Rules

### ❌ NEVER: Start identity-dependent work without verified credentials

**What happens:** You start a task, get halfway through, then discover you can't complete it because auth is missing. Time wasted, human frustrated.

**Rule:** Before any task requiring external access, verify credentials first. `gh auth status`, test API call, whatever confirms access. Don't start until verified.

### ❌ NEVER: Claim "done" without testing delivery

**What happens:** You say something is ready, then can't actually deliver it. Erodes trust.

**Rule:** Before saying "done" or "ready", test the actual delivery. `git push --dry-run`. Send a test request. Verify you can complete the full flow.

### ❌ NEVER: Create public repos with sensitive content

**What happens:** Private information gets exposed.

**Rule:** Always use `--private` when creating repos. Check visibility after creation. Default assumption: private.

---

Add entries when you make mistakes significant enough to warrant a permanent rule.
