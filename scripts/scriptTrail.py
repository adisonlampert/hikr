from scripts import google_places
from scripts import google_geocoding
from scripts import weather
from dotenv import load_dotenv
from flask import url_for
import os
import datetime

def getInfoByLatLong(lat, long, place_id):

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')
    weatherApi = weather.Weather(OPEN_WEATHER_KEY)
    placesApi = google_places.GooglePlaces(GOOGLE_API_KEY)

    fields = ['name', 'formatted_address', 'photos', 'website', 'rating', 'review', 'geometry', 'opening_hours']

    details = placesApi.get_place_details(place_id, fields)

    placeDict = {}

    placeDict['lat'] = lat
    placeDict['long'] = long

    try:
        placeDict['photos']=[]
        for i in range(len(details['result']['photos'])):
          if i==7:
            break
          placeDict['photos'].append("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="+details['result']['photos'][i]['photo_reference']+"&key="+GOOGLE_API_KEY)
    except KeyError:
        placeDict['photos'] = ""

    try:
        placeDict['is_open'] = details['result']['opening_hours']['open_now']
    except KeyError:
        placeDict['is_open'] = ""

    try:
      placeDict['hours'] = details['result']['opening_hours']['weekday_text']
      

    except:
      placeDict['hours']=""

    try:
        placeDict['website'] = details['result']['website']
    except KeyError:
        placeDict['website'] = ""

    try:
        placeDict['rating'] = details['result']['rating']
    except KeyError:
        placeDict['rating'] = ""

    try:
        placeDict['name'] = details['result']['name']
    except KeyError:
        placeDict['name'] = ""

    try:
        placeDict['address'] = details['result']['formatted_address']
    except KeyError:
        placeDict['address'] = ""

    try:
        placeDict['reviews'] = details['result']['reviews']
    except KeyError:
        placeDict['reviews'] = []

    weatherResponse = weatherApi.get_weather(lat, long)
    placeDict["weatherData"] = {}

    dayCount = 0
    for day in weatherResponse["daily"]:
      currentDay = dayCount
      placeDict["weatherData"][currentDay]= {}

      dateOf, sunrise = str(datetime.datetime.utcfromtimestamp(day["sunrise"]+weatherResponse["timezone_offset"])).split(" ")
      dateOf, sunset = str(datetime.datetime.utcfromtimestamp(day["sunset"]+weatherResponse["timezone_offset"])).split(" ")
      dayTemp = day["temp"]["day"]
      mornTemp = day["temp"]["morn"]
      eveTemp = day["temp"]["eve"]
      nightTemp = day["temp"]["night"]
      humidity = day["humidity"]
      wind_speed = day["wind_speed"]
      weatherMain = day["weather"][0]["main"]
      weatherDescription = day["weather"][0]["description"]
      weatherIcon = day["weather"][0]["icon"]
      clouds = day["clouds"]
      rain = day["pop"]
      uvi = day["uvi"]

      placeDict["weatherData"][currentDay]["day"] = dateOf
      placeDict["weatherData"][currentDay]["sunrise"] = sunrise
      placeDict["weatherData"][currentDay]["sunset"] = sunset
      placeDict["weatherData"][currentDay]["temp"] = {}
      placeDict["weatherData"][currentDay]["temp"]["day"] = dayTemp
      placeDict["weatherData"][currentDay]["temp"]["morn"] = mornTemp
      placeDict["weatherData"][currentDay]["temp"]["eve"] = eveTemp
      placeDict["weatherData"][currentDay]["temp"]["night"] = nightTemp
      placeDict["weatherData"][currentDay]["humidity"] = humidity
      placeDict["weatherData"][currentDay]["wind_speed"] = wind_speed
      placeDict["weatherData"][currentDay]["weather"] = {}
      placeDict["weatherData"][currentDay]["weather"]["main"] = weatherMain
      placeDict["weatherData"][currentDay]["weather"]["description"] = weatherDescription.title()
      placeDict["weatherData"][currentDay]["weather"]["icon"] = weatherIcon
      placeDict["weatherData"][currentDay]["clouds"] = clouds
      placeDict["weatherData"][currentDay]["rain"] = rain
      placeDict["weatherData"][currentDay]["uvi"] = uvi

      dayCount+=1

    return placeDict

