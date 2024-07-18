"""
В этом модуле находятся настроки для запроса к API.
"""

from django.conf import settings

URL = "https://api.open-meteo.com/v1/forecast"

REQUEST_CONFIG = {
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m"],
    "timeformat": "unixtime",
    "timezone": settings.TIME_ZONE,
    "forecast_days": 1,
}

VARIABLES_LEXICON = {
    "time": "Время",
    "temperature_2m": "Температура воздуха",
    "relative_humidity_2m": "Относительная влажность",
    "precipitation": "Атмосферные осадки",
    "wind_speed_10m": "Скорость ветра",
}
