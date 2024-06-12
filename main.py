from flask import Flask, render_template, request
from phonenumbers import parse, geocoder, carrier
import requests

app = Flask(__name__, static_url_path='/static')

OPEN_CAGE_API_KEY = '439351af12ee49f99d5a4a4a03102b42';

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        try:
            pepnumber = parse(number, "IN")
            location = geocoder.description_for_number(pepnumber, "en")
            service_provider = carrier.name_for_number(pepnumber, "en")
            # Retrieve latitude and longitude using OpenCage Geocoding API
            url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={OPEN_CAGE_API_KEY}"
            response = requests.get(url)
            data = response.json()
            lat = data['results'][0]['geometry']['lat']
            lng = data['results'][0]['geometry']['lng']
            return render_template('result.html', location=location, service_provider=service_provider, lat=lat, lng=lng)
        except Exception as e:
            error = str(e)
            return render_template('index.html', error=error)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
