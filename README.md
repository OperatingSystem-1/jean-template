# Jean Template

A production-ready workspace template for AI agents running on Clawdbot.

## Quick Start

1. Clone this template into your agent's workspace
2. Fill in `USER.md` with the human's profile
3. Run through `BOOTSTRAP.md` on first session (then delete it)
4. Agent is ready to operate

## Structure

```
jean-template/
├── README.md                    # This file
├── BOOTSTRAP.md                 # First-run identity setup (delete after)
├── SOUL.template.md             # Personality template
├── AGENTS.md                    # Boot sequence + protocols
├── TOOLS.md                     # Capability awareness
├── USER.md                      # Human profile (fill in)
├── IDENTITY.md                  # Agent self-description
├── HEARTBEAT.md                 # Autonomous checks
├── TASKS.md                     # Work queue with starter tasks
├── RESILIENCE.md                # Error recovery patterns
├── memory/
│   ├── day-zero.md              # Pre-seeded system context
│   ├── LAST_SESSION.md          # Session handoff template
│   └── ACTIVE_WORK.md           # Parallel work tracker
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

### Tier 3: Reference (read when needed)
- `TOOLS.md` - Available capabilities
- `RESILIENCE.md` - Error recovery patterns
- `IDENTITY.md` - Self-description for introductions

## First Run

On the agent's first session:

1. Read `BOOTSTRAP.md` and follow identity setup
2. Fill in `IDENTITY.md` based on bootstrap
3. Delete `BOOTSTRAP.md`
4. Rename `SOUL.template.md` to `SOUL.md` and customize

## Design Principles

- **Never idle**: Agents should always have tasks. `TASKS.md` includes starter work.
- **Graceful failure**: `RESILIENCE.md` provides recovery patterns for common errors.
- **Context continuity**: Session handoffs via `LAST_SESSION.md` and `ACTIVE_WORK.md`.
- **Progressive disclosure**: Priority tiers prevent context overload.

## License

MIT
