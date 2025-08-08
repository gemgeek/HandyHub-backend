from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model.
    """
    class Meta:
        model = Location
        fields = ['id', 'name', 'parent', 'type']