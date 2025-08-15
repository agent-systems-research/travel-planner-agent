# Schemas

All contracts are in `app/core/schemas.py` using **Pydantic**.

- `TravelerProfile`, `Party`: multi-user preferences
- `POI`, `Leg`: activity and commute entries
- `DayPlan`: a single day's items + hour-by-hour blocks
- `Itinerary`: all days, totals, links, images, and reservations
- `CriticReport`: validation result from the Critic

Pro tip: keep schemas stable even if you swap tool providers.
