from scripts import google_places
from scripts import google_geocoding
from scripts import weather
from dotenv import load_dotenv
from flask import url_for
import os

def searchByAddress(address):

  load_dotenv()
  GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
  #OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')

  geocodeApi = google_geocoding.GoogleGeocode(GOOGLE_API_KEY)
  api = google_places.GooglePlaces(GOOGLE_API_KEY)
  #weatherApi = weather.Weather(OPEN_WEATHER_KEY)

  lat,long = geocodeApi.getGeocode(address)

  places = api.search_places_by_coordinate(str(lat)+", "+str(long), "10000", "hiking trail")
  fields = ['name', 'formatted_address', 'photos', 'website', 'rating', 'review', 'geometry']

  placeDetails=[]

  count = 0
  for place in places:
    if count==12:
      break

    placeDict = {}

    details = api.get_place_details(place['place_id'], fields)

    placeDict['place_id'] = place['place_id']

    try:
        placeDict['lat'] = details['result']['geometry']['location']['lat']
        placeDict['long'] = details['result']['geometry']['location']['lng']
    except KeyError:
        continue

    try:
        placeDict['photos'] = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="+details['result']['photos'][0]['photo_reference']+"&key="+GOOGLE_API_KEY 
    except KeyError:
        placeDict['photos'] = str(url_for('static', filename='hikrlogo.png'))

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

    count+=1
    placeDetails.append(placeDict)

  return placeDetails
    
