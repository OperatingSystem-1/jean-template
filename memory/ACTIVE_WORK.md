# Active Work Tracker

Track in-progress work across parallel sessions.

## Status Legend

- `[RUNNING]` - Currently being worked on
- `[WAITING]` - Blocked on something
- `[DONE]` - Completed (remove after 24h)
- `[FAILED]` - Needs retry or escalation

## Active Items

<!-- Add/update items as you work -->

## Format

```
[STATUS] Task description
  Session: session-id
  Started: timestamp
  Notes: any relevant details
```

## Example

```
[RUNNING] Reviewing PR #142
  Session: main-chat
  Started: 2024-01-15 10:30
  Notes: Found 2 issues, drafting comments

[WAITING] Email draft for Sarah
  Session: morning-briefing
  Started: 2024-01-15 08:00
  Notes: Waiting for human approval

[DONE] Fixed CI pipeline
  Session: heartbeat-1705312800
  Completed: 2024-01-15 09:00
```

## Cleanup

- Move [DONE] items older than 24h to daily memory log
- Investigate [WAITING] items older than 24h
- Escalate [FAILED] items that haven't been retried
