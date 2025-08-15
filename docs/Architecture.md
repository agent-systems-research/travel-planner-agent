# Architecture

```
User Input (ConversationInput)
        |
        v
   Planner Agent  ----> Draft Itinerary (POIs/day, hotel link, images)
        |
        v
   Tool Caller     ----> Enrich: travel legs, costs, totals
        |
        v
     Critic        ----> Checks: budget, opening hours; adds directives
        |  (if failing)
        └─────────────── revise Draft (drop/replace paid items)  [max 2 rounds]
        v
   Timeboxing      ----> Hour-by-hour blocks + commute totals
        |
        v
  Reservations     ----> Dummy holds (hotel/activity), links
        |
        v
     Output        ----> JSON + console summary
```

**Directories**
- `app/agents/`: planner, tool_caller, critic
- `app/tools/`: wrappers around external abilities (here: dummy data)
- `app/core/`: shared logic (schemas, cost, bookings, timebox, graph/orchestrator)
- `app/api/`: FastAPI server for programmatic planning
- `data/`: local JSON catalogs for hotels & activities
