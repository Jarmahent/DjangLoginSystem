from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from storefront.models import store_item
from django.contrib.auth.decorators import user_passes_test
from storefront.forms import NewItemForm

def store(request):
    items = list(store_item.objects.values())
    return render(request, 'storefront/item.html', {"items": items})

@user_passes_test(lambda u: u.is_superuser)
def submit_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/store')
    else:
        form = NewItemForm()
    return render(request, 'storefront/submit_item.html', {"form": form})
