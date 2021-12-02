from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # TODO: 업로드 되는 파일이 비디오 파일인지 여부를 검사
    video_file = models.FileField()
    thumbnail_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
