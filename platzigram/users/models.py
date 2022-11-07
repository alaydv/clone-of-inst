from tkinter import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Profile(models.Model):
    """
    Profile User

    Proxy model that extends the base data with cumtomize information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return user name"""
        return self.user.username