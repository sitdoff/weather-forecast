from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count


# Create your models here.
class HistoryModel(models.Model):
    """
    Модель записи запроса в истории.
    """

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="history",
        null=True,
        default=None,
        verbose_name="Пользователь",
    )
    city = models.CharField(max_length=100, verbose_name="Город")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def get_requests(self):
        """
        Возвращает количество запросов по городам.
        """
        cities = HistoryModel.objects.values("city").annotate(count=Count("city")).order_by("-count")
        result = {city["city"]: city["count"] for city in cities}
        return result
