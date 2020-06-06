from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birthday = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
