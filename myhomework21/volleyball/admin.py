from django.contrib import admin

from volleyball.models import Category, Player, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
