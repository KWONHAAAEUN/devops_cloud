from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Kirby(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=30,db_index=True)
    photo=models.ImageField(upload_to="star/kirby/%Y/%m/%d")
    day=models.DateField()
    story=models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Review(TimestampedModel):
    kirby = models.ForeignKey(Kirby, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']

class Tag(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

