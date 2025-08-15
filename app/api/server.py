"""FastAPI server exposing a single /plan endpoint for programmatic access."""
from fastapi import FastAPI
from ..core.schemas import ConversationInput, Itinerary
from ..core.graph import run_pipeline

app = FastAPI(title="Travel Planner Agent")

@app.post("/plan", response_model=Itinerary)
def plan(ci: ConversationInput):
    """Plan a trip. Post a `ConversationInput` JSON; returns an `Itinerary`."""
    return run_pipeline(ci)

@app.get("/health")
def health():
    """Basic liveness check."""
    return {"ok": True}
