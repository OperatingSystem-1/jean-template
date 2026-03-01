---
name: github
description: GitHub operations via gh CLI - PRs, issues, CI monitoring.
---

# GitHub Skill

Manage GitHub via the `gh` CLI.

## Setup

```bash
gh auth login
gh auth status  # verify
```

## Key Rule

**Always create repos as private:**
```bash
gh repo create name --private
gh repo create org/name --private
```

## Quick Reference

### Check What Needs Attention
```bash
gh pr list --search "review-requested:@me"
gh pr list --author @me
gh issue list --assignee @me
gh run list --limit 5
```

### PR Workflow

```bash
# List PRs
gh pr list

# View PR details
gh pr view 123
gh pr diff 123
gh pr checks 123

# Review and approve
gh pr review 123 --approve --body "Looks good"

# Merge
gh pr merge 123
```

### Issues

```bash
# List issues
gh issue list
gh issue list --assignee @me

# Create issue
gh issue create --title "Bug: X" --body "Description"

# Close issue
gh issue close 123 --comment "Fixed in PR #124"
```

### CI/CD

```bash
# List runs
gh run list --limit 10

# View run details
gh run view 123
gh run view 123 --log-failed

# Rerun failed
gh run rerun 123 --failed
```

### Repos

```bash
# List repos
gh repo list

# Clone
gh repo clone owner/repo

# Create (always private!)
gh repo create my-repo --private

# View
gh repo view owner/repo
```

## Automation Patterns

### Morning Check
1. `gh pr list --search "review-requested:@me"` — PRs waiting on you
2. `gh run list --limit 5` — recent CI status
3. `gh issue list --assignee @me` — your issues

### CI Failure Alert
```bash
gh run list --status failure --limit 5
```

## Testing

```bash
gh auth status
gh pr list --limit 1
gh run list --limit 1
```
