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
lald = "-7.567466, 110.280876"
print("Latitude and Longitude:",lald)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.620938, 110.334822"
print("Latitude and Longitude:",lald)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.692486, 110.333235"
print("Latitude and Longitude:",lald)

