from django.urls import path
from . import views


urlpatterns = [
    path('', views.logged_in, name="logged_in"),
    path('json', views.json, name="json"),
    path('userinfo', views.user_info, name="user_info"),
    path('register', views.register, name="register")
]
