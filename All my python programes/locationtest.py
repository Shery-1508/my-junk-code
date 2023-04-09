import geopy.geocoders
import geocoder

g = geocoder.ip('me')
location = g.latlng
# address  = geocoder.reverse(location[0],location[1])
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my")
locationn = geolocator.reverse(f"{location[0]}, {location[1]}",language='en')
print(locationn.address)


print(location)
# print(address)
# print(help(geocoder))
