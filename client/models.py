from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.CharField(max_length=100)