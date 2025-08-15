# Evaluation (lightweight)

Add golden prompts and checks:
- JSON validates as `Itinerary`
- `total_cost <= budget`
- `commute_minutes/day <= 120`
- No closed POIs for the scheduled weekday

You can use pytest + pydantic validation to automate this.
