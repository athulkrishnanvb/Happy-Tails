from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from shelters.models import Shelter

# Create your models here.

class Pet(models.Model):
    photo = models.ImageField(upload_to='pet_photos/')
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    health_status = models.TextField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name