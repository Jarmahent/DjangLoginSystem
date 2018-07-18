from django.urls import path
from . import views
from django.contrib.auth.views import password_change

urlpatterns = [
    path('', views.logged_in, name="logged_in"),
    path('json', views.json, name="json"),
    path('userinfo', views.user_info, name="user_info"),
    path('register', views.register, name="register"),
    path('user/<int:userID>', views.user_page, name="user_info")
]
