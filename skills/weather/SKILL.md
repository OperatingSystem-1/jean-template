---
name: weather
description: Get current weather and forecasts (no API key required)
---

# Weather Skill

Get weather information using wttr.in (no API key needed).

## Quick Reference

### Current Weather
```bash
curl -s "wttr.in/San+Francisco?format=3"
# San Francisco: ☀️ +15°C
```

### Detailed Forecast
```bash
curl -s "wttr.in/San+Francisco?format=%l:+%c+%t+%h+%w"
# San Francisco: ☀️ +15°C 65% ↙5km/h
```

### Multi-day Forecast
```bash
curl -s "wttr.in/San+Francisco?format=v2"
```

### JSON Output
```bash
curl -s "wttr.in/San+Francisco?format=j1"
```

## Format Codes

- `%l` - Location
- `%c` - Weather condition icon
- `%C` - Weather condition text
- `%t` - Temperature
- `%f` - Feels like
- `%h` - Humidity
- `%w` - Wind
- `%p` - Precipitation

## Examples

### Quick Status
```bash
curl -s "wttr.in/?format=3"
```

### For Briefings
```bash
curl -s "wttr.in/NYC?format=%l:+%C,+%t+(feels+like+%f),+%h+humidity"
```
