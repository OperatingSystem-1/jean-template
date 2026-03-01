# Jean Template

A production-ready workspace template for AI agents running on Clawdbot.

## Quick Start

1. Clone this template into your agent's workspace
2. Fill in `USER.md` with the human's profile
3. Run through `BOOTSTRAP.md` on first session (then delete it)
4. Agent is ready to operate

## Where This Lives

On Jean's machine, this workspace lives at `/home/ubuntu/clawd/`. Clawdbot loads these files into the agent's system prompt at session start.

Key paths:
- **Workspace root**: `/home/ubuntu/clawd/`
- **Memory files**: `/home/ubuntu/clawd/memory/`
- **Skills**: `/home/ubuntu/clawd/skills/`
- **Clawdbot config**: `~/.clawdbot/clawdbot.json`
- **Secrets**: `~/.clawdbot/secrets/` (never in workspace)
- **Browser profile**: `~/.clawdbot/browser/clawd/`
- **Email credentials**: `~/.config/email/credentials.json`

The workspace is the agent's "home directory" — persistent across sessions, version-controlled, and the source of truth for the agent's identity and protocols.

## Structure

```
jean-template/
├── README.md                    # This file
├── BOOTSTRAP.md                 # First-run identity setup (delete after)
├── SOUL.md                      # Personality and principles
├── AGENTS.md                    # Boot sequence + protocols
├── TOOLS.md                     # Capability awareness
├── USER.md                      # Human profile (fill in)
├── IDENTITY.md                  # Agent self-description
├── HEARTBEAT.md                 # Autonomous checks
├── TASKS.md                     # Work queue with starter tasks
├── RESILIENCE.md                # Error recovery patterns
├── LESSONS.md                   # Self-improvement loop (add mistakes here)
├── NEVER_AGAIN.md               # Traumatic learnings (permanent rules)
├── memory/
│   ├── day-zero.md              # Pre-seeded system context
│   ├── LAST_SESSION.md          # Session handoff template
│   └── ACTIVE_WORK.md           # Parallel work tracker
├── patterns/
│   ├── tooling-prerequisites.md # Verify credentials before work
│   └── local-infra.md           # Optional local PostgreSQL + Redis
├── templates/
│   └── SKILL-TEMPLATE.md        # Standard skill structure
├── scripts/
│   ├── agent-health             # Quick system check
│   ├── agent-log                # Daily logging helper
│   └── agent-tasks              # Task management
├── skills/
│   ├── weather/                 # No API key needed
│   ├── github/                  # gh CLI operations
│   └── notion/                  # API integration
└── config/
    └── clawdbot.template.json   # Example configuration
```

## Priority Tiers

### Tier 1: Critical (read every session)
- `AGENTS.md` - Boot sequence and core protocols
- `SOUL.template.md` - Personality and voice
- `memory/LAST_SESSION.md` - Context from previous session

### Tier 2: Important (read on relevant tasks)
- `USER.md` - Human preferences and context
- `HEARTBEAT.md` - Autonomous check routines
- `TASKS.md` - Current work queue
- `LESSONS.md` - Self-improvement rules (review daily)
- `NEVER_AGAIN.md` - Traumatic learnings (review every session)

### Tier 3: Reference (read when needed)
- `TOOLS.md` - Available capabilities
- `RESILIENCE.md` - Error recovery patterns
- `IDENTITY.md` - Self-description for introductions
- `patterns/` - Proven behavioral patterns

## First Run

On the agent's first session:

1. Read `BOOTSTRAP.md` and follow setup steps
2. Fill in `USER.md` with the human
3. Verify tools with `./scripts/agent-health`
4. Delete `BOOTSTRAP.md` when done

## Design Principles

- **Never idle**: Agents should always have tasks. `TASKS.md` includes starter work.
- **Graceful failure**: `RESILIENCE.md` provides recovery patterns for common errors.
- **Context continuity**: Session handoffs via `LAST_SESSION.md` and `ACTIVE_WORK.md`.
- **Progressive disclosure**: Priority tiers prevent context overload.

## License

MIT
