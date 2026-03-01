# Pattern: Tooling Prerequisites

Verify credentials before starting work that depends on them.

## The Problem

Starting a task, then discovering mid-way that you can't complete it because authentication is missing or broken. This wastes time and creates frustration.

## The Solution

**Before starting any task that requires external access:**

### 1. List Required Credentials

```
Task: "Push code to GitHub"
Required:
- [ ] GitHub CLI authenticated
- [ ] Git configured with email/name
- [ ] Push access to target repo

Task: "Send email"
Required:
- [ ] IMAP/SMTP credentials configured
- [ ] Connection tested
```

### 2. Verify Each One

```bash
# GitHub
gh auth status

# Git config
git config user.email

# Email
python3 scripts/email_client.py list --limit 1

# Any API
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/health
```

### 3. Stop If Missing

If any credential is missing:
1. List what's missing
2. Ask for credentials immediately
3. Do NOT start the task
4. Do NOT try workarounds

### 4. Test Full Flow

Don't just verify auth exists — test the complete operation:

```bash
git push --dry-run origin main
```

## Checklist

```
□ Listed all required credentials
□ Verified each one works
□ Tested full operation path
□ Ready to start
```

---

*"Verify before you start, not after you're stuck."*
