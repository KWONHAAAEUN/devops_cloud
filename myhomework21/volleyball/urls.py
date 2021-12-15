from django.urls import path

from volleyball import views

app_name="volleyball"

urlpatterns=[
    path("",views.player_list,name="player_list"),
    path("<int:pk>/",views.player_deatil,name="player_detail"),
    path("new/",views.player_new,name="player_new"),
    path("<int:pk>/edit/",views.player_edit,name="player_edit"),
]