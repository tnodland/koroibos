from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Event
from .models import Sport
from .models import Olympian

class BaseTest(APITestCase):
    client = APIClient()

class AllOlymipiansTest(BaseTest):

    def test_it_can_get_all_olympians_on_the_database(self):
        sport = Sport(
            name='Sportsball'
        )
        sport.save()

        event = Event(
            name='Big Sport Blast'
        )
        event.save()

        olympian_1 = Olympian(
            name='Sport Man',
            sex='M',
            age=25,
            height=150,
            weight=200,
            team='America',
            games='2016 Summer',
            event=event,
            sport=sport
        )
        olympian_1.save()
        import code; code.interact(local=dict(globals(), **locals()))
