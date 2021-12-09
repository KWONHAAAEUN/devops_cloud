from django.urls import path

from dancer import views

app_name="dancer"

urlpatterns=[
    path("",views.post_list,name="post_list"),
    path("<int:pk>/",views.post_detail,name="post_detail"),
]