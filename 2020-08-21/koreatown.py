"""LA Metro/Koreatown

LA Metro has GPS trackers in all of their vehicles that live-report back.
They also offer a JSON API that allows for query that live reporting for
vehicles locations.

The API is available at: http://api.metro.net/agencies/lametro/vehicles/

It just so happens that Koreatown is a rectangle. In (latitude, longitude)
format, Koreatown's borders are:

- Northwest corner of (34.068987, -118.3113447)
- Southeast corner of (34.052648, -118.291619)

Make a function that returns all vehicle IDs currently in LA's Koreatown.

print(koreatown_vehicles())
['9412', '5901', ...]

The goal here to provide a readable proof-of-concept-grade solution.
- Find interesting stats about the traffic on this area 
  - Number of vehicles in the last 30 secs
  - Spot with highest traffic
  - Route with most cars
  - etc.

Notes:

- Access the API directly. (Do not download the content)
"""
