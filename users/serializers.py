from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomerProfile, ArtisanProfile
from locations.models import Location
from services.models import ServiceCategory

# Get our custom User model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to display user details.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'first_name', 'last_name', 'phone_number']


class CustomerProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomerProfile model.
    """
    user = UserSerializer(read_only=True)
    primary_location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), required=False)

    class Meta:
        model = CustomerProfile
        fields = ['id', 'user', 'primary_location', 'address_line_1', 'city']
        
    def create(self, validated_data):
        user = self.context['request'].user
        profile, created = CustomerProfile.objects.get_or_create(user=user, **validated_data)
        return profile


class ArtisanProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the ArtisanProfile model.
    """
    user = UserSerializer(read_only=True)
    services = serializers.PrimaryKeyRelatedField(many=True, queryset=ServiceCategory.objects.all())
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())

    class Meta:
        model = ArtisanProfile
        fields = ['id', 'user', 'business_name', 'bio', 'national_id_number', 'is_verified', 'average_rating', 'services', 'locations']
        
    def create(self, validated_data):
        user = self.context['request'].user
        services_data = validated_data.pop('services', [])
        locations_data = validated_data.pop('locations', [])

        profile, created = ArtisanProfile.objects.get_or_create(user=user, **validated_data)
        profile.services.set(services_data)
        profile.locations.set(locations_data)
        return profile


class RegisterSerializer(serializers.Serializer):
    """
    Serializer for user registration.
    """
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
    national_id_number = serializers.CharField(max_length=50, required=False, allow_blank=True)


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        phone_number = validated_data.pop('phone_number', '')
        national_id_number = validated_data.pop('national_id_number', '')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=user_type, # <-- Pass user_type directly here
            phone_number=phone_number # <-- Pass phone_number directly here
        )
        if user_type == 'customer':
            CustomerProfile.objects.create(user=user)
        elif user_type == 'artisan':
            ArtisanProfile.objects.create(user=user, national_id_number=national_id_number)
        return user
