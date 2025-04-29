import requests
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
address = '1600 Amphitheatre Parkway, Mountain View, CA'
url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
response = requests.get(url)
data = response.json()
if data['status'] == 'OK':
    location = data['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    print(f'Координати: {lat}, {lng}')
else:
    print('Помилка геокодування')