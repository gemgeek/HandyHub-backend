from django.urls import path
from .views import LocationListView

urlpatterns = [
    path('locations/', LocationListView.as_view(), name='locations'),
]
