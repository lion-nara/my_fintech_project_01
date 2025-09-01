# photos/models.py
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

def user_photo_path(instance, filename):
    return f"photos/{instance.user_id}/{filename}"

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to=user_photo_path)
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.caption[:20]}"


# Create your models here.
