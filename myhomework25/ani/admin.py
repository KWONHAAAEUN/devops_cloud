from django.contrib import admin

from ani.models import Category, Ani, Comment, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Ani)
class AniAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
