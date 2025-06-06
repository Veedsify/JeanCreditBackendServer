from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    # optional: add custom fields
    profile_image = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, unique=True, null=True)
    is_verified = models.BooleanField(default=False)
    user_id = models.CharField(max_length=50, verbose_name="user_id")
    country = models.CharField(
        max_length=10, choices=[("NG", "Nigeria"), ("GH", "Ghana")], default="NG"
    )
    pass
