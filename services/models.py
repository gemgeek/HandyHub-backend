from django.db import models

class ServiceCategory(models.Model):
    """
    Model for different types of artisan services (e.g., Plumbing, Electrical).
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
