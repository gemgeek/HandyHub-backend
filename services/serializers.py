from rest_framework import serializers
from .models import ServiceCategory

class ServiceCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the ServiceCategory model.
    """
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'description', 'image_url']