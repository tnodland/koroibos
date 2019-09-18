from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Event
from .models import Sport

class BaseTest(APITestCase):
    client = APIClient()

class AllEventsTest(BaseTest):
    def test_it_can_get_all_events_by_sport(self):
        sport_1 = Sport(
            name='Sportsball'
        )
        sport_1.save()

        sport_2 = Sport(
            name='Archery'
        )
        sport_2.save()

        event_1 = Event(
            name='Big Sport Blast',
            sport = sport_1
        )
        event_1.save()

        event_2 = Event(
            name='Small Sport Blast',
            sport = sport_1
        )
        event_2.save()

        event_3 = Event(
            name="Archery men's Team",
            sport = sport_2
        )
        event_3.save()

        event_4 = Event(
            name="Archery women's Team",
            sport = sport_2
        )
        event_4.save()

        response = self.client.get('/api/v1/events')
        # import code; code.interact(local=dict(globals(), **locals()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['sport'], sport_1.name)
        self.assertEqual(response.data[0]['events'][0], event_2.name)
        self.assertEqual(response.data[0]['events'][1], event_1.name)
        self.assertEqual(response.data[1]['sport'], sport_2.name)
        self.assertEqual(response.data[1]['events'][0], event_4.name)
        self.assertEqual(response.data[1]['events'][1], event_3.name)
