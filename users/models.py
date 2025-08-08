from django.db import models
from django.contrib.auth.models import AbstractUser
from services.models import ServiceCategory
from locations.models import Location

class User(AbstractUser):
    """
    A custom user model to allow for different user types (customer or artisan).
    """
    USER_TYPE_CHOICES = (
        ("customer", "Customer"),
        ("artisan", "Artisan"),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="customer")
    phone_number = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.email

class CustomerProfile(models.Model):
    """
    Profile model for customers.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    primary_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class ArtisanProfile(models.Model):
    """
    Profile model for artisans.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artisan_profile')
    business_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    national_id_number = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    services = models.ManyToManyField(ServiceCategory, related_name='artisans')
    locations = models.ManyToManyField(Location, related_name='artisans')

    def __str__(self):
        return self.business_name or self.user.username