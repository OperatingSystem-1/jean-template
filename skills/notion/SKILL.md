---
name: notion
description: Notion API for pages, databases, and blocks
---

# Notion Skill

Interact with Notion via API.

## Setup

1. Create integration at https://www.notion.so/my-integrations
2. Get API key
3. Share pages/databases with integration
4. Store key in `~/.clawdbot/secrets/notion-key`

## Authentication

```bash
NOTION_KEY=$(cat ~/.clawdbot/secrets/notion-key)
```

## API Endpoints

Base URL: `https://api.notion.com/v1`

### List Databases
```bash
curl -s "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"filter": {"property": "object", "value": "database"}}'
```

### Query Database
```bash
curl -s "https://api.notion.com/v1/databases/DATABASE_ID/query" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Get Page
```bash
curl -s "https://api.notion.com/v1/pages/PAGE_ID" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28"
```

### Create Page
```bash
curl -s "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"database_id": "DATABASE_ID"},
    "properties": {
      "Name": {"title": [{"text": {"content": "New Page"}}]}
    }
  }'
```

## Common Patterns

### Find a Page by Title
```bash
curl -s "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"query": "Page Title"}'
```

### Add Content to Page
Use the blocks endpoint to append content.

## Notes

- API key must be shared with specific pages
- Rate limit: 3 requests/second
- Notion-Version header required
