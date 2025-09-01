# portfolio/models.py
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Account(models.Model):
    TYPE = [("CASH","현금"), ("SEC","증권")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=4, choices=TYPE, default="SEC")
    currency = models.CharField(max_length=10, default="KRW")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"[{self.user}] {self.name}"


# Create your models here.
