from accounts import views
from django.urls import path

app_name="accounts"

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]