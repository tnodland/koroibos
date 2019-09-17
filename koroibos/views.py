from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sport
from .models import Event
from .models import Olympian
from .serializers import OlympianSerializer

class ListOlympiansView(generics.ListAPIView):
    queryset = Olympian.objects.all()
    serializer_class = OlympianSerializer
