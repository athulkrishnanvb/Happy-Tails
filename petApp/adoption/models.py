from django.db import models
from django.contrib.auth.models import User
from petinfo.models import Pet
# Create your models here.

class AdoptionApplication(models.Model):
    STATUST_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUST_CHOICES, default='submitted')
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"
    