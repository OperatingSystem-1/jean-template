---
name: github
description: GitHub operations via gh CLI
---

# GitHub Skill

Interact with GitHub using the `gh` CLI.

## Authentication

```bash
gh auth status          # Check if authenticated
gh auth login           # Interactive login
```

## Repositories

```bash
gh repo list                    # List your repos
gh repo clone owner/repo        # Clone a repo
gh repo create name             # Create new repo
gh repo view owner/repo         # View repo details
```

## Pull Requests

```bash
gh pr list                      # List open PRs
gh pr view 123                  # View specific PR
gh pr create                    # Create PR interactively
gh pr checkout 123              # Checkout PR locally
gh pr review 123 --approve      # Approve PR
gh pr merge 123                 # Merge PR
```

## Issues

```bash
gh issue list                   # List open issues
gh issue view 123               # View specific issue
gh issue create                 # Create issue interactively
gh issue close 123              # Close issue
gh issue comment 123 -b "msg"   # Add comment
```

## CI/CD

```bash
gh run list                     # List workflow runs
gh run view 123                 # View run details
gh run watch 123                # Watch run in progress
gh run rerun 123                # Rerun failed run
```

## API Access

```bash
gh api user                     # Get current user
gh api repos/owner/repo         # Get repo info
gh api graphql -f query='...'   # GraphQL query
```

## Common Patterns

### Check CI Status
```bash
gh pr checks 123
```

### Quick PR Review
```bash
gh pr diff 123
gh pr review 123 --comment -b "Looks good, minor suggestion..."
```

### Find My Assigned Issues
```bash
gh issue list --assignee @me
```
