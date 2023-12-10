import csv
import requests
import urllib.parse
# google map api
API_KEY = 'AIzaSyC_VHUB2js-NasURML-iXxlKNbqioox3kY'
# GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
# STATIC_MAP_BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap'
STREET_VIEW_BASE_URL = 'https://maps.googleapis.com/maps/api/streetview'
COUNTRY = 'France'
#Audio fix

with open('address_100_sample_NEW.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for i, row in enumerate(reader):
        name = row[1]
        address = row[2]
        zip_code = row[3]
        house_number = row[1]

        # # geocode_params = {'address': address, 'key': API_KEY, 'components': f'country:{COUNTRY}'}
        # street_view_params  = {'address': f'{address}, {zip_code}', 'key': API_KEY, 'components': f'country:{COUNTRY}|postal_code:{zip_code}'}
        # geocode_response = requests.get(GEOCODE_BASE_URL, params=geocode_params).json()

        # if geocode_response['status'] == 'OK':
        #     # Get the latitude and longitude of the address
        #     lat = geocode_response['results'][0]['geometry']['location']['lat']
        #     lng = geocode_response['results'][0]['geometry']['location']['lng']

        #     # Build the URL for the static map image
        #     static_map_params = {'center': f'{lat},{lng}', 'zoom': 14, 'size': '400x400', 'key': API_KEY}
        #     static_map_url = f'{STATIC_MAP_BASE_URL}?{urllib.parse.urlencode(static_map_params)}'
        #     # static_map_url = f'{STATIC_MAP_BASE_URL}?center={lat},{lng}&zoom=20&size=400x400&key={API_KEY}'
        #     response = requests.get(static_map_url)
        #     with open(f'{row[0]}.png', 'wb') as f:
        #         f.write(response.content)
        street_view_params = {'location': f'{address},{house_number}', 'size': '400x400', 'key': API_KEY, 'components': f'country:{COUNTRY}'}
        street_view_url = f'{STREET_VIEW_BASE_URL}?{urllib.parse.urlencode(street_view_params)}'

        # Send a request to the Google Street View Static API and save the image
        response = requests.get(street_view_url)
        with open(f'{row[0]}.png', 'wb') as f:
            f.write(response.content)

