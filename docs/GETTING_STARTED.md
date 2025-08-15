# Getting Started

## 1) Install & run
```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt

python main.py                # CLI run
uvicorn app.api.server:app --reload   # API server
```

## 2) Inspect outputs
- `itinerary.json` contains the validated Pydantic `Itinerary`.
- CLI prints a formatted summary with day schedules and costs.

## 3) Next steps
- Tweak `ConversationInput` in `main.py`.
- Replace dummy tools with real APIs (see `docs/TOOLS.md`).
- Enforce JSON schema validation in automated tests.
