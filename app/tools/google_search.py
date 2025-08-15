"""Dummy Google-like search returning a couple of placeholder results.

Swap this for a real search API and keep the return shape stable.
"""
from typing import List, Dict, Optional

def search(query: str, location: Optional[str] = None) -> List[Dict]:
    return [
        {"title": f"Result 1 for {query}", "snippet": "Some useful info...", "url": "https://example.com/1"},
        {"title": f"Result 2 for {query}", "snippet": "More info...", "url": "https://example.com/2"},
    ]
