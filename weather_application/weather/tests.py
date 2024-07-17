from datetime import datetime
from unittest.mock import MagicMock, patch

from django.test import TestCase
from django.utils import timezone
from weather.utils import data_formatting, get_coordinates, get_forecast, get_response


class TestUtilsFunctions(TestCase):

    @patch("weather.utils.Nominatim.geocode")
    def test_get_coordinates(self, mock_geocode):
        # Подготовка мок объекта Nominatim
        mock_geocode.return_value.latitude = 52.520008
        mock_geocode.return_value.longitude = 13.404954

        # Тестирование функции get_coordinates
        city = "Berlin"
        latitude, longitude = get_coordinates(city)
        self.assertEqual(latitude, 52.520008)
        self.assertEqual(longitude, 13.404954)

        # Тест на случай, если город не найден
        mock_geocode.return_value = None
        with self.assertRaises(ValueError):
            get_coordinates(city)
