import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
 
class GooglePlaces(object):
    # Creates GooglePaces object
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey

    # Uses long and lat for location (string seperated by comma)
    # radius in m and a list of location types
    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'keyword': types,
            'location': location,
            'radius': radius,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details

