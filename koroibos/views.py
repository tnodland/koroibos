from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Sport
from .models import Event
from .models import Olympian
from .serializers import OlympianSerializer
from django.db.models import Min

class ListOlympiansView(generics.ListAPIView):
    serializer_class = OlympianSerializer
    queryset = Olympian.objects.all()

    def get(self, request, *args, **kwargs):
        if 'age' in request.query_params:
            if request.query_params['age'] == 'youngest':
                youngest = Olympian.objects.filter().annotate(Min('age')).order_by('age')[0]
                olympian = {
                    'name': youngest.name,
                    'team': youngest.team,
                    'age': youngest.age,
                    'sport': youngest.sport.name,
                    'total_medals_won': youngest.total_medals()
                }
                return Response(olympian)
        else:
            return self.list(request, *args, **kwargs)
