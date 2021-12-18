from django.urls import path

from ani import views

app_name="ani"

urlpatterns=[
    path("",views.ani_list,name="ani_list"),
    path("<int:pk>/",views.ani_detail,name="ani_detail"),
    path("<int:ani_pk>/comments/new/",views.comment_new,name="comment_new"),
    path("<int:ani_pk>/comments/<int:pk>/edit/",views.comment_edit,name="comment_edit"),
]