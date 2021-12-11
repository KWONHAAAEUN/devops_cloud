from django.urls import path
from car import views

app_name="car"

urlpatterns=[
    path("",views.shop_list,name="shop_lost"),
    path("<int:pk>/",views.shop_detail,name="shop_detail"),
]