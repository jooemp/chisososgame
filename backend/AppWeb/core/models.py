import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Character(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/characters")
    rules = models.TextField()

class Games(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/games")
    rules = models.TextField()
