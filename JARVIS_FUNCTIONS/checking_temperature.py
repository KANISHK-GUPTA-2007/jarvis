import requests
import json
from jarvis_speak.speak import speak_safe

def get_temp_open_weather_map(city):
    api_key = 'da45ce263f805531026f1e79b411d6f5'
    end_point = 'https://api.openweathermap.org/data/2.5/weather'
    response = requests.get(end_point, params = {'q': city, 'appid':api_key,'units':'metric'})
    if response.status_code == 200:
        data = json.loads(response.text)
        if 'main' in data:
            temp_celsius = data['main']['temp']
            return temp_celsius
        else:
            speak_safe("error : 'main' key not found in API response")
    else:
        speak_safe("error : failed fetch data from API.")
    return None

def temp():
    city = 'jaipur,Rajasthan'
    temp_celsius = get_temp_open_weather_map(city)
    if temp_celsius is not None:
        speak_safe(f'the weather in city {city} is {temp_celsius} degree celsius')
    else:
        speak_safe('temperature data not available')


