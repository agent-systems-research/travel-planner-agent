"""Simple image helper that returns a placeholder image URL.

Swap with Unsplash/Pexels/Google CSE for real POI photos.
"""
def image_for(name: str) -> str:
    import random
    w, h = 800, 500
    seed = abs(hash(name)) % 10000 + random.randint(0, 9999)
    return f"https://picsum.photos/seed/{seed}/{w}/{h}"
