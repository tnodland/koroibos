from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Event
from .models import Sport

class BaseTest(APITestCase):
    client = APIClient()

class AllEventsTest(BaseTest):
    def test_it_can_get_all_events_by_sport:
        
