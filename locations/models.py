from django.db import models

class Location(models.Model):
    """
    Model for geographical locations (e.g., regions, districts, areas).
    """
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
