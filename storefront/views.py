from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from storefront.models import storeItem
from django.contrib.auth.decorators import user_passes_test
from storefront.forms import ItemModelForm

def store(request):
    items = list(storeItem.objects.values())
    return render(request, 'storefront/item.html', {"items": items})

@user_passes_test(lambda u: u.is_superuser)
def submit_item(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print({
                "item_name": form.cleaned_data.get('item_name'),
                "item_description": form.cleaned_data.get('item_description'),
                "item_price": form.cleaned_data.get('item_price'),
                "item_is_available": form.cleaned_data.get('item_is_available'),
                "item_image": form.cleaned_data.get('item_image')
            })

            return HttpResponseRedirect('/store')
    else:
        form = ItemModelForm()
        print(form.errors)
    return render(request, 'storefront/submit_item.html', {"form": form})



# storefront/static/storefront/media/Aywsy5a.png
