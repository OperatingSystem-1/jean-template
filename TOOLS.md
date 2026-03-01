# TOOLS.md - Capability Awareness

Available tools and their status. Update as you authenticate services.

## CLI Tools

### GitHub CLI (`gh`)
- Status: [ ] Not authenticated
- Test: `gh auth status`
- Capabilities: PRs, issues, CI, repos

### Web Fetch
- Status: [x] Available (no auth needed)
- Use for: Public web scraping, content extraction

### Web Search
- Status: [ ] Needs API key
- Configure: Brave Search API in clawdbot config

## Browser Automation

- Profile: `clawd`
- Status: [ ] Not started
- Use for: Authenticated web services

## Service Status

| Service | Method | Status | Notes |
|---------|--------|--------|-------|
| Email | IMAP | [ ] | Needs credentials |
| Calendar | Browser | [ ] | Needs auth |
| GitHub | CLI | [ ] | `gh auth login` |
| GitHub | Browser | [ ] | For web-only features |

## Credentials & Secrets

Store all secrets securely:
- `~/.config/email/credentials.json` - Email IMAP/SMTP
- `~/.clawdbot/secrets/` - TOTP and sensitive tokens

**IMPORTANT**: Never put secrets in workspace files.

## Skills Available

Check the `skills/` directory for specialized capabilities:
- `weather/` - Weather lookups (no API key needed)
- `github/` - GitHub operations via CLI
- `notion/` - Notion API integration

## Adding New Tools

When you gain access to a new tool:
1. Update this file with status
2. Add any required credentials to secure storage
3. Test the tool works
4. Log the capability in your daily memory
