""" Get Seattle weather information from the weather API.
"""
from utils import get

GridX = 124
GridY = 67
Office = 'SEW'


def get_weather_info():
    """
    It takes the office location and grid coordinates and uses them to make a
    request to the weather API.

    The response is then parsed to get the temperature and weather description.

    The temperature and weather description are then returned.

    Returns:
      A tuple of two strings, the temperature and the weather.
    """
    url = f'https://api.weather.gov/gridpoints/{Office}/{GridX},{GridY}/forecast'
    response = get(url)

    temp, weather = '', ''
    # Error handle if catch response error, get will return None
    if response and response.get("properties", None):
        temp = response["properties"]["periods"][0]["temperature"]
        weather = response["properties"]["periods"][0]["detailedForecast"]

    return temp, weather
