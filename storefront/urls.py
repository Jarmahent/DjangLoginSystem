from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.store, name="store"),
    path('submit', views.submit_item, name="submit"),
    path('catalog/<str:item_name>', views.item_view, name="item_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
