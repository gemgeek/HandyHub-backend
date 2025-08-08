from django.urls import path
from .views import ArtisanListView

urlpatterns = [
    path('artisans/', ArtisanListView.as_view(), name='artisan-list'),
]