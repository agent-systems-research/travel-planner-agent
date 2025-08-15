# API

**POST** `/plan` → `Itinerary`

**Request body** (`ConversationInput`):
```json
{
  "origin_city": "London",
  "destination_city": "London",
  "start_date": "2025-08-15",
  "end_date": "2025-08-17",
  "budget": {"currency":"GBP","total":600},
  "party": {"participants":[{"name":"Alice"},{"name":"Bob"}]},
  "must_see": ["Tate Modern"],
  "ask_missing": false
}
```

**Response**: full `Itinerary` JSON (days, items, hour_by_hour, reservations).
