from django.urls import path
from volleyball import views

app_name="volleyball"

urlpatterns=[
    path("",views.player_list,name="player_list"),
    path("<int:pk>/",views.player_detail,name="player_detail"),
]