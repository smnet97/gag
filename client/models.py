from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

from gag.helpers import UploadTo


class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo('profile'))

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url

        return static('img/no-user.jpg')