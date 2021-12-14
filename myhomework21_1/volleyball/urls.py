from django.urls import path
from volleyball import views

app_name="volleyball"

urlpatterns=[
    path("",views.player_list,name="player_list"),
    path("<int:pk>/",views.player_detail,name="player_detail"),
    path("new/", views.player_new, name="player_new"),
    path("<int:pk>/edit/", views.player_edit, name="player_edit"),
    path("<int:player_pk>/comments/new",views.comment_new,name="comment_new"),
    path("<int:player_pk>/comments/<int:pk>/edit/",views.comment_edit,name="comment_edit"),
]