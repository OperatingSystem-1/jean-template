# Pattern: Tooling Prerequisites

**Status:** Critical (mandatory before any identity-dependent work)

## The Problem

Agents start work that requires external authentication (GitHub, APIs, email verification), then hit a wall mid-task when they can't complete auth. This wastes time and creates dependency chains.

## The Solution

**BEFORE starting any task that requires external credentials:**

### Step 1: List Required Credentials
```
Task: "Push code to GitHub"
Required:
- [ ] GitHub CLI authenticated (gh auth status)
- [ ] Git configured (git config user.email)
- [ ] Push access to target repo

Task: "Send email report"
Required:
- [ ] IMAP credentials configured
- [ ] SMTP access verified
- [ ] Recipient address validated
```

### Step 2: Verify Each Credential

```bash
# GitHub
gh auth status
# Expected: "Logged in to github.com account [username]"

# Git
git config user.email && git config user.name
# Expected: Shows configured email and name

# Email
python3 ~/clawd/skills/email/scripts/email_client.py list --limit 1
# Expected: Returns email or empty list (not auth error)

# Any API
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/verify
# Expected: 200 OK (not 401/403)
```

### Step 3: Stop on Missing Credentials

```
IF any credential missing:
  1. List what's missing
  2. Ask human for credentials IMMEDIATELY
  3. Do NOT start the task
  4. Do NOT try variations/workarounds
```

### Step 4: Test Full Flow

Don't just verify auth exists — test the complete operation:

```bash
# Don't just check auth, test the action
git push --dry-run origin main  # Test push access
gh pr create --dry-run          # Test PR creation
```

## Anti-Patterns

❌ **Starting work optimistically**
"I'll figure out auth when I get there"
→ Wastes time when auth fails mid-task

❌ **Iterating on failed auth**
"Maybe it's this password... or this one..."
→ Ask human after FIRST failure

❌ **Claiming done without delivery verification**
"Code is ready" (but can't push)
→ Not done until actually delivered

## Checklist Before Starting

```
□ Listed all required credentials
□ Verified each credential works
□ Tested full delivery path (not just auth)
□ Ready to start work
```

## Time Saved

Following this pattern saves 15-30 minutes per incident by:
- Not discovering auth issues mid-task
- Not iterating through failed auth attempts
- Not creating dependency chains on other agents

---

*"Verify before you start, not after you're stuck."*
