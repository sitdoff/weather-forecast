from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import City
from .utils import get_forecast


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = City()
    if request.method == "POST":
        form = City(request.POST)
        if form.is_valid():
            city = request.POST["city"]
            try:
                forecast = get_forecast(city)
                return render(request, "weather/index.html", {"form": form, "forecast": forecast})
            except ValueError:
                form.errors["city"] = "Error: City not found"

    return render(request, "weather/index.html", context={"form": form})
