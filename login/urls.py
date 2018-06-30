from django.urls import path
from . import views


urlpatterns = [
    path('json', views.json, name="json"),
    path('', views.logged_in, name="logged_in")
]
