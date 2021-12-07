from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 디버그 툴바의 urls
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/",include(debug_toolbar.urls)),
    ]