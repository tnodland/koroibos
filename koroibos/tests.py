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

        olympian_2 = Olympian(
            name='Sport Woman',
            sex='F',
            age=25,
            height=150,
            weight=200,
            team='Brazil',
            games='2016 Summer',
            event=event,
            sport=sport,
            medal='Gold'
        )
        olympian_2.save()

        olympian_3 = Olympian(
            name='Sport Person',
            sex='U',
            age=25,
            height=150,
            weight=200,
            team='Germany',
            games='2016 Summer',
            event=event,
            sport=sport
        )
        olympian_3.save()

        response = self.client.get('/api/v1/olympians')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], olympian_1.name)
        self.assertEqual(response.data[0]['age'], olympian_1.age)
        self.assertEqual(response.data[0]['sport'], sport.name)
        self.assertEqual(response.data[0]['total_medals_won'], 0)
        self.assertEqual(response.data[1]['total_medals_won'], 1)

class OlympianAge(BaseTest):
    def test_it_can_get_the_youngest_olympian(self):
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

        olympian_2 = Olympian(
            name='Sport Woman',
            sex='F',
            age=27,
            height=150,
            weight=200,
            team='Brazil',
            games='2016 Summer',
            event=event,
            sport=sport,
            medal='Gold'
        )
        olympian_2.save()

        response = self.client.get('/api/v1/olympians?age=youngest')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], olympian_1.name)
        self.assertEqual(response.data['age'], olympian_1.age)
        self.assertEqual(response.data['sport'], sport.name)
        self.assertEqual(response.data['total_medals_won'], 0)

    def test_it_can_get_the_oldest_olympian(self):
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

        olympian_2 = Olympian(
            name='Sport Woman',
            sex='F',
            age=27,
            height=150,
            weight=200,
            team='Brazil',
            games='2016 Summer',
            event=event,
            sport=sport,
            medal='Gold'
        )
        olympian_2.save()

        response = self.client.get('/api/v1/olympians?age=oldest')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], olympian_2.name)
        self.assertEqual(response.data['age'], olympian_2.age)
        self.assertEqual(response.data['sport'], sport.name)
        self.assertEqual(response.data['total_medals_won'], 1)
