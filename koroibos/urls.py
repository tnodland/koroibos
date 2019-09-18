from django.urls import path
from .views import ListOlympiansView
from .views import ListOlympianStatsView
from .views import ListEventsView

urlpatterns = [
    path('olympians', ListOlympiansView.as_view()),
    path('olympian_stats', ListOlympianStatsView.as_view()),
    path('events', ListEventsView.as_view())
]
