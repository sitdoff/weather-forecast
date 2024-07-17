"""
В этом модуле находятся вспомогательные функции для работы с API.
"""

from datetime import datetime

import requests
from geopy.geocoders import Nominatim
from weather.request_config import REQUEST_CONFIG, URL


def get_coordinates(city: str) -> tuple:
    """
    Получает координаты города по его названию.
    """
    geolocator = Nominatim(user_agent="weather_application")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    raise ValueError("City not found")


def get_response(latitude, longitude) -> dict:
    """
    Получает данные от API.
    """
    REQUEST_CONFIG.update({"latitude": latitude, "longitude": longitude})
    with requests.get(URL, params=REQUEST_CONFIG) as response:
        response = response.json()
    return response


def data_formatting(response: dict) -> dict:
    """
    Приводит данные к удобному формату.
    """
    result = {}
    for i, time in enumerate(response["hourly"]["time"]):
        if time < datetime.now().timestamp():
            continue
        time = datetime.fromtimestamp(time)
        result[time] = {}
        for variable in REQUEST_CONFIG["hourly"]:
            result[time][variable] = f"{response["hourly"][variable][i]} {response["hourly_units"][variable]}"

    return result


def get_forecast(city: str) -> dict[datetime, dict[str, str]]:
    """
    Получает прогноз погоды.
    """
    latitude, longitude = get_coordinates(city)
    response = get_response(latitude, longitude)
    forecast = data_formatting(response)
    return forecast
