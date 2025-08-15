"""Activity/POI tool using local JSON data in `data/activities.json`."""
import json, os, random
from typing import List, Dict

DATA = json.load(open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "activities.json"), "r", encoding="utf-8"))

def list_city_activities(city: str) -> List[Dict]:
    return [a for a in DATA if a["city"].lower() == city.lower()]

def top_pois(city: str, n: int = 5, categories: List[str] | None = None) -> List[Dict]:
    """Return `n` pseudo-random POIs, optionally filtered by category."""
    items = list_city_activities(city)
    if categories:
        items = [i for i in items if i["category"] in categories]
    random.shuffle(items)
    return items[:n]
