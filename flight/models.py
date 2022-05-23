from django.db import models

# Create your models here.
from service.models import Service


class Flight(models.Model):
    flightNo = models.CharField(max_length=4)
    origin = models.ForeignKey(Service,related_name='origin',on_delete=models.PROTECT)
    destination = models.ForeignKey(Service,related_name='destination',on_delete=models.PROTECT)
    edt = models.DecimalField(decimal_places=2, max_digits=5)
    estimatedDuration = models.DecimalField(decimal_places=2, max_digits=5)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.flightNo[0:50]
