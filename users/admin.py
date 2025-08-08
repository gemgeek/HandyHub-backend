from django.contrib import admin
from .models import User, CustomerProfile, ArtisanProfile

# Register the User model
admin.site.register(User)

# Register the CustomerProfile and ArtisanProfile models
admin.site.register(CustomerProfile)
admin.site.register(ArtisanProfile)
