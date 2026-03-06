from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    national_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    # The MVP Savings Tracker
    savings_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_full_name()} - KES {self.savings_balance}"

class SaccoForm(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='forms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)