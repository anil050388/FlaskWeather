import requests
#from dotenv import load_dotenv
import os
from dataclasses import dataclass
from config import get_secret

API = get_secret()
API_Key = API['MY_KEY']


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: round
    Country: str
    FeelsLike: round
    Humidity: round
    Speed: float


def get_lan_lon(city_name, state_code, country_code, API_key):
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}')
        resp.raise_for_status()
        response = resp.json()
        data = response['coord']
        lat, lon = data.get('lat'), data.get('lon')
        return lat, lon
    except requests.exceptions.HTTPError as Err:
        error = Err
        errorcode = 9999
        return errorcode, error

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temperature = resp.get('main').get('temp'),
        Country = resp.get('sys').get('country'),
        FeelsLike = resp.get('main').get('feels_like'),
        Humidity = resp.get('main').get('humidity'),
        Speed = resp.get('wind').get('speed')
    )
    return data

def main(city_name, state_name, country_name):
    error = ''
    lat, lon = get_lan_lon(city_name,state_name,country_name,API_key)
    if lat != 9999:
        weather_data = get_current_weather(lat, lon, API_key)
    else:
        weather_data = "Error"
    return weather_data