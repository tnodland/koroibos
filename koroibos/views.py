from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Sport
from .models import Event
from .models import Olympian
from .serializers import OlympianSerializer
from .serializers import SportSerializer
from django.db.models import Min
from django.db.models import Avg

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
                oldest = Olympian.objects.filter().annotate(Min('age')).order_by('age').reverse()[0]
                olympian = {
                    'name': oldest.name,
                    'team': oldest.team,
                    'age': oldest.age,
                    'sport': oldest.sport.name,
                    'total_medals_won': oldest.total_medals()
                }
                return Response(olympian)
        else:
            return self.list(request, *args, **kwargs)

class ListOlympianStatsView(APIView):
    def get(self, request):
        total = Olympian.objects.count()
        average_age = Olympian.objects.all().aggregate(Avg('age'))['age__avg']
        average_male_weight = Olympian.objects.all().filter(sex='M').aggregate(Avg('weight'))['weight__avg']
        average_female_weight = Olympian.objects.all().filter(sex='F').aggregate(Avg('weight'))['weight__avg']
        # import code; code.interact(local=dict(globals(), **locals()))
        data = {
            'olympian_stats': {
                'total_competing_olympians': total,
                'average_weight': {
                    'unit': 'kg',
                    'male_olympians': average_male_weight,
                    'female_olympians': average_female_weight
                },
                'average_age': average_age
            }
        }

        return Response(data)

class ListEventsView(generics.ListAPIView):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()

class ListMedalistsView(APIView):
    def get(self, request, **kwargs):
        event_id = kwargs['event_id']
        event = Event.objects.filter(id=event_id)[0]
        medalists = Olympian.objects.filter(event=event).exclude(medal=None)
        data = {
            "event": event.name,
            "medalists": [
                {
                    "name": medalists[0].name,
                    "team": medalists[0].team,
                    "age": medalists[0].age,
                    "medal": medalists[0].medal
                },
                {
                    "name": medalists[1].name,
                    "team": medalists[1].team,
                    "age": medalists[1].age,
                    "medal": medalists[1].medal
                },
                {
                    "name": medalists[2].name,
                    "team": medalists[2].team,
                    "age": medalists[2].age,
                    "medal": medalists[2].medal
                },
            ]
        }
        return Response(data)
