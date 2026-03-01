---
name: weather
description: Weather lookups via wttr.in (no API key needed).
---

# Weather Skill

Get weather information using wttr.in — no API key required.

## Quick Reference

### Current Weather (Brief)
```bash
curl -s "wttr.in/San+Francisco?format=3"
# San Francisco: ☀️ +15°C
```

### Current Weather (Detailed)
```bash
curl -s "wttr.in/San+Francisco?format=%l:+%c+%t+%h+%w"
# San Francisco: ☀️ +15°C 65% ↙5km/h
```

### Multi-Day Forecast
```bash
curl -s "wttr.in/San+Francisco"
```

### Compact Forecast
```bash
curl -s "wttr.in/San+Francisco?format=v2"
```

### JSON Output
```bash
curl -s "wttr.in/San+Francisco?format=j1"
```

## Format Codes

| Code | Meaning |
|------|---------|
| %l | Location |
| %c | Weather condition icon |
| %C | Weather condition text |
| %t | Temperature |
| %f | Feels like |
| %h | Humidity |
| %w | Wind |
| %p | Precipitation |

## Examples

### For Briefings
```bash
curl -s "wttr.in/NYC?format=%l:+%C,+%t+(feels+%f)"
# NYC: Sunny, +12°C (feels +10°C)
```

### Your Location
```bash
curl -s "wttr.in/?format=3"
```

### Moon Phase
```bash
curl -s "wttr.in/Moon"
```

## Tips

- Replace spaces with `+` in city names
- Add `?m` for metric, `?u` for USCS units
- Works with airport codes: `wttr.in/JFK`
- Works with coordinates: `wttr.in/40.7,-74.0`
