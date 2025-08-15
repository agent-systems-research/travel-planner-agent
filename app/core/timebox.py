"""Scheduling logic: turn unordered items into an hour-by-hour timeline."""
from typing import List, Tuple
from .schemas import POI, Leg, TimelineBlock, DayPlan
from datetime import datetime, timedelta

def _fmt(t):
    return t.strftime("%H:%M")

def schedule_day(date_str: str, items: List):
    """Naive scheduler starting at 09:00. Places each item and accumulates commute minutes."""
    start = datetime.strptime(date_str + " 09:00", "%Y-%m-%d %H:%M")
    blocks: List[TimelineBlock] = []
    commute_total = 0
    for it in items:
        if isinstance(it, POI):
            dur = int(it.est_time_mins or 60)
            end = start + timedelta(minutes=dur)
            blocks.append(TimelineBlock(start=_fmt(start), end=_fmt(end), item_type="poi", ref_id=it.id, title=it.name))
            start = end
        else:
            dur = int(it.eta_mins or 10)
            end = start + timedelta(minutes=dur)
            blocks.append(TimelineBlock(start=_fmt(start), end=_fmt(end), item_type="leg", title=f"{it.mode.title()} to {it.dest_name}"))
            start = end
            commute_total += dur
    return blocks, commute_total
