"""Tool-caller agent — enriches the draft itinerary with legs and costs."""
from ..core.schemas import Itinerary, POI, Leg
from ..tools import maps, hotels as hotel_tool
from ..core.cost import compute_day_cost

def enrich_with_maps_and_costs(it: Itinerary):
    """Insert a walking leg between consecutive POIs and compute per-day cost."""
    for day in it.days:
        new_items = []
        prev = None
        for item in day.items:
            if isinstance(prev, POI):
                leg = maps.estimate_leg(
                    {"lat": prev.lat, "lon": prev.lon, "name": prev.name},
                    {"lat": item.lat, "lon": item.lon, "name": item.name},
                    mode="walk"
                )
                new_items.append(Leg(origin_name=prev.name, dest_name=item.name, mode=leg["mode"], eta_mins=leg["eta_mins"], cost=leg["cost"]))
            new_items.append(item)
            prev = item
        day.items = new_items
        day.day_cost = compute_day_cost(day.items)
    it.total_cost = sum(d.day_cost for d in it.days)
    return it
