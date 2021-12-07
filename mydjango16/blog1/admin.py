from django.contrib import admin

from blog1.models import Post,Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Post,PostAdmin)
#위 코드 대신 @admin..을 사용

@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
    list_display = ['pk','post','message','created_at','updated_at']
    list_display_links = ['post']
#admin.site.register(Comment,CommnetAdmin)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass