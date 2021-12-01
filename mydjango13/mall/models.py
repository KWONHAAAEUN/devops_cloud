from django.db import models
import datetime


class Shop(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    telephone = models.CharField(max_length=13)
    # open_time=models.TimeField(default=datetime.time)
    photo=models.ImageField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        # 관련 쿼리셋에서 order_by를 지정하지 않을 때
        # 적용될 디포트 정렬
        ordering = ['-id']
