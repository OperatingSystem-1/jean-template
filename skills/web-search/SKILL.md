---
name: web-search
description: Search the web and fetch page content.
---

# Web Search Skill

Search and fetch web content.

## Web Search (via Clawdbot)

If running in Clawdbot, use the built-in `web_search` tool:
```
Query: "latest news on topic"
```

## Web Fetch

Fetch and extract content from URLs:

```bash
# Get readable content
curl -s "https://example.com" | python3 -c "
import sys
from html.parser import HTMLParser
from html import unescape

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style', 'nav', 'footer']:
            self.skip = True
    def handle_endtag(self, tag):
        if tag in ['script', 'style', 'nav', 'footer']:
            self.skip = False
    def handle_data(self, data):
        if not self.skip:
            self.text.append(data.strip())
    def get_text(self):
        return ' '.join(filter(None, self.text))

parser = TextExtractor()
parser.feed(sys.stdin.read())
print(parser.get_text()[:5000])
"
```

## Quick Search Patterns

### DuckDuckGo Instant Answers
```bash
curl -s "https://api.duckduckgo.com/?q=python+requests&format=json" | jq '.Abstract'
```

### Wikipedia Summary
```bash
curl -s "https://en.wikipedia.org/api/rest_v1/page/summary/Python_(programming_language)" | jq '{title, extract}'
```

## Using in Clawdbot

The `web_search` and `web_fetch` tools are available:

- `web_search` — Search with Brave API
- `web_fetch` — Fetch URL and extract readable content

These are preferred over curl when available.
