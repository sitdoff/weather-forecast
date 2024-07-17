from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from history.utils import add_history

from .forms import CityForm
from .utils import get_forecast


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Функция главной страницы.

    Тут вызывается функция возвращающая данные прогноза погоды.
    Тут обновляется история запросов.
    Тут устанавливается кука с данными о последнем городе, для которого запрашивали прогноз погоды.
    """
    last_city = request.COOKIES.get("last_city", None)
    if last_city:
        try:
            last_city = urlsafe_base64_decode(last_city).decode("utf-8")
        except (TypeError, ValueError, UnicodeError):
            last_city = None

    if request.method == "GET":
        form = CityForm(initial={"city": last_city} if last_city else None)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            # Если функцию add_history вызывать в этом месте,
            # то в историю будут попадать даже невалидные запросы.
            # Если такое не надо, то вызов функции надо перенести в блок else.
            add_history(request)
            try:
                forecast = get_forecast(city)
            except ValueError:
                form.add_error("city", "Error: City not found")
            else:
                response = render(request, "weather/index.html", {"form": form, "forecast": forecast})
                encoded_city = urlsafe_base64_encode(city.encode())
                response.set_cookie("last_city", encoded_city)
                return response
    return render(request, "weather/index.html", context={"form": form})
