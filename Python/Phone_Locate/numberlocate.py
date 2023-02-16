import phonenumbers
import opencage
import folium
from myphone import *
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number3)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service = phonenumbers.parse(number)
print(carrier.name_for_number(service, "en"))

key = '80d72e8bfd6c4627b0ab141ba909ff2f'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0] ['geometry'] ['lat']
lng = results[0] ['geometry'] ['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")
