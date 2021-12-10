from django.contrib import admin

from car.models import Shop, Comment, Tag


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass