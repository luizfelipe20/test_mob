
import time
import pymongo
import pprint
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyDtt-ixG49WuKZdFEJPhTj6q1sMk_KluxE'
location_search = "Av. Abolição 4140"
keyword_search = "Padaria"

google_places = GooglePlaces(YOUR_API_KEY)

query_result = google_places.nearby_search(location=location_search, keyword=keyword_search, radius=300000, rankby='distance')


def coordinates():
    data = []
    for place in query_result.places:
        data.append(place)
    return data

