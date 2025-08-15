"""Pydantic models that define all input/output contracts used by the agent.

These schemas keep the pipeline **stable** even when tool internals change.
"""
from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field
from datetime import date, datetime

Weekday = Literal['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

class TravelerProfile(BaseModel):
    """Preferences for a single traveler in the party."""
    name: str
    role: Literal['adult','child'] = 'adult'
    prefs_walkability: Optional[Literal['low','medium','high']] = 'medium'
    prefs_foodie: Optional[bool] = True
    prefs_museums: Optional[bool] = True
    dietary: Optional[str] = None
    accessibility: Optional[Literal['none','limited','wheelchair']] = 'none'

class Party(BaseModel):
    """Group traveling together."""
    participants: List[TravelerProfile] = Field(default_factory=list)

class Budget(BaseModel):
    """Trip budget in a given currency."""
    currency: str = "GBP"
    total: float = 600.0

class Place(BaseModel):
    """City and optional country."""
    city: str
    country: Optional[str] = "UK"

class Leg(BaseModel):
    """A commute leg from one item to another."""
    origin_name: str
    dest_name: str
    mode: Literal['walk','transit','car'] = 'walk'
    eta_mins: int = 10
    cost: float = 0.0

class POI(BaseModel):
    """Point of interest (museum, attraction, food, outdoors)."""
    id: str
    name: str
    city: str
    lat: float
    lon: float
    category: str
    est_time_mins: int = 60
    est_cost: float = 0.0
    open_hours: Optional[dict] = None
    url: Optional[str] = None
    image_url: Optional[str] = None

class TimelineBlock(BaseModel):
    """A block on the hour-by-hour schedule."""
    start: str
    end: str
    item_type: Literal['poi','leg','meal','hotel']
    ref_id: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None

class DayPlan(BaseModel):
    """Plan for a single day: items, timeline, commute, and cost."""
    date: str
    items: List[Union[POI, Leg]] = Field(default_factory=list)
    hour_by_hour: List[TimelineBlock] = Field(default_factory=list)
    commute_minutes: int = 0
    day_cost: float = 0.0

class ReservationHold(BaseModel):
    """A dummy reservation 'hold' to simulate bookings."""
    hold_id: str
    kind: Literal['hotel','activity']
    item_id: str
    party_size: int
    valid_until: str
    url: str

class Itinerary(BaseModel):
    """Top-level itinerary for the entire trip."""
    city: str
    start_date: str
    end_date: str
    currency: str = "GBP"
    days: List[DayPlan] = Field(default_factory=list)
    total_cost: float = 0.0
    links: List[str] = Field(default_factory=list)
    images: List[str] = Field(default_factory=list)
    reservations: List[ReservationHold] = Field(default_factory=list)

class ConversationInput(BaseModel):
    """API input for planning a trip."""
    user_group_id: str = "demo"
    origin_city: Optional[str] = None
    destination_city: str = "London"
    start_date: str = "2025-08-15"
    end_date: str = "2025-08-17"
    budget: Budget = Budget()
    party: Party = Party(participants=[TravelerProfile(name="Alice"), TravelerProfile(name="Bob")])
    must_see: Optional[list] = None
    ask_missing: bool = True

class CriticReport(BaseModel):
    """Validation report from the critic agent."""
    ok: bool = True
    messages: List[str] = Field(default_factory=list)
    directives: List[str] = Field(default_factory=list)
    violations: List[str] = Field(default_factory=list)
