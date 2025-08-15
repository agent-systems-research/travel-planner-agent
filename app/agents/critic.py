"""Critic agent — validates budget and opening-hour constraints."""
from ..core.schemas import Itinerary, CriticReport, POI, Leg
from datetime import datetime

def _weekday(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][dt.weekday()]

def review_itinerary(it: Itinerary, budget_total: float, commute_cap_per_day: int = 120) -> CriticReport:
    """Return a report; `ok=False` when violations need fixing.

- Budget: sum of day costs <= total budget
- Opening hours: flag POIs that might be closed for the weekday
"""
    messages = []
    directives = []
    violations = []
    ok = True

    if it.total_cost > budget_total:
        ok = False
        violations.append(f"Budget overrun: {it.total_cost:.2f} > {budget_total:.2f}")
        directives.append("Replace one paid activity per day with a free/low-cost option.")

    for day in it.days:
        wd = _weekday(day.date)
        for item in day.items:
            if isinstance(item, POI) and item.open_hours:
                hrs = item.open_hours.get(wd)
                if not hrs:
                    ok = False
                    violations.append(f"{item.name} might be closed on {wd}.")
                    directives.append(f"Swap {item.name} with another open POI on {wd}.")

    messages.append("Checked budget & opening hours.")
    return CriticReport(ok=ok, messages=messages, directives=directives, violations=violations)
