from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

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
