from django.db import models

class Post(models.Model):
    team_name=models.CharField(max_length=50, db_index=True)
    member=models.CharField(max_length=200)
    content=models.TextField()
    photo=models.ImageField(upload_to="dancer/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self)->str:
        return self.team_name

    class Meta:
        verbose_name="댄서 팀" #단수
        verbose_name_plural="댄서 팀 목록" #플로럴는 복수

class Comment(models.Model):
    # post에 따라 comment를 넣어줄 것이기에 외래키를 지정하겠습니다
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    message=models.TextField()

    class Meta:
        verbose_name="댓글"
        verbose_name_plural="댓글 목록"

class Tag(models.Model):
    name=models.CharField(max_length=200, db_index=True)

# tag가 보일 때 저장한 태그로 보이게 해줌
    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name="태그"
        verbose_name_plural="태그 목록"