"""Simple CLI runner for the travel planner agent.

Edit the `ConversationInput` below and run `python main.py` to generate an itinerary.
"""
from app.core.schemas import ConversationInput, Budget, Party, TravelerProfile
from app.core.graph import run_pipeline
import json

def main():
    ci = ConversationInput(
        origin_city="London",
        destination_city="New York",
        start_date="2025-08-16",
        end_date="2025-08-20",
        budget=Budget(currency="GBP", total=2000),
        party=Party(participants=[
            TravelerProfile(name="Alice", role="adult", prefs_museums=True, prefs_walkability="medium"),
            TravelerProfile(name="Bob", role="adult", prefs_museums=False, prefs_walkability="low"),
        ]),
        must_see=["Statute of Liberty", "Central Park"],
        ask_missing=False
    )
    itinerary = run_pipeline(ci)

    # Save the full JSON output for programmatic use.
    with open("itinerary.json", "w", encoding="utf-8") as f:
        json.dump(json.loads(itinerary.json()), f, indent=2)

    # Print a human-readable summary.
    print("# Itinerary")
    print(f"City: {itinerary.city} ({itinerary.start_date} → {itinerary.end_date})")
    print(f"Total cost (est.): {itinerary.total_cost:.2f} {itinerary.currency}")
    for day in itinerary.days:
        print(f"\n## {day.date}")
        for block in day.hour_by_hour:
            print(f"- {block.start}-{block.end}: {block.title or block.item_type}")
        print(f"  Commute: {day.commute_minutes} mins, Day cost: {day.day_cost:.2f}")

    if itinerary.reservations:
        print("\n### Dummy Reservations")
        for r in itinerary.reservations:
            print(f"- [{r.kind.upper()}] {r.hold_id} for item {r.item_id} (valid until {r.valid_until}) → {r.url}")

if __name__ == "__main__":
    main()
