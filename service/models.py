
# Create your models here.
from django.db import models



class Service(models.Model):
    locationCode = models.CharField(max_length=3)
    locationName = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=200)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.locationName[0:50]
