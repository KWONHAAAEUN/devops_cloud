from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        ordering=["-name"]

class Player(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,db_index=True)
    photo=models.ImageField(upload_to="volleyball/player/%Y/%m/%d")
    team=models.CharField(max_length=30)
    position=models.CharField(max_length=30)
    description=models.TextField(blank=True)
    tag_set=models.ManyToManyField('Tag',blank=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        ordering=["-name"]

class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        ordering=["-name"]

