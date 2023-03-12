import os
import requests
import json

api_key_file = os.path.join('C:', os.sep, 'temp', 'api_key.txt')

with open(api_key_file, 'r') as f:
    api_key = f.read().strip()

lat = input("Enter latitude: ")
lon = input("Enter longitude: ")

def get_weather_data(api_key, lat, lon):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

weather_data = get_weather_data(api_key, lat, lon)

if weather_data is not None:
    name = weather_data['name']
    pressure = weather_data['main']['pressure']
    temp_max = weather_data['main']['temp_max']
    
    print(f"Name: {name}")
    print(f"Pressure: {pressure}")
    print(f"Maximum temperature: {temp_max}")
else:
    print("Error getting weather data.")
