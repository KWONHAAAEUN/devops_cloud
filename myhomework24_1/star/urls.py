from django.urls import path

from star import views

app_name="star"

urlpatterns=[
    path('',views.kirby_list,name="kirby_list"),
    path('<int:pk>',views.kirby_detail,name="kirby_detail"),
    path('new/',views.kirby_new,name="kirby_new"),
    path('<int:pk>/edit/', views.kirby_edit, name='kirby_edit'),
    path('<int:pk>/delete/', views.kirby_delete, name='kirby_delete'),
]