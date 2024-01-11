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
lald = "-7.795772, 110.341729"
print("Latitude and Longitude:",lald)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.787221, 110.393758"
print("Latitude and Longitude:",lald)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "-7.781485, 110.410368"
print("Latitude and Longitude:",lald)

