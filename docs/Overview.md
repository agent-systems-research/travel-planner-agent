# Overview

This project is a **teaching-first starter** for building an *agentic* travel planner.

**Key ideas covered:**
- **Multi-turn orchestration**: Planner → ToolCaller → Critic loop with bounded revisions.
- **Tool use**: search, hotels, activities, maps, images (dummy data, easy to swap for real APIs).
- **Contracts-first**: Pydantic schemas ensure the final itinerary remains machine-usable.
- **Timeboxing**: simple hour-by-hour scheduling with commute tracking.
- **Reservations**: dummy holds to demonstrate write actions and link-outs.

Use this to learn patterns that generalize to LangGraph/CrewAI/AutoGen or your own orchestrator.
