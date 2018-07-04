from django.shortcuts import render, HttpResponse


def store(request):
    return render(request, 'storefront/item.html')
