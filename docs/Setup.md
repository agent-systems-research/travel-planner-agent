# Setup

1. **Python environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -U pip
   pip install -r requirements.txt
   ```

2. **Run the CLI demo**
   ```bash
   python main.py
   ```

3. **Run the API**
   ```bash
   uvicorn app.api.server:app --reload
   # POST http://127.0.0.1:8000/plan with a ConversationInput JSON body
   ```

4. **Environment variables**
   Copy `.env.example` to `.env` if you plan to integrate real APIs.
