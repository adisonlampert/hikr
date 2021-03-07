import requests
import json
import os
import time

#Google Places Object lets us interact with Google Places API to find locations and get their information
class GooglePlaces(object):
    # Creates GooglePaces object
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey

    # Uses long and lat for location (string seperated by comma)
    # radius in m and a list of location types
    def search_places_by_coordinate(self, location, radius, types):
        #google places API
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []

        #request parameters
        params = {
            'keyword': types,
            'location': location,
            'radius': radius,
            'key': self.apiKey
        }

        #make Google Places request and handle response
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        return places

    #returns info for specified fields based on Google Places place_id
    def get_place_details(self, place_id, fields):
        #google places API
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"

        #request parameters
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }

        #make Google Places request and handle response
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details
