#------------------------------ PHONE NUMBER TRACKER --------------------------------

import phonenumbers
from phonenumbers import timezone,geocoder,carrier

#-------------------------------- Getting Detaols ----------------------------------------

number=input("Masukan Nomer    :   ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
reg=geocoder.description_for_number(phone,'en')
car=carrier.name_for_number(phone,'en')

#-------------------------------- Printing Details ----------------------------------------

print("Info  :")
print(phone)
print(time)
print(reg)
print(car)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.754306, 110.384712"
print("Latitude and Longitude:",lald)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.760040, 110.383308"
print("Latitude and Longitude:",lald)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.768044, 110.390126"
print("Latitude and Longitude:",lald)
