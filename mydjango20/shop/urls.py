from django.urls import path

from shop import views
# namespace의 역할
app_name="shop"

urlpatterns=[
    path("new/",views.shop_new,name="shop_new"),
    path("<int:pk>/",views.shop_detail,name="shop_detail"),
    path("",views.shop_list,name="shop_list"),
    path("<int:pk>/edit/",views.shop_edit,name="shop_edit"),
]