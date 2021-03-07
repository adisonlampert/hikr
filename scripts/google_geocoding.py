import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


class GoogleGeocode(object):
    #Creates GooglePaces object
    def __init__(self, apiKey):
        super(GoogleGeocode, self).__init__()
        self.apiKey = apiKey

    #Uses long and lat for location (string seperated )
    def getGeocode(self, address):
        endpoint_url = "https://maps.googleapis.com/maps/api/geocode/json"

        params = {
            'address': address,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        lat = results['results'][0]['geometry']['location']['lat']
        lng = results['results'][0]['geometry']['location']['lng']
        
        return lat, lng