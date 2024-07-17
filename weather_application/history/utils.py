from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest

from .models import HistoryModel


def add_history(request: HttpRequest):
    user = request.user if not isinstance(request.user, AnonymousUser) else None
    HistoryModel.objects.create(user=user, city=request.POST["city"])
