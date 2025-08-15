# Extending

## 1) Replace dummy tools with real APIs
- **Maps**: Google Distance Matrix → replace `tools/maps.py` internals.
- **Search/Attractions**: SerpAPI/Yelp/Foursquare → normalize to `POI` fields.
- **Hotels**: Amadeus/Booking/Skyscanner → normalize to {name, lat, lon, nightly_price, rating, url}.
- **Images**: Google CSE / Unsplash / Pexels → return an `image_url` string.

Keep the **function signatures** stable so agents don't need changes.

## 2) Add weather-awareness
- Fetch daily/hourly weather and filter outdoor POIs or propose indoor alternates.

## 3) Cost optimization strategies
- Swap hotel tiers; replace paid activities; cluster POIs by area to cut commute costs.

## 4) Multi-city
- Add a `cities: [Place]` field and an explicit intercity travel day with a `Leg` block.

## 5) UI
- Wrap a Streamlit frontend; render maps, images, and an export-to-Calendar (iCal).
