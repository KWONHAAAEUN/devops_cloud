from django.db import models

class TimestampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Shop(TimestampedModel):
    name=models.CharField(max_length=100,db_index=True)
    type=models.CharField(max_length=50)
    option=models.TextField()
    cost=models.CharField(max_length=20)
    photo=models.ImageField(upload_to="car/shop/%Y/%m/%d")
    tag_set=models.ManyToManyField('Tag',blank=True)

    class Meta:
        verbose_name="차"
        verbose_name_plural="차 모델 목록"

    def __str__(self)->str:
        return self.name

class Review(TimestampedModel):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    message=models.TextField()

    class Meta:
        verbose_name="댓글"
        verbose_name_plural="댓글 목록"

class Tag(TimestampedModel):
    name=models.CharField(max_length=100,db_index=True)

    class Meta:
        verbose_name="태그"
        verbose_name_plural="태그 목록"

    def __str__(self)->str:
        return self.name



