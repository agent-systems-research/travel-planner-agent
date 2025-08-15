# Agents

## Planner
- **Goal**: Draft a feasible plan using preferences & must-see items.
- **Output**: `Itinerary` with a few POIs per day and image links.

## ToolCaller
- **Goal**: Enrich the draft: insert commute legs, compute day & total costs.
- **How**: Uses `tools/maps` to estimate distances and times; sums item costs.

## Critic
- **Goal**: Validate the itinerary against **budget** and **opening hours**.
- **Result**: If violations are found, emits **directives** and we revise by dropping paid items first.
- **Bounded Loop**: Max 2 iterations to avoid infinite refinement.
