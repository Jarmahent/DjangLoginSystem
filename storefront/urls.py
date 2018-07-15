from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.store, name="store"),
    path('submit', views.submit_item, name="submit"),
    path('catalog/<str:item_name>', views.item_view, name="item_view")
]
