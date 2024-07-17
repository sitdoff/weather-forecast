from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HistoryModel
from .serializers import HistorySerializer

# Create your views here.


class RequestHistory(APIView):
    def get(self, request):
        serializer = HistorySerializer(HistoryModel())
        return Response(serializer.data)
