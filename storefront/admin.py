from django.contrib import admin
from .models import storeItem
# Register your models here.

@admin.register(storeItem)
class ItemAdmin(admin.ModelAdmin):
    pass
