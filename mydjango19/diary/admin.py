from django.contrib import admin
# 테이블을 만들어서 나타낼 것들만 import하는 것이 맞다
from diary.models import Post,Comment,Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass