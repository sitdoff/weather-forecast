from django.urls import path

from . import views

app_name = "history"
urlpatterns = [
    path("history/", views.RequestHistory.as_view(), name="city-request"),
]
