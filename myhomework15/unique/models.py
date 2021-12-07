from django.db import models

class Shop(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    address=models.CharField(max_length=100)
    telephone=models.CharField(max_length=15)
    description=models.TextField(blank=True)