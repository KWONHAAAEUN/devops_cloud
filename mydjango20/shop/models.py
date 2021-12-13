from django.core.validators import RegexValidator
from django.db import models

class TimestampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Shop(TimestampedModel):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,db_index=True)
    description=models.TextField(blank=True)
    telephone=models.CharField(max_length=14,
                               validators=[
                                   RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$",message="전화번호를 입력해주세요"), # 정규표현식, F멘트
                               ],
                               help_text="입력 예) 042-1234-1234") # 도움말
    tag_set=models.ManyToManyField('Tag',blank=True) # 태그 설정 없어도 된다->blank=True

    def __str__(self)->str:
        return self.name

class Review(TimestampedModel):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE) #1:N # 하나의 shop이 삭제되면 그 안에 리뷰들 삭제
    author_name=models.CharField(max_length=20)
    message=models.TextField()

class Tag(TimestampedModel):
    name=models.CharField(max_length=100, unique=True) # 유일성 옵션

    def __str__(self)->str:
        return self.name

