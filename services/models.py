from django.db import models

class ServiceCategory(models.Model):
    """
    Model for different types of artisan services (e.g., Plumbing, Electrical).
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
