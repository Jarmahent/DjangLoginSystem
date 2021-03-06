from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from login.forms import CustomUserForm
from django.contrib.auth.models import User
from json import loads
from django.core import serializers



def index(request):
    return HttpResponse("Hello!")


def json(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return JsonResponse({'STATUS': ip})

def logged_in(request):
    return render(request, 'login/success.html')

@login_required
def user_info(request):
    return render(request, 'users/userinfo.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password) #User is coming out as None
            login(request, user)
            return HttpResponseRedirect('/homepage')
    else:
        form = CustomUserForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_page(request, userID):
    raw_results = User.objects.defer("password", "email").filter(id__iexact=userID)
    parsed_results = loads(
    serializers.serialize("json",
    raw_results,
    fields=("username", "last_login", "id", "is_superuser", "first_name", "last_name", "is_active", "date_joined") ))
    return render(request, 'users/user_page.html', {'items': parsed_results})
