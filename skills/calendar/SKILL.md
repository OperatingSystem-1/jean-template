---
name: calendar
description: Read and manage Google Calendar events.
---

# Calendar Skill

Access Google Calendar via API.

## Setup

### 1. Google Cloud Project
1. Go to https://console.cloud.google.com/
2. Create or select a project
3. Enable Google Calendar API:
   - APIs & Services → Enable APIs → Search "Calendar" → Enable

### 2. OAuth Credentials
1. APIs & Services → Credentials
2. Create Credentials → OAuth Client ID
3. Application type: Desktop app
4. Download JSON → save as `~/.config/calendar/credentials.json`

### 3. First Authorization
```bash
python3 skills/calendar/scripts/calendar_client.py auth
```
Opens browser for Google login, stores token in `~/.config/calendar/token.json`

## Quick Reference

### Today's Events
```bash
python3 skills/calendar/scripts/calendar_client.py today
```

### Upcoming Week
```bash
python3 skills/calendar/scripts/calendar_client.py list --days 7
```

### Specific Date
```bash
python3 skills/calendar/scripts/calendar_client.py list --date 2026-03-01
```

### Find Free Time
```bash
python3 skills/calendar/scripts/calendar_client.py free --date 2026-03-01
```

### Create Event
```bash
python3 skills/calendar/scripts/calendar_client.py create \
  --title "Team Meeting" \
  --start "2026-03-01 14:00" \
  --duration 60
```

## Output Format

```json
{
  "id": "abc123",
  "title": "Team Standup",
  "start": "2026-03-01T10:00:00-08:00",
  "end": "2026-03-01T10:30:00-08:00",
  "location": "Zoom"
}
```

## Testing

```bash
# Check credentials
ls -la ~/.config/calendar/credentials.json

# Test read access
python3 skills/calendar/scripts/calendar_client.py today
```

## Common Issues

| Issue | Fix |
|-------|-----|
| Token expired | Re-run `auth` command |
| No credentials | Complete Google Cloud setup |
| Invalid grant | Delete token.json, re-auth |
