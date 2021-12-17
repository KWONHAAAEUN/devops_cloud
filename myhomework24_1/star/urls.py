from django.urls import path

from star import views

app_name="star"

urlpatterns=[
    path('',views.kirby_list,name="kirby_list"),
    path('<int:pk>',views.kirby_detail,name="kirby_detail"),
    path('new/',views.kirby_new,name="kirby_new"),
    path('<int:pk>/edit/', views.kirby_edit, name='kirby_edit'),
    path('<int:pk>/delete/', views.kirby_delete, name='kirby_delete'),
    path("<int:star_pk>/reviews/new",views.review_new,name="review_new"),
    path('<int:star_pk>/reviews/delete/', views.review_delete, name='review_delete'),
    path('<int:star_pk>/reviews/edit/', views.review_edit, name='review_edit'),
]