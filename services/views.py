from django.shortcuts import render
from rest_framework import generics
from .models import ServiceCategory
from .serializers import ServiceCategorySerializer

class ServiceCategoryListView(generics.ListAPIView):
    """
    API view to list all service categories.
    """
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
