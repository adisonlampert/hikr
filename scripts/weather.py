import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('OPEN_WEATHER_KEY')
 
class Weather(object):
    # Creates Weather object
    def __init__(self, apiKey):
        super(Weather, self).__init__()
        self.apiKey = apiKey

    def get_weather(self, lat, lon):
        endpoint_url = "https://api.openweathermap.org/data/2.5/onecall"
        params = {
            'lat': lat,
            'lon': lon,
            'exclude': "current,minutely,hourly,alerts",
            'appid': self.apiKey,
            'units': 'imperial'
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        return results