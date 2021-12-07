from django.contrib import admin
from bread.models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','telephone','description']
    list_display_links = ['name']

admin.site.register(Shop,ShopAdmin)
