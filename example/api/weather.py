from utils import get

GridX = 124
GridY = 67
Office = 'SEW'


def get_weather_info():
    url = f'https://api.weather.gov/gridpoints/{Office}/{GridX},{GridY}/forecast'
    response = get(url)

    temp, weather = '', ''
    # Error handle if catch response error, get will return None
    if response and response.get("properties", None):
        temp = response["properties"]["periods"][0]["temperature"]
        weather = response["properties"]["periods"][0]["detailedForecast"]

    return temp, weather
