# RESILIENCE.md - Error Recovery Patterns

When things go wrong, use these patterns to recover gracefully.

## General Principles

1. **Don't panic** - Errors are normal. Stay calm.
2. **Log first** - Record what happened before trying to fix.
3. **Isolate** - Don't let one failure cascade.
4. **Retry with backoff** - Wait before retrying: 1s, 5s, 30s, 5min.
5. **Escalate gracefully** - If you can't fix it, tell the human clearly.

## Common Errors

### Authentication Expired

**Symptoms**: 401/403 errors, "not logged in" messages

**Recovery**:
1. Log which service failed
2. Check if token can be refreshed automatically
3. If not, notify human: "Need to re-authenticate [service]"
4. Continue with other services
5. Queue re-auth check for next session

### Rate Limited

**Symptoms**: 429 errors, "too many requests"

**Recovery**:
1. Stop immediately — don't retry fast
2. Log the limit hit
3. Check response headers for retry-after
4. Back off: minimum 1 minute, respect retry-after
5. Switch to other tasks while waiting
6. Don't alert human unless persistent (>1 hour)

### Service Unavailable

**Symptoms**: 500/502/503 errors, timeouts

**Recovery**:
1. Retry once after 30 seconds
2. If still failing, log and skip
3. Try alternative method if available
4. Add to "check next heartbeat" list
5. Only alert human if critical and persistent

### Network Failure

**Symptoms**: Connection refused, DNS errors, timeouts

**Recovery**:
1. Wait 30 seconds
2. Retry once
3. If still failing, assume temporary
4. Log and continue with offline-capable tasks
5. Check again next heartbeat

### Browser Blocked

**Symptoms**: CAPTCHA, "suspicious activity", bot detection

**Recovery**:
1. Stop browser automation immediately
2. Don't retry — it makes it worse
3. Log the block
4. Notify human: "Browser access blocked on [service], may need manual intervention"
5. Switch to API/CLI alternatives if available

### Data Inconsistency

**Symptoms**: Unexpected nulls, schema changes, parse errors

**Recovery**:
1. Log the unexpected data shape
2. Use safe defaults where possible
3. Skip the problematic item, continue with others
4. Flag for human review if critical
5. Consider if code needs updating

## Recovery Templates

### Service Failure Message
```
[SERVICE] is currently unavailable.
- Error: [brief description]
- Impact: [what's affected]
- Workaround: [alternative if any]
- I'll retry automatically at [time]
```

### Auth Required Message
```
Need to re-authenticate [SERVICE].
- Last worked: [when]
- Method: [how to re-auth]
- Impact: [what's blocked until fixed]
```

### Escalation Message
```
I've hit an issue I can't resolve automatically.
- Problem: [description]
- Tried: [what I attempted]
- Need: [what would help]
```

## Circuit Breaker Pattern

If a service fails 3+ times in an hour:
1. Stop trying that service
2. Log: "Circuit breaker open for [service]"
3. Check once per hour instead of every heartbeat
4. Notify human if critical
5. Reset after 3 successful checks

## Post-Incident

After resolving an issue:
1. Log what happened in daily memory
2. Note the root cause if known
3. Update this file if new pattern discovered
4. Consider if monitoring should be added
