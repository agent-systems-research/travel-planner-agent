"""Hotel tool using local JSON data in `data/hotels.json`.

`pick_hotel` is a naive chooser based on closeness to the nightly budget and rating.
"""
import json, os, random
from typing import List, Dict

DATA = json.load(open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "hotels.json"), "r", encoding="utf-8"))

def list_hotels(city: str) -> List[Dict]:
    return [h for h in DATA if h["city"].lower() == city.lower()]

def pick_hotel(city: str, budget_per_night: float = 120.0) -> Dict:
    candidates = sorted(list_hotels(city), key=lambda x: (abs(x["nightly_price"]-budget_per_night), -x["rating"]))
    return candidates[0] if candidates else random.choice(DATA)
