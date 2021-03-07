import requests
import json
import os

class Weather(object):
    # Creates Weather object
    def __init__(self, apiKey):
        super(Weather, self).__init__()
        self.apiKey = apiKey

    def get_weather(self, lat, lon):
        #openWeather API
        endpoint_url = "https://api.openweathermap.org/data/2.5/onecall"

        #request parameters
        params = {
            'lat': lat,
            'lon': lon,
            'exclude': "current,minutely,hourly,alerts",
            'appid': self.apiKey,
            'units': 'imperial'
        }

        #makes api request and handles response
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        return results
