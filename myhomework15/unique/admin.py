from django.contrib import admin
from unique.models import Unique

class UniqueAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','telephone','description']
    list_display_links = ['name']

admin.site.register(Unique,UniqueAdmin)