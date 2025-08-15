"""Cost aggregation utilities."""
from typing import List, Union
from .schemas import POI, Leg

def compute_day_cost(items: List[Union[POI, Leg]]) -> float:
    """Sum up estimated costs across items in a day."""
    cost = 0.0
    for it in items:
        if isinstance(it, POI):
            cost += float(it.est_cost or 0.0)
        else:
            cost += float(getattr(it, "cost", 0.0) or 0.0)
    return round(cost, 2)
