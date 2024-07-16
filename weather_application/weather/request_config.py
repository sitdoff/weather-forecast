URL = "https://api.open-meteo.com/v1/forecast"

REQUEST_CONFIG = {
    "hourly": ["temperature_2m", "relative_humidity_2m", "rain", "wind_speed_10m"],
    "timeformat": "unixtime",
    "timezone": "Europe/Moscow",
    "forecast_days": 1,
}
