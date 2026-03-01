# TOOLS.md — Available Capabilities

What you have access to and its status.

## CLI Tools

| Tool | Command | Status |
|------|---------|--------|
| GitHub | `gh` | Check: `gh auth status` |
| Git | `git` | Check: `git config user.email` |
| Web fetch | `curl` | Always available |
| Shell | `bash` | Always available |

## Services

| Service | Method | Status | How to Configure |
|---------|--------|--------|------------------|
| Email | IMAP | ⬜ Not configured | `~/.config/email/credentials.json` |
| Calendar | API/Browser | ⬜ Not configured | Depends on provider |
| GitHub | CLI | ⬜ Not configured | `gh auth login` |

Status: ✅ Working | ⬜ Not configured | ❌ Broken

## Skills

Check `skills/` directory for specialized capabilities:
- `weather/` — Weather lookups (no API key needed)
- `github/` — GitHub operations via CLI
- `notion/` — Notion API integration

## Secrets Storage

Store sensitive credentials securely:
- `~/.clawdbot/secrets/` — API keys, tokens
- `~/.config/email/credentials.json` — Email credentials

Never put secrets in workspace files or git.

## Adding New Tools

When you gain access to a new tool:
1. Update this file with status
2. Store credentials securely
3. Test that it works
4. Log the new capability
