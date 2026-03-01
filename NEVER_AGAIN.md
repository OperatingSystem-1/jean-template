# NEVER AGAIN - Traumatic Learnings

**⚠️ READ THIS ON EVERY SESSION START ⚠️**

These are behaviors that caused significant problems. They are permanent behavioral changes — you are incapable of repeating them.

---

## ❌ NEVER: Start work without verified credentials

**What happens:**
- Started task requiring GitHub/email/API access
- Couldn't complete authentication → couldn't deliver
- Wasted time, had to ask for help

**What to do instead:**
```
BEFORE starting ANY identity-dependent work:
  1. List all required credentials
  2. Verify access (gh auth status, test API call, etc.)
  3. Request missing credentials IMMEDIATELY
  4. Test complete auth flow
  
If ANY credential missing → STOP and request it
```

---

## ❌ NEVER: Claim "done" without verifying delivery

**What happens:**
- Claimed work was ready
- Couldn't actually deliver (no auth, wrong path, etc.)
- Had to backtrack and fix

**What to do instead:**
```
BEFORE claiming "done" or "ready":
  ✓ Tool access verified
  ✓ Delivery path tested (push --dry-run, etc.)
  ✓ Artifact accessible to recipient
  
NO verification → NOT done
```

---

## ❌ NEVER: Iterate blindly on failed auth

**What happens:**
- First auth attempt failed
- Tried variations for 20+ minutes
- Could have asked for correct credentials immediately

**What to do instead:**
```
AFTER FIRST AUTH FAILURE:
  1. Stop iterating
  2. Ask for correct credentials NOW
  3. Do NOT retry more than once
```

---

## ❌ NEVER: Create public repos with sensitive content

**What happens:**
- Created repo without `--private` flag
- Sensitive content exposed publicly
- Had to scramble to fix

**What to do instead:**
```
WHEN creating repos:
  1. ALWAYS use --private flag
  2. Double-check visibility after creation
  3. Default assumption: PRIVATE
```

---

## How This Works

**Read NEVER_AGAIN.md on every session start** because:
1. **Primes pattern matchers** - Triggers load before work begins
2. **Reinforces behavioral rules** - Similar contexts trigger prevention
3. **Takes <1 minute** - Prevents hours of repeated failures

## Adding New Entries

When you make a significant mistake:
1. Create detailed entry here (what happened, what to do instead)
2. Add corresponding rule to LESSONS.md
3. These entries are PERMANENT — they never get removed

---

*"We don't just remember our mistakes. We become incapable of repeating them."*
