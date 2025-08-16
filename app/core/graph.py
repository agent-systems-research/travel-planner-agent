"""A tiny orchestrator that wires Planner → ToolCaller → Critic → Timebox → Reservations."""
from .schemas import ConversationInput, Itinerary
from ..agents.planner_llm import plan_with_llm as plan_draft
from ..agents.tool_caller import enrich_with_maps_and_costs
from ..agents.critic import review_itinerary
from .timebox import schedule_day
from .cost import compute_day_cost
from .bookings import reserve_dummy

def run_pipeline(ci: ConversationInput, max_revisions: int = 2) -> Itinerary:
    # 1) Draft
    it = plan_draft(ci)
    # 2) Enrich with legs + costs
    it = enrich_with_maps_and_costs(it)
    # 3) Critic loop (bounded)
    rev = 0
    while rev <= max_revisions:
        report = review_itinerary(it, budget_total=ci.budget.total)
        if report.ok:
            break
        # naive revision: drop one paid item per day (last one)
        for day in it.days:
            for idx in range(len(day.items)-1, -1, -1):
                item = day.items[idx]
                if hasattr(item, "est_cost") and getattr(item, "est_cost", 0) > 0:
                    del day.items[idx]
                    break
            day.day_cost = compute_day_cost(day.items)
        it.total_cost = sum(d.day_cost for d in it.days)
        rev += 1

    # 4) Hour-by-hour scheduling
    for day in it.days:
        blocks, commute_total = schedule_day(day.date, day.items)
        day.hour_by_hour = blocks
        day.commute_minutes = commute_total

    # 5) Dummy reservations: one activity + one hotel hold
    if it.days and it.days[0].items:
        first_poi = next((x for x in it.days[0].items if hasattr(x, "id")), None)
        if first_poi:
            it.reservations.append(reserve_dummy("activity", getattr(first_poi, "id", "A0"), party_size=len(ci.party.participants)))
    it.reservations.append(reserve_dummy("hotel", "H1", party_size=len(ci.party.participants)))

    return it
