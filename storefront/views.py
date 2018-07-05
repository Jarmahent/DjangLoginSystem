from django.shortcuts import render, HttpResponse
from storefront.models import store_item


def store(request):
    items = list(store_item.objects.values())
    return render(request, 'storefront/item.html', {"items": items})
