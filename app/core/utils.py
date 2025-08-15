"""Math helpers for distance and simple travel-time estimation."""
from math import radians, sin, cos, sqrt, atan2

def haversine_km(lat1, lon1, lat2, lon2):
    """Compute geodesic distance between two lat/lon points in kilometers."""
    R = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def minutes_for_distance_km(km: float, mode: str = "walk"):
    """Very rough travel time from distance (km) and mode."""
    if mode == "walk":
        speed_kmh = 4.5
    elif mode == "transit":
        speed_kmh = 20.0
    else:
        speed_kmh = 25.0
    return int((km / speed_kmh) * 60)
