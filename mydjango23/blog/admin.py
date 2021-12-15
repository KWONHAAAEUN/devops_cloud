from django.contrib import admin

from blog.models import Category, Post, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass