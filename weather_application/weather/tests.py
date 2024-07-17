from unittest.mock import patch

from django.test import Client, TestCase
from django.urls import reverse
from history.models import HistoryModel

from .forms import CityForm


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("weather:index")

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")
        self.assertIsInstance(response.context["form"], CityForm)

    @patch("weather.views.get_forecast")
    def test_post_request_valid_city(self, mock_get_forecast):
        mock_forecast = {"datetime": {"temperature": "20 °C", "humidity": "80 %"}}
        mock_get_forecast.return_value = mock_forecast

        response = self.client.post(self.url, {"city": "Berlin"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")
        self.assertIsInstance(response.context["form"], CityForm)
        self.assertEqual(response.context["forecast"], mock_forecast)

    @patch("weather.views.get_forecast")
    def test_post_request_invalid_city(self, mock_get_forecast):
        mock_get_forecast.side_effect = ValueError("City not found")

        response = self.client.post(self.url, {"city": "InvalidCity"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")
        self.assertIsInstance(response.context["form"], CityForm)
        self.assertIn("Error: City not found", response.context["form"].errors["city"])

    def test_post_request_add_history(self):
        response = self.client.post(self.url, {"city": "Berlin"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(HistoryModel.objects.filter(city="Berlin").exists())
