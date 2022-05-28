import pyowm
from pyowm import OWM

owm = pyowm.OWM('2c7eb73c2d4e9c7ef84681d3289f35d6')
mgr = owm.weather_manager()
# Запрос у пользователя в каком городе он хочет узнать погоду
place = input("В каком городе\стране?: ")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.get_weather()
print(w)