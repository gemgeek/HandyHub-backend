from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.db.models import F
from users.models import ArtisanProfile
from users.serializers import ArtisanProfileSerializer

class ArtisanListView(generics.ListAPIView):
    """
    API view to list and search artisans.
    """
    queryset = ArtisanProfile.objects.filter(is_verified=True).order_by(F('average_rating').desc(nulls_last=True), '-id')
    serializer_class = ArtisanProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['services__name', 'locations__name']
