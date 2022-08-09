import folium
import opencage
import phonenumbers
from myphonenumber import myphone

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(myphone)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(myphone)
print(carrier.name_for_number(service_provider,"en"))


from opencage.geocoder import OpenCageGeocode
key = "d4f68bd8477c4abe904764842094aba9"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat,lng],popup = location).add_to(myMap)

myMap.save("mylocation.html")

