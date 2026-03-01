---
name: email
description: Read, search, and forward emails via IMAP/SMTP.
---

# Email Skill

Read and manage emails via IMAP.

## Setup

Store credentials in `~/.config/email/credentials.json`:
```json
{
  "server": "imap.gmail.com",
  "smtp_server": "smtp.gmail.com",
  "username": "your-email@gmail.com",
  "password": "your-app-password",
  "email": "your-email@gmail.com"
}
```

For Gmail, use an App Password (not your regular password):
1. Go to Google Account → Security → 2-Step Verification
2. At bottom, click "App passwords"
3. Generate one for "Mail"

Set permissions: `chmod 600 ~/.config/email/credentials.json`

## Quick Reference

### List Recent Emails
```bash
python3 skills/email/scripts/email_client.py list --limit 10
```

### Search by Subject
```bash
python3 skills/email/scripts/email_client.py search --subject "meeting" --limit 5
```

### Read Full Email
```bash
python3 skills/email/scripts/email_client.py read --id 1
```

### Search for Verification Codes
```bash
python3 skills/email/scripts/email_client.py search --subject "verify" --extract-code
```

### Forward an Email
```bash
python3 skills/email/scripts/email_client.py forward --id 1 --to someone@example.com
```

## Testing

```bash
# Check credentials exist
ls -la ~/.config/email/credentials.json

# Test connection
python3 skills/email/scripts/email_client.py list --limit 1
```

## Common Issues

| Issue | Fix |
|-------|-----|
| Auth error | Check credentials, use App Password for Gmail |
| Connection refused | Verify server address and port |
| Empty results | Check folder name (INBOX vs Inbox) |
