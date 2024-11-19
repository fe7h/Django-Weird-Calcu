from django.shortcuts import render
from django.http import JsonResponse
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.context_processors import request
from . import services

# Create your views here.

def helo(request):
    return render(request,'calcu/home.html')


def calculated(request):
    first, second = int(request.GET['first']),int(request.GET['second'])
    ans = services.calculat(first, second)
    img = services.img_gen(str(ans), staticfiles_storage.path('calcu/img/meme.png'))

    return JsonResponse({'img':img})
