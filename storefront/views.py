from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from storefront.models import storeItem
from django.contrib.auth.decorators import user_passes_test
from storefront.forms import ItemModelForm
from django.core import serializers
from json import loads, dumps
from django.contrib.auth.decorators import login_required

def store(request):
    if request.method == 'POST':
        search_query = request.POST.get("search")
        raw_results = storeItem.objects.filter(item_name__icontains=search_query)
        parsed_results = loads(serializers.serialize("json", raw_results))
        return render(request, "storefront/item.html", {"items": list(parsed_results)})

    data = loads(serializers.serialize("json", storeItem.objects.all()))
    return render(request, 'storefront/item.html', {"items": list(data)})

# @user_passes_test(lambda u: u.is_superuser)
@login_required
def submit_item(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
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
