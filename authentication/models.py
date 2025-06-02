from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    address = models.TextField(blank=True)  # <-- Add this for address

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"
