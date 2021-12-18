from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Category(TimestampedModel):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=["name"]
        verbose_name="카테고리"
        verbose_name_plural="카테고리들"

class Ani(TimestampedModel):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,db_index=True)
    photo=models.ImageField(upload_to="ani/ani/%Y/%m/%d",blank=True)
    description=models.TextField(blank=True)
    tag_set=models.ManyToManyField('Tag',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=["name"]
        verbose_name="캐릭터"
        verbose_name_plural="캐릭터 이름들"

    def get_absolute_url(self):
        return reverse("ani:ani_detail",args=[self.pk])

class Comment(TimestampedModel):
    ani=models.ForeignKey(Ani,on_delete=models.CASCADE)
    user=models.CharField(max_length=30,db_index=True)
    message=models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering=["-id"]
        verbose_name="댓글"
        verbose_name_plural="댓글 목록"

class Tag(TimestampedModel):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=["name"]
        verbose_name="태그"
        verbose_name_plural="태그 목록"
