from flask import Flask, render_template, request, redirect, url_for
from flask_sslify import SSLify
from scripts import script
from scripts import scriptTrail

#create Flask app
app = Flask(__name__)
sslify = SSLify(app) 

#directs user to home page
@app.route('/')
def index():
	return render_template('index.html')

#renders search results page based on location searched
@app.route('/hikes/<location>')
def get_results(location):
  hikes = script.searchByAddress(location)
  return render_template('search.html', address=location.replace("-",", "), hikes = hikes, hikeLength=len(hikes))

#renders detailed trail info based on trail latitude, longitude and Google Places' placeId
@app.route('/trail/<lat>/<long>/<place_id>')
def get_trail(lat,long, place_id):
  trail = scriptTrail.getInfoByLatLong(lat,long,place_id)
  return render_template('trail.html',trail=trail, photoLen=len(trail['photos']))

#redirects search-results to url that displays the address entered
@app.route('/search-results', methods=["POST"])
def return_info():
  address = request.form.get('address')
  address = address.replace(", ", "-")
  return redirect(url_for('get_results', location=address))


if __name__ == '__main__':
    # This is used when running locally. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)