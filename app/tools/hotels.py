# Python 3.9-safe
from typing import List, Dict
from .places_live import google_places_hotels

def list_hotels(city: str) -> List[Dict]:
    return google_places_hotels(city, limit=10)

def pick_hotel(city: str, budget_per_night: float = 120.0) -> Dict:
    hotels = list_hotels(city)
    if not hotels:
        return {"id":"H0","name":"TBD Hotel","city":city,"lat":0,"lon":0,"nightly_price":budget_per_night,"rating":0,"url":"#"}
    hotels = sorted(hotels, key=lambda x: (abs(x["nightly_price"]-budget_per_night), -x.get("rating",0)))
    return hotels[0]
