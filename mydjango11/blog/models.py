from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 포스팅이 된 글을 외부에서 타이플로 보여지게 한다
    def __str__(self):
        return self.title
