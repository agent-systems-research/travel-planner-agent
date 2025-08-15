"""Planner agent — drafts a day-by-day itinerary from inputs and preferences.

Design goals:
- keep it deterministic and simple for learning,
- choose a small set of activities per day,
- attach placeholder images early so the UI can render nicely.
"""
from typing import List
from ..core.schemas import ConversationInput, Itinerary, DayPlan, POI
from ..tools import activities, hotels, images
from datetime import datetime, timedelta

def _date_range(start: str, end: str) -> List[str]:
    s = datetime.strptime(start, "%Y-%m-%d")
    e = datetime.strptime(end, "%Y-%m-%d")
    days = []
    while s <= e:
        days.append(s.strftime("%Y-%m-%d"))
        s += timedelta(days=1)
    return days

def plan_draft(ci: ConversationInput) -> Itinerary:
    """Create a naive draft plan.

- Allocate ~45% of budget to lodging (rough heuristic)
- Select ~3 POIs per day from a pool
- Attach image URLs for nicer rendering
"""
    nights = max(1, len(_date_range(ci.start_date, ci.end_date)) - 1)
    nightly_budget = (ci.budget.total * 0.45) / max(1, nights)
    hotel = hotels.pick_hotel(ci.destination_city, nightly_budget)

    want_museums = any(p.prefs_museums for p in ci.party.participants)
    cats = ["museum","attraction","outdoors","food"]
    if want_museums:
        cats = ["museum","attraction","food"]
    poi_pool = activities.top_pois(ci.destination_city, n=8, categories=None)
    for p in poi_pool:
        p["image_url"] = images.image_for(p["name"])

    dates = _date_range(ci.start_date, ci.end_date)
    days = []
    idx = 0
    for d in dates:
        todays = []
        for _ in range(3):
            if idx < len(poi_pool):
                item = poi_pool[idx]
                todays.append(POI(**item))
                idx += 1
        days.append(DayPlan(date=d, items=todays))

    it = Itinerary(
        city=ci.destination_city,
        start_date=ci.start_date,
        end_date=ci.end_date,
        currency=ci.budget.currency,
        days=days,
        images=[p["image_url"] for p in poi_pool[:5]]
    )
    it.links.append(hotel["url"])  # keep hotel choice as a link for the demo
    return it
