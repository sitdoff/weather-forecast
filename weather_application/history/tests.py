from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import HistoryModel


class CityRequestViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="testuser", password="12345")
        HistoryModel.objects.create(user=self.user, city="Berlin")
        HistoryModel.objects.create(user=self.user, city="Berlin")
        HistoryModel.objects.create(user=self.user, city="Paris")

    def test_get_city_requests(self):
        response = self.client.get("/history/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("requests", response.data)
        requests = response.data["requests"]
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests["Berlin"], 2)
        self.assertEqual(requests["Paris"], 1)
