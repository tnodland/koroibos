from rest_framework import serializers
from .models import Sport
from .models import Event
from .models import Olympian

class OlympianSerializer(serializers.ModelSerializer):
    sport = serializers.CharField(source='sport.name')
    total_medals_won = serializers.IntegerField(source='total_medals')
    class Meta:
        model = Olympian
        fields = ('id', 'name', 'team', 'age', 'sport', 'total_medals_won')
