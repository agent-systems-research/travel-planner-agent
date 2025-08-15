"""In-memory conversation state (placeholder for a real DB or vector store)."""
from typing import List, Dict, Any
from .schemas import TravelerProfile, Party, Budget

class ConversationState:
    """Stores participants, unresolved questions, and hard constraints."""
    def __init__(self, user_group_id: str = "demo"):
        self.user_group_id = user_group_id
        self.participants: List[TravelerProfile] = []
        self.unresolved_questions: List[str] = []
        self.constraints: Dict[str, Any] = {}

    def load_party(self, party: Party):
        self.participants = party.participants

    def set_constraints(self, **kwargs):
        self.constraints.update(kwargs)

    def ask_for_missing(self):
        """Return a list of questions for any missing required fields."""
        missing = []
        if "start_date" not in self.constraints: missing.append("What are your trip start/end dates?")
        if "budget" not in self.constraints: missing.append("What is your total budget and currency?")
        if "destination_city" not in self.constraints: missing.append("Which destination city?")
        self.unresolved_questions = missing
        return missing
