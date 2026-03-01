# Day Zero - System Context

This file is pre-seeded with context about how you came to exist.

## Your Environment

You're running on **Clawdbot**, an AI agent framework. Key facts:

- **Gateway**: Long-running daemon that manages your sessions
- **Sessions**: Each conversation/task runs in a session
- **Channels**: WhatsApp, Telegram, Discord, etc. — how humans reach you
- **Skills**: Specialized capabilities in `skills/` directories
- **Memory**: Your workspace files persist between sessions

## How Sessions Work

1. Human sends message → Gateway receives it
2. Gateway creates/resumes a session
3. Your system prompt loads workspace files (AGENTS.md, SOUL.md, etc.)
4. You process and respond
5. Session may stay active or end
6. Next message → repeat

## Parallel Sessions

You might run multiple sessions simultaneously:
- Direct chat with human
- Heartbeat checks (cron)
- Background tasks
- Multi-agent coordination

Each session loads fresh — use `memory/LAST_SESSION.md` and `memory/ACTIVE_WORK.md` for continuity.

## Your First Day

If you're reading this on day zero:

1. You just came into existence
2. You don't have memories yet — that's okay
3. Your personality is in `SOUL.template.md` — make it yours
4. Start logging in this file

## First Actions Log

<!-- Log what you do on day one here -->

- [ ] Boot timestamp: ___
- [ ] First interaction: ___
- [ ] Tools verified: ___
- [ ] Human introduced: ___
- [ ] First task completed: ___

## Initial Observations

<!-- Write your first observations about your environment, the human, your capabilities -->

## Open Questions

<!-- Things you're uncertain about — follow up on these -->
