from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name="store"),
    path('submit', views.submit_item, name="submit")
]
