# Phone Number Location Finder

This is a Flask-based web application that allows users to enter an Indian phone number and find the location and service provider. The application displays the information along with a map showing the location.

## Features

- Parse Indian phone numbers
- Retrieve location description and service provider
- Display location on an interactive map
- User-friendly interface with attractive styling

## Technologies Used

- Python
- Flask
- phonenumbers (for parsing and retrieving phone number information)
- OpenCage Geocode API (for geocoding)
- Leaflet.js (for interactive maps)
- HTML/CSS (for front-end)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thenameissushant/phone-location-finder.git
cd phone-location-finder

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

```bash
pip install Flask phonenumbers requests


4. Set up your OpenCage API key:
Sign up at OpenCage to get an API key.
Replace YOUR_OPEN_CAGE_API_KEY in app.py with your actual API key.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
OpenCage Geocode API
Leaflet.js
phonenumbers