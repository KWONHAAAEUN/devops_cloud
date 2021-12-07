from django.contrib import admin
from django.urls import path, include

from delicious.views import shop_list, shop_detail, shop_new_1, shop_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delicious/',include('delicious.urls')),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('delicious/', shop_list),
#     path('delicious/<int:pk>/', shop_detail),
#     path('delicious/new1/', shop_new_1),
#     path('delicious/new/', shop_new),
# ]
