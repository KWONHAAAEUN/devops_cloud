from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Shop, Review, Tag, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form=ShopForm # 내가 지정한 폼 사용

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass