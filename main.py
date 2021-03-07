from flask import Flask, render_template, request, redirect, url_for
from scripts import script
from scripts import scriptTrail

web_site = Flask(__name__)


@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/hikes/<location>')
def get_results(location):
  hikes = script.searchByAddress(location)
  return render_template('search.html', address=location.replace("-",", "), hikes = hikes, hikeLength=len(hikes))

@web_site.route('/trail/<lat>/<long>/<place_id>')
def get_trail(lat,long, place_id):
  trail = scriptTrail.getInfoByLatLong(lat,long,place_id)
  daysOfTheWeek = ["Sunday","Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday"]
  return render_template('trail.html',trail=trail, photoLen=len(trail['photos']), weekDays=daysOfTheWeek)

@web_site.route('/search-results', methods=["POST"])
def return_info():
  address = request.form.get('address')
  address = address.replace(", ", "-")
  return redirect(url_for('get_results', location=address))



web_site.run(host='0.0.0.0', port=8080)