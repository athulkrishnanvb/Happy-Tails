from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    staff = models.ManyToManyField(User, related_name='shelters')

    def __str__(self):
        return self.name
