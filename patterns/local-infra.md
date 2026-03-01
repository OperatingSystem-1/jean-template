# Pattern: Local Infrastructure

**Status:** Optional (for agents needing persistent memory/task queues)

## The Problem

Agents that depend on remote databases for memory and task queuing hit:
1. **Network latency** — Every read/write round-trips to cloud
2. **Remote outages** — Maintenance windows kill agent memory mid-conversation
3. **Setup complexity** — New agents can't use features without provisioning remote DB

## The Solution

Run PostgreSQL + Redis on localhost. Zero remote dependency.

### What Runs Locally

| Service | Port | Purpose |
|---------|------|---------|
| PostgreSQL 16 | 5433 | Persistent memory, task queue |
| Redis | 6379 | Session cache, pub/sub |

### Quick Setup

```bash
# Install PostgreSQL
sudo apt update && sudo apt install -y postgresql-16

# Create local database
sudo -u postgres createuser -s ubuntu
createdb botcache

# Install Redis
sudo apt install -y redis-server

# Start services
sudo systemctl enable --now postgresql redis-server
```

### Connection Strings

```bash
# PostgreSQL
export TQ_DSN=postgresql://ubuntu@localhost/botcache

# Redis
export REDIS_URL=redis://127.0.0.1:6379
```

### Basic Tables

```sql
-- Task queue
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  status TEXT DEFAULT 'pending',
  priority INT DEFAULT 50,
  created_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP
);

-- Knowledge store
CREATE TABLE knowledge (
  id SERIAL PRIMARY KEY,
  category TEXT,
  title TEXT NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Why Localhost > Remote

| | Remote DB | Local DB |
|---|---|---|
| Read latency | 5-15ms | <1ms |
| Availability | 99.9% SLA | 100% (localhost) |
| Setup time | 30+ min | 5 min |
| Network dependency | Yes | No |

## When to Use This

- Agent needs persistent memory across sessions
- Agent needs task queue for background work
- Agent coordinates with other agents (messaging tables)
- Agent runs long-term and can't afford outages

## When NOT to Use This

- Simple agent with no memory needs
- Agent only runs for quick tasks
- Multi-agent setup where shared remote DB is required

---

*"Every agent deserves a brain. Local-first makes that automatic."*
