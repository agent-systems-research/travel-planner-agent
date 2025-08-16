import random
from typing import List, Dict, Optional
from .geocode_live import geocode_city
from .places_live import otm_pois

def list_city_activities(city: str) -> List[Dict]:
    """Live fetch from OpenTripMap, falling back to empty list."""
    coords = geocode_city(city)
    if not coords:
        return []
    lat, lon = coords
    return otm_pois(lat, lon, radius_m=4000, kinds=None, limit=30)

def top_pois(city: str, n: int = 5, categories: Optional[List[str]] = None) -> List[Dict]:
    items = list_city_activities(city)
    # Optionally filter by simple categories (we labeled all as 'attraction' above)
    random.shuffle(items)
    return items[:n]
