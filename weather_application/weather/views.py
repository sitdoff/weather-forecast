from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from history.utils import add_history

from .forms import CityForm
from .utils import get_forecast


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = CityForm()
    if request.method == "POST":
        add_history(request)
        form = CityForm(request.POST)
        if form.is_valid():
            city = request.POST["city"]
            try:
                forecast = get_forecast(city)
                return render(request, "weather/index.html", {"form": form, "forecast": forecast})
            except ValueError:
                form.errors["city"] = "Error: City not found"
    return render(request, "weather/index.html", context={"form": form})
