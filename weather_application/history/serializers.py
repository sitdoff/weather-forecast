from rest_framework import serializers

from .models import HistoryModel


class HistorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных количества запросов по городам.
    """

    requests = serializers.SerializerMethodField()

    class Meta:
        model = HistoryModel
        fields = ["requests"]

    def get_requests(self, obj):
        return obj.get_requests()
