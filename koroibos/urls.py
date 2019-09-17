from django.urls import path
from .views import ListOlympiansView

urlpatterns = [
    path('olympians', ListOlympiansView.as_view())
]
