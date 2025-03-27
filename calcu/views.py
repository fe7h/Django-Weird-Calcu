from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.finders import find

from . import services

# Create your views here.

def helo(request):
    return render(request,'calcu/home.html')


def calculated(request):
    first, second = int(request.GET['first']),int(request.GET['second'])

    ans = services.calculat(first, second)
    img = services.img_gen(str(ans), find('calcu/img/meme.png'))

    return HttpResponse(img, content_type='image/png')
