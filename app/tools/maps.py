"""Rudimentary distance/time estimates using haversine + average speeds.

For production, replace with Google Distance Matrix or similar.
"""
from typing import Dict
from ..core.utils import haversine_km, minutes_for_distance_km

def estimate_leg(origin: Dict, dest: Dict, mode: str = "walk"):
    km = haversine_km(origin["lat"], origin["lon"], dest["lat"], dest["lon"])
    mins = minutes_for_distance_km(km, mode=mode)
    cost = 0.0 if mode in ("walk","transit") else round(km * 1.2, 2)
    return {"km": round(km, 2), "eta_mins": mins, "mode": mode, "cost": cost}
