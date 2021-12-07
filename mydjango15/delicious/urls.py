from django.urls import path
from delicious.views import shop_list,shop_detail,shop_new,shop_new_1

app_name = "delicious"
urlpatterns=[
    path('',shop_list, name='shop_list'),
    path('<int:pk>/',shop_detail, name='shop_detail'),
    path('new1/',shop_new_1, name='shop_new_1'),
    path('new/',shop_new, name='shop_new'),
]