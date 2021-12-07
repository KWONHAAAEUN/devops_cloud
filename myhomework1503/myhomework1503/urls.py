from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from bread.views import shop_list,shop_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bread/',shop_list),
    path('bread/<int:pk>',shop_detail),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/',include(debug_toolbar.urls)),
    ]
