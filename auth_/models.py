from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    is_super_admin = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
