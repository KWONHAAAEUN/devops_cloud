from django.db import models

class Post(models.Model):
    team_name=models.CharField(max_length=50, db_index=True)
    member=models.CharField(max_length=200)
    content=models.TextField()
    photo=models.ImageField(upload_to="dancer/post/%Y/%m/%d")
    tag_set=models.ManyToManyField('Tag',blank=True)

    def __str__(self)->str:
        return self.team_name

    class Meta:
        verbose_name="댄서 팀"
        verbose_name_plural="댄서 팀 목록"

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    message=models.TextField()

    class Meta:
        verbose_name="댓글"
        verbose_name_plural="댓글 목록"

class Tag(models.Model):
    name=models.CharField(max_length=200,db_index=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name="태그"
        verbose_name_plural="태그 목록"