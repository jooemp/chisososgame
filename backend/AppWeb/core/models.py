import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

GRADES = (
    (1, 'Primero'),
    (2, 'Segundo'),
    (3, 'Tercero'),
    (0, 'Ninguno')
)

class Characte(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/characters")
    rules = models.TextField()

class Games(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="images/games")
    rules = models.TextField()
    first= models.IntegerField()
    second = models.IntegerField()
    thrid = models.IntegerField()

class ChooseCharacter(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    character = models.ForeignKey(Characte, on_delete=models.CASCADE, null=True)

class NightGame(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, null=True)
    choose_character = models.ForeignKey(ChooseCharacter,on_delete=models.CASCADE, null=True)
    position = models.IntegerField('puesto', choices=GRADES, default=0, blank=True)
    score = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    passive = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    