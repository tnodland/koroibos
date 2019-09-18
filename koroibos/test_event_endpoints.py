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

class EventMedalistTest(BaseTest):
    def test_it_can_get_medalists_by_event(self):
        sport = Sport(
            name='Sportsball'
        )
        sport.save()

        event_1 = Event(
            id=1
            name='Big Sport Blast',
            sport = sport
        )
        event_1.save()

        event_2 = Event(
            id=2
            name='Big Sport Blast',
            sport = sport
        )
        event_2.save()

        olympian_1 = Olympian(
            name='Sport Man',
            sex='M',
            age=25,
            height=150,
            weight=200,
            team='America',
            games='2016 Summer',
            event=event_1,
            sport=sport,
            medal='Gold'
        )
        olympian_1.save()

        olympian_2 = Olympian(
            name='Sport Man',
            sex='M',
            age=25,
            height=150,
            weight=200,
            team='America',
            games='2016 Summer',
            event=event_1,
            sport=sport,
            medal='Silver'
        )
        olympian_2.save()

        olympian_3 = Olympian(
            name='Sport Man',
            sex='M',
            age=25,
            height=150,
            weight=200,
            team='America',
            games='2016 Summer',
            event=event_2,
            sport=sport
        )
        olympian_3.save()

        olympian_4 = Olympian(
            name='Sport Man',
            sex='M',
            age=25,
            height=150,
            weight=200,
            team='America',
            games='2016 Summer',
            event=event_1,
            sport=sport,
            medal='Gold'
        )
        olympian_4.save()

        response = self.client.get('/api/v1/events/1/medalists')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        response2 = self.client.get('/api/v1/events/2/medalists')

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(len(response2.data), 1)
