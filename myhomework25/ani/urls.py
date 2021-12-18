from django.urls import path

from ani import views

app_name="ani"

urlpatterns=[
    path("",views.ani_list,name="ani_list"),
    path("<int:pk>/",views.ani_detail,name="ani_detail"),
]