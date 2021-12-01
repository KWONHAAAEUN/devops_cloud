from django.db import models

class Shop(models.Medel):
    name=models.CharField(max_length=100)
    description=models.TextField(black=True)
    photo=models.ImageField(black=True)
