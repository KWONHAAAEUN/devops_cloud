from django.contrib import admin
from dingo.models import Video


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)