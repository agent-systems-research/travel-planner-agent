from typing import Optional
from .images_live import image_for as live_image_for

def image_for(name: str) -> str:
    url = live_image_for(name)
    if url:
        return url
    # fallback placeholder
    import random
    w, h = 800, 500
    seed = abs(hash(name)) % 10000 + random.randint(0, 9999)
    return f"https://picsum.photos/seed/{seed}/{w}/{h}"
