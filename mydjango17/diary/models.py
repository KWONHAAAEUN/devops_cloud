from django.db import models

class TimestampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True # 추상 클래스로서, DB 테이블이 생기지 않는다다

#db_index는 db에 인덱스를 생성시켜 조건을 넣으면 검색이 가능하게 하는 부분
class Post(TimestampedModel):
    author_name=models.CharField(max_length=20)
    title=models.CharField(max_length=200, db_index=True)
    content=models.TextField()
    photo=models.ImageField(upload_to="diary/post/%Y/%m/%d")
    # 그냥 Tag를 적으면 Tag가 아래에 있기에 받지 못한다
    # 문자열로 넣어주면 현재 앱에서 Tag를 찾아 받아준다
    # tag_set이 아닌 tag라고 하면 단수형이기에 의미가 좋지는 않다
    tag_set=models.ManyToManyField('Tag',blank=True)

    def __str__(self)->str:
        return self.title

    class Meta:
        # 단수
        verbose_name="포스팅"
        # 복수
        verbose_name_plural="포스팅 목록"

class Comment(TimestampedModel):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    message=models.TextField()

    class Meta:
        verbose_name="댓글"
        verbose_name_plural="댓글 목록"

class Tag(TimestampedModel):
    name=models.CharField(max_length=200, db_index=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name="태그"
        verbose_name_plural="태그그 목록"

#class에 TimestampedModel를 넣음으로 상속을 하는 것