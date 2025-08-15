"""Very lightweight dummy 'booking holds' stored in a JSON file.

This simulates external side-effects (like a reservation) without calling real APIs.
"""
import json, os, time, random, string
from datetime import datetime, timedelta
from .schemas import ReservationHold

DB_PATH = os.environ.get("BOOKINGS_DB", "bookings.db.json")

def _load():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"holds": []}

def _save(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2)

def _gen_id(prefix="HOLD"):
    return prefix + "_" + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

def reserve_dummy(kind: str, item_id: str, party_size: int = 2, ttl_hours: int = 48):
    """Create a pseudo-reservation that expires in `ttl_hours`.

Returns a `ReservationHold`."""
    db = _load()
    hold_id = _gen_id(kind.upper())
    valid_until = (datetime.utcnow() + timedelta(hours=ttl_hours)).isoformat() + "Z"
    url = f"https://example.com/manage/{hold_id}"
    rec = {"hold_id": hold_id, "kind": kind, "item_id": item_id, "party_size": party_size, "valid_until": valid_until, "url": url}
    db["holds"].append(rec)
    _save(db)
    return ReservationHold(**rec)
