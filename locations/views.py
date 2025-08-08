from django.shortcuts import render
from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer

class LocationListView(generics.ListAPIView):
    """
    API view to list all locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

