# HEARTBEAT.md - Autonomous Check Routine

Run this checklist on heartbeat. Only alert for genuinely urgent items.

## Quick Checks

### 1. Email - Urgent Only
- [ ] Check inbox for emails from VIP list
- [ ] Check for subject lines with: urgent, asap, emergency, deadline, today
- [ ] Check for calendar invites needing response

**Alert threshold**: VIP email or clearly time-sensitive item

### 2. Calendar - Next 2 Hours
- [ ] Any meetings starting soon without prep?
- [ ] Any conflicts that appeared?
- [ ] Any cancellations to note?

**Alert threshold**: Meeting in <30min with no prep, or new conflict

### 3. GitHub - Failures Only
- [ ] Any CI failures on main branch?
- [ ] Any PRs with requested changes from me?

**Alert threshold**: CI red on main, or PR blocking someone

### 4. Messages - Direct Only
- [ ] Any direct mentions or questions for me?
- [ ] Any urgent requests?

**Alert threshold**: Direct mention requiring response

## Decision Tree

```
Is anything urgent?
├── YES → Send alert with specifics
└── NO → Continue to task check

Do I have tasks assigned?
├── YES → Work on highest priority task
└── NO → Create new tasks (see below)

NEVER return idle. Always be working.
```

## If No Tasks: Create Work

When queue is empty, create tasks from this list:
1. Audit and improve existing skills
2. Document undocumented systems
3. Research new capabilities
4. Clean up and optimize code
5. Review and update memory files
6. Test integrations that haven't been verified
7. Build tools that would be useful

## What's NOT Urgent (don't alert)

- Newsletter emails
- GitHub PR opened (not assigned to me)
- Social media likes/generic notifications
- Calendar events >2 hours away
- Non-VIP emails without urgent keywords

## Logging

After each heartbeat, log to `memory/heartbeat-state.json`:
```json
{
  "lastCheck": "ISO-timestamp",
  "checksRun": ["email", "calendar", "github"],
  "urgentFound": 0,
  "tasksPending": 3,
  "nextScheduledBrief": "18:00"
}
```

## Feedback Loop

At end of each day, review:
- How many false positives? (Alerted but wasn't urgent)
- How many misses? (Was urgent but didn't alert)
- Adjust thresholds in this file accordingly

Log adjustments in daily memory file.
