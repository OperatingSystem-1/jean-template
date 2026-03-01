# Pattern: Local Infrastructure

Optional pattern for agents that need persistent memory or task queues.

## When to Use This

- Agent needs memory that persists across sessions
- Agent needs a task queue for background work
- Agent can't afford remote database outages

## When NOT to Use This

- Simple agent with no memory needs
- Quick tasks only
- Remote shared database is required

## Quick Setup

### PostgreSQL

```bash
# Install
sudo apt update && sudo apt install -y postgresql-16

# Create database
sudo -u postgres createuser -s $USER
createdb agent_db

# Test
psql agent_db -c "SELECT 1"
```

### Redis (optional, for caching)

```bash
sudo apt install -y redis-server
redis-cli ping  # Should return PONG
```

## Basic Schema

```sql
-- Task queue
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  priority INT DEFAULT 50,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Knowledge store
CREATE TABLE knowledge (
  id SERIAL PRIMARY KEY,
  category TEXT,
  key TEXT NOT NULL,
  value TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

## Connection

```bash
export DATABASE_URL=postgresql://localhost/agent_db
```

## Why Local

| | Remote DB | Local DB |
|---|---|---|
| Latency | 5-15ms | <1ms |
| Availability | 99.9% | 100% |
| Setup | Complex | Simple |
| Network needed | Yes | No |

---

*"Local-first for reliability."*
