# Testing & Evals

- `test_schemas` (suggested): run the pipeline on a canned input; validate `Itinerary` shape.
- **Golden prompts**: save 3–5 scenarios and assert rubrics (e.g., `total_cost <= budget`, commute minutes/day <= 120).
- **Snapshot JSON**: store outputs to detect regressions when you change tools/models.
