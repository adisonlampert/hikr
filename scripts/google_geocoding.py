import requests
import json
from dotenv import load_dotenv
import os
import time

#Google geocode object allows us to convert addresses into specific latitude and longitude coordinates
class GoogleGeocode(object):
    #Creates GooglePaces object
    def __init__(self, apiKey):
        super(GoogleGeocode, self).__init__()
        self.apiKey = apiKey

    #Uses long and lat for location (string seperated )
    def getGeocode(self, address):
        #geocode API
        endpoint_url = "https://maps.googleapis.com/maps/api/geocode/json"

        #request parameters
        params = {
            'address': address,
            'key': self.apiKey
        }

        #process request results
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        lat = results['results'][0]['geometry']['location']['lat']
        lng = results['results'][0]['geometry']['location']['lng']
        
        return lat, lng