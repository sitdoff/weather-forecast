from datetime import datetime

import requests
from geopy.geocoders import Nominatim
from request_config import REQUEST_CONFIG, URL


def get_coordinates(city: str) -> tuple:
    """
    Получает координаты города по его названию.
    """
    geolocator = Nominatim(user_agent="weather_application")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


def get_response(city: str) -> dict:
    """
    Получает данные от API.
    """
    latitude, longitude = get_coordinates(city)
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
        time = datetime.fromtimestamp(time).strftime("%d.%m.%Y, %H:%M:%S")
        result[time] = {}
        for variable in REQUEST_CONFIG["hourly"]:
            result[time][variable] = f"{response["hourly"][variable][i]} {response["hourly_units"][variable]}"

    return result


def get_forecast(city: str) -> dict[datetime, dict[str, str]]:
    """
    Получает прогноз погоды.
    """
    response = get_response(city)
    forecast = data_formatting(response)
    return forecast
