from django.urls import path
from .views import ListOlympiansView
from .views import ListOlympianStatsView

urlpatterns = [
    path('olympians', ListOlympiansView.as_view()),
    path('olympian_stats', ListOlympianStatsView.as_view())
]
