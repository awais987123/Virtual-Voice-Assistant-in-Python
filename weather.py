import requests
from ss import *

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name CITY = "Hyderabad"
# API key API_KEY = "Your API Key"
# upadting the URL
api_address = BASE_URL + "q=" + "Bhalwal" + "&appid=" + key1

json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description


