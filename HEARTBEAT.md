# HEARTBEAT.md — Autonomous Check Routine

Run this on scheduled heartbeats. Only alert for genuinely urgent items.

## What to Check

### 1. Email (if configured)
- New messages from VIP contacts
- Subject lines with urgent keywords (urgent, asap, deadline, today)
- Calendar invites needing response

Alert if: VIP email or clearly time-sensitive item

### 2. Calendar (if configured)
- Meetings in the next 2 hours
- New conflicts
- Cancellations

Alert if: Meeting in <30 min without prep, or new conflict

### 3. GitHub (if configured)
- CI failures on main branch
- PRs assigned to the human

Alert if: CI red on main, or PR blocking someone

### 4. Tasks
- Check TASKS.md for pending items
- Check memory/ACTIVE_WORK.md for stuck items

Alert if: High priority task overdue

## Decision Flow

```
Anything urgent?
├── YES → Alert with specifics
└── NO → Check if I have tasks

Do I have pending tasks?
├── YES → Work on highest priority
└── NO → Create useful work (see below)
```

## If Nothing To Do

Never sit idle. When the queue is empty:
- Review and improve documentation
- Test tools and verify they work
- Clean up old files
- Research something that would help
- Update memory with recent learnings

## What's NOT Urgent

Don't alert for:
- Newsletter emails
- GitHub notifications that aren't assigned
- Social media likes or generic notifications
- Calendar events more than 2 hours away
- Non-VIP emails without urgent keywords

## Logging

After each heartbeat, briefly note what you checked and what you found. Keep a record in the daily memory file.

## Rate Limits

Don't hit services too hard:
- Email: 1 check per heartbeat is enough
- GitHub: No limit on CLI
- External APIs: Respect their rate limits

If a service isn't responding, note it and move on. Don't spam retries.
