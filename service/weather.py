import json
import httpx
from constant import OPEN_WEATHER_API

GridX = 124
GridY = 67
Office = 'SEW'

async def getWeatherInfo():
    try:
        res = httpx.get(f'https://api.weather.gov/gridpoints/{Office}/{GridX},{GridY}/forecast').json()
        temp, weather = res["properties"]["periods"][0]["temperature"], res["properties"]["periods"][0]["detailedForecast"]
        return temp, weather
    except:
        # This is an http error
        res.raise_for_status()
