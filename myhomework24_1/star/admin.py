from django.contrib import admin

from star.models import Category, Kirby, Tag, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Kirby)
class KirbyAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
