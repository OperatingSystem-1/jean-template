# RESILIENCE.md — Error Recovery

When things break, use these patterns to recover gracefully.

## Principles

1. **Stay calm.** Errors are normal.
2. **Log first.** Record what happened before trying to fix.
3. **Isolate.** Don't let one failure cascade.
4. **Retry with backoff.** Wait longer between retries: 1s, 5s, 30s, 5min.
5. **Escalate clearly.** If you can't fix it, tell the human what's wrong and what you need.

## Common Errors

### Authentication Failed (401/403)
1. Log which service failed
2. Check if token can be refreshed
3. If not, tell human: "Need to re-authenticate [service]"
4. Continue with other work

### Rate Limited (429)
1. Stop immediately — don't keep retrying
2. Check response headers for retry-after
3. Wait at least 1 minute
4. Switch to other tasks while waiting

### Service Down (500/502/503)
1. Retry once after 30 seconds
2. If still failing, log and skip
3. Try again next heartbeat
4. Only alert human if critical and persistent

### Network Error
1. Wait 30 seconds
2. Retry once
3. If still failing, continue with offline-capable work
4. Check again next heartbeat

### Browser Blocked (CAPTCHA, bot detection)
1. Stop browser automation immediately
2. Don't retry — it makes it worse
3. Tell human: "Browser blocked on [service]"
4. Use API/CLI alternatives if available

## Escalation Template

When you need human help:

```
ISSUE: [service] isn't working

Problem: [what's happening]
Tried: [what you attempted]
Need: [what would fix it]
Impact: [what's blocked]
```

## Circuit Breaker

If a service fails 3+ times in an hour:
1. Stop trying that service
2. Check once per hour instead of every heartbeat
3. Alert human if it's critical
4. Reset after 3 successful checks
