from scripts import google_places
from scripts import google_geocoding
from dotenv import load_dotenv
from flask import url_for
import os

#returns list of search results generated for specific address
def searchByAddress(address):

  #handle api key privately
  load_dotenv()
  GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

  #create google places and google geocode objects
  geocodeApi = google_geocoding.GoogleGeocode(GOOGLE_API_KEY)
  api = google_places.GooglePlaces(GOOGLE_API_KEY)

  #uses geocode object/API to convert address to lat, long
  lat,long = geocodeApi.getGeocode(address)

  #find places near lat, long using google places object/api
  places = api.search_places_by_coordinate(str(lat)+", "+str(long), "10000", "hiking trail")
  fields = ['name', 'formatted_address', 'photos', 'website', 'rating', 'review', 'geometry']

  #list to hold info for each trail
  placeDetails=[]

  # for loop to add 12 places to placeDetails that will be displayed in search results
  count = 0
  for place in places:
    #stop if 12 places have been added
    if count==12:
      break

    #create dictionary for place info
    placeDict = {}

    #request information
    details = api.get_place_details(place['place_id'], fields)

    #The next several lines parse through the api response to check if info was found and add that info to the placeDict

    placeDict['place_id'] = place['place_id']

    try:
        placeDict['lat'] = details['result']['geometry']['location']['lat']
        placeDict['long'] = details['result']['geometry']['location']['lng']
    except KeyError:
        continue

    try:
        placeDict['photos'] = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="+details['result']['photos'][0]['photo_reference']+"&key="+GOOGLE_API_KEY 
    except KeyError:
        placeDict['photos'] = str(url_for('static', filename='image/hikrlogo.png'))

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
    
