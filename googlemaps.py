import googlemaps

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=API_KEY)

# Get coordinates from an address
address = "Masinde Muliro University, Kenya"
geocode_result = gmaps.geocode(address)

if geocode_result:
    location = geocode_result[0]['geometry']['location']
    print("Latitude:", location['lat'], "Longitude:", location['lng'])
